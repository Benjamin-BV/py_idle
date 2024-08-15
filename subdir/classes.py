### CREATING BUYABLE AND UPGRADE SETTERS ###
class buyable:
    def set(self, cost, cost_factor, money):
        self.cost = cost
        self.money = money
        self.cost_factor = cost_factor



###PSEUDOCODE FOR UPGRADE CLASS###
#
#class upgrade:
#    def set(self, cost, buyable, effect, money):
#        self.cost = cost
#        if(effect == "exp"):
#            buyable.money **= money
#        elif(effect == "mult"):
#            buyable.money *= money 
