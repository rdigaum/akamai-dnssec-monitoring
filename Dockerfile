FROM python:3.10

WORKDIR /app

# Copy the Python script to the working directory
COPY dnssec_monitoring.py .

# Install required Python packages
RUN pip3 install dnspython python-dateutil

# Defina a variável de ambiente ZONES com as zonas desejadas
ENV ZONES '["via.com.br"]'

# Defina o comando para executar o script Python
CMD ["python3", "/app/dnssec_monitoring.py"]