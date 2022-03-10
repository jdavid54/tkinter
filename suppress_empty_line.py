def read_all():
    f = open("tkinter_pacman.py", "r")
    text = f.read()  # all text as a string
    f.close()
    #print(text)
    return text.replace('\n\n','\n')

def read_text():
    f = open("tkinter_pacman.py", "r")
    text = f.readlines()   # array of lines
    f.close()
    return ''.join(map(lambda x: x, text)).replace('\n\n','\n')

text = read_all()

def save_text(text):
    f = open("tkinter_pacman2.py", "w")
    f.writelines(text)
    f.close()

#save_text(text)
print(text)
