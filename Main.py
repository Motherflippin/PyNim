### CODE ENTRY POINT

from NeuralNetwork import *
from NimGame import *

Tester = NeuralNetwork()

Tester.ImportNetwork("test.txt")
Tester.RunNetwork()
Tester.UpdateNetwork()
Tester.ExportNetwork("test3.txt")
#Tester.ExportNetwork("test.txt")

#print(Tester.OutputLayer[0].CurrentActivation)
#print(Tester.OutputLayer[1].CurrentActivation)

#print(Tester.CategoriseOutput(Tester.OutputLayer[0].CurrentActivation, Tester.OutputLayer[1].CurrentActivation))

NimBoard = Nim()
NimBoard.RemovePieces(1, 6)
NimBoard.RemovePieces(2, 6)
NimBoard.RemovePieces(3, 6)
NimBoard.RemovePieces(4, 6)
#NimBoard.PrintBoard()

def CreateInputPayload(Board):
    Numbers = []
    Payload = []
    for i in range(0,18): Payload.append(Node())
    for i in Board.Row1: Numbers.append(Decimal(i))
    for i in Board.Row2: Numbers.append(Decimal(i))
    for i in Board.Row3: Numbers.append(Decimal(i))
    for i in Board.Row4: Numbers.append(Decimal(i))
    for i in range(0, len(Numbers)): Payload[i].CurrentActivation = Numbers[i]

    return Payload

def TestAIs(Config1, Config2):
    A = NeuralNetwork()
    B = NeuralNetwork()

    A.ImportNetwork(Config1)
    B.ImportNetwork(Config1)

    Board = Nim()

    CurrentPlayer = "B"
    HasGameBeenWon = False

    while not HasGameBeenWon:
        if CurrentPlayer == "A":
            Row = 0
            Pieces = 0

            A.InputLayer = CreateInputPayload(Board)
            A.RunNetwork()
            Row, Pieces = A.CategoriseOwnOutput()

            #print(Row)
            #print(Pieces)

            HasGameBeenWon = Board.RemovePieces(Row, Pieces)

            #Board.PrintBoard()

            if not HasGameBeenWon:
                CurrentPlayer = "B"

        if CurrentPlayer == "B":
            Row = 0
            Pieces = 0

            B.InputLayer = CreateInputPayload(Board)
            B.RunNetwork()
            Row, Pieces = B.CategoriseOwnOutput()

            #print(Row)
            #print(Pieces)

            HasGameBeenWon = Board.RemovePieces(Row, Pieces)

            #Board.PrintBoard()

            if not HasGameBeenWon:
                CurrentPlayer = "A"

    if CurrentPlayer == "A":
        #print("A Victory")
        return Config1

    if CurrentPlayer == "B":
        #print("B Victory")
        return Config2


#TestAIs("test.txt", "test2.txt")

i = 0
while True:
    A = "LearningTests/v1.txt"
    B = "LearningTests/v2.txt"

    Winner1 = TestAIs(A, B)
    Winner2 = TestAIs(B, A)

    Generator = NeuralNetwork()

    if Winner1 == Winner2:
        if Winner1 == A:
            Generator.ImportNetwork(A)
            Generator.UpdateNetwork()
            Generator.ExportNetwork(B)

        if Winner1 == B:
            Generator.ImportNetwork(B)
            Generator.UpdateNetwork()
            Generator.ExportNetwork(A)

    else: # Evenly matched
        #Backup A

        if i % 1000 == 0:
            Generator.ImportNetwork(B)
            Generator.ExportNetwork(B.rstrip(".txt") + "Old" + str(i) + ".txt")

        i += 1
        Generator.ImportNetwork(B) #Edit B
        Generator.UpdateNetwork()
        Generator.ExportNetwork(B)

    print("Iteration Complete")


