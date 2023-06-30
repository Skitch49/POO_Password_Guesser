from Word import Word

class First_letter_uppercase(Word):
    
    def __init__(self, words):
        super().__init__(words)

    def first_letter_uppercase(self):
        items = []
        for item in self.words:
            items += [item.title()]
        return items