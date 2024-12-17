from os.path import exists
import hashlib


def return_file_content(fileName:str) -> str | bytes:
    if not exists(fileName):
        return b"File Not Found"

    with open(f"{fileName}", "r+") as file:
        CONTENT: str = str(file.read())

    return CONTENT

def calculate_SHA256_server(fileName:str) -> str:
    SHA256_hash = hashlib.sha256()

    with open(f"{fileName}", "rb") as file:
        SHA256_hash.update(file.read())

    return SHA256_hash.hexdigest()

def calculate_SHA256_client(CONTENT:str) -> str:
    SHA256_hash = hashlib.sha256()
    SHA256_hash.update(CONTENT.encode())
    return SHA256_hash.hexdigest()

def save_to_disk(content:str, fileName:str) -> None:
    with open(f"{fileName}", "w+") as file:
        file.write(content)

