from pieces import *

class Board:

    def __init__(self):
        self.mainlist = {}
        self.placePieces()

    def placePieces(self):
        self.mainlist = {}
        self.mainlist = {"G1": ("Pawn", "White"), "G2": ("Pawn", "White"), "G3": ("Pawn", "White"), "G4": ("Pawn", "White"),
                         "G5": ("Pawn", "White"), "G6": ("Pawn", "White"), "G7": ("Pawn", "White"), "G8": ("Pawn", "White"),
                         "H1": ("Rook", "White"), "H8": ("Rook", "White"), "H2": ("Knight", "White"), "H7": ("Knight", "White"),
                         "H3": ("Bishop", "White"), "H6": ("Bishop", "White"), "H4": ("Queen", "White"), "H5": ("King", "White"),
                         "B1": ("Pawn", "Black"), "B2": ("Pawn", "Black"), "B3": ("Pawn", "Black"), "B4": ("Pawn", "Black"),
                         "B5": ("Pawn", "Black"), "B6": ("Pawn", "Black"), "B7": ("Pawn", "Black"), "B8": ("Pawn", "Black"),
                         "A1": ("Rook", "Black"), "A8": ("Rook", "Black"), "A2": ("Knight", "Black"), "A7": ("Knight", "Black"),
                         "A3": ("Bishop", "Black"), "A6": ("Bishop", "Black"), "A5": ("Queen", "Black"), "A4": ("King", "Black")}

    def setPiece(self, position, piece):
        positionstr = str(position[0]+str(position[1]))
        self.mainlist[positionstr] = (piece.getName(),piece.color)

    def getPiece(self, position):
        positionstr = str(position[0] + str(position[1]))
        color = self.mainlist[positionstr][1]
        if self.mainlist[positionstr][0] == "Pawn":
            piece = Pawn(color, self, position)
        elif self.mainlist[positionstr][0] == "Rook":
            piece = Rook(color, self, position)
        elif self.mainlist[positionstr][0] == "Bishop":
            piece = Bishop(color, self, position)
        elif self.mainlist[positionstr][0] == "Knight":
            piece = Knight(color, self, position)
        elif self.mainlist[positionstr][0] == "Queen":
            piece = Queen(color, self, position)
        else:
            piece = King(color, self, position)
        return piece

    def makeMove(self, startPosition, endPosition, player):
        piece = self.getPiece(startPosition)
        startpositionstr = str(startPosition[0]+str(startPosition[1]))
        endpositionstr = str(endPosition[0]+str(endPosition[1]))
        del(self.mainlist[startpositionstr])
        pieceTuple = (piece.getName(), player)
        self.mainlist[endpositionstr] = pieceTuple



    def displayBoard(self):
        boardlst = []
        for i in range (65,73):
            rowlist = []
            for j in range(1,9):
                currentboxstr = str(chr(i)+str(j))
                if currentboxstr in self.mainlist.keys():
                    if self.mainlist[currentboxstr][1] == "White":
                        rowlist.append("[" + whiteIcons[self.mainlist[currentboxstr][0]] + "]")
                    else:
                        rowlist.append("[" + blackIcons[self.mainlist[currentboxstr][0]] + "]")
                else:
                    rowlist.append("[ ]")
            boardlst.append(rowlist)

        print(" X ", end ="")
        for i in range (1,9):
            print("("+str(i)+")", end ="")
        print()
        for i in range(65, 73):
            print("(" + chr(i) + ")", end="")
            for j in range(1, 9):
                print(boardlst[i-65][j-1], end ="")
            print()
        print()