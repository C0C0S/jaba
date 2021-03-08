import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 1234))


def listen_server():
	while True:
		data = client.recv(1024)
		print(data.decode('utf-8'))


def send_server():

	listen_thread = threading.Thread(target=listen_server)
	listen_thread.start()
	while True:
		client.send(input(':').encode('utf-8'))


if __name__ == '__main__':
	send_server()