import random

class ExerciceOne:
    def __init__(self):
        self.randomSentences = [
            "Je veux et j'exige d'exquises excuses.",
            "En Sicile, Cécile a les cils plus lisses que les lys d'Alice.",
            "Six cent six suisses sucent six cent six saucisses dont six en sauce et six sans sauce.",
            "Les chaussettes de l’archi-duchesse, sont-elles sèches ou archi-sèches ?",
            "Natacha n'attacha pas son chat Pacha qui s'échappa.",
            "Cela fâcha Sacha qui chassa son chat Natacha."
            ]
        
    def _get_one(self):
        randomInt = random.randint(0, len(self.randomSentences) - 1)
        print(self.randomSentences[randomInt])
    
result = ExerciceOne()
result._get_one()
