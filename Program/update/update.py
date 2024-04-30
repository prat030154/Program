import os

class update:
    def __init__(self):
        pass
    def get_programUpdate(self):
        print("getting update")
        os.system("curl -o D:/Project/Terminal/file/update/update.json https://prat030154.github.io/Program/update.json")
        os.system("curl -o D:/Project/Terminal/file/update/package.py https://prat030154.github.io/Program/package.py")
        os.system("curl -o D:/Project/Terminal/file/update/updatelog.txt https://prat030154.github.io/Program/updatelog.txt")

    def run_programUpdate(self):
        os.system("del D:/Project/Terminal/file/update/update.json")
        os.system("del D:/Project/Terminal/file/update/package.py")
        os.system("del D:/Project/Terminal/file/update/updatelog.txt")
