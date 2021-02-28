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


@app.route("/staffCertDownload")
def download_to_browser():
    return send_from_directory(app.config["default"],
                               filename="staffCert1.txt",
                               mimetype="txt/csv",
                               cache_timeout=0)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
