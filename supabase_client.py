from supabase import create_client, Client
from config import get_supabase_config
import logging

# Configuração básica de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_supabase_client() -> Client:
    """Inicializa e retorna o cliente do Supabase."""
    url, key = get_supabase_config()
    return create_client(url, key)

def buscar_contatos():
    """Busca todos os contatos da tabela 'contatos'."""
    client = get_supabase_client()
    
    try:
        logging.info("Conectando ao Supabase e buscando contatos...")
        response = client.table("contatos").select("*").execute()
        contatos = response.data
        
        logging.info(f" {len(contatos)} contatos encontrados no banco de dados.")
        return contatos
        
    except Exception as e:
        logging.error(f" Erro ao buscar contatos no Supabase: {e}")
        return []

# Teste rápido para ver se está funcionando
if __name__ == "__main__":
    buscar_contatos()