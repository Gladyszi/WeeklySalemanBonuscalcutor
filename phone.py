class Phone:

    def __init__(self,make,color, year):
        self.make= make
        self.color= color
        self.year= year

    def turn_on(self):
        print("The "+ self.make +" is turned on")

    def turn_off(self):
        print("The " + self.make +" is turned off")