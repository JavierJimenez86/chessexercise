import argparse

# Creating bidimensional list for the 8x8 chess board

chessBoard = [[1, 1, 1, 1, 1, 1, 1, 1] for i in range(8)]

# Mapping letter to index and index to letter

chess_map_from_letter_to_index = { "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}

chess_map_from_index_to_letter = { 0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

# Function to obtain all the possible rook movements given a certain position

def getRookMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_letter_to_index[column]
    i,j = row, column
    solutionMoves = []

    # Compute the moves for the row
    for j in xrange(8):
        if j != column:
            solutionMoves.append((row, j))

    # Compute the moves the column
    for i in xrange(8):
        if i != row:
           solutionMoves.append((i, column))

    solutionMovesFinal = []
    solutionMovesFinal = ["".join([chess_map_from_index_to_letter[i[1]], str(i[0] + 1)]) for i in solutionMoves]
    return solutionMovesFinal

# Function to obtain all the possible bishop movements given a certain position

def getBishopMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_letter_to_index[column]
    i, j = row, column
    solutionMoves = []

    # Compute the moves for the diagonals to the left and down
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        solutionMoves.append((i, j))

    i, j = row, column

    # Compute the moves for the diagonals to the right and up

    while i < 7 and j < 7:
        i += 1
        j += 1
        solutionMoves.append((i, j))

    i, j = row, column

    # Compute the moves for the diagonals to the left and up

    while i < 7 and j > 0:
        i += 1
        j -= 1
        solutionMoves.append((i, j))

    i, j = row, column

    # Compute the moves for the diagonals to the right and down

    while i > 0 and j < 7:
        i -= 1
        j += 1
        solutionMoves.append((i, j))
    solutionMovesFinal = []
    solutionMovesFinal = ["".join([chess_map_from_index_to_letter[i[1]], str(i[0] + 1)]) for i in solutionMoves]
    return solutionMovesFinal

#Function to obtain all the possible rook movements given a certain position

def getQueenMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_letter_to_index[column]
    i,j = row, column
    solutionMovesRook = []
    solutionMovesBishop = []
    solutionMovesQueen = []

    # Compute the moves as rook
    for j in xrange(8):
        if j != column:
            solutionMovesRook.append((row, j))

    for i in xrange(8):
        if i != row:
           solutionMovesRook.append((i, column))

    solutionMovesRook = ["".join([chess_map_from_index_to_letter[i[1]], str(i[0] + 1)]) for i in solutionMovesRook]

    # Compute the moves as bishop
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_letter_to_index[column]
    i, j = row, column

    while i > 0 and j > 0:
        i -= 1
        j -= 1
        solutionMovesBishop.append((i, j))

    i, j = row, column

    while i < 7 and j < 7:
        i += 1
        j += 1
        solutionMovesBishop.append((i, j))

    i, j = row, column

    while i < 7 and j > 0:
        i += 1
        j -= 1
        solutionMovesBishop.append((i, j))

    i, j = row, column

    while i > 0 and j < 7:
        i -= 1
        j += 1
        solutionMovesBishop.append((i, j))

    solutionMovesBishop = ["".join([chess_map_from_index_to_letter[i[1]], str(i[0] + 1)]) for i in solutionMovesBishop]
    solutionMovesQueen = solutionMovesRook + solutionMovesBishop
    return solutionMovesQueen

#Function to obtain all the possible knight movements given a certain position


def getKnightMoves(pos, chessBoard):

    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_letter_to_index[column]
    i,j = row, column
    solutionMoves = []
    try:
        temp = chessBoard[i + 1][j - 2]
        solutionMoves.append([i + 1, j - 2])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j - 1]
        solutionMoves.append([i + 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j + 1]
        solutionMoves.append([i + 2, j + 1])
    except:
        pass
    try:
        temp = chessBoard[i + 1][j + 2]
        solutionMoves.append([i + 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j + 2]
        solutionMoves.append([i - 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j + 1]
        solutionMoves.append([i - 2, j + 1])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j - 1]
        solutionMoves.append([i - 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j - 2]
        solutionMoves.append([i - 1, j - 2])
    except:
        pass

    # Filter all negative values
    temp = [i for i in solutionMoves if i[0] >=0 and i[1] >=0]
    allPossibleMoves = ["".join([chess_map_from_index_to_letter[i[1]], str(i[0] + 1)]) for i in temp]
    allPossibleMoves.sort()
    return allPossibleMoves


def getKnightMoves(pos, chessBoard):
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = chess_map_from_letter_to_index[column]
    i, j = row, column
    solutionMovesKnight = []

    # Getting all possibles positions for the L movements of the knight given its current position

    solutionMovesKnight.append([i + 1, j - 2])

    solutionMovesKnight.append([i + 1, j + 2])

    solutionMovesKnight.append([i + 2, j - 1])

    solutionMovesKnight.append([i + 2, j + 1])

    solutionMovesKnight.append([i - 1, j + 2])

    solutionMovesKnight.append([i - 1, j - 2])

    solutionMovesKnight.append([i - 2, j + 1])

    solutionMovesKnight.append([i - 2, j - 1])

    # Filtering all negative values
    solutionMovesKnightFinal = [i for i in solutionMovesKnight if i[0] >= 0 and i[1] >= 0]
    allPossibleMoves = ["".join([chess_map_from_index_to_letter[i[1]], str(i[0] + 1)]) for i in solutionMovesKnightFinal]
    return allPossibleMoves

# Defining the main

if __name__ == '__main__':

   # Using the argparse module to get the input arguments

    parser = argparse.ArgumentParser()
    parser.add_argument("-piece", "--piece", help=" This is the argument for the chess piece name: Ex: rook, bishop, knight or queen")
    parser.add_argument("-position", "--position", help="This is the notation for a position in the chess board: Ex: E4, D6, etc")
    args = parser.parse_args()

    piece = args.piece.strip().lower()
    position = args.position.strip()

    # According to the piece passing by parameter, adjust function
    if (piece == "rook"):
        print("moves for the " + piece + " in the position " + position + " :")
        print(getRookMoves(position, chessBoard))
    if (piece == "bishop"):
        print("moves for the " + piece + " in the position " + position +" :")
        print(getBishopMoves(position, chessBoard))
    elif (piece == "knight"):
        print("moves for the " + piece + " in the position " + position + " :")
        print(getKnightMoves(position, chessBoard))
    elif (piece == "queen"):
        print("moves for the " + piece + " in the position " + position + " :")
        print(getQueenMoves(position, chessBoard))