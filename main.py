temp = 0
s = 0
ss = 0

print("This program get the word, and say you how many litters \"s\" and \"ss\" in word")
word = list(input('word: '))
for x in word:
    if x == 's':
        if temp == 's':
            ss+=1
        else:
            s+=1
            temp = 's'
    else:
        continue




print(word)


