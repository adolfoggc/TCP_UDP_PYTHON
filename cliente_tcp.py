import socket
import threading

def turn_on(HOST, PORT):
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST, PORT)
	tcp.connect(dest)
	listener = threading.Thread(target=listen, args=(tcp,))
	global run_thread
	run_thread = True
	listener.start()
	print 'Para sair use \CLOSE\n'
	msg = raw_input()
	while msg <> '\CLOSE':
			print 'Esperando mensagem'
			tcp.send (msg)
			msg = raw_input()
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
h = raw_input("Digite o host que deseja alcancar: ")
p = int(raw_input("Digite a porta a qual deseja enviar: "))
turn_on(h,p)
