FROM python:3.9

WORKDIR /app

# Copiar o código fonte para o diretório de trabalho
COPY . /app

# Instalação do psycopg2
RUN pip install --no-cache-dir psycopg2

# Comando para iniciar o aplicativo
CMD [ "python", "app.py" ]
