#!/user/bin/python3          


                                                                         
from termcolor import colored
import socket
import os



##############################################
# not my fault what you do with this program #
##################################################
#programed by DeAuth (don't change the name foo!)#
##################################################

os.system("clear")
     

print('')                                                                                                            
print(colored(' ▓█████▄ ▓█████ ▄▄▄       █    ██ ▄▄▄█████▓ ██░ ██   ██████ ▓█████  ▄████▄  ', 'green'))
print(colored(' ▒██▀ ██▌▓█   ▀▒████▄     ██  ▓██▒▓  ██▒ ▓▒▓██░ ██▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ', 'green'))
print(colored(' ░██   █▌▒███  ▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██▀▀██░░ ▓██▄   ▒███   ▒▓█    ▄ ', 'green'))
print(colored(' ░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ░▓█ ░██   ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒', 'green'))
print(colored(' ░▒████▓ ░▒████▒▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░▓█▒░██▓▒██████▒▒░▒████▒▒ ▓███▀ ░', 'green'))
print(colored('  ▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░    ▒ ░░▒░▒▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░', 'green'))
print(colored('  ░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░░░▒░ ░ ░     ░     ▒ ░▒░ ░░ ░▒  ░ ░ ░ ░  ░  ░  ▒   ', 'green'))
print(colored('  ░ ░  ░    ░    ░   ▒    ░░░ ░ ░   ░       ░  ░░ ░░  ░  ░     ░   ░        ', 'green'))
print(colored('    ░       ░  ░     ░  ░   ░               ░  ░  ░      ░     ░  ░░ ░      ', 'green'))
print(colored('  ░                                                                ░   v.01 ', 'green'))
print(colored('                  xXx Programed by DeAuth @authdesec xXx                     ', 'yellow'))
print(colored('                     xXx For fast port scanning! xXx                         ', 'yellow'))
print('')
                                                                                                
                                                                                                            
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)



host = input(colored('  Enter ip you want to scan: ','green'))
port = int(input(colored('  Enter port you want to scan: ','green')))

def portScanner(port):
    if s.connect_ex((host, port)):
       print (colored('  the port is','white'), colored('closed', 'red'))     
    else:
       print (colored('  the port is','white'), colored('open', 'green'))

portScanner(port)                                                                                                                  
                                                                                                                         
                                                                                                                         
                                                                                                                                      
                                                                                                        
