
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse

from webscraper import webscraper

hostName = "0.0.0.0"
serverPort = 8080 


class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        data = self.getRequestData()
        allData = data['ids']

        ids = allData.split()
        tester = webscraper()
        tester.get_Data(ids)
        colNames = tester.get_Cols()
        allData = tester.get_Rows()

        
        print(tester.allStaff)
        self.set_headers(200)
        self.wfile.write(bytes("{}".format(self.get_output(colNames, allData)), "utf-8"))
    
    def get_output(self, cols, rows):
        output = "<table>"
        output = output + "<tr>"
        for x in cols:
            output = output + "<th>" + str(x) + "</th>" 
        output = output + "</tr>"
        for x in rows:
            output = output + "<tr>"
            for y in x:
                output = output + "<td>" + str(y) + "</td>"
            output = output + "</tr>"
        output = output + "</table>"
        return output

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
