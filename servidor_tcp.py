import socket
import datetime
import time

def turn_on(PORT):
	HOST = ''              # Endereco IP do Servidor
	#PORT = 5000            # Porta que o Servidor esta
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	orig = (HOST, PORT)
	tcp.bind(orig)
	tcp.listen(1)
	print 'Iniciando servidor na porta', PORT
	reqnum = 0
	starting_time = datetime.datetime.now()
    #starting_time = datetime.strptime(starting_time, '%H:%M:%S')
	while True:
	    con, cliente = tcp.accept()
	    print 'Conectado por', cliente
	    con.send('Bem-vindo, meu citoplasma!')
	    try:
		    while True:
		        msg = con.recv(1024)
		        if not msg: break
		        if(msg != ''):
		        	print 'opa', cliente
		        	con.send(str('opa'))
		        if(msg == 'SAIR'):
					print 'Finalizando conexao do cliente', cliente
					con.send(str('\nBye bye, jovem padawan'))
       	
	    #print 'Finalizando conexao do cliente', cliente
	    finally:
	    	con.close()

p = int(raw_input("Digite a porta que deseja ouvir: "))
turn_on(p)