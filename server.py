import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 1234))

server.listen(5)
print('server is listening')

users = []


def send_all(data):
	for user in users:
		user.send(data)
	print('data была отправлена')


def listen_user(user):
	print(f'listening user')
	while True:
		data = user.recv(1024)
		send_all(data)
		print('пришла data:', data.decode('utf-8'))


def start_server():
	while True:
		user_sock, adress = server.accept()

		print(f'User: {adress} - connected')

		users.append(user_sock)
		listen_thread = threading.Thread(
			target=listen_user,
			args=(user_sock,)
		)
		listen_thread.start()


if __name__ == '__main__':
	start_server()