import turtle as tw

# configuramos el mundo de tortugas
screen = tw.Screen()
screen.setup( 800, 600 )
screen.title( "Actividad 01" )

# creamos una tortuga
tortuga = tw.Turtle()
tortuga.shape( 'turtle' )
tortuga.setheading( 90 )
tortuga.speed( 4 )

# la preparamos para dibujar
tortuga.pensize( 5 )
tortuga.pencolor( "#00FFFF" )

# dibujamos
tortuga.penup()
tortuga.goto( 0, 0 )
tortuga.pendown()

tortuga.forward( 200 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 200 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.left( 90 )

tortuga.penup()
tortuga.goto(-100,100)
tortuga.pendown()
tortuga.right(90)
tortuga.forward(160)
tortuga.right(120)
tortuga.forward(160)
tortuga.right(120)
tortuga.forward(160)

tortuga.penup()
tortuga.goto(-100,200)
tortuga.pendown()
tortuga.right(120)
tortuga.forward(160)
tortuga.left(120)
tortuga.forward(160)
tortuga.left(120)
tortuga.forward(160)

tortuga.penup()
tortuga.goto(-100,-100)
tortuga.pendown()
tortuga.left(120)
tortuga.right(45)
tortuga.forward(50)
tortuga.left(45)
tortuga.forward(90)
tortuga.left(45)
tortuga.forward(50)
tortuga.left(45)
tortuga.forward(90)
tortuga.left(45)
tortuga.forward(50)
tortuga.left(45)
tortuga.forward(90)
tortuga.left(45)
tortuga.forward(50)
tortuga.left(45)
tortuga.forward(90)
tortuga.penup()

# eso es todo
tw.done()