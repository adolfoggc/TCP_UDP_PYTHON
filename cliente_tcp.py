import socket
import threading
import time

def menu():
	print '='*10
	print 'menu = Ver menu'
	print '1 = Dizer "oi"'
	print '='*10

def turn_on(HOST, PORT):
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST, PORT)
	tcp.connect(dest)
	listener = threading.Thread(target=listen, args=(tcp,))
	global run_thread
	run_thread = True
	listener.start()
	print 'Para sair use SAIR\n'
	msg = '-'
	while msg <> 'SAIR':
			if msg == 'menu':
				menu()
				msg = ''
			else:
				msg = raw_input()			
				tcp.send (msg)
				
				if msg == 'SAIR':
					run_thread = False
	tcp.close()

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
