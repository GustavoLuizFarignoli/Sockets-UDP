#importar a biblioteca da API
from ast import While
import socket

#HOST : loopback
print("Iniciando O Servidor")
HOST = '127.0.0.1'
PORTA = int(input('Entre com a porta do servidor'))

#criação do nosso socket
#inicialização com o tipo de endereçamento e IP e PROTOCOLO
#IPV4 : AF_INET
#TCP : SOCK_STREAM
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#vincular host e porta : BIND
while True:
    try:
        sock.bind((HOST,PORTA))
        break
    except:
        print("Erro em executar o bind")
        continue

print(f"Servidor em {HOST}:{PORTA}")


while True:
    dados = sock.recvfrom(1024) #tamanho do buffer
    if not dados:
        print("fechando")
        break
    print(f"{dados[0]} {dados[1]}...")


