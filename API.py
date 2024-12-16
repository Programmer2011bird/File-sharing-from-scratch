from fastapi import FastAPI
import client
import os

app = FastAPI()


def searchForFiles(fileName:str, search_path:str):
    results: list[str] = []

    for root, dir, files in os.walk(search_path):
        if fileName in files:
            results.append(os.path.join(root, fileName))
    
    return results

@app.get("/file/search/{fileName}")
async def searchFileName(fileName:str):
    foundFiles = searchForFiles(fileName, "../testFiles")
    return {"files": foundFiles}

@app.get("/file/download/{fileName}")
async def getFile(fileName:str):
    CLIENT: client.client = client.client(fileName=f"./testFiles/{fileName}")
