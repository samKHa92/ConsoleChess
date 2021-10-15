from board import Board
from pieces import *

class Chess:
    def __init__(self):
        self.board = Board()
        self.currentPlayer = "White"

    def swapPlayers(self):
        self.currentPlayer = "Black" if self.currentPlayer == "White" else "White"
    
    def isStringValidMove(self, moveStr):
        if len(moveStr) != 5:
            return False
        if ord(moveStr[0]) < 65 or ord(moveStr[0]) > 72:
            return False
        if int(moveStr[1]) < 1 or int(moveStr[1]) > 8:
            return False
        if moveStr[2] != " ":
            return False
        if ord(moveStr[3]) < 65 or ord(moveStr[3]) > 72:
            return False
        if int(moveStr[4]) < 1 or int(moveStr[4]) > 8:
            return False
        return True

    def haveAnyPiece(self, moveStr):
        if str(moveStr[0]+moveStr[1]) not in self.board.mainlist.keys():
            return False
        if self.board.mainlist[str(moveStr[0]+moveStr[1])][1] != self.currentPlayer:
            return False
        return True

    def wantsExit(self, str):
        if str == "EXIT":
            return True
        return False

    def checkIfWhiteWon(self):
        for i in self.board.mainlist.values():
            if i[1] == "Black":
                return False
        return True

    def checkIfBlackWon(self):
        for i in self.board.mainlist.values():
            if i[1] == "White":
                return False
        return True

    def checkWhitePromotion(self):
        for i in self.board.mainlist.keys():
            if i[0] == "A" and self.board.mainlist[i][0] == "Pawn" and self.board.mainlist[i][1] == "White":
                return int(i[1])
        return -1

    def checkBlackPromotion(self):
        for i in self.board.mainlist.keys():
            if i[0] == "H" and self.board.mainlist[i][0] == "Pawn" and self.board.mainlist[i][1] == "Black":
                return int(i[1])
        return -1

    def play(self):
        self.board.displayBoard()
        print("White player starts! Please input your move in the console:")
        while(True):
            while(True):
                val = input()
                if self.wantsExit(val):
                    print("Thank you for playing chess, and making world more clever... See you next time!")
                    return
                if not self.isStringValidMove(val):
                    print("Your string format is not correct... Please try again:")
                    continue
                if not self.haveAnyPiece(val):
                    print("You do not have any piece on this coordinates... Please try again:")
                    continue
                startPosTuple = (val[0], int(val[1]))
                destTuple = (val[3],int(val[4]))
                piece = self.board.getPiece(startPosTuple)
                if not piece.checkMove(destTuple):
                    print("You cant move your " + piece.getName() + " here... PLease try again:")
                    continue
                break

            posTuple = (val[0], int(val[1]))
            destTuple = (val[3], int(val[4]))
            self.board.makeMove(posTuple,destTuple,self.currentPlayer)
            self.board.displayBoard()
            checkwhitepromotion = self.checkWhitePromotion()
            if checkwhitepromotion != -1:
                coordinates = str("A"+str(checkwhitepromotion))
                print("You can promote your Pawn! Please write the name of the piece you want instead of this Pawn: (Bishop, Rook, Queen)")
                prom = ""
                while (prom != "Queen" or prom != "Bishop" or prom != "Rook"):
                    prom = input()
                    if prom == "Queen":
                        self.board.mainlist[coordinates] = ("Queen", "White")
                    elif prom == "Bishop":
                        self.board.mainlist[coordinates] = ("Bishop", "White")
                    elif prom == "Rook":
                        self.board.mainlist[coordinates] = ("Rook", "White")
                self.board.displayBoard()

            checkblackpromotion = self.checkBlackPromotion()
            if checkblackpromotion != -1:
                coordinates = str("H" + str(checkblackpromotion))
                print("You can promote your Pawn! Please write the name of the piece you want instead of this Pawn: (Bishop, Rook, Queen)")
                prom = ""
                while (prom != "Queen" or prom != "Bishop" or prom != "Rook"):
                    prom = input()
                    if prom == "Queen":
                        self.board.mainlist[coordinates] = ("Queen", "Black")
                    elif prom == "Bishop":
                        self.board.mainlist[coordinates] = ("Bishop", "Black")
                    elif prom == "Rook":
                        self.board.mainlist[coordinates] = ("Rook", "Black")
                self.board.displayBoard()

            if self.checkIfWhiteWon():
                print("Congrats!!! Whites won the game!!! Want another game? (y/n)")
                inp = input()
                if inp == "y" or inp == "Y":
                    game = Chess()
                    game.play()
                return
            if self.checkIfBlackWon():
                print("Congrats!!! Blacks won the game!!!")
                inp = input()
                if inp == "y" or inp == "Y":
                    game = Chess()
                    game.play()
                return
            self.swapPlayers()
            print("Now it is turn of " + self.currentPlayer + "s. Please input your move in the console:")

if __name__ == "__main__":
    game = Chess()
    game.play()