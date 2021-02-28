from webscraper import webscraper
from urllib import parse
from urllib import parse
from webscraper import webscraper


def get_output(cols, rows):
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


class Server:
    def __init__(self, data):
        self.allData = data

    def do_Thing(self):
        ids = self.allData.split()

        tester = webscraper()
        tester.get_Data(ids)
        colNames = tester.get_Cols()
        allData = tester.get_Rows()

        return("{}".format(get_output(colNames, allData)))

 #   def getRequestData(self):
 #       body = self.rfile.read(int(self.headers.get('Content-Length')))
 #       body = body.decode("utf-8")
 #       return dict(parse.parse_qsl(body))

 #   def getParams(self):
 #       output = {}
 #       queryList = parse.parse_qs(parse.urlsplit(self.path).query)
 #       for key in queryList:
 #           if len(queryList[key]) == 1:
 #               output[key] = queryList[key][0]
 #       return output
