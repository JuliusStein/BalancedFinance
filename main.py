#----------------- Imports -------------------
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from cards import Card, Deck, playerDeck
import pygame

#----------------- Variables -------------------
global cash, health, happiness, age, retirementAge, savings, savingsGoal, lives
global morgage, car, student_loan, credit_card, married, rent_cost, morgage_cost
global student_loan_cost, credit_card_cost, num_kids, income, retirementPlanAmount

cash = 1000
health = 100
happiness = 100
lives = 1 #invisible to player

age = 18
retirementAge = 65
savings = 0
savingsGoal = 100000

morgage = False
car = False
student_loan = False
credit_card = False
married = False
dating = False

rent_cost = 750 
morgage_cost = 0
income = 1000
retirementPlanAmount = 150

num_kids = 0
#----------------- Window -------------------
global window
pygame.mixer.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/sounds/background.mp3'))

window = Tk()
window.title("Money Honeys")
window.geometry('1200x800')

#----------------- Functions -------------------
def playCardSound():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sounds/card.mp3'))

def resizeImage(file, width, height):
  image = Image.open(file)
  resize_image = image.resize((width, height))
  img = ImageTk.PhotoImage(resize_image)
  return img

from random import randint
def draw():
  playCardSound()
  #check if cash, happiness, or health is 0
  global cash, health, happiness, age, retirementAge, savings, savingsGoal
  global morgage, car, student_loan, credit_card, married, rent_cost, morgage_cost
  global car_cost, student_loan_cost, credit_card_cost, num_kids, lives
  if cash <= 0:
    if savings < 2500:
      endGame() #with a loss
    else:
      cash = 250
      savings -= 2500
  if (happiness <= 0) or (health <= 0):
    if lives > 0:
      lives -= 1
      happiness = 50
      health = 50
      keepGoing()
    else:
      endGame() #with a loss
  if savings >= savingsGoal:
    winGame()
  if age >= retirementAge:
    if savings >= savingsGoal:
      winGame() #with a win
    else:
      endGame() #with a loss

  global playerDeck
  playerDeck.shuffle()
  card = playerDeck.drawCard()
  return card

def homeScreen():
  global window
  top = Toplevel(window)
  top.geometry("750x250")
  top.title("Child Window")
  Label(top, text= "Hello World!", font=('Mistral 18 bold')).place(x=150,y=80)

def survey():
  #cash = tkSimpleDialog.askstring("Cash", "How much cash do you want to start with?")
  pass

def keepGoing():
  global window
  top = Toplevel(window)
  top.geometry("500x250")
  top.title("Keep going!")
  Label(top, text= "You're not doing so well - have a boost on the house", font=('Mistral 18 bold'), foreground="blue").place(x=50,y=70)


def endGame():
  global window
  top = Toplevel(window)
  top.geometry("500x250")
  top.title("Try Again")
  Label(top, text= "You didn't hit your goal :(", font=('Mistral 18 bold'), foreground='red').place(x=150,y=70)
  window.destroy()


def winGame():
  global window
  top = Toplevel(window)
  top.geometry("500x250")
  top.title("Winner")
  Label(top, text= "!! You Did It !!", font=('Mistral 18 bold'), foreground='green').place(x=150,y=70)
  window.destroy()


global currentCard
def updateCard():
  global window, cardText, cardImage, cardImageLabel, currentCard, leftText, rightText
  global cardCategory, cardCategoryLabel
  currentCard = draw()
  cardText.configure(text=currentCard.description)
  leftText.configure(text=currentCard.leftText)
  rightText.configure(text=currentCard.rightText)
  cardImage = resizeImage(currentCard.image, 300, 200)
  cardImageLabel.configure(image=cardImage)
  cardCategory = resizeImage(currentCard.outline,385, 560)
  cardCategoryLabel.configure(image=cardCategory)   

def applyCard(card, side):
  global cashLabel, cashButton, happinessLabel, happinessBar, healthLabel, healthBar, ageLabel, ageBar, savingsLabel, savingsBar, savingsGoalLabel, savingsGoalBar
  global cash, health, happiness, age, retirementAge, savings, savingsGoal, morgage, car, student_loan, credit_card, married, rent_cost, morgage_cost, car_cost, student_loan_cost, credit_card_cost, num_kids

  if side == "LEFT":
    cash += card.leftCost
    happiness += card.leftHappiness
    health += card.leftHealth
    savings += card.leftSavings
  elif side == "RIGHT":
    cash += card.rightCost
    happiness += card.rightHappiness
    health += card.rightHealth
    savings += card.rightSavings
  
  if happiness > 100:
    happiness = 100
  if health > 100:
    health = 100

  cashButton.configure(text="$" + str(cash))
  happinessBar.configure(value=happiness)
  healthBar.configure(value=health)
  savingsGoalBar.configure(value=savings)
  savingsGoalBar.configure(maximum=savingsGoal)
  savingsButton.configure(text="$" + str(savings))
  
def nextYear():
  global age, ageBar, ageLabel, ageNumberLabel, bear, bearButton, savings, cash, income
  global rent_cost, retirementPlanAmount, savingsGoal, savingsGoalBar, savingsButton

  age += 1
  ageNumberLabel.configure(text=str(age))
  ageBar.configure(value=age)
  ageBar.configure(maximum=retirementAge)
  if age >= retirementAge:
    ageLabel.configure(text="Retired")
    ageLabel.configure(foreground="red")
    ageLabel.place(x=1100, y=50)
    ageBar.configure(value=retirementAge)
    ageBar.configure(maximum=retirementAge)

  #Passive Income and Passive Debts?
  cash += (income - rent_cost - retirementPlanAmount)

  #Passive Savings deposit from income?
  savings *= 1.065
  savings += retirementPlanAmount
  savings = round(savings)
  savingsGoalBar.configure(value=savings)
  savingsButton.configure(text="$" + str(savings))

  #Update Bear
  satisfaction = (happiness + health) / 2

  if satisfaction >= 95:
    bear = resizeImage("assets/bear/bear_thriving_250X150-01.png", 175, 125)
  elif satisfaction >= 80:
    bear = resizeImage("assets/bear/bear_happy_250X150-01.png", 175, 125)
  elif satisfaction >= 65:
    bear = resizeImage("assets/bear/bear_neutral_250X150-01.png", 175, 125)
  elif satisfaction >= 50:
    bear = resizeImage("assets/bear/bear_sad_250X150-01.png", 175, 125)
  elif satisfaction >= 35:
    bear = resizeImage("assets/bear/bear_warning_250X150-01.png", 175, 125)
  else:
    bear = resizeImage("assets/bear/bear_warning_250X150-01.png", 175, 125)

  bearButton.configure(image=bear)           
    
def clickedLeft():
  global currentCard
  updateCard()
  applyCard(currentCard, "LEFT")
  nextYear()

def clickedRight():
  global currentCard
  updateCard()
  applyCard(currentCard, "RIGHT")
  nextYear()


#window.wm_attributes('-transparentcolor','grey')

#--------------- Header Bar ---------------------
headerImage = resizeImage('assets/static_elements/header_1200X150.png', 1200, 150)
lbl = Label(window, text="", image=headerImage)
lbl.place(x=0, y=0)
headerFont = ("Helvetica",12,"bold italic")
headerNumFont = ("Helvetica",12,"bold")

global bear, bearButton, cashLabel, cashButton, happinessLabel, happinessBar, healthLabel, healthBar, ageLabel, ageBar, savingsLabel, savingsBar, savingsGoalLabel, savingsGoalBar
bear = resizeImage("assets/bear/bear_happy_250X150-01.png", 175, 125)
bearButton = Button(window, image=bear, command=None)
bearButton.place(x=515, y=10)

cashLabel = Label(window, text="Cash", font=headerNumFont, bg='#483c33', fg='white')
cashLabel.place(x=215, y=105)
cashButton = Button(window, text="$"+str(cash), command=None, font=headerNumFont, bg='#483c33', fg='white')
cashButton.place(x=270, y=100)

happinessLabel = Label(window, text="Happiness", bg='#483c33', fg='white', font=headerFont)
happinessLabel.place(x=50, y=25)
happinessBar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
happinessBar.place(x=50, y=50)
happinessBar['value'] = happiness
happinessBar['maximum'] = 100
happinessBar['variable'] = happiness

healthLabel = Label(window, text="Health", bg='#483c33', fg='white', font=headerFont)
healthLabel.place(x=275, y=25)
healthBar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
healthBar.place(x=275, y=50)
healthBar['value'] = health
healthBar['maximum'] = 100
healthBar['variable'] = health

savingsGoalLabel = Label(window, text="Savings Goal", bg='#483c33', fg='white', font=headerFont)
savingsGoalLabel.place(x=770, y=25)
savingsGoalBar = ttk.Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
savingsGoalBar.place(x=770, y=50)
savingsGoalBar['value'] = savings
savingsGoalBar['maximum'] = savingsGoal
savingsGoalBar['variable'] = savings

savingsLabel = Label(window, text="Savings", font=headerNumFont, bg='#483c33', fg='white')
savingsLabel.place(x=770, y=105)
savingsButton = Button(window, text="$"+str(savings), command=None, font=headerNumFont, bg='#483c33', fg='white')
savingsButton.place(x=845, y=100)

ageLabel = Label(window, text="Age", bg='#483c33', fg='white', font=headerFont)
ageLabel.place(x=1010, y=25)
ageBar = ttk.Progressbar(window, orient=VERTICAL, length=120, mode='determinate')
ageBar.place(x=1050, y=5)
ageBar['value'] = age - 25
ageBar['maximum'] = retirementAge
ageBar['variable'] = age

ageNumberLabel = Label(window, text=str(age), font=headerNumFont, bg='#483c33', fg='white')
ageNumberLabel.place(x=1051, y=125)
retirementNumberLabel = Label(window, text=str(retirementAge), font=headerNumFont, bg='#483c33', fg='white')
retirementNumberLabel.place(x=1075, y=10)

#------------------------------------

ttk.Separator(window, orient=HORIZONTAL).place(x=0, y=150, width=1200)

#------------- Game Space -----------------------
#Background
backgroundImage = resizeImage('assets/static_elements/background_1200X700.png', 1200, 750)
backgroundLabel = Label(window, image=backgroundImage)
backgroundLabel.place(x=0, y=150)

#Card Outline
global cardCategory, cardCategoryLabel
cardCategory = resizeImage('assets/card_categories/card_default.png',385, 560)
cardCategoryLabel = Label(window, image=cardCategory, bg='#eee1b5')
cardCategoryLabel.place(x=415, y=200)

#Card Image
global cardImage, cardImageLabel
cardImage = resizeImage('assets/card_images/default.png', 150, 60)
cardImageLabel = Label(window, image=cardImage, bg='#eee1b5')
cardImageLabel.place(x=460, y=285)

#Card Text
global cardText
cardText = Label(window, text="This is the card text", bg='#eee1b5', fg='black', font=("Arial", 12), wraplength=300, justify=CENTER, width=35, height=7)
cardText.place(x=450, y=515)

#Card Left Button
global cardLeftButton
leftButton = resizeImage('assets/static_elements/leftButton_300X100.png', 300, 100)
cardLeftButton = Button(window, command=clickedLeft, bg='#eee1b5', fg='white', image=leftButton)
cardLeftButton.place(x=50, y=400)

#Left Button Text
global leftText
leftText = Label(window, text="Left", bg='#eee1b5', fg='black', font=("Arial Bold", 16),width=15, justify=CENTER)
leftText.place(x=100, y=440)
#leftText.bind("<Button-1>", lambda e:clickedLeft)

#Card Right Button
global cardRightButton
rightButton = resizeImage('assets/static_elements/rightButton_300X100.png', 300, 100)
cardRightButton = Button(window, command=clickedRight, bg='#eee1b5', fg='white', image=rightButton)
cardRightButton.place(x=860, y=400)

#Right Button Text
global rightText
rightText = Label(window, text="Right", bg='#eee1b5', fg='black', font=("Arial Bold", 16),width=15, justify=CENTER)
rightText.place(x=910, y=440)

#---------------- MAIN --------------------

global deck
deck = playerDeck

#homeScreen()
survey()

draw()
updateCard()

window.mainloop()

# if __name__ == "__main__":
#   deck = playerDeck
#   card = deck.drawCard()
#   pygame.mixer.init()
#   pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/sounds/background.mp3'))
#   window.mainloop()