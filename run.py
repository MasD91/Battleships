"""
Battleships Game

This program allows two players to play the Battleships game on separate grids.
Each player's fleet of battleships is marked on their own grid.
Players take turns guessing the locations of the opponent's battleships.
You must destroy the opponent's fleet by guessing the correct coordinates.

"""

import random

GRID_SIZE = 5


class Player:
    def __init__(self, name):
        self.name = name
        self.grid = self.create_grid()
        self.enemy_grid = self.create_grid()
        self.battleships = []

    def create_grid(self):
        """
        Create an empty grid.
        """
        grid = []
        for _ in range(GRID_SIZE):
            grid.append(['O'] * GRID_SIZE)
        return grid

    def place_battleships(self, num_battleships):
        """
        Place the battleships on the grid.
        """
        size = len(self.grid)
        battleships_placed = 0

        while battleships_placed < num_battleships:
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)

            if self.grid[x][y] == 'O':
                self.grid[x][y] = 'B'
                self.battleships.append((x, y))
                battleships_placed += 1

    def is_off_grid(self, guess):
        """
        Check if the guess is off the grid.
        """
        x, y = guess
        return x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE

    def is_hit(self, guess):
        """
        Check if the guess hits a battleship.
        """
        x, y = guess
        return (x, y) in self.battleships

    def update_enemy_grid(self, guess, result):
        """
        Update the enemy grid with the result of the guess.
        """
        x, y = guess
        if result == 'Hit':
            self.enemy_grid[x][y] = 'X'
        else:
            self.enemy_grid[x][y] = 'M'

    def print_grids(self):
        """
        Print the player's grid and the enemy grid.
        """
        print(f"\nPlayer: {self.name}")
        print("Your Grid:")
        self.print_grid(self.grid)
        print("\nEnemy Grid:")
        self.print_grid(self.enemy_grid)

    def print_grid(self, grid):
        """
        Print the grid.
        """
        for row in grid:
            print(' '.join(row))


def play_game():
    print("Welcome to Battleships!")
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    player1 = Player(player1_name)
    player2 = Player(player2_name)

    num_battleships = int(input("Enter the number of battleships: "))

    player1.place_battleships(num_battleships)
    player2.place_battleships(num_battleships)

    current_player = player1
    opponent = player2

    while True:
        current_player.print_grids()

        guess = input(f"\n{current_player.name}, FIRE (row column): ")
        guess = guess.split()

        if len(guess) != 2:
            print("Invalid guess. Please enter two numbers.")
            continue

        try:
            x = int(guess[0])
            y = int(guess[1])
        except ValueError:
            print("Invalid guess. Please enter two numbers.")
            continue

        if current_player.is_off_grid((x, y)):
            print("Guess is off-grid. Try again.")
            continue

        if current_player.is_hit((x, y)):
            print("Hit!")
            current_player.update_enemy_grid((x, y), 'Hit')
            opponent.update_enemy_grid((x, y), 'Hit')
        else:
            print("Miss!")
            current_player.update_enemy_grid((x, y), 'Miss')
            opponent.update_enemy_grid((x, y), 'Miss')

        if all(cell == 'X' for row in opponent.enemy_grid for cell in row):
            print(f"\n{current_player.name}! You sank all the Battleships.")
            break

        current_player, opponent = opponent, current_player


# Run the game
if __name__ == "__main__":
    play_game()
