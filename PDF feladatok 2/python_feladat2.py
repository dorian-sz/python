  def hetNapja(indulas, tavol):
    hetList = ["Hétfő", "Kedd", "Szerda", "Csütörtök",
               "Péntek", "Szombat", "Vasárnap"]
    return hetList[(indulas + tavol) % 7 - 1]

loop = True
while loop:
    try:
        print(hetNapja(int(input("Hányas számú napon indult: ")),
                       int(input("Hány napig volt távol: "))))
        loop = False
    except IndexError:
        gotdata = 'null'
        print("A szám túl nagy")

    
