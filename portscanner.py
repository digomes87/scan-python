import socket
from IPy import IP

def scan(target):
    converter_ip = check_ip(target)
    print('\n' + '[0 - Scaneando Alvo] '+ str(target))

    for port in range(1,20):
        scan_port(converter_ip, port)


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
        #pass
       print('[-] Portas '+ str(port)+' Fechadas! ')

targets = input('[+] Digite o Ip do Alvo: ')

#if ',' in targets:
 #   for ip_add in targets.split(','):
  #      scan(ip_add.split(' '))
#else:
scan(targets)