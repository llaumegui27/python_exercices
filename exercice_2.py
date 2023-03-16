import json

class ExerciceTwo:
     def __init__(self):
        self.Person = {
            "Name": "Guillaume Merat",
            "Age": "21",
            "Size": 175,
            "Birth": "21-09-2001",
            "City": "Rouen"
        }

     def _get_json(self):
          obj = json.dumps(self.Person, indent = 4)
          print(obj)

result = ExerciceTwo()
result._get_json()