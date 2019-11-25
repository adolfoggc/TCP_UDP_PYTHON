import socket
import threading
from datetime import datetime 
import traceback
import time
from cryptography.fernet import Fernet

def fernet_crypt(n):
	key = Fernet.generate_key()
	f = Fernet(key)
	token = f.encrypt(bytes(n))
	return token 

def conta(n):
	lista = []
	contador = 0
	while contador < n:
		lista.append(contador)
		contador+=1
	return lista

def get_time(inicio, fim):
	return fim - inicio

def turn_on(HOST, PORT):
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST, PORT)
	tcp.connect(dest)
	listener = threading.Thread(target=listen, args=(tcp,))
	global run_thread
	run_thread = True
	listener.start()
	#print 'Para sair use SAIR\n'
	print("Iniciando...")
	palavra = 'papibaquigrafo'
	time.sleep(1)
	try:
		inicio = datetime.now()
		cifra = fernet_crypt(palavra)
		fim = datetime.now()
		gerar_cifra = get_time(inicio, fim)
		print(cifra)
		time.sleep(1)
		# for x in lista: 		
		# 	tcp.send(str(x))
		tcp.send(str('1'))
	except Exception: 
		traceback.print_exc()
	finally:
		print("Encerrando")
		time.sleep(2)
		tcp.send(str('SAIR'))					
		run_thread = False
		tcp.close()
		print("="*10)
		print("Tempo para gerar dado:")
		print(gerar_cifra)
		print("-"*10)
		print("Tamanho da string original: ", len(palavra))
		print("Tamanho da cifra: ", len(crifra))
		print("="*10)

def listen(socket):
	print 'Listener ligado!\n'
	global run_thread
	while run_thread:
		recived = socket.recv(1024)
		print(recived)
	print 'Listener desligado'

run_thread = False
h = 'localhost' #raw_input("Digite o host que deseja alcancar: ")
p = int(raw_input("Digite a porta a qual deseja conectar: "))
turn_on(h,p)
#print(conta(50))