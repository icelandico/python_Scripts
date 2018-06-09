pyg = 'ay'

userInput = input("Enter a word:")
if len(userInput) > 0 and userInput.isalpha():
    word = userInput.lower()
    first = word[0]
    if first == ('a' or 'e' or 'i' or 'o' or 'u'):
        new_word = word + pyg
        print (new_word)
    else:
        new_word = word[1:] + first + pyg
        print (new_word)
else:
    print ("Type a word or sentence")
