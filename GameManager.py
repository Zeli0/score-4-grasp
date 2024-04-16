from enum import Enum
import numpy as np

class Turn(Enum):
  PLAYER1 = "Player 1"
  PLAYER2 = "Player 2"

class GameManager():
  def __init__(self) -> None:
    self.player1_moves = np.zeros((4, 4, 4), dtype=bool)
    self.player2_moves = np.zeros((4, 4, 4), dtype=bool)
    self.board_z = np.zeros((4, 4), dtype=int)
    self.player_turn = Turn.PLAYER1
    self.winner = None

  def get_board_size(self):
    return (4,4,4)

  def get_player1_moves(self):
    return np.where(self.player1_moves)
  
  def get_player2_moves(self):
    return np.where(self.player2_moves)

  def get_full_board(self):
    return self.player1_moves | self.player2_moves

  def is_top(self, y, x):
    return self.board_z[y,x] == 4
  
  def get_top_z(self, y, x):
    return self.board_z[y,x]
  
  def make_move(self, y, x):
    z = self.board_z[y,x]
    if self.player_turn == Turn.PLAYER1:
      self.player1_moves[y, x, z] = 1
    else:
      self.player2_moves[y, x, z] = 1
    self.board_z[y,x] = z + 1

  def switch_turns(self):
    self.player_turn = Turn.PLAYER2 if self.player_turn == Turn.PLAYER1 else Turn.PLAYER1

  def has_player_won(self):
    if self.player_turn == Turn.PLAYER1:
      player_moves = self.player1_moves
    else:
      player_moves = self.player2_moves

    has_won = False

    has_won_z = (player_moves == np.array([1,1,1,1])).all(axis=2).any()
    has_won_x = (player_moves == np.array([1,1,1,1])).all(axis=1).any()
    has_won_y = (player_moves == np.array([1,1,1,1])).all(axis=0).any()

    has_won = has_won or has_won_x or has_won_y or has_won_z

    if has_won:
      return has_won
    

    has_won_diag = False #np.all(player_moves[diag1] == 1) and np.all(player_moves[diag2] == 1)

    diag1 = np.array([[0,0], [1,1], [2,2], [3,3]])
    diag2 = np.array([[3,0], [2,1], [1,2], [0,3]])

    for i in range(4):
      for j in range(3):
        curr_diag1 = np.insert(diag1, j, i, axis=1)
        curr_diag2 = np.insert(diag2, j, i, axis=1)
        has_won_diag1 = np.all(player_moves[curr_diag1] == 1)
        has_won_diag2 = np.all(player_moves[curr_diag2] == 1)
        has_won_diag = has_won_diag or has_won_diag1 or has_won_diag2
    
    has_won = has_won or has_won_diag
    return has_won

    
