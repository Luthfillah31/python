def replace_word():
    string = "Hi guys, i am Luthfi, and i'm a male"
    print(string)
    word_to_replace = input("Enter the word you want to replace : ")
    word_replacement = input("Enter the replacement : ")
    print(string.replace(word_to_replace,word_replacement))

replace_word()