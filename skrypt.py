def program1(szukana):
    licznik = 0
    n=(input("|wpisz tekst|\n"))
    for a in n:
        if a == szukana:
            licznik+=1
    return licznik 
A= program1((input("|wpisz litere|\n")))
B= program1((input("|wpisz litere|\n")))
C = A-B
print (C)

