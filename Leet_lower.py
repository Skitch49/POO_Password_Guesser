from Word import Word

class Leet_lower(Word):
    
    def __init__(self, words):
        self.words = words
        super().__init__(words)

    def leet_lower (self):
        items = []
        for item in self.words:
            s= item.lower()
            leet = {'a':'4','à':'4','á':'4','â':'4','ã':'4','ä':'4','å':'4','e':'3','é':'3','è':'3','ê':'3','ë':'3','i':'1','ì':'1','í':'1','î':'1','ï':'1','o':'0','ò':'0','ó':'0','ô':'0','õ':'0','ö':'0','l':'1','s':'5','b':'8','t':'7','z':'2','g':'6'}
            crypted = "".join(leet.get(k,k) for k in s)
            items += [crypted]
        return items 

    