import random

def obscure(message):
    i = 0
    st = ""
    while i < len(message):
        if i == random.randint((0+i-6),i) :
            st = st + " krrshh "
            i = i + 1
        else:
            st = st+message[i]
        i = i + 1
    
    return st

def cricri(message):
    st = "Bzt "
    st = st + message + " Bzt"
    return st