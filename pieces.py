
blackIcons = {"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" }
whiteIcons = {"Pawn" : "♟", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" }

class Piece:

    def __init__(self, color, board, position):
        self.__color = color
        self._board = board
        self.__position = position

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        if ord(pos[0]) >= 65 and ord(pos[0]) <= 72 and pos[1] >= 1 and pos[1] <= 8 and len(pos) == 2:
            self.__position = pos

    def checkMove(self, dest):
        return False

    def move(self, dest):
        return False

        
    def getName(self):
        return "Imena zogadad figura"

    def getIcon(self):
        return None



class Knight(Piece):
    def checkMove(self, dest):
        deststr = str(dest[0] + str(dest[1]))
        a = abs(ord(dest[0]) - ord(self.position[0]))
        b = abs(dest[1]-self.position[1])

        if (((abs(ord(dest[0]) - ord(self.position[0])) == 1) and (abs(dest[1]-self.position[1]) == 2))) or (
                ((abs(ord(dest[0]) - ord(self.position[0])) == 2) and (abs(dest[1] - self.position[1]) == 1))):
            if deststr in self._board.mainlist.keys():
                if self._board.mainlist[deststr][1] == self.color:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return False

    def move(self, dest):
        deststr = str(dest[0] + str(dest[1]))
        posstr = str(self.position[0] + str(self.position[1]))
        if self.checkMove():
            self.position = dest
            self._board.mainlist[deststr] = self._board.mainlist[posstr]
            del self._board.mainlist[posstr]

    def getName(self):
        return "Knight"

    def getIcon(self):
        return whiteIcons["Knight"] if self.color == "White" else blackIcons["Knight"]

    def abs(x):
        return x if x>=0 else -x

class Rook(Piece):
    def checkMove(self, dest):
        deststr = str(dest[0] + str(dest[1]))
        letterCurse = 0
        numberCurse = 0

        if abs(ord(dest[0]) - ord(self.position[0])) == 0:
            if dest[1] > self.position[1]:
                numberCurse = 1
            else:
                numberCurse = -1
            numberPos = self.position[1]+numberCurse
            for i in range(0, abs(dest[1]-self.position[1])-1):
                boxstr = str(dest[0] + str(numberPos))
                if boxstr in self._board.mainlist.keys():
                    return False
                numberPos += numberCurse
            if deststr in self._board.mainlist.keys():
                if self._board.mainlist[deststr][1] == self.color:
                    return False
                else:
                    return True
            else:
                return True
        elif abs(int(dest[1]) - int(self.position[1])) == 0:
            if ord(dest[0]) > ord(self.position[0]):
                letterCurse = 1
            else:
                letterCurse = -1
            letterPos = ord(self.position[0])+letterCurse
            for i in range(0, abs(ord(dest[0])-ord(self.position[0]))-1):
                boxstr = str(chr(letterPos) + str(dest[1]))
                if boxstr in self._board.mainlist.keys():
                    return False
                letterPos += letterCurse
            if deststr in self._board.mainlist.keys():
                if self._board.mainlist[deststr][1] == self.color:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return False



    def move(self, dest):
        deststr = str(dest[0] + dest[1])
        posstr = str(self.position[0] + self.position[1])
        if self.checkMove():
            self.position = dest
            self._board.mainlist[deststr] = self._board.mainlist[posstr]
            del self._board.mainlist[posstr]

    def getName(self):
        return "Rook"

    def getIcon(self):
        return whiteIcons["Rook"] if self.color == "White" else blackIcons["Rook"]

    def abs(x):
        return x if x >= 0 else -x
        
class Bishop(Piece):
    def checkMove(self, dest):
        deststr = str(dest[0] + str(dest[1]))
        letterCurse = 0
        numberCurse = 0
        if abs(ord(dest[0]) - ord(self.position[0])) == abs(int(dest[1]) - int(self.position[1])):
            if ord(dest[0]) > ord(self.position[0]):
                letterCurse = 1
            else:
                letterCurse = -1
            if dest[1] > self.position[1]:
                numberCurse = 1
            else:
                numberCurse = -1

            letterPos = ord(self.position[0])+letterCurse
            numberPos = self.position[1]+numberCurse

            for x in range (0, abs(int(dest[1]) - int(self.position[1]))-1):
                boxstr = str(chr(letterPos) + str(numberPos))
                if boxstr in self._board.mainlist.keys():
                    return False
                letterPos+=letterCurse
                numberPos+=numberCurse
            if deststr in self._board.mainlist.keys():
                if self._board.mainlist[deststr][1] == self.color:
                    return False
                else:
                    return True
            else:
                return True

    def move(self, dest):
        deststr = str(dest[0] + dest[1])
        posstr = str(self.position[0] + self.position[1])
        if self.checkMove():
            self.position = dest
            self._board.mainlist[deststr] = self._board.mainlist[posstr]
            del self._board.mainlist[posstr]

    def getName(self):
        return "Bishop"

    def getIcon(self):
        return whiteIcons["Bishop"] if self.color == "White" else blackIcons["Bishop"]

    def abs(x):
        return x if x >= 0 else -x
        
class Queen(Piece):
    def checkMoveForRook(self, dest):
        deststr = str(dest[0] + str(dest[1]))
        letterCurse = 0
        numberCurse = 0

        if abs(ord(dest[0]) - ord(self.position[0])) == 0:
            if dest[1] > self.position[1]:
                numberCurse = 1
            else:
                numberCurse = -1
            numberPos = self.position[1]+numberCurse
            for i in range(0, abs(dest[1]-self.position[1])-1):
                boxstr = str(dest[0] + str(numberPos))
                if boxstr in self._board.mainlist.keys():
                    return False
                numberPos += numberCurse
            if deststr in self._board.mainlist.keys():
                if self._board.mainlist[deststr][1] == self.color:
                    return False
                else:
                    return True
            else:
                return True
        elif abs(int(dest[1]) - int(self.position[1])) == 0:
            if ord(dest[0]) > ord(self.position[0]):
                letterCurse = 1
            else:
                letterCurse = -1
            letterPos = self.position[1]+numberCurse
            for i in range(0, abs(ord(dest[0])-ord(self.position[0]))-1):
                boxstr = str(chr(letterPos) + str(dest[1]))
                if boxstr in self._board.mainlist.keys():
                    return False
                letterPos += letterCurse
            if deststr in self._board.mainlist.keys():
                if self._board.mainlist[deststr][1] == self.color:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return False


    def checkMoveForBishop(self, dest):
        deststr = str(dest[0] + str(dest[1]))
        letterCurse = 0
        numberCurse = 0
        if abs(ord(dest[0]) - ord(self.position[0])) == abs(int(dest[1]) - int(self.position[1])):
            if ord(dest[0]) > ord(self.position[0]):
                letterCurse = 1
            else:
                letterCurse = -1
            if dest[1] > self.position[1]:
                numberCurse = 1
            else:
                numberCurse = -1

            letterPos = ord(self.position[0])+letterCurse
            numberPos = self.position[1]+numberCurse

            for x in range (0, abs(int(dest[1]) - int(self.position[1]))-1):
                boxstr = str(chr(letterPos) + str(numberPos))
                if boxstr in self._board.mainlist.keys():
                    return False
                letterPos+=letterCurse
                numberPos+=numberCurse
            if deststr in self._board.mainlist.keys():
                if self._board.mainlist[deststr][1] == self.color:
                    return False
                else:
                    return True
            else:
                return True

    def checkMove(self, dest):
        return self.checkMoveForBishop(dest) or self.checkMoveForRook(dest)

    def move(self, dest):
        deststr = str(dest[0] + dest[1])
        posstr = str(self.position[0] + self.position[1])
        if self.checkMove():
            self.position = dest
            self._board.mainlist[deststr] = self._board.mainlist[posstr]
            del self._board.mainlist[posstr]

    def getName(self):
        return "Queen"

    def getIcon(self):
        return whiteIcons["Queen"] if self.color == "White" else blackIcons["Queen"]

    def abs(x):
        return x if x >= 0 else -x

class King(Piece):
    def checkMove(self, dest):
        deststr = str(dest[0] + str(dest[1]))
        if abs(ord(deststr[0]) - ord(self.position[0])) <= 1 and abs(dest[1] - self.position[1]) <= 1:
            if deststr in self._board.mainlist.keys():
                if self._board.mainlist[deststr][1] == self.color:
                    return False
                else:
                    return True
            else:
                return True
            return True
        return False

    def move(self, dest):
        deststr = str(dest[0] + dest[1])
        posstr = str(self.position[0] + self.position[1])
        if self.checkMove():
            self.position = dest
            self._board.mainlist[deststr] = self._board.mainlist[posstr]
            del self._board.mainlist[posstr]

    def getName(self):
        return "King"

    def getIcon(self):
        return whiteIcons["King"] if self.color == "White" else blackIcons["King"]

    def abs(x):
        return x if x >= 0 else -x

class Pawn(Piece):
    def checkMove(self, dest):
        deststr = str(dest[0] + str(dest[1]))
        if (ord(self.position[0]) - ord(dest[0])) == 1 and self.color == "White" and self.position[1] == dest[1]:
            if deststr in self._board.mainlist.keys():
                return False
            else:
                return True
            return True

        elif (ord(dest[0]) - ord(self.position[0])) == 1 and self.color == "Black" and self.position[1] == dest[1]:
            if deststr in self._board.mainlist.keys():
                return False
            else:
                return True
            return True

        elif (ord(self.position[0]) - ord(dest[0])) == 2 and self.color == "White" and self.position[0] == "G" and self.position[1] == dest[1]:
            newbox = str("E"+str(dest[1]))
            if newbox in self._board.mainlist.keys():
                return False
            if deststr in self._board.mainlist.keys():
                return False
            else:
                return True
            return True

        elif (ord(dest[0]) - ord(self.position[0])) == 2 and self.color == "Black" and self.position[0] == "B" and self.position[1] == dest[1]:
            newbox = str("D"+str(dest[1]))
            if newbox in self._board.mainlist.keys():
                return False
            if deststr in self._board.mainlist.keys():
                return False
            else:
                return True
            return True

        elif abs(dest[1]-self.position[1]) == 1 and (ord(self.position[0]) - ord(dest[0])) == 1 and self.color == "White":
            if deststr in self._board.mainlist.keys() and self._board.mainlist[deststr][1] == "Black":
                return True
            return False

        elif abs(dest[1]-self.position[1]) == 1 and (ord(dest[0]) - ord(self.position[0])) == 1 and self.color == "Black":
            if deststr in self._board.mainlist.keys() and self._board.mainlist[deststr][1] == "White":
                return True
            return False

    def move(self, dest):
        deststr = str(dest[0] + dest[1])
        posstr = str(self.position[0] + self.position[1])
        if self.checkMove():
            self.position = dest
            self._board.mainlist[deststr] = self._board.mainlist[posstr]
            del self._board.mainlist[posstr]

    def getName(self):
        return "Pawn"

    def getIcon(self):
        return whiteIcons["Pawn"] if self.color == "Pawn" else blackIcons["Pawn"]

    def abs(x):
        return x if x >= 0 else -x