class Animal:

    def __init__(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound




obj = Animal("Sound")
print(obj.getSound())