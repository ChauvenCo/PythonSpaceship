import time


class Vector2 :
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y

    def SetXY(self, x, y):
        self.x = x
        self.y = y

    def GetXY(self):
        return [self.x, self.y]

    def AddXY(self, xy):
        self.x += xy[0]
        self.y += xy[1]

class Spaceship :
    def __init__(self, name = ""):
        self.name = name
        self.direction = Vector2(0, 0)
        self.coords = Vector2(0, 0)
        self.launched = False

    def GetPosition(self):
        return self.coords.GetXY()

    def GetName(self):
        return self.name

    def SetDirectionVector(self, x, y):
        self.direction = Vector2(x, y)

    def Start(self):
        self.launched = True
        while (self.launched):
            self.coords.AddXY(self.direction.GetXY())
            time.sleep(1.0)


    def Stop(self):
        self.launched = False


