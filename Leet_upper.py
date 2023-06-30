from Word import Word

class Leet_upper(Word):
    
    def __init__(self, words):
        self.words = words
        super().__init__(words)

    def leet_upper (self):
        items = []
        for item in self.words:
            s= item.upper()
            leet = {'A':'4','À':'4','Á':'4','Â':'4','Ã':'4','Ä':'4','Å':'4','E':'3','É':'3','È':'3','Ê':'3','Ë':'3','I':'1','Ì':'1','Í':'1','Î':'1','Ï':'1','O':'0','Ò':'0','Ó':'0','Ô':'0','Õ':'0','Ö':'0','L':'1','S':'5','B':'8','T':'7','Z':'2','G':'6'}
            crypted = "".join(leet.get(k,k) for k in s)
            items += [crypted]
        return items 

    