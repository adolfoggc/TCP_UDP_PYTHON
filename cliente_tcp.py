import socket

def turn_on(HOST, PORT):
	HOST = '127.0.0.1'     # Endereco IP do Servidor
	PORT = 5000            # Porta que o Servidor esta
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST, PORT)
	tcp.connect(dest)
	print 'Para sair use \CLOSE\n'
	msg = tcp.recv(1024)
	print(msg)
	msg = raw_input()
	while msg <> '\CLOSE':
	    tcp.send (msg)
	    msg = raw_input()

	tcp.close()


h = raw_input("Digite o host que deseja alcancar: ")
p = int(raw_input("Digite a porta a qual deseja enviar: "))
turn_on(h,p)
