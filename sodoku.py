"""
Sodoku Solver

Input: partially complete board

Output: a solution, if one exists
"""

def solve(board, x, y):
  if x == 8 and y == 8 and accept(board):
    print_solution(board)
    return True
  if board[y][x] is not None:
    if x < 8:
      solve(board, x + 1, y)
    elif y < 8:
      solve(board, 0, y + 1)
  else:
    for i in range(1, 10):
      next_partial = next(board, x, y, i)
      if reject(next_partial, x, y):
        continue
      if x < 8:
        if solve(next_partial, x + 1, y):
          return True
      elif y < 8:
        if solve(next_partial, 0, y + 1):
          return True
      elif accept(next_partial):
        print_solution(next_partial)
        return True
      else:
        return False
    return False


def next(board, x, y, i):
  """
  Returns the next board to try.
  Fills position (x, y) with i.
  """
  new_board = [row[:] for row in board]
  new_board[y][x] = i
  return new_board


def accept(board):
  """
  Returns True if board is a valid solution.
  """
  for row in board:
    if None in row:
      return False
  for c in range(9):
    for r in range(9):
      if reject(board, c, r):
        return False
  return True


def reject(board, x, y):
  """
  Newest fill position (x,y).
  Returns True if board is not valid.
  """
  row_numbers = [n for n in board[y] if n is not None]
  is_unique_row = len(row_numbers) == len(set(row_numbers))
  column_numbers = [n[x] for n in board if n[x] is not None]
  is_unique_column = len(column_numbers) == len(set(column_numbers))
  box_numbers = []
  column_start = (x / 3) * 3
  row_start = (y / 3) * 3
  for c in range(3):
    for r in range(3):
      curr = board[row_start + r][column_start + c]
      if curr is not None:
        box_numbers.append(curr)
  is_unique_box = len(box_numbers) == len(set(box_numbers))
  return not is_unique_row or not is_unique_column or not is_unique_box


def print_solution(board):
  for row in board:
    print ' '.join([str(i) for i in row])


if __name__ == '__main__':
#  board = [[1, 4, 5, 3, 2, 7, 6, None, 8],
#          [8, 3, 9, None, 5, 4, 1, 2, 7],
#          [None, 7, 2, 9, 1, 8, 5, 4, 3],
#          [4, 9, None, 1, 8, 5, 3, None, 2],
#          [2, 1, 8, 4, None, 3, 9, 5, 6],
#          [7, None, 3, 2, 9, 6, 4, 8, None],
#          [3, 6, 7, 5, 4, 2, 8, 1, 9],
#          [9, None, 4, 7, None, 1, 2, 3, 5],
#          [5, 2, 1, 8, 3, 9, 7, 6, None]]
  board = []
  for i in range(9):
    board.append([None] * 9)
  solve(board, 0, 0)
    
