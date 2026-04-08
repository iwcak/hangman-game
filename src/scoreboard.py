import json

class Scoreboard:
    def __init__(self, file = "scores.json"):
        self.file = file

    def save(self, name, score):
        data = self.load()
        data.append({"name": name, "score": score})
        with open(self.file, "w") as f:
            json.dump(data, f)

    def load(self):
        try:
            with open(self.file) as f:
                return json.load(f)
        except:
            return []