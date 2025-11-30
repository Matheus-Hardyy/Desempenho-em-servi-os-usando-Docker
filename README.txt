Torne os scripts executáveis no gitbash:
chmod +x client.py
Subir o ambiente:
docker-compose up --build

Em outro terminal, executar o cliente:
python3 client.py

Exemplo de saída esperada:
Fazendo requisições para o load balancer...
============================================
Requisição 1: Resposta do container: app1
Requisição 2: Resposta do container: app2
Requisição 3: Resposta do container: app1
Requisição 4: Resposta do container: app2
...
============================================
Estatísticas:
Resposta do container: app1: 8 respostas
Resposta do container: app2: 7 respostas

Health Check: OK
