from flask import Flask, redirect, render_template, request, url_for
import requests

app: Flask = Flask(__name__, template_folder='../frontend')

@app.route("/")
def HomePage():
    return render_template('index.html')

@app.route("/search/<fileName>")
def search(fileName):
    output: dict = dict(requests.get(f"http://127.0.0.1:8000/file/search/{fileName}").json())
    return render_template("searchFormat.html", fileList=output['files'])

@app.route("/download/<fileName>")
def download(fileName) -> str:
    output: str = str(requests.get(f"http://127.0.0.1:8000/file/download/{fileName}").json())
    return render_template("successORfail.html", output=output)

@app.route("/search-html", methods=["GET"])
def searchHtml():
    return render_template('search.html')

@app.route("/download-html", methods=["GET"])
def downloadHtml():
    return render_template('Download.html')

@app.route("/search-form", methods=["GET"])
def searchForm():
    fileName = request.args.get('query')
    return redirect(url_for('search', fileName=fileName))

@app.route("/download-form", methods=["GET"])
def downloadForm():
    fileName = request.args.get('fileName')
    return redirect(url_for('download', fileName=fileName))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7070, debug=True)
