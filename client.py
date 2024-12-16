## CLIENT ##

from functions import *
import socket


class client:
    def __init__(self, HOST:str="127.0.0.1", PORT:int=8080, fileName:str="") -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.SOCKET:
            self.SOCKET.connect((HOST, PORT))
            
            self.SOCKET.sendall(fileName.encode())

            CONTENT: str = self.SOCKET.recv(1024).decode()
            RECIEVED_SHA256_HASH: str = self.SOCKET.recv(1024).decode()
            CALCULATED_SHA256_HASH: str = calculate_SHA256_client(CONTENT)

            # print("REC : ", RECIEVED_SHA256_HASH)
            # print("CALC : ", CALCULATED_SHA256_HASH)
            # print("CONTENT : ", CONTENT)

            if RECIEVED_SHA256_HASH == CALCULATED_SHA256_HASH:
                print("File integrity verified")

                save_to_disk(CONTENT, fileName)

            else:
                print("File integrity verification failed")

            self.SOCKET.close()
