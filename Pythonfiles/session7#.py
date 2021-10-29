class Animal:
    def __init__(self,name,sound,legs,tale,food):
        self.name = name
        self.sound = sound
        self.legs = legs
        self.food = food
        if tale == True:
            self.tale = 'it has tale'
        elif tale == False:
            self.tale = "it doesn't have tale" 
    def full_info(self):
        return 'the '+self.name+' has '+str(self.legs)+' legs and eats '+self.food
    def __str__(self):
        return 'the object was made by the best programmer in world'
    def __add__(self,other):
        return self.legs+other.legs

cat = Animal('cat','meow',4,True,'meat')
print(cat.name)
print(cat.tale)
print(cat.sound)
print(cat.legs)
print(cat.full_info())
cat2 = Animal('persian-cat','mew',4,False,'vegetable')
print(cat+cat2)
print(cat2.sound)
