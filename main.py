import turtle, os

t = turtle.Turtle() # t is instance of class Turtle
t.up() #stops turtle from drawing
t.speed(0) #sets speed to 0
with open('appear.txt', 'r') as f:
    appe = f.read().splitlines() #appe is list of lines in file

#configurations for turtle
t.shape(appe[0])
t.shapesize(int(appe[1]))
t.color(appe[2])
t.speed(appe[3])

if os.path.exists('@key.txt'): #checks if path exists
    with open('@key.txt', 'r') as f:
        control = f.read().splitlines() #control is list of lines from file
else:
    with open('@key.txt', 'w') as f:
        control = ['w', 'a', 's', 'd']
        f.write('\n'.join(control))

def w():
    t.forward(5)
def s():
    t.backward(5)
def a():
    t.left(5)
def d():
    t.right(5)

screen = turtle.Screen() #instance of class Screen
screen.onkeypress(w, control[0])
screen.onkeypress(a, control[-3])
screen.onkeypress(s, control[-2])
screen.onkeypress(d, control[-1])
screen.listen()

turtle.mainloop() #loop
