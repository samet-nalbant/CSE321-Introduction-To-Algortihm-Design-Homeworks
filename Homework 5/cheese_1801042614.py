class Cheese:
    def __init__(self,weight_init,price_init):
        self.weight = weight_init
        self.price = price_init
        
    def getRate(self):
        return self.weight/self.price


def order_by_price_rate(inventory):
    for i in range(0,len(inventory)):
        for j in range(i, len(inventory)):
            if inventory[i].getRate() > inventory[j].getRate() :
                temp = inventory[i]
                inventory[i] = inventory[j]
                inventory[j] = temp

def find_max_price(inventory, weight):
    order_by_price_rate(inventory)
    i=0
    max_price=0
    while True:
        if(inventory[i].weight <= weight):
            max_price+= inventory[i].price
            weight-=inventory[i].weight
        else:
            max_price+= inventory[i].price*(weight/inventory[i].weight)
            break
        i+=1

    return max_price


inventory = [Cheese(10,60),Cheese(20,100),Cheese(30,120)]
print(find_max_price(inventory,50))