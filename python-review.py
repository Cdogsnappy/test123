# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 13:01:35 2021

@author: Martin
"""

for x in range(0, 101, 5):
    print(x, end=" ")
    
len("what is the length of this string")

print("waffle"[5])

print("123456789"[0:10:2])

count = 0
for char in "supercalifragilisticexpialidocious":
    if char in "aeiou":
        count+=1
print(count)

t = (1, "spaghetti", 3.2, 'h')
print(len(t), t[0:5:2])

a_list = [2, 'b', 4.2, [1, 5]]
a_list.append(46)
a_list[2] = 9.2
print(a_list)
print(a_list[:])

b_list = a_list[:]
a_list.extend([1, 2, 3])
b_list.append([1, 2, 3])
print(a_list, "\n", b_list)

print(list("spaghetti"))
print("i love python".split(" "))

class Board(object):
    '''
    Creates board of None objects with default size of 8
    '''
    def __init__(self, size=8):
        self.board = [[None for _ in range(size)] for _ in range(size)]
        
    def show_board(self):
        #need a cleaner way to print
        for row in self.board:
            print(row)
            
    def change(self, y, x, item):
        self.board[y][x] = item
        
chess_board = Board()

chess_board.change(4, 0, 5)
chess_board.change(7, 7, 28)
chess_board.show_board()
