## SERVER ##

import hashlib
from os.path import exists
import socket


def return_file_content(fileName:str) -> str | bytes:
    if not exists(fileName):
        return b"File Not Found"

    with open(f"{fileName}", "r+") as file:
        CONTENT: str = str(file.read())

    return CONTENT


class server:
    def __init__(self, HOST:str="127.0.0.1", PORT:int=8080) -> None:
        self.HOST: str = HOST
        self.PORT: int = PORT

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.SOCKET:
            self.SOCKET.bind((HOST, PORT))
            self.SOCKET.listen()
            
            while True:
                connection, address = self.SOCKET.accept()

                fileName: str = str(connection.recv(1024).decode()).split("\n")[-1]
                content: str | bytes = return_file_content(fileName)
    
                if type(content) == bytes and content.decode() == "File Not Found":
                    print(f"[{address[0]}:{address[1]}] {fileName} -> Status : ERROR > File Not Found")
                    connection.close()
    
                else:
                    connection.sendall(content.encode())
                    print(f"[{address[0]}:{address[1]}] {fileName} -> Status : OK")
                    connection.close()


if __name__ == "__main__":
    WEBSOCKET: server = server()
