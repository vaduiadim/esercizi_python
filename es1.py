def find_and_replace(text, old_text, new_text):
    if len(old_text) == 0:
        return text
    newText = []
    i = 0
    while i < len(text):
        flag = True
        for t in range(0, len(old_text)):
            if flag:
                flag = text[i+t] == old_text[t]
        if flag:
            newText.append(new_text)
            i=i+len(old_text)
        else:
            newText.append(text[i])
            i=i+1
    return ''.join(newText)

print(find_and_replace("Oggi Lorenzo ammazza x", "x" , "Vadim Duia"))