from Word import Word

class Lowercase(Word):
    
    def __init__(self, words):
        super().__init__(words)

    def lowercase(self):
        items = []
        for item in self.words:
            items += [item.lower()]
        return items
