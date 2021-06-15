temp_s = False
s = 0
ss = 0

print("This program get the word, and say you how many litters \"s\" and \"ss\" in word")
word = list(input('word: '))
for x in word:
    if x == 's':
        s+=1
        if temp_s:
            ss+=1
            temp_s = False
        else:
            temp_s = True
    else:
        temp_s = False
        continue

print(s,ss)


