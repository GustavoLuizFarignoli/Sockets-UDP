#SCRIPT PARA CLIENTE
import socket
#FAZ ASSOCIAÇÃO AS INFOS DO SERVIDOR
print("Iniciando Cliente")
HOST = input('Entre com o ip de host ')
PORTA = int(input('Entre com a porta do servidor'))
mensagem = input("mensagem: ")

#criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#cliente se conecta ao servidor
sock.connect((HOST,PORTA))

#enviar uma string de dados
sock.send(str.encode(mensagem))