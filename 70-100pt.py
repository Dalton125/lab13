#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

enemy1 = drawpad.create_rectangle(110,120,170,180, fill="blue")
direction = 5
enemy2 = drawpad.create_rectangle(200,300,250,390, fill="green")
direction = 10
enemy3 = drawpad.create_rectangle(370,510,290,530, fill="yellow")
direction = 13

# Create your "enemies" here, before the class

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "blue")
       	    self.down.grid(row=0,column=1)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "yellow")
       	    self.left.grid(row=0,column=2)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "red")
       	    self.right.grid(row=0,column=3)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
       	    self.animate1()
       	    self.animate2()

	
	def animate(self):
	    global drawpad
	    global player
            global enemy1 
            x1, y1, x2, y2 = drawpad.coords(enemy1)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(enemy1, -(drawpad.winfo_width()) +(x2-x1), 0)
            drawpad.move(enemy1,direction,0)
            drawpad.after(10,self.animate)
            
	def animate1(self):
	    global drawpad
	    global player
            global enemy2
            x3, y3, x4, y4 = drawpad.coords(enemy2)
            if x4 > drawpad.winfo_width(): 
                drawpad.move(enemy2, -(drawpad.winfo_width()) +(x4-x3), 0)
            drawpad.move(enemy2,direction,0)
            drawpad.after(10,self.animate1)
        
        def animate2(self):
	    global drawpad
	    global player
            global enemy3 
            x5, y5, x6, y6 = drawpad.coords(enemy3)
            if x6 > drawpad.winfo_width(): 
                drawpad.move(enemy3, -(drawpad.winfo_width()) +(x6-x5), 0)
            drawpad.move(enemy3,direction,0)
            drawpad.after(10,self.animate2)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	  
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
		

app = MyApp(root)
root.mainloop()