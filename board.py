import json
class Board:

    def __init__(self):

        self.squares = [[0 for _ in range(8)]
                        for _ in range(8)]
        
        with open('piece_movements.json') as f:
            self.piece_movements = json.load(f)
        
        self.black_king = (0,4)
        self.white_king = (7,4)
        
    def check_if_in_check(self):
        if self.black_king in self.get_all_valid_moves(1):
            print("Black is in check!")
            
        if self.white_king in self.get_all_valid_moves(-1):
            print("White is in check!")
        
    
    def get_all_valid_moves(self, player):
        moves = []
        for i in range(8):
            for j in range(8):
                if player*self.squares[i][j]>0:
                    moves.extend(self.get_valid_piece_moves((i,j)))
                    moves.extend(self.get_valid_pawn_moves((i,j)))
        return moves
        
    def get_valid_piece_moves(self, piece):
        '''
        Returns all possible moves for the given piece by square coordinates.
        '''
          
        current_piece = self.squares[piece[0]][piece[1]]
        
        piece_dir = self.piece_movements[str(abs(current_piece))]['direction']
        rows = piece_dir['row']
        cols = piece_dir['col']
        
        distance = self.piece_movements[str(abs(current_piece))]['distance']
        
        valid_moves = []
        
        for r,c in zip(rows, cols): 
            for d in range(1, distance+1):
                row = piece[0]+d*r
                col = piece[1]+d*c
                if 0 <= row <= 7 and  0 <= col <= 7:
                    
                    # Empty square
                    if(self.squares[row][col]==0): 
                        valid_moves.append((row, col))
                    # Own square    
                    elif(self.squares[row][col]*current_piece>0):
                        break
                    # Enemy square
                    else:
                        valid_moves.append((row, col))
                        break
        return valid_moves
    
    def get_valid_pawn_moves(self, piece):
        '''
        Gives out all valid pawn moves, white goes up, black is down
        '''
        current_piece = self.squares[piece[0]][piece[1]]

        valid_moves=[]
        
        if self.squares[-current_piece+piece[0]][piece[1]]==0:
            valid_moves.append((-current_piece+piece[0],piece[1]))
            
        row = int(-current_piece+piece[0])
        col = int(piece[1])
        # Checks if the front is empty
        if self.squares[row][col]==0:
            valid_moves.append((row,col))
            if (piece[0]*current_piece == 6 or piece[0]*current_piece == -1) and self.squares[-current_piece*2+piece[0]][piece[1]]==0:
                valid_moves.append((row-current_piece,col))       
        
        # Checks if enemy squary        
        if col+1 <= 7:
            if self.squares[row][col+1]*current_piece<0:
                valid_moves.append((row,col+1))
        
        if col-1 >= 0:
            if self.squares[row][col-1]*current_piece<0:
                valid_moves.append((row,col-1))    
        return valid_moves