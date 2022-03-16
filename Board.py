import numpy as np


class Board:
    def __init__(self):
        self.fields = np.zeros((8,8), dtype="u8")
        self.initalise_white_figueres()
        self.initialise_black_figures()

    def initialise_black_figures(self):
        self.fields[7][0] = 22  # black rook
        self.fields[7][7] = 22  # black rook
        self.fields[7][1] = 23  # black knight
        self.fields[7][6] = 23  # black knight
        self.fields[7][2] = 24  # black bishop
        self.fields[7][5] = 24  # black bishop
        self.fields[7][3] = 25  # black queen
        self.fields[7][4] = 26  # black king
        self.fields[6] = 21  # black pawns

    def initalise_white_figueres(self):
        self.fields[0][0] = 12  # white rook
        self.fields[0][7] = 12  # white rook
        self.fields[0][1] = 13  # white knight
        self.fields[0][6] = 13  # white knight
        self.fields[0][2] = 14  # white bishop
        self.fields[0][5] = 14  # white bishop
        self.fields[0][3] = 15  # white queen
        self.fields[0][4] = 16  # white king
        self.fields[1] = 11  # white pawns
