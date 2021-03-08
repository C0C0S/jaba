import socket
import multiprocessing as mp
import threading

users = []


def listen_users(user):
    while True:
        data = user.recv(1024)
        for user1 in users:
            if user1 != user:
                user1.send(data)
        print(f'was send {data.decode("utf-8")} from {user.getsockname()}')


def main():
    while True:
        user, adress = server.accept()
        users.append(user)
        print(f'{user.getsockname()} connected')
        thread = threading.Thread(target=listen_users, args=(user,))
        thread.start()
        #proc = mp.Process(target=listen_users, args=(user,))
        #proc.start()
        # proc.join()


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 3254
    server.bind((host, port))
    server.listen(5)
    print('server listening')
    main()
