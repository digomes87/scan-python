import socket
from IPy import IP


ipaddress = input('[+] Digite o Ip do Alvo: ')
port = 80


try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print('[+] Portas Abertas!')
except:
    print('[-] Portas Fechadas! ')