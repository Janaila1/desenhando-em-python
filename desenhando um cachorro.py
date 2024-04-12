import turtle as t

t.screensize(500, 500)

# Contorno da cabeça
t.pensize(5)
t.home()
t.seth(0)
t.pd() # pendente
t.color('black')
t.circle(20, 80) # 0
t.circle(200, 30) # 1
t.circle(30, 60) # 2
t.circle(200, 29.5) # 3
t.color('black')
t.circle(20, 60) # 4
t.circle(-150, 22) # 5
t.circle(-50, 10) # 6
t.circle(50, 70) # 7

# Nariz
x_nariz = t.xcor()
y_nariz = t.ycor()
t.circle(30, 62) # 8
t.circle(200, 15) # 9

# Nariz
t.pu() 
t.goto(x_nariz, y_nariz + 25)
t.seth(90) 
t.pd()
t.begin_fill()
t.circle(10)
t.end_fill()

#  Olho 
t.pu()
t.goto(x_nariz + 48, y_nariz + 55)
t.seth(90)
t.pd()
t.begin_fill()
t.circle(8)
t.end_fill()

# Orelhas
t.pu()
t.color('#333333')
t.goto(x_nariz + 100, y_nariz + 110)
t.seth(182)
t.pd()
t.circle(15, 45)
t.color('black')
t.circle(10, 15)
t.circle(90, 70)
t.circle(25, 110)
t.rt(4)
t.circle(90, 70)
t.circle(10, 15)
t.color('#333333')
t.circle(15, 45)


# Corpo
t.pu()
t.color('black')
t.goto(x_nariz + 90, y_nariz - 30)
t.seth(-130)
t.pd()
t.circle(250, 28)
t.circle(10, 140)
t.circle(-250, 25)
t.circle(-200, 25)
t.circle(-50, 85)
t.circle(8, 145)
t.circle(90, 45)
t.circle(550, 5)

# Rabo
t.seth(0)
t.circle(60, 85)
t.circle(40, 65)
t.circle(40, 60)
t.lt(150)
t.circle(-40, 90)
t.circle(-25, 100)
t.lt(5)
t.fd(20)
t.circle(10, 60)

# Fazer a volta do rabo
t.rt(80)
t.circle(200, 35)


# Colarinho
t.pensize(20)
t.color('#0000FF')
t.circle(-200, 25)



