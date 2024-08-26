### CREATING BUYABLE AND UPGRADE SETTERS ###
class buyable:
    def set(self, cost, cost_factor, money):
        self.cost = cost
        self.money = money
        self.cost_factor = cost_factor
   
### CLASS THAT CONTAINS PLAYER DATA ###
class player:
    def callMoney(money):
        player.money = money
        return player.money 

###PSEUDOCODE FOR UPGRADE CLASS###
#not functional yet, might scrap constructors for now and be a lazy shit, WE LOVE HARDCODING
class upgrade:
    #Setting cost parameters for the upgrade
    def set(self, cost, buyable, effect, magnitude, name, null):
        self.cost = cost
        if(effect == "exp"):
            buyable.money **= magnitude
        elif(effect == "mult"):
            buyable.money *= magnitude 

        #Text description for the upgrade, seperate bc it gets wordy if in just one function call
    def description(self, text):
        
        #Create a label that changes based on the hover of an upgrade
        pass

        #Checking if player can afford upgrade
    def affordable(self, cost):
        if(player.money > self.cost):
            return True
    