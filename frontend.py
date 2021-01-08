
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse

from webscraper import webscraper

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        data = self.getRequestData()
        allData = data['ids']

        ids = allData.split()
        tester = webscraper()
        tester.get_Data(ids)

        self.set_headers(200)
        self.wfile.write(bytes("<h1>things and stuff</h1>", "utf-8"))
        self.wfile.write(bytes("<h2> Testing another lvl</h2>", "utf-8"))

    def getRequestData(self):
        body = self.rfile.read(int(self.headers.get('Content-Length')))
        body = body.decode("utf-8")
        return dict(parse.parse_qsl(body))

    def getParams(self):
        output = {}
        queryList = parse.parse_qs(parse.urlsplit(self.path).query)
        for key in queryList:
            if len(queryList[key]) == 1:
                output[key] = queryList[key][0]
        return output

    def set_headers(self, responseCode):
        self.send_response(responseCode)
        self.send_header("Content-type", "text/html")
        self.send_header('Access-Control-Allow-Origin', "*")
        self.send_header('Access-Control-Allow-Headers', "*")
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except:
        webServer.server_close()
        print("Server stopped.")
        sys.exit()
    webServer.server_close()
    print("Server stopped.")
    sys.exit()
