from tkinter import *
from tkinter import ttk

click = 0
amount = 1
cost1 = 50

amt_cash = 10000
amt_ira = 0
amt_bonds = 0
amt_stocks = 0
amt_roth = 0
amt_401k = 0
amt_403b = 0

morgage = False
car = False
student_loan = False
credit_card = False
married = False

rent_cost = 0
morgage_cost = 0
utilities_cost = 0
food_costs = 0
car_cost = 0
student_loan_cost = 0
credit_card_cost = 0

num_kids = 0

#--------------------- Window Defn -------------------------
window = Tk()
window.title("Clicker game")
window.geometry('800x600')

background_image = PhotoImage(file="hillandale.png")
background_label = Label(window, image=background_image)
background_label.place(x=160, y=0, relwidth=0.6, relheight=1)


#----------------- Functions -------------------

from random import randint
def rollCard():
  roll = randint(1, 5)
  if roll <= 1:
    print("You got a good card!")
  elif roll <= 2:
    print("You got no card.")
  elif roll <= 3:
    print("You got no card.")
  elif roll <= 4:
    print("You got no card.")
  elif roll <= 5:
    print("You got a bad card!") 

def clicked():
  rollCard()

  global click
  global amount
  click += amount
  lbl.configure(text=click)

def buy1():    
  global amount    
  global click    
  global cost1    
  if click >= cost1:    
    click = click - cost1    
    amount = amount + 1    
    cost1 = round(cost1*1.15)   
    milk_man.configure(text="$"+str(cost1))
    lbl.configure(text=click)

#--------------- Current You ---------------------
lbl = Label(window, text="0")
lbl.place(x=10, y=10)

current = PhotoImage(file='current.png')
current.configure(width=100, height=100)
btn = Button(window, image=current, command=clicked)
btn.place(x=10, y=30)

cashLabel = Label(window, text="Cash")
cashLabel.place(x=10, y=150)
cashButton = Button(window, text="$"+str(amt_cash), command=buy1)
cashButton.place(x=10, y=170)

rentLabel = Label(window, text="Rent")
rentLabel.place(x=10, y=200)
rent_amt = Label(window, text="$"+str(rent_cost))
rent_amt.place(x=10, y=220)

foodLabel = Label(window, text="Food Costs")
foodLabel.place(x=10, y=250)
food_amt = Label(window, text="$"+str(food_costs))
food_amt.place(x=10, y=270)

ttk.Separator(window, orient=VERTICAL).place(x=150, y=0, height=500)
#------------------------------------

#Game Space

#----------------- Future You -------------------
ttk.Separator(window, orient=VERTICAL).place(x=650, y=0, height=500)

lbl2 = Label(window, text="0")
lbl2.place(x=680, y=10)

future = PhotoImage(file='future.png')
future.configure(width=100, height=100)
btn = Button(window, image=future, command=clicked)
btn.place(x=680, y=30)

bondLabel = Label(window, text="Bonds")
bondLabel.place(x=680, y=150)
bondVal = Label(window, text="$"+str(amt_bonds))
bondVal.place(x=680, y=170)

stockLabel = Label(window, text="Stocks")
stockLabel.place(x=680, y=200)
stockVal = Label(window, text="$"+str(amt_stocks))
stockVal.place(x=680, y=220)

iraLabel = Label(window, text="IRA")
iraLabel.place(x=680, y=250)
iraVal = Label(window, text="$"+str(amt_ira))
iraVal.place(x=680, y=270)

#--------------------------------------------

window.mainloop()
