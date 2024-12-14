import socket


class client:
    def __init__(self, HOST:str="127.0.0.1", PORT:int=8080, fileName:str="") -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.SOCKET:
            self.SOCKET.connect((HOST, PORT))

            self.SOCKET.sendall(fileName.encode())
            print(self.SOCKET.recv(1024).decode())

            self.SOCKET.close()


if __name__ == "__main__":
    CLIENT: client = client(fileName="todos.txt")
