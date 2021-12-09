import turtle

def rajzolj_oszlopot(t, magassag):
    ertekList = [[0, 100, "green"], [100, 200, "yellow"], [200, 1000, "red"]]
    for i in ertekList:
        if i[0] < magassag < i[1]:
            t.fillcolor(i[2])
            t.begin_fill()
            t.left(90)

            t.forward(magassag)
            t.write(" "+ str(magassag))
            t.right(90)
            t.forward(40)
            t.right(90)
            t.forward(magassag)
            t.left(90)

            t.end_fill()
            t.penup()
            t.forward(10)
            t.pendown()

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.color("blue", "red")
Eszti.pensize(3)


xs = [48,117,200,240,160,260,220]
for m in xs:
    rajzolj_oszlopot(Eszti, m)
