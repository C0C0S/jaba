import socket
import threading

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind(('localhost', 6666))

socket.listen(5)
print('Server is listening')

users = []

def sendall(data):
	for user in users:
		user.send(data)
		print('Data была отправлена')


def taken(user):
	print(f'Listening user')
	while True:
		data = user.recv(1024)
		sendall(data)
		print('Пришла data:', data.decode('utf-8'))


def start_server():
	while True:
		conn, adress = socket.accept()
		print(f'User: {adress} - connected')
		users.append(conn)
		proc1 = threading.Thread(target=taken,args=(conn,))
		proc1.start()


if __name__ == '__main__':
	start_server()
