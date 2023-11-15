import json
from types import SimpleNamespace

class Parser:
    def parse_file(self, filename):
        with open(filename, 'r') as f:  
            return self.parse(f.read())

    def parse(self, content):
        # raise NotImplementedError
        data = json.loads(content)
    
        self.name = self.name_parse(data=data)
        #  self.name = "\"Mr Homer J Simpson\""
        return self
    
    #Wraps in input in quotation marks
    def quote_wrapper(self,data):
        return "\"" + data + "\""
    
    def name_parse(self, data):
        title = data["meta"].split("\"")[3]
        
        seperateNames = data["name"].split(", ")
        seperateNonSur = seperateNames[1].split(" ")

        fullName = title

        #Reduces any non forename or surname to an Initial
        for index, name in enumerate(seperateNonSur):
            if index == 0:
                fullName += " " + name
            else:
                fullName += " " + name[0]
        fullName += " " + seperateNames[0]
        fullName = self.quote_wrapper(data=fullName)

        return fullName
    