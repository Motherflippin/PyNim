import math

def Sigmoid(x): return (1/(1+math.exp(-x)))
def AdjustedSigmoid(x): return Sigmoid(x/10)