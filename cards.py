import random
global playerDeck

class Card:
    def __init__(self, cardCategory, cardDescription, leftText = "No", rightText = "Yes", cardImage = "",  cardCost=0, cardHappiness=0, cardHealth=0, cardSavings=0):
        self.image = cardImage
        self.description = cardDescription
        self.cost = cardCost
        self.happiness = cardHappiness
        self.health = cardHealth
        self.savings = cardSavings
        self.category = cardCategory
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
    
playerDeck = Deck("Main Deck")
card1 = Card("Category BB", "Description", "Left", "Right", "Image", 1, 2, 3, 4)
playerDeck.addCard(card1)

def addRelationshipCards():
    global playerDeck
    card2 = Card("Category", "Description", "Left", "Right", "Image", 4, 3, 2, 1)
    playerDeck.addCard(card2)