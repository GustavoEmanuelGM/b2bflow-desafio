# b2bflow-desafio

Projeto para desafio técnico da b2bflow - Integração Supabase + Z-API em Python.

## Descrição

Script Python que lê contatos cadastrados no Supabase e envia mensagens personalizadas via Z-API no formato: "Olá, <nome_contato> tudo bem com você?".

# Como rodar:

## 1. Clone o repositório:

git clone https://github.com/GustavoEmanuelGM/b2bflow-desafio.git

cd b2bflow-desafio

# 2. Prepare o ambiente:
python -m venv venv

 ## Windows:
 
.\venv\Scripts\activate

## Linux/Mac:

source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

# 3. Variáveis de Ambiente (.env)
### Crie um arquivo .env na raiz do projeto com suas credenciais:
SUPABASE_URL=https://seu_projeto.supabase.co
SUPABASE_KEY=sua_chave_anon_public
ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token

# 4. Setup da Tabela no Supabase:
Execute este SQL no editor do Supabase:

CREATE TABLE contatos (
    id BIGSERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    telefones TEXT NOT NULL,
    criado_em TIMESTAMPTZ DEFAULT NOW()
);

# 5. Execute:
python main.py

## Formato da Mensagem:
Olá, {nome_contato} tudo bem com você?

# Boas Práticas
Credenciais protegidas via .env

Tratamento de erros e logs estruturados

Separação de responsabilidades (Supabase, Z-API e Orquestrador)

Suporte a múltiplos telefones por contato (até 3)

# Autor
Gustavo Emanuel Gonçalves Magalhães
