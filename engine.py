from Word import Word
class Engine:

  pass


word1 = Word('Alexis')
word2 = Word('Angérs')
word3 = Word('élika')


def SwitchWord(word1,word2):
    all_word1 = word1.all_word_posibility()
    all_word2 = word2.all_word_posibility()
    for x in all_word1:
            for y in all_word2:
                print(x,y)
            
    print(all_word1,all_word2)


SwitchWord(word3,word2)


