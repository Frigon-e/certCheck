import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

class webscraper:
    allStaff = pd.DataFrame()
    allCerts = [
            "National Lifeguard - Pool",
            "National Lifeguard - Waterpark",
            "CPR-C",
            "Standard First Aid",
            "AED"]
    def get_Data(self, ids):
        url = "https://www.lifesaving.bc.ca/_PartialEUmembers"
        header = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-lauguage": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-length": "30",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.lifesaving.bc.ca",
            "referer": "https://www.lifesaving.bc.ca/members",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        namelist = []
        for id in ids:
            cleanDates = []
            cleanCerts = []
            dirtyCerts = []
            name = ""
            usefulCerts = []
            usefulDates = []
            
            payload = {"memberid": id, "current_only": "1"}
            s = requests.Session()
            s.headers = header
            r = s.post(url, data=payload)

            try:
                soup = BeautifulSoup(r.content, "html.parser").find(id='DivIdToPrint')
                name = soup.find(class_='ml-3')
                name = name.text
                name = name.replace("  ", " ")
                namelist.append(name)
                dirtyCerts = soup.find_all(class_="col-md-6")
            except:
                continue

            #https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
            for certs in dirtyCerts:
                certs = certs.text
                certs = certs.strip()
                certs = certs.replace(
                    'CPR - Level "C" /AED - valid 3 yr', "CPR-C/AED")
                certs = certs.replace(
                    "Standard First Aid (OFA 1 Equivalent)", "Standard First Aid")
                cleanCerts.append(certs)

            dirtyDates = soup.find_all(class_="col-md-3")
            for dates in dirtyDates:
                dates = dates.text
                dates = dates.strip()
                cleanDates.append(dates)
            cleanCerts.pop(0)
            cleanDates.pop(0)

            rowData = []
            for certNames in self.allCerts: 
                rowData.append(self.newest_Cert(cleanCerts, cleanDates, certNames))
                
            columnNames = self.allCerts
            rowData.insert(0, id)
            rowData.insert(1, name)
            columnNames.insert(0, "LSS#")
            columnNames.insert(1, "Name")

            person = pd.DataFrame([rowData], columns=list(columnNames))
            self.allStaff= self.allStaff.loc[~self.allStaff.index.duplicated(keep='first')]
            self.allStaff = self.allStaff.append(person, ignore_index=True)

    def newest_Cert(self, certs, dates, certName):
        indices = [i for i, x in enumerate(certs) if certName in x]
        if len(indices) > 1:
            newDates = [dates[x] for x in indices]
            return min(newDates)
        elif len(indices) == 1:
            return dates[indices[0]]
        else:
            return None

    def get_Cols(self):
        return list(self.allStaff.columns.values)
    
    def get_Rows(self):
        return list(self.allStaff.values.tolist())

    def to_Csv(self):
        self.allStaff.to_csv("staffCert.csv", index=True)

