class Nim:
    def __init__(self):
        self.Row1 = [True for i in range(0, 6)]
        self.Row2 = [True for i in range(0, 5)]
        self.Row3 = [True for i in range(0, 4)]
        self.Row4 = [True for i in range(0, 3)]

    def RemovePieces(self, Row, Pieces):
        if Pieces < 1: Pieces = 1

        StartingTargetRow = []
        if Row == 1: StartingTargetRow = self.Row1
        if Row == 2: StartingTargetRow = self.Row2
        if Row == 3: StartingTargetRow = self.Row3
        if Row == 4: StartingTargetRow = self.Row4

        if Row == 1:
            LastUsedColumn = -1
            for i in self.Row1:
                if i: LastUsedColumn += 1

            if LastUsedColumn < Pieces:
                self.Row1 = [False for i in range(0, 6)]

            else:
                while Pieces > 0:
                    self.Row1[LastUsedColumn] = False
                    LastUsedColumn -= 1
                    Pieces -= 1

        if Row == 2:
            LastUsedColumn = -1
            for i in self.Row2:
                if i: LastUsedColumn += 1

            if LastUsedColumn < Pieces:
                self.Row2 = [False for i in range(0, 5)]

            else:
                while Pieces > 0:
                    self.Row2[LastUsedColumn] = False
                    LastUsedColumn -= 1
                    Pieces -= 1

        if Row == 3:
            LastUsedColumn = -1
            for i in self.Row3:
                if i: LastUsedColumn += 1

            if LastUsedColumn < Pieces:
                self.Row3 = [False for i in range(0, 4)]

            else:
                while Pieces > 0:
                    self.Row3[LastUsedColumn] = False
                    LastUsedColumn -= 1
                    Pieces -= 1

        if Row == 4:
            LastUsedColumn = -1
            for i in self.Row4:
                if i: LastUsedColumn += 1

            if LastUsedColumn < Pieces:
                self.Row4 = [False for i in range(0, 3)]

            else:
                while Pieces > 0:
                    self.Row4[LastUsedColumn] = False
                    LastUsedColumn -= 1
                    Pieces -= 1

        if Row == 1 and StartingTargetRow == self.Row1:
            self.RemovePieces(2, Pieces)

        if Row == 2 and StartingTargetRow == self.Row2:
            self.RemovePieces(3, Pieces)

        if Row == 3 and StartingTargetRow == self.Row3:
            self.RemovePieces(4, Pieces)

        if Row == 4 and StartingTargetRow == self.Row4:
            self.RemovePieces(1, Pieces)

        WinnerIsKnown = True

        for i in self.Row1:
            if i: WinnerIsKnown = False

        for i in self.Row2:
            if i: WinnerIsKnown = False

        for i in self.Row3:
            if i: WinnerIsKnown = False

        for i in self.Row4:
            if i: WinnerIsKnown = False

        return WinnerIsKnown

    def PrintBoard(self):
        print(self.Row1)
        print(self.Row2)
        print(self.Row3)
        print(self.Row4)