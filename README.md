# Title

Chess Exercise

# Description

A python program consisting in give all the potential chess board positions of a given piece (rook, bishop, knight and queen) could advance to, with one move, from the given position, with the assumption there are no other pieces on the chess board.

# Getting Started

The project consists of one simple file named chessgame.py. which received two parameters: 

  - piece: This is the argument for the chess piece name: Ex: rook, bishop, knight or queen.
  - position: This is the notation for a position in the chess board: Ex: E4, D6, etc.
 
In addition, the parameter **help** to receiv will show a help message 
  
The output will be all the possible moves given the piece and its position

# Prerequisites

This project was developed with Python 2.7.9 in Windows

# Examples

In this section are presented four test cases, one for each chess piece that is included in our implementation:

**1. Rook**

Rook moves horizontally and vertically. If the parameters passed are:  “rook E6”
The output would be: A6, B6, C6, D6, F6, G6, H6, E1, E2, E3, E4, E5, E7, E8

Test:

  - Input

   > chessgame.py -piece rook -position E6

  - Output: 

   > moves for the rook in the position E6 :

   > ['a6', 'b6', 'c6', 'd6', 'f6', 'g6', 'h6', 'e1', 'e2', 'e3', 'e4', 'e5', 'e7', 'e8']
   
**2. Bishop**

Bishop moves diagonally. If the parameters passed are:  “bishop E6”
The output would be: D5, C4, B3, A2, F7, G8, D7, C8, F5, G4, H3

Test:

  - Input

   > chessgame.py -piece bishop -position E6

  - Output: 

   > moves for the bishop in the position e6 :

   > ['d5', 'c4', 'b3', 'a2', 'f7', 'g8', 'd7', 'c8', 'f5', 'g4', 'h3']
   
**3. Queen**

Queen moves horizontally, vertically and diagonally. If the parameters passed are:  “queen E6”
The output would be: A6, B6, C6, D6, F6, G6, H6, E1, E2, E3, E4, E5, E7, E8, D5, C4, B3, A2, F7, G8, D7, C8, F5, g4, H3

  Test:

  - Input

   > chessgame.py -piece queen -position E6

  - Output: 

   > moves for the queen in the position e6 :

   > ['a6', 'b6', 'c6', 'd6', 'f6', 'g6', 'h6', 'e1', 'e2', 'e3', 'e4', 'e5', 'e7', 'e8', 'd5', 'c4', 'b3', 'a2', 'f7', 'g8', 'd7', 'c8', 'f5', 'g4', 'h3']
   
**4. Knight**

Knight moves in an L way, that means two positions in the row direction and the other in the column direction and vice versa, two in the column direction and the other in the row direction. If the parametters passed are:  “knight E6”
The output would be: C7, G7, D8, F8, G5, C5, F4, D4

  Test:

  - Input

   > chessgame.py -piece queen -position E6

  - Output: 

   > moves for the knight in the position e6 :

   > ['c7', 'g7', 'd8', 'f8', 'g5', 'c5', 'f4', 'd4']


# Authors

Javier Jiménez - javierjaleman1986@gmail.com
