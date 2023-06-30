from Word import Word
import unicodedata

class Strip_accents(Word):
    
    def __init__(self, words):
        super().__init__(words)

    def strip_accents(self):
        items = []
        for item in self.words:
            result =''.join(c for c in unicodedata.normalize('NFD', item)
                           if unicodedata.category(c) != 'Mn')
            items += [result]
        return items
       