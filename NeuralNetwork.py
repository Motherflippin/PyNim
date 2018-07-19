from Node import *
from Link import *
from decimal import *
from random import uniform as randfloat

class NeuralNetwork:
    def __init__(self):
        self.InputLayerWidth = 18
        #self.HiddenLayerWidth = 10
        #self.OutputLayerWidth = 2
        self.HiddenLayerWidth = 21
        self.OutputLayerWidth = 24

        self.NumInputToHiddenLinks = 18 * 21 #18 * 10
        self.NumHiddenToHiddenLinks = 21*21 #10 * 10
        self.NumHiddenToOutputLinks = 21 * 24 #10 * 2

        self.InputLayer = []
        for i in range(0, self.InputLayerWidth): self.InputLayer.append(Node())
        self.InputLayer[0].CurrentActivation = Decimal(0)

        self.HiddenLayer1 = []
        self.HiddenLayer2 = []
        self.HiddenLayer3 = []
        for i in range(0, self.HiddenLayerWidth):
            self.HiddenLayer1.append(Node())
            self.HiddenLayer2.append(Node())
            self.HiddenLayer3.append(Node())

        self.OutputLayer = []
        for i in range(0, self.OutputLayerWidth): self.OutputLayer.append(Node())

        self.InputToHidden1Links = []
        for i in range(0, self.NumInputToHiddenLinks): self.InputToHidden1Links.append(Link())

        self.Hidden1ToHidden2Links = []
        self.Hidden2ToHidden3Links = []
        for i in range(0, self.NumHiddenToHiddenLinks):
            self.Hidden1ToHidden2Links.append(Link())
            self.Hidden2ToHidden3Links.append(Link())

        self.Hidden3ToOutputLinks = []
        for i in range(0, self.NumHiddenToOutputLinks):
            self.Hidden3ToOutputLinks.append(Link())

    def RunNetwork(self):
        for i in range(0, self.HiddenLayerWidth):
            self.HiddenLayer1[i].SumOfInputActivation = Decimal(0)
            self.HiddenLayer2[i].SumOfInputActivation = Decimal(0)
            self.HiddenLayer3[i].SumOfInputActivation = Decimal(0)

        for i in self.OutputLayer:
            i.SumOfInputActivation = 0

        for i in range(0, self.InputLayerWidth):
            for e in range(0, self.HiddenLayerWidth):
                self.InputToHidden1Links[e*self.InputLayerWidth+i].CurrentValue = self.InputLayer[i].CurrentActivation

        for i in self.InputToHidden1Links: i.Activate()

        for i in range(0, self.InputLayerWidth):
            for e in range(0, self.HiddenLayerWidth):
                self.HiddenLayer1[e].SumOfInputActivations += self.InputToHidden1Links[i+e*self.InputLayerWidth].CurrentValue

        for i in self.HiddenLayer1: i.DefineCurrentActivation()

        for i in range(0, self.HiddenLayerWidth):
            for e in range(0, self.HiddenLayerWidth):
                self.Hidden1ToHidden2Links[i*self.HiddenLayerWidth+e].CurrentValue = self.HiddenLayer1[i].CurrentActivation

        for i in self.Hidden1ToHidden2Links: i.Activate()

        for i in range(0, self.HiddenLayerWidth):
            for e in range(self.HiddenLayerWidth):
                self.HiddenLayer2[e].SumOfInputActivations += self.Hidden1ToHidden2Links[i+e*self.HiddenLayerWidth].CurrentValue

        for i in self.HiddenLayer2: i.DefineCurrentActivation()

        for i in range(0, self.HiddenLayerWidth):
            for e in range(0, self.HiddenLayerWidth):
                self.Hidden2ToHidden3Links[i*self.HiddenLayerWidth+e].CurrentValue = self.HiddenLayer2[i].CurrentActivation

        for i in self.Hidden2ToHidden3Links: i.Activate()

        for i in range(0, self.HiddenLayerWidth):
            for e in range(self.HiddenLayerWidth):
                self.HiddenLayer3[e].SumOfInputActivations += self.Hidden2ToHidden3Links[i+e*self.HiddenLayerWidth].CurrentValue

        for i in self.HiddenLayer3: i.DefineCurrentActivation()

        for i in range(0, self.HiddenLayerWidth):
            for e in range(0, self.OutputLayerWidth):
                self.Hidden3ToOutputLinks[e*self.HiddenLayerWidth+i].CurrentValue = self.HiddenLayer3[i].CurrentActivation

        for i in self.Hidden3ToOutputLinks: i.Activate()

        for i in range(0, self.HiddenLayerWidth):
            for e in range(self.OutputLayerWidth):
                self.OutputLayer[e].SumOfInputActivations += self.Hidden3ToOutputLinks[i+e*self.HiddenLayerWidth].CurrentValue

        for i in self.OutputLayer: i.DefineCurrentActivation()

    def ExportNetwork(self, Location):
        # Nodes have thresholds, links have multipliers, i.e. for each item in the network, it has one stored property.
        FileString = ""
        for i in self.InputLayer:
            FileString += "{0:f}".format(i.Threshold)
            FileString += "\n"

        for i in self.InputToHidden1Links:
            FileString += "{0:f}".format(i.Multiplier)
            FileString += "\n"

        for i in self.HiddenLayer1:
            FileString += "{0:f}".format(i.Threshold)
            FileString += "\n"

        for i in self.Hidden1ToHidden2Links:
            FileString += "{0:f}".format(i.Multiplier)
            FileString += "\n"

        for i in self.HiddenLayer2:
            FileString += "{0:f}".format(i.Threshold)
            FileString += "\n"

        for i in self.Hidden2ToHidden3Links:
            FileString += "{0:f}".format(i.Multiplier)
            FileString += "\n"

        for i in self.HiddenLayer3:
            FileString += "{0:f}".format(i.Threshold)
            FileString += "\n"

        for i in self.Hidden3ToOutputLinks:
            FileString += "{0:f}".format(i.Multiplier)
            FileString += "\n"

        with open(Location, mode="w+") as NetFile:
            NetFile.write(FileString)

    def ImportNetwork(self, Location):
        with open(Location, mode="r") as NetFile:
            for i in self.InputLayer:
                exec("i.Threshold = Decimal(" + NetFile.readline().rstrip("\n") + ")")

            for i in self.InputToHidden1Links:
                exec("i.Multiplier = Decimal(" + NetFile.readline().rstrip("\n") + ")")

            for i in self.HiddenLayer1:
                exec("i.Threshold = Decimal(" + NetFile.readline().rstrip("\n") + ")")

            for i in self.Hidden1ToHidden2Links:
                exec("i.Multiplier = Decimal(" + NetFile.readline().rstrip("\n") + ")")

            for i in self.HiddenLayer2:
                exec("i.Threshold = Decimal(" + NetFile.readline().rstrip("\n") + ")")

            for i in self.Hidden2ToHidden3Links:
                exec("i.Multiplier = Decimal(" + NetFile.readline().rstrip("\n") + ")")

            for i in self.HiddenLayer3:
                exec("i.Threshold = Decimal(" + NetFile.readline().rstrip("\n") + ")")

            for i in self.Hidden3ToOutputLinks:
                exec("i.Multiplier = Decimal(" + NetFile.readline().rstrip("\n") + ")")

            for i in self.OutputLayer:
                exec("i.Threshold = Decimal(" + NetFile.readline().rstrip("\n") + ")")

    def UpdateNetwork(self):
        TweakLowerBound = -1
        TweakUpperBound = 1

        for i in self.InputLayer:
            i.Threshold += Decimal(randfloat(TweakLowerBound, TweakUpperBound))

        for i in self.InputToHidden1Links:
            i.Multiplier += Decimal(randfloat(TweakLowerBound, TweakUpperBound))

        for i in self.HiddenLayer1:
            i.Threshold += Decimal(randfloat(TweakLowerBound, TweakUpperBound))

        for i in self.Hidden1ToHidden2Links:
            i.Multiplier += Decimal(randfloat(TweakLowerBound, TweakUpperBound))

        for i in self.HiddenLayer2:
            i.Threshold += Decimal(randfloat(TweakLowerBound, TweakUpperBound))

        for i in self.Hidden2ToHidden3Links:
            i.Multiplier += Decimal(randfloat(TweakLowerBound, TweakUpperBound))

        for i in self.HiddenLayer3:
            i.Threshold += Decimal(randfloat(TweakLowerBound, TweakUpperBound))

        for i in self.Hidden3ToOutputLinks:
            i.Multiplier += Decimal(randfloat(TweakLowerBound, TweakUpperBound))

        for i in self.OutputLayer:
            i.Threshold += Decimal(randfloat(TweakLowerBound, TweakUpperBound))



    def CategoriseOutput(self, Output1, Output2):
        Row = 0 #Row of board to make move on
        Pieces = 0 #Number of pieces to take

        if Output1 < 0.25: Row = 1
        elif Output1 < 0.5: Row = 2
        elif Output2 < 0.75: Row = 3
        else: Row = 4

        if Output2 < (1/6): Pieces = 1
        if Output2 < (2/6): Pieces = 2
        if Output2 < (3/6): Pieces = 3
        if Output2 < (4/6): Pieces = 4
        if Output2 < (5/6): Pieces = 5
        else: Pieces = 6

        return Row, Pieces

    #def CategoriseOwnOutput(self):
        Row = 0 #Row of board to make move on
        Pieces = 0 #Number of pieces to take

    #    if self.OutputLayer[0].CurrentActivation < 0.25: Row = 1
    #    elif self.OutputLayer[0].CurrentActivation < 0.5: Row = 2
     #   elif self.OutputLayer[0].CurrentActivation < 0.75: Row = 3
     #   else: Row = 4

    #    if self.OutputLayer[1].CurrentActivation < (1/6): Pieces = 1
     #   if self.OutputLayer[1].CurrentActivation < (2/6): Pieces = 2
     #   if self.OutputLayer[1].CurrentActivation < (3/6): Pieces = 3
     #   if self.OutputLayer[1].CurrentActivation < (4/6): Pieces = 4
     #   if self.OutputLayer[1].CurrentActivation < (5/6): Pieces = 5
     #   else: Pieces = 6

     #  return Row, Pieces

    def CategoriseOwnOutput(self):
        OutputNums = [i.CurrentActivation for i in self.OutputLayer]
        ValueOfMax = max(OutputNums)

        Index = 0
        i = 0
        while i < len(self.OutputLayer):
            if self.OutputLayer[i] == ValueOfMax: Index = i
            i += 1

        Row = (Index % 6) + 1
        Pieces = int(Index / 6) + 1

        return Row, Pieces
