class Order:

    def __init__ (self, meal, items):
        self.meal = meal
        self.items = items
        self.output = ""

        if (self.meal == "Breakfast"):
            print (self.checkBreakfast ())
        elif (self.meal == "Lunch"):
            print (self.checkLunch ())
        elif (self.meal == "Dinner"):
            print (self.checkDinner ())
    
    def checkBreakfast (self):
        menu = ["Eggs", "Toast", "Coffee"]
        output = ""
        if (self.items.count (1) == 0):
            output = "Unable to process: Main is missing"
            if (self.items.count(2) == 0):
                output += ", side is missing"
            return output
        if (self.items.count (2) == 0):
            output = "Unable to process: Side is missing"
            return output
        output += menu[0]
        if (self.items.count(1) > 1):
            output = "Unable to process: " + menu[0] + " cannot be ordered more than once"
            return output
        else:
            output += ", "
        output += menu[1]      
        if (self.items.count (2) > 1):
            output = "Unable to process: " + menu[1] + " cannot be ordered more than once"
            return output
        if (self.items.count (3) == 1):
            output += ", "+menu[2]
        elif (self.items.count(3) > 1):
            output += ", " + menu[2] + "("+str(self.items.count(3))+ ")"
        else:
            output += ", Water"
        return output
        

    def checkLunch (self):
        menu = ["Salad", "Chips", "Soda"]
        output = ""
        if (self.items.count (1) == 0):
            output = "Unable to process: Main is missing"
            if (self.items.count(2) == 0):
                output += ", side is missing"
            return output
        if (self.items.count (2) == 0):
            output = "Unable to process: Side is missing"
            return output
        output += menu[0]
        if (self.items.count(1) > 1):
            output = "Unable to process: " + menu[0] + " cannot be ordered more than once"
            return output
        else:
            output += ", "
        output += menu[1]      
        if (self.items.count (2) > 1):
            output += "("+str(self.items.count(2))+ ")"
            
        if (self.items.count (3) == 1):
            output += ", "+menu[2]
        elif (self.items.count(3) > 1):
            output = "Unable to process: " + menu[2] + " cannot be ordered more than once"
            return output
        else:
            output += ", Water"
        return output

    def checkDinner (self):
        menu = ["Steak", "Potatoes", "Wine", "Cake"]
        output = ""
        if (self.items.count (1) == 0):
            output = "Unable to process: Main is missing"
            if (self.items.count(2) == 0):
                output += ", side is missing"
            if (self.items.count(3) == 0):
                output += ", dessert is missing"
            return output
        if (self.items.count (2) == 0):
            output = "Unable to process: Side is missing"
            if (self.items.count(3) == 0):
                output += ", dessert is missing"
            return output
        if (self.items.count (4) == 0):
            output = "Unable to process: Dessert is missing"
            return output
        output += menu[0]
        if (self.items.count(1) > 1):
            output = "Unable to process: " + menu[0] + " cannot be ordered more than once"
            return output
        else:
            output += ", "
        output += menu[1]      
        if (self.items.count (2) > 1):
            output = "Unable to process: " + menu[1] + " cannot be ordered more than once"
            return output
        else:
            output += ", "
        if (self.items.count (3) == 1):
            output += menu[2] + ", "
        elif (self.items.count(3) > 1):
            output = "Unable to process: " + menu[2] + " cannot be ordered more than once"
            return output
        output += "Water"
        if (self.items.count(4) == 1):
            output += ", "+menu[3]
        else:
            output = "Unable to process: " + menu[3] + " cannot be ordered more than once"
        return output

input_str = input()
separate = input_str.split (" ")
meal = separate[0]
try:
    items = separate[1].split (",")
    items = [int(i) for i in items]
    items.sort ()
except:
    items = []

order = Order (meal, items)



