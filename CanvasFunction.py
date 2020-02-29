from tkinter import *



def createCanvas(count,canvasFrame):

    can = Canvas(canvasFrame,width = 350,height = 350)
    if count ==0:
        pass
    elif count==1:
        can.create_line(20,340,60,340)  # the base



    elif count==2:
        can.create_line(20,340,60,340)  # the base
        can.create_line(40,340,40,100) # the pole



    elif count==3:
        can.create_line(20,340,60,340)  # the base
        can.create_line(40,340,40,100) # the pole
        can.create_line(40,100,150,100) # the extend


    elif count==4:
        can.create_line(20,340,60,340)  # the base
        can.create_line(40,340,40,100) # the pole
        can.create_line(40,100,150,100) # the extend
        can.create_line(150,100,150,160) # the rope



    elif count==5:
        can.create_line(20,340,60,340)  # the base
        can.create_line(40,340,40,100) # the pole
        can.create_line(40,100,150,100) # the extend
        can.create_line(150,100,150,160) # the rope
        def create_circle(x, y, r, canvasName): #the head
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r

            return canvasName.create_oval(x0,y0,x1,y1)

        create_circle(150,183,20,can)



    elif count==6:
        can.create_line(20,340,60,340)  # the base
        can.create_line(40,340,40,100) # the pole
        can.create_line(40,100,150,100) # the extend
        can.create_line(150,100,150,160) # the rope
        def create_circle(x, y, r, canvasName): #the head
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r

            return canvasName.create_oval(x0,y0,x1,y1)

        create_circle(150,183,20,can)
        can.create_line(150 ,205 ,150 ,250 ) # the body




    elif count==7:
        can.create_line(20,340,60,340)  # the base
        can.create_line(40,340,40,100) # the pole
        can.create_line(40,100,150,100) # the extend
        can.create_line(150,100,150,160) # the rope
        def create_circle(x, y, r, canvasName): #the head
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r

            return canvasName.create_oval(x0,y0,x1,y1)

        create_circle(150,183,20,can)
        can.create_line(150 ,205 ,150 ,250 ) # the body
        can.create_line(150,250,180,280)  #right leg


    elif count==8:
        can.create_line(20,340,60,340)  # the base
        can.create_line(40,340,40,100) # the pole
        can.create_line(40,100,150,100) # the extend
        can.create_line(150,100,150,160) # the rope
        def create_circle(x, y, r, canvasName): #the head
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r

            return canvasName.create_oval(x0,y0,x1,y1)

        create_circle(150,183,20,can)
        can.create_line(150 ,205 ,150 ,250 ) # the body
        can.create_line(150,250,180,280)  #right leg
        can.create_line(150,250,120,280) #left leg


    elif count == 9:
        can = Canvas(canvasFrame,width = 350,height = 350)
        can.create_line(20,340,60,340)  # the base
        can.create_line(40,340,40,100) # the pole

        can.create_line(40,100,150,100) # the extend

        can.create_line(150,100,150,160) # the rope



        def create_circle(x, y, r, canvasName): # the head
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r

            return canvasName.create_oval(x0,y0,x1,y1)

        create_circle(150,183,20,can)

        can.create_line(150 ,205 ,150 ,250 ) # the body

        can.create_line(150,250,180,280)  #right leg

        can.create_line(150,250,120,280) #left leg


        can.create_line(150,220,180,240) # right hand



    elif count == 10:
        can = Canvas(canvasFrame,width = 350,height = 350)
        can.create_line(20,340,60,340)  # the base
        can.create_line(40,340,40,100) # the pole

        can.create_line(40,100,150,100) # the extend

        can.create_line(150,100,150,160) # the rope



        def create_circle(x, y, r, canvasName): # the head
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r

            return canvasName.create_oval(x0,y0,x1,y1)

        create_circle(150,183,20,can)

        can.create_line(150 ,205 ,150 ,250 ) # the body

        can.create_line(150,250,180,280)  #right leg

        can.create_line(150,250,120,280) #left leg


        can.create_line(150,220,180,240) # right hand

        can.create_line(150,220,120,240) #left hand




    can.grid(row=1)
