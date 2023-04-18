#----------------- Imports -------------------
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from cards import Card, Deck, playerDeck, addRelationshipCards

#----------------- Variables -------------------
click = 0
amount = 1

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
#----------------- Functions -------------------

def resizeImage(file, width, height):
  image = Image.open(file)
  resize_image = image.resize((width, height))
  img = ImageTk.PhotoImage(resize_image)
  return img

from random import randint
def draw():
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
  draw()

  global click
  global amount
  click += amount
  lbl.configure(text=click)

def clickedLeft():
  global amount
  amount -= 1

def clickedRight():
  global amount
  amount += 1

#----------------- Window -------------------

window = Tk()
window.title("Money v Happy")
window.geometry('1200x900')
#window.wm_attributes('-transparentcolor','grey')

#--------------- Header Bar ---------------------
headerImage = resizeImage('assets/header_1200x150.png', 1200, 150)
lbl = Label(window, text="0", image=headerImage)
lbl.place(x=0, y=0)

bear = resizeImage("assets/bear_happy_150X150.png", 125, 125)
bearButton = Button(window, image=bear, command=clicked)
bearButton.place(x=550, y=10)

cashLabel = Label(window, text="Cash", font=("Arial", 12), bg='#565040', fg='white')
cashLabel.place(x=215, y=100)
cashButton = Button(window, text="$"+str(cash), command=clicked, font=("Arial", 10), bg='#565040', fg='white')
cashButton.place(x=270, y=100)

happinessLabel = Label(window, text="Happiness", bg='#565040', fg='white', font=("Arial", 10))
happinessLabel.place(x=50, y=25)
happinessBar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
happinessBar.place(x=50, y=50)
happinessBar['value'] = happiness
happinessBar['maximum'] = 100
happinessBar['variable'] = happiness

healthLabel = Label(window, text="Health", bg='#565040', fg='white', font=("Arial", 10))
healthLabel.place(x=275, y=25)
healthBar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
healthBar.place(x=275, y=50)
healthBar['value'] = health
healthBar['maximum'] = 100
healthBar['variable'] = health

savingsGoalLabel = Label(window, text="Savings Goal", bg='#565040', fg='white', font=("Arial", 10))
savingsGoalLabel.place(x=770, y=25)
savingsGoalBar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
savingsGoalBar.place(x=770, y=50)
savingsGoalBar['value'] = savings
savingsGoalBar['maximum'] = savingsGoal
savingsGoalBar['variable'] = savings

savingsLabel = Label(window, text="Savings", font=("Arial", 12), bg='#565040', fg='white')
savingsLabel.place(x=770, y=100)
savingsButton = Button(window, text="$"+str(savings), command=clicked, font=("Arial", 10), bg='#565040', fg='white')
savingsButton.place(x=845, y=100)

ageLabel = Label(window, text="Age", bg='#565040', fg='white', font=("Arial", 10))
ageLabel.place(x=1010, y=25)
ageBar = ttk.Progressbar(window, orient=VERTICAL, length=120, mode='determinate')
ageBar.place(x=1050, y=5)
ageBar['value'] = age
ageBar['maximum'] = retirementAge
ageBar['variable'] = age

ageNumberLabel = Label(window, text=str(age), font=("Arial", 10), bg='#565040', fg='white')
ageNumberLabel.place(x=1051, y=125)
retirementNumberLabel = Label(window, text=str(retirementAge), font=("Arial", 10), bg='#565040', fg='white')
retirementNumberLabel.place(x=1075, y=10)

#------------------------------------

ttk.Separator(window, orient=HORIZONTAL).place(x=0, y=150, width=1200)

#------------- Game Space -----------------------
#Background
backgroundImage = resizeImage('assets/background_1200x750.png', 1200, 750)
backgroundLabel = Label(window, image=backgroundImage)
backgroundLabel.place(x=0, y=150)

#Card Outline
img = resizeImage('assets/blankCard.png',370, 550)
cardOutlineLabel = Label(window, image=img, bg='#565040')
cardOutlineLabel.place(x=425, y=200)

#Card Image
cardImage = resizeImage('assets/blankCard.png', 320, 270)
cardImageLabel = Label(window, image=cardImage, bg='#565040')
cardImageLabel.place(x=450, y=225)

#Card Text
cardText = Label(window, text="This is the card text", bg='#565040', fg='white', font=("Arial", 10), wraplength=300, justify=CENTER)
cardText.place(x=470, y=500)

#Left Text
leftText = Label(window, text="Left", bg='#565040', fg='white', font=("Arial", 10),width=10)
leftText.place(x=250, y=425)

#Right Text
rightText = Label(window, text="Right", bg='#565040', fg='white', font=("Arial", 10),width=10)
rightText.place(x=900, y=425)

#Card Left Button
leftButton = resizeImage('assets/leftButton.png', 79, 79)
cardLeftButton = Button(window, command=clickedLeft, bg='#565040', fg='white', image=leftButton)
cardLeftButton.place(x=250, y=450)

#Card Right Button
rightButton = resizeImage('assets/rightButton.png', 79, 79)
cardRightButton = Button(window, command=clickedRight, bg='#565040', fg='white', image=rightButton)
cardRightButton.place(x=900, y=450)

#------------------------------------

cardText.configure(text="This is the card text "*30)

deck = playerDeck
card = deck.drawCard()
print(card.category)

window.mainloop()
