import socket
from IPy import IP


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print('[+] Porta '+str(port)+' Abertas!')
    except:
        print('[-] Portas '+ str(port)+' Fechadas! ')

ipaddress = input('[+] Digite o Ip do Alvo: ')

for port in range(1,10):
    scan_port(ipaddress, port)