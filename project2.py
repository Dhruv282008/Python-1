introstring = input("Enter your introduction : ")
charactercount = 0
wordcount = 1

for character in introstring:
    charactercount = charactercount + 1
    if (character == " "):
        wordcount += 1

print(wordcount)
print(charactercount)