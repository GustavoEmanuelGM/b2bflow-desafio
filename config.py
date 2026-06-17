import os
from dotenv import load_dotenv

load_dotenv()

def get_supabase_config():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("SUPABASE_URL e SUPABASE_KEY devem estar configuradas no .env")
    
    return url, key

def get_zapi_config():
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")
    
    if not instance_id or not token:
        raise ValueError("ZAPI_INSTANCE_ID e ZAPI_TOKEN devem estar configuradas no .env")
    
    return instance_id, token