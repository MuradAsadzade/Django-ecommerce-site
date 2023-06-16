
azen_eq={
    'ü':'u','ö':'o','ş':'sh',"ğ":"gh","ç":"ch","ı":"i","ə":"e",
    'Ü':'U','Ö':'O','Ş':'Sh',"Ğ":"Gh","Ç":"Ch","I":"İ","Ə":"E",
}

def get_slug(text):
    result=""
    for letter in text:
        if letter.isalnum():
            result+=azen_eq.get(letter,letter)
        elif letter==" ":
            result+='-'
    return result
        