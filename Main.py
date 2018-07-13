### CODE ENTRY POINT

from NeuralNetwork import *
from NimGame import *

Tester = NeuralNetwork()

Tester.ImportNetwork("test.txt")
Tester.RunNetwork()
Tester.UpdateNetwork()
Tester.ExportNetwork("test3.txt")
#Tester.ExportNetwork("test.txt")

print(Tester.OutputLayer[0].CurrentActivation)
print(Tester.OutputLayer[1].CurrentActivation)

print(Tester.CategoriseOutput(Tester.OutputLayer[0].CurrentActivation, Tester.OutputLayer[1].CurrentActivation))

NimBoard = Nim()
print(NimBoard.RemovePieces(1, 6))
NimBoard.RemovePieces(2, 6)
NimBoard.RemovePieces(3, 6)
print(NimBoard.RemovePieces(4, 6))
NimBoard.PrintBoard()