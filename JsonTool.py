import json

class JsonTool():
    def __init__(self, osPathOrName, databaseTemplate={}):
        self.osPathOrName = osPathOrName
        self.database = databaseTemplate
        self.load()

    def create(self):
        with open(f"{self.osPathOrName}.json", "w") as js:
            json.dump(self.database,js)
        print("Created json file")

    def load(self):
        try:
            with open(f"{self.osPathOrName}.json", "r") as js:
                    self.database = json.load(js)
        except FileNotFoundError as e:
            self.create()

    def save(self):
        try:
            with open(f"{self.osPathOrName}.json", "w") as js:
                json.dump(self.database, js, indent=2)
            self.load()
        except Exception as e:
            print(e)