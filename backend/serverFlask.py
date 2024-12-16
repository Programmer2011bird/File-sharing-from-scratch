from flask import Flask, render_template
import requests

app: Flask = Flask(__name__, template_folder='../frontend')

@app.route("/")
def HomePage():
    return render_template('index.html')

@app.route("/search/<fileName>")
def search(fileName):
    output: dict = dict(requests.get(f"http://127.0.0.1:8000/file/search/{fileName}").json())
    return f"<h1>{output['files']}</h1>"

@app.route("/download/<fileName>")
def download(fileName) -> str:
    output: str = str(requests.get(f"http://127.0.0.1:8000/file/download/{fileName}").json())
    return f"<h1>{output}</h1>"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7070, debug=True)

