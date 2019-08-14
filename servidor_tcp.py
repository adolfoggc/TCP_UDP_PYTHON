import socket
import datetime


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
	    print 'Concetado por', cliente
	    con.send('Bem-vindo, meu citoplasma!')
	    while True:
	        msg = con.recv(1024)
	        if not msg: break
	        if(msg == '\REQNUM'):
	        	reqnum += 1
	        	print(str(reqnum))
	        elif(msg == '\UPTIME'):
	        	print(str(datetime.datetime.now() - starting_time))
	        else:
	        	print cliente, msg
	    print 'Finalizando conexao do cliente', cliente
	    con.close()

#p = int(input("Digite a porta que deseja ouvir: "))
turn_on(5000)