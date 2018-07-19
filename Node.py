import Maths
from decimal import *

class Node:
    def __init__(self):
        self.Threshold = Decimal(0)
        self.CurrentActivation = Decimal(0)
        self.SumOfInputActivations = Decimal(0)

    def DefineCurrentActivation(self):
        self.CurrentActivation = Decimal(Maths.AdjustedSigmoid(self.SumOfInputActivations))
        if self.CurrentActivation < self.Threshold: self.CurrentActivation = 0

    def LazyDefineCurrentActivation(self):
        self.CurrentActivation = Decimal(self.SumOfInputActivations)