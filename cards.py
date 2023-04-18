import random
global playerDeck

class Card:
    def __init__(self, cardCategory, cardDescription, leftText = "Left", rightText = "Right", 
                 cardImage = "assets\cardImages\defaultCardImage.png",
                 leftCost=0, rightCost=0,leftHappiness=0,rightHappiness=0, 
                 leftHealth=0, rightHealth=0, leftSavings=0, rightSavings=0):
        
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
                    card = Card(row[0], row[1], row[2], row[3], "assets\cardImages\defaultCardImage.png", float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]))
                    playerDeck.addCard(card)
                line_count += 1

                #  For Debuging Decks:
                #print(f'Card #{line_count}: {row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]} {row[11]}')

        
playerDeck = Deck("Main Deck")
playerDeck.loadCards('cards_v1.csv')