import requests
import logging
from config import get_zapi_config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def enviar_mensagem_zapi(telefone: str, mensagem: str) -> bool:
    """
    Envia mensagem via Z-API.
    
    Args:
        telefone: Número do telefone (ex: 5511999999999)
        mensagem: Texto da mensagem
        
    Returns:
        True se enviou com sucesso, False caso contrário
    """
    instance_id, token = get_zapi_config()
    
    # URL correta da Z-API
    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"
    
    # Dados para enviar
    payload = {
        "phone": telefone,
        "message": mensagem
    }
    
    try:
        logging.info(f" Enviando mensagem para {telefone}...")
        
        response = requests.post(url, json=payload, timeout=30)
        
        if response.status_code == 200:
            logging.info(f" Mensagem enviada com sucesso para {telefone}!")
            return True
        else:
            logging.error(f" Erro ao enviar para {telefone}: {response.status_code} - {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        logging.error(f"️ Timeout ao enviar para {telefone}")
        return False
    except Exception as e:
        logging.error(f" Erro ao enviar mensagem para {telefone}: {e}")
        return False

# Teste
if __name__ == "__main__":
    enviar_mensagem_zapi("5511999999999", "Olá, teste! Tudo bem com você?")