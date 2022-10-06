import unicodedata

class Word:
    
    def __init__(self, name):
        self.name = name


    def lowercase(self):
        return self.name.lower()

    def uppercase(self):
        return self.name.upper()

    def first_letter_uppercase(self):
        return self.name.title()

    # def leet(self):
    #     letters = {'a':'0','e':'3','i':'1','o':'0','l':'1','s':'5','b':'8','t':'7','z':'2','g':'6'}
    #     for i in self.name:
    #         if(i)


    def strip_accents(self):
        return ''.join(c for c in unicodedata.normalize('NFD', self.name)
            if unicodedata.category(c) != 'Mn')

    def all_word_posibility(self):
        return [self.name,self.lowercase(),self.uppercase(),self.first_letter_uppercase(),self.strip_accents()]
    # def leet(self):
    #     import re
    #     self = re.sub(u"[àáâãäåa]", '4', self.name)
    #     self = re.sub(u"[èéêëe]", '3', self.name)
    #     self = re.sub(u"[ìíîïi]", '1', self.name)
    #     self = re.sub(u"[òóôõöo]", '0', self.name)
    #     self = re.sub(u"[l]", '1', self.name)
    #     self = re.sub(u"[s]", '5', self.name)
    #     self = re.sub(u"[b]", '8', self.name)
    #     self = re.sub(u"[t]", '7', self.name)
    #     self = re.sub(u"[z]", '2', self.name)
    #     self = re.sub(u"[g]", '6', self.name)
    #     return self
