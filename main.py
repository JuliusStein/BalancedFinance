from tkinter import *
from tkinter import ttk

click = 0
amount = 1
cost1 = 50

cash = 10000
health = 100
happiness = 100

age = 25
retirementAge = 65
savings = 0
savingsGoal = 1000000

morgage = False
car = False
student_loan = False
credit_card = False
married = False

rent_cost = 0
morgage_cost = 0
car_cost = 0
student_loan_cost = 0
credit_card_cost = 0

num_kids = 0

#--------------------- Window Defn -------------------------
window = Tk()
window.title("Money v Happy")
window.geometry('1200x900')

background_image = PhotoImage(file="hillandale.png")
background_label = Label(window, image=background_image)
background_label.place(x=475, y=175, relwidth=0.5, relheight=0.5)


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



#--------------- Header Bar ---------------------
lbl = Label(window, text="0")
lbl.place(x=10, y=10)

current = PhotoImage(file='current.png')
current.configure(width=120, height=120)
btn = Button(window, image=current, command=clicked)
btn.place(x=525, y=0)

cashLabel = Label(window, text="Cash")
cashLabel.place(x=150, y=100)
cashButton = Button(window, text="$"+str(cash), command=clicked)
cashButton.place(x=225, y=100)

happinessLabel = Label(window, text="Happiness")
happinessLabel.place(x=50, y=25)
happinessBar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
happinessBar.place(x=50, y=50)
happinessBar['value'] = happiness
happinessBar['maximum'] = 100
happinessBar['variable'] = happiness

healthLabel = Label(window, text="Health")
healthLabel.place(x=275, y=25)
healthBar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
healthBar.place(x=275, y=50)
healthBar['value'] = health
healthBar['maximum'] = 100
healthBar['variable'] = health

savingsLabel = Label(window, text="Savings")
savingsLabel.place(x=700, y=25)
savingsBar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
savingsBar.place(x=700, y=50)
savingsBar['value'] = savings
savingsBar['maximum'] = savingsGoal
savingsBar['variable'] = savings

ageLabel = Label(window, text="Age")
ageLabel.place(x=950, y=25)
ageBar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
ageBar.place(x=950, y=50)
ageBar['value'] = age
ageBar['maximum'] = retirementAge
ageBar['variable'] = age

#------------------------------------


ttk.Separator(window, orient=HORIZONTAL).place(x=0, y=150, width=1200)
#------------------------------------

#Game Space



window.mainloop()
