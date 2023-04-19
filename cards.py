import random
global playerDeck

def getImageByCategory(category):
    if category == "Work":
        return "assets/cardImages/newJob.png"
    elif category == "Education":
        #return "assets/cardImages/education.png"
        return "assets/cardImages/defaultCardImage.png"
    elif category == "Happiness":
        return "assets/cardImages/raise.png"
        #return "assets/cardImages/defaultCardImage.png"
    elif category == "Health":
        #return "assets/cardImages/health.png"
        return "assets/cardImages/defaultCardImage.png"
    elif category == "Travel":
        #return "assets/cardImages/travel.png"
        return "assets/cardImages/defaultCardImage.png"
    elif category == "Investment":
        return "assets/cardImages/spendOrInvest.png"
        #return "assets/cardImages/defaultCardImage.png"
    elif category == "Social":
        return "assets/cardImages/joinOrNo.png"
        #return "assets/cardImages/defaultCardImage.png"
    elif category == "Housing":
        return "assets/cardImages/newJob.png"
        #return "assets/cardImages/defaultCardImage.png"
    elif category == "Unexpected":
        return "assets/cardImages/payCut.png"
        #return "assets/cardImages/defaultCardImage.png"
    elif category == "Relationship":
        #return "assets/cardImages/relationship.png"
        return "assets/cardImages/defaultCardImage.png"
    else:
        return "assets/cardImages/defaultCardImage.png"
    
class Card:
    def __init__(self, cardCategory, cardDescription, leftText = "Left", rightText = "Right", 
                 cardImage = "assets\cardImages\defaultCardImage.png",
                 leftHappiness=0, leftHealth=0,leftCost=0,leftSavings=0, 
                 rightHappiness=0, rightHealth=0, rightCost=0, rightSavings=0):
        
        self.image = cardImage
        self.description = cardDescription
        self.category = cardCategory
        self.leftCost = leftCost
        self.rightCost = rightCost
        self.leftHappiness = leftHappiness
        self.rightHappiness = rightHappiness
        self.leftHealth = leftHealth
        self.rightHealth = rightHealth
        self.leftSavings = leftSavings
        self.rightSavings = rightSavings
        self.leftText = leftText
        self.rightText = rightText

class Deck:
    def __init__(self, deckName):
        self.deckName = deckName
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def addCards(self, cards):
        self.cards.extend(cards)
    
    def removeCard(self, card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()
    
    def getCard(self, index):
        return self.cards[index]
    
    def loadCards(self, pathToCSV):
        import csv
        global playerDeck
        with open(pathToCSV) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    #cleaning up the data
                    row[1] = ''.join([i for i in row[1] if (i.isalnum() or i == ' ' or i == '.'or i=='!' or i=='?')])
                    #Create and add card
                    card = Card(row[0], row[1], row[2], row[3], getImageByCategory(row[0]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]))
                    playerDeck.addCard(card)
                line_count += 1

                #  For Debuging Decks:
                #print(f'Card #{line_count}: {row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]} {row[11]}')

        
playerDeck = Deck("Main Deck")
playerDeck.loadCards('cards_v1.csv')