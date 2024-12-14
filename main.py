import socket


class websocket:
    def __init__(self, HOST:str="127.0.0.1", PORT:int=8080) -> None:
        self.HOST: str = HOST
        self.PORT: int = PORT

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.SOCKET:
            self.SOCKET.bind((HOST, PORT))
            self.SOCKET.listen()

            connection, address = self.SOCKET.accept()

            fileName: str = str(connection.recv(1024).decode()).split("\n")[-1]

            connection.close()


if __name__ == "__main__":
    WEBSOCKET: websocket = websocket()
