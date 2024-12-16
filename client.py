## CLIENT ##

from functions import *
import socket


class client:
    def __init__(self, HOST:str="127.0.0.1", PORT:int=8080, fileName:str="") -> None:
        self.HOST: str = HOST
        self.PORT: int = PORT
        self.fileName: str = fileName

    def main(self) -> int:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.SOCKET:
            self.SOCKET.connect((self.HOST, self.PORT))
            
            self.SOCKET.sendall(self.fileName.encode())

            SERVER_MESSAGE: str = self.SOCKET.recv(4096).decode()
            CONTENT, RECIEVED_SHA256_HASH = SERVER_MESSAGE.split("|||")
            CALCULATED_SHA256_HASH: str = calculate_SHA256_client(CONTENT)

            # print("REC : ", RECIEVED_SHA256_HASH)
            # print("CALC : ", CALCULATED_SHA256_HASH)
            # print("CONTENT : ", CONTENT)

            if RECIEVED_SHA256_HASH == CALCULATED_SHA256_HASH:
                print("File integrity verified")
                save_to_disk(CONTENT, self.fileName)

                self.SOCKET.close()

                return 1

            else:
                print("File integrity verification failed")
                
                self.SOCKET.close()

                return 0
