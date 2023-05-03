import random
global playerDeck

def getCardImage(lineNum):
    if lineNum <= 100:
        return f"assets/card_images/{lineNum}.png"
    else:
        return f"assets/card_images/{lineNum-100}.png"

def getCategoryImage(category):
    if category == "Work":
        return "assets/card_categories/card_work_450X710-01.png"
    elif category == "Education":
        #return "assets/cardImages/education.png"
        return "assets/card_categories/card_education_450X710-01.png"
    elif category == "Happiness":
        return "assets/card_categories/card_happiness_450X710-01.png"
        #return "assets/cardImages/defaultCardImage.png"
    elif category == "Health":
        #return "assets/cardImages/health.png"
        return "assets/card_categories/card_health_450X710-01.png"
    elif category == "Travel":
        #return "assets/cardImages/travel.png"
        return "assets/card_categories/card_travel_450X710-01.png"
    elif category == "Investment":
        return "assets/card_categories/card_investment_450X710-01.png"
        #return "assets/cardImages/defaultCardImage.png"
    elif category == "Social":
        return "assets/card_categories/card_social_450X710-01.png"
        #return "assets/cardImages/defaultCardImage.png"
    elif category == "Housing":
        return "assets/card_categories/card_housing_450X710-01.png"
        #return "assets/cardImages/defaultCardImage.png"
    elif category == "Unexpected":
        return "assets/card_categories/card_unexpected_450X710-01.png"
        #return "assets/cardImages/defaultCardImage.png"
    elif category == "Relationship":
        #return "assets/cardImages/relationship.png"
        return "assets/card_categories/card_relationship_450X710-01.png"
    else:
        return "assets/card_categories/card_default.png"
    
class Card:
    def __init__(self, cardCategory, cardDescription, leftText = "Left", rightText = "Right", 
                 categoryImage = "assets\card_categories\card_default.png",
                 cardImage = "assets\card_images\default.png",
                 leftHappiness=0, leftHealth=0,leftCost=0,leftSavings=0, 
                 rightHappiness=0, rightHealth=0, rightCost=0, rightSavings=0):
        
        self.image = cardImage
        self.outline = categoryImage
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
            line_num = 0
            for row in csv_reader:
                if line_num != 0:
                    #cleaning up the data
                    row[1] = ''.join([i for i in row[1] if (i.isalnum() or i == ' ' or i == '.'or i=='!' or i=='?')])
                    #Create and add card
                    try:
                        card = Card(row[0], row[1], row[2], row[3], getCategoryImage(row[0]), getCardImage(line_num), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), float(row[10]), float(row[11]))
                        playerDeck.addCard(card)
                    except:
                        print(f'Error: {row}')
                line_num += 1

                #  For Debuging Decks:
                #print(f'Card #{line_count}: {row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]} {row[7]} {row[8]} {row[9]} {row[10]} {row[11]}')

        
playerDeck = Deck("Main Deck")
#playerDeck.loadCards('cards_v1.csv')
playerDeck.loadCards('cards_v2.csv')