import socket
import threading
from datetime import datetime
import traceback
import time
from cryptography.fernet import Fernet

def fernet_modelo():
	key = Fernet.generate_key()
	f = Fernet(key)
	return f

def fernet_crypt(n, f):
	token = f.encrypt(bytes(n))
	return token

def fernet_dec(n, f):
	return f.decrypt(n)

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
	print("Iniciando...")
	palavra = 'papibaquigrafo'
	time.sleep(1)
	try:
		nome_cifra = 'Fernet'
		modelo = fernet_modelo()
		inicio = datetime.now()
		cifra = fernet_crypt(palavra, modelo)
		fim = datetime.now()
		gerar_cifra = get_time(inicio, fim)

		inicio = datetime.now()
		decriptado = fernet_dec(cifra, modelo)
		fim = datetime.now()
		decriptacao = get_time(inicio,fim)

		time.sleep(1)

		tcp.send(str(cifra))
	except Exception: 
		traceback.print_exc()
	finally:
		print("Encerrando")
		time.sleep(2)
		tcp.send(str('SAIR'))					
		run_thread = False
		tcp.close()
		print("="*10)
		print("Cifra: {}".format(nome_cifra))
		print("="*10)
		print("Tempo para encriptar:")
		print(gerar_cifra)
		print("Tempo para decriptar")
		print(decriptacao)
		print("-"*10)
		print("Tamanho da string original: {}".format(len(palavra)))
		print("Tamanho da cifra: {}".format(len(cifra)))
		print("-"*10)
		print("Cifra gerada: {}".format(cifra))
		print("-"*10)
		print("Tempo que chegou no destino: {}".format(tempo))
		print(type(tempo))
		print("="*10)

def listen(socket):
	#print 'Listener ligado!\n'
	global run_thread
	global tempo
	cont = 0
	while run_thread:
		recived = socket.recv(1024)
		if cont < 2:
			tempo = recived
			cont+=1
		else:
			print(recived)
	#print 'Listener desligado'

run_thread = False
h = 'localhost' #raw_input("Digite o host que deseja alcancar: ")
p = int(raw_input("Digite a porta a qual deseja conectar: "))
turn_on(h,p)
#print(conta(50))