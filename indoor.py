text=input("Enter your text:")
def change_letters(text):
    new_text=""
    if text.islower()==True:
        return(text)
    else:
        for i in text:
            if i.isalpha()==True:
                new_text+=i.lower()
            else:
                new_text+=i
        return(new_text)


result=change_letters(text)
print(result)
