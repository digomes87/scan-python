import socket
from IPy import IP


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
                      
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        print('[+] Porta '+str(port)+' Abertas!')
    except:
        print('[-] Portas '+ str(port)+' Fechadas! ')

ipaddress = input('[+] Digite o Ip do Alvo: ')
convert_ip = check_ip(ipaddress)

for port in range(75,85):
    scan_port(convert_ip, port)