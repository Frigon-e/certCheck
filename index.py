from flask import Flask, request, render_template, send_from_directory
from frontend import Server

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("old.html")


@app.route("/", methods=['POST'])
def do_POST():
    text = request.form['lifesavingNumbers']
    webServer = Server(text)
    output = webServer.do_Thing()
    return output


@app.route('/staffCert.txt')
def download_to_browser():
    itemOne = send_from_directory(directory="/home/ebfrigon/code/",
                               filename="staffCert.txt",
                               mimetype="txt/csv")
    itemTwo = send_from_directory(directory="/home/ebfrigon/code/",
                               filename="staffCert2.txt",
                               mimetype="txt/csv")
    return itemOne, itemTwo

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
