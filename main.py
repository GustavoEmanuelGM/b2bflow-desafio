import logging
from supabase_client import buscar_contatos
from zapi_client import enviar_mensagem_zapi

# Configuração de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def processar_contatos():
    """Processa todos os contatos e envia mensagens."""
    
    logging.info(" Iniciando processo de envio de mensagens...")
    
    # Busca contatos do Supabase
    contatos = buscar_contatos()
    
    if not contatos:
        logging.warning(" Nenhum contato encontrado!")
        return
    
    logging.info(f" Processando {len(contatos)} contatos...")
    
    # Contadores
    enviados = 0
    falhas = 0
    
    # Processa cada contato
    for contato in contatos:
        nome = contato.get('nome', 'Contato')
        telefones_str = contato.get('telefones', '')
        
        # Separa os telefones (separados por vírgula)
        telefones = [tel.strip() for tel in telefones_str.split(',') if tel.strip()]
        
        # Limita a até 3 números
        telefones = telefones[:3]
        
        logging.info(f"\n Processando: {nome}")
        logging.info(f" Telefones: {', '.join(telefones)}")
        
        # Envia para cada telefone
        for telefone in telefones:
            # Personaliza a mensagem
            mensagem = f"Olá, {nome} tudo bem com você?"
            
            sucesso = enviar_mensagem_zapi(telefone, mensagem)
            
            if sucesso:
                enviados += 1
            else:
                falhas += 1
    
    # Resumo final
    logging.info("\n" + "="*50)
    logging.info(" RESUMO FINAL:")
    logging.info(f" Mensagens enviadas: {enviados}")
    logging.info(f" Falhas: {falhas}")
    logging.info("="*50)

if __name__ == "__main__":
    processar_contatos()