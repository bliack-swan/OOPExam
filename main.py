class Algorithm:
    def __init__(self,word):
        self.temp_s = False
        self.s = 0
        self.ss = 0
        self.word = list(word)
    def algo(self):
        for x in self.word:
            if x == 's':
                self.s+=1
                if self.temp_s:
                    self.ss+=1
                    self.temp_s = False
                else:
                    self.temp_s = True
            else:
                self.temp_s = False
                continue
    def get_result( self ):
        return self.s, self.ss
    def get_word( self ):
        return self.word


print("This program get the word, and say you how many litters \"s\" and \"ss\" in word")
word = input ("word: ")
a = Algorithm(word)
a.algo()
s,ss=a.get_result()
print(s,ss)



