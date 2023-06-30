from Word import Word

class Uppercase(Word):
    
    def __init__(self, words):
        super().__init__(words)

    def uppercase(self):
        items = []
        for item in self.words:
            items += [item.upper()]
        return items
 