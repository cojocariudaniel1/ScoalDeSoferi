from PIL import Image

def chess_table():
    square_gray_dark = "sprites/square gray dark _1x_ns.png"
    square_gray_light ="sprites/square gray light _1x_ns.png"
    return square_gray_dark, square_gray_light

    


def pieces(nr):
    b_bishop = "sprites/b_bishop.png"
    b_knight = "sprites/b_knight.png"
    b_pawn = "sprites/b_pawn.png"
    b_queen = "sprites/b_queen.png"
    b_rook = "sprites/b_rook.png"
    b_king = "sprites/b_king.png"

    w_bishop = "sprites/w_bishop.png"
    w_knight = "sprites/w_knight.png"
    w_king = "sprites/w_king.png"
    w_pawn = "sprites/w_pawn.png"
    w_queen = "sprites/w_queen.png"
    w_rook_ns = "sprites/w_rook_ns.png"
    
    if nr == 50 or nr == 51:
        return w_rook_ns
    elif nr == -50 or nr == -51:
        return b_rook
    elif nr == 40 or nr == 41:
        return w_bishop
    elif nr == -40 or nr == -41:
        return b_bishop
    elif nr == 30 or nr == 31:
        return w_knight
    elif nr == -30 or nr == -31:
        return b_knight
    elif nr == 9:
        return w_queen
    elif nr == -9:
        return b_queen
    elif nr == 10:
        return w_king
    elif nr == -10:
        return b_king
    elif nr in [10,11,12,13,14,15,16,17,18]:
        return w_pawn
    elif nr in [-10,-11,-12,-13,-14,-15,-16,-17,-18]:
        return b_pawn
    