from decimal import *

class Link:
    def __init__(self):
        self.Multiplier = Decimal(1) # Identity Link by default
        self.CurrentValue = Decimal(0)

    def Activate(self):
        self.CurrentValue *= self.Multiplier