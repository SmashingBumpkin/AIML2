"""
Coding
Implement a depth 2 limited minimax player that uses as evalation function:
f(n)=(# of 3 lengths open for MAX)-(# open for MIN)
Benchmark this agent by playing 20 games against:
A) A random player.
B) An expectimax that uses uniform probabilities associated to the actions.
C) MTCS player (N=200).
Collect and report the winning percentages by alternating the player that has the advantage of the first
move.
"""

import time
import random
import numpy as np
from collections import namedtuple

MAXVALUE = np.inf
MINVALUE = -np.inf


class Game:
    def __init__(self, initial_state):
        self.initial = initial_state

    def play(self, players):
        state = self.initial
        while True:
            for player in players:
                if self.is_terminal(state):
                    return
                move = player(self, state)
                state = self.result(state, move)
                self.display(state)

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, move):
        raise NotImplementedError

    def utility(self, state, player):
        raise NotImplementedError

    def is_terminal(self, state):
        return NotImplementedError

    def display(self, state):
        return NotImplementedError


GameState = namedtuple("GameState", ["to_move", "utility", "board", "moves"])


class TicTacToe(Game):
    def __init__(self, h=3, v=3, k=3):
        """Initialize TicTacToe with board size and winning condition."""
        super().__init__(
            GameState(
                to_move="X", utility=0, board={}, moves=self._all_possible_moves(h, v)
            )
        )
        self.h = h
        self.v = v
        self.k = k

    def _all_possible_moves(self, h, v):
        """Generate all possible moves on the given board size."""
        return [(x, y) for x in range(1, h + 1) for y in range(1, v + 1)]

    def actions(self, state):
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state
        board = state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        next_player = "O" if state.to_move == "X" else "X"
        return GameState(
            to_move=next_player,
            utility=self.compute_utility(board, move, state.to_move),
            board=board,
            moves=moves,
        )

    def utility(self, state, player):
        return state.utility if player == "X" else -state.utility

    def is_terminal(self, state):
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), "."), end=" ")
            print()

    def compute_utility(self, board, move, player):
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."""
        if (
            self.k_in_row(board, move, player, (0, 1))
            or self.k_in_row(board, move, player, (1, 0))
            or self.k_in_row(board, move, player, (1, -1))
            or self.k_in_row(board, move, player, (1, 1))
        ):
            return +1 if player == "X" else -1
        else:
            return 0

    def k_in_row(self, board, move, player, delta_x_y):
        """Return true if there is a line through move on board for player."""
        (delta_x, delta_y) = delta_x_y
        x, y = move
        n = 0  # n is number of moves in row
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Because we counted move itself twice
        return n >= self.k


def minmax_search(game, state):
    player = state.to_move

    def max_value(state):
        if game.is_terminal(state):
            return game.utility(state, player)
        v = MINVALUE
        for a in game.actions(state):
            v = max(v, min_value(game.result(state, a)))
        return v

    def min_value(state):
        if game.is_terminal(state):
            return game.utility(state, player)
        v = MAXVALUE
        for a in game.actions(state):
            v = min(v, max_value(game.result(state, a)))
        return v

    print(f" Turn of {player}, available actions {game.actions(state)}")
    return max(game.actions(state), key=lambda a: min_value(game.result(state, a)))


def random_player(game, state):
    return random.choice(list(game.actions(state)))


def player(search_algo):
    return lambda game, state: search_algo(game, state)


start_t = time.time()
TicTacToe().play([player(minmax_search), random_player])
end_t = time.time()
print(f"Execution time: {end_t-start_t:.2f} seconds")
