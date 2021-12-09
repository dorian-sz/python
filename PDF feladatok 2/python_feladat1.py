def hetNapja(n):
    hetList = ["Hétfő", "Kedd", "Szerda", "Csütörtök",
               "Péntek", "Szombat", "Vasárnap"]
    return hetList[n-1]

loop = True
while loop:
    try:
        print(hetNapja(int(input("Adja meg a napot: "))))
        loop = False
    except IndexError:
        gotdata = 'null'
        print("A szám túl nagy")

    
