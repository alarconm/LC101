def analyze_text(text):
    # your code here

    alphacount = 0
    ecount = 0
    text = text.lower()
    textl = len(text)
    for i in range(textl):
        if text[i].isalpha():
            alphacount += 1
        if text[i] == "e":
            ecount += 1
    percentage = (ecount / textl)*100
    print(type(percentage))
    finalstr = "The text contains"+str(alphacount)+"alphabetic characters, of which"+str(ecount)+"("+str(percentage)+"% are 'e'."

    return finalstr

print(analyze_text("Eeeee"))
