#!/usr/bin/env python3
import requests
import time

def make_requests():
    print("Fazendo requisições para o load balancer...")
    print("=" * 50)
    
    instances_responses = {}
    
    for i in range(15):
        try:
            response = requests.get('http://localhost:8080/', timeout=5)
            instance_name = response.text.strip()
            
            # Contabiliza as respostas por instância
            if instance_name in instances_responses:
                instances_responses[instance_name] += 1
            else:
                instances_responses[instance_name] = 1
                
            print(f"Requisição {i+1}: {instance_name}")
            time.sleep(0.5)
            
        except requests.exceptions.RequestException as e:
            print(f"Requisição {i+1}: Erro - {e}")
    
    print("=" * 50)
    print("Estatísticas:")
    for instance, count in instances_responses.items():
        print(f"{instance}: {count} respostas")
    
    # Teste de health check
    try:
        health_response = requests.get('http://localhost:8080/health', timeout=5)
        print(f"\nHealth Check: {health_response.text.strip()}")
    except requests.exceptions.RequestException as e:
        print(f"\nHealth Check falhou: {e}")

if __name__ == "__main__":
    make_requests()
