FROM python:3.12-slim
#Diretório de trabalho dentro do container 
# Todos os comandos a seguir serão executados a partir desta pasta.
WORKDIR /app

# ───Copia o arquivo de dependências PRIMEIRO ──
# Se apenas o código mudar (app.py, etc.), esta camada de dependências
# não precisa ser re-executada → build muito mais rápido.
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# ──Copia o restante do código ─
COPY . .

EXPOSE 5000

CMD ["python", "main.py"]