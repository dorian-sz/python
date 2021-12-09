def pontozas(pont):
    pontList = [["Elégtelen", 0 , 60], ["Elégséges",60, 70], ["Közepes", 70, 80],
                ["Jó", 80, 90], ["Jeles", 90, 100]]

    for i in pontList:
        if i[1] <= pont < i[2]:
            print("Eredménye: ", i[0])

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in xs:
    pontozas(i)
    
