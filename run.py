"""
Battleships Game

This program allows two players to play the Battleships game on separate grids.
Each player's fleet of battleships is marked on their own grid.
Players take turns guessing the locations of the opponent's battleships.
This is a 2 player turn based game.
After your go is over, the board flips to the next players view.
You must destroy the opponent's fleet by guessing the correct coordinates.


"""

import random

GRID_SIZE = 5


class Player:
    """
    Class representing a player in the Battleships game.
    """

    def __init__(self, name):
        """
        Initialize a new Player instance.

        Args:
            name (str): The name of the player.
        """
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

        Args:
            num_battleships (int): The number of battleships to be placed.
        """
        size = len(self.grid)
        battleships_placed = 0

        while battleships_placed < num_battleships:
            row = random.randint(0, size - 1)
            column = random.randint(0, size - 1)

            if self.grid[row][column] == 'O':
                self.grid[row][column] = 'B'
                self.battleships.append((row, column))
                battleships_placed += 1

    def is_off_grid(self, guess):
        """
        Check if the guess is off the grid.

        Args:
            guess (tuple): The (row, column) coordinates of the guess.

        Returns:
            bool: True if the guess is off the grid, False otherwise.
        """
        row, column = guess
        return row < 0 or row >= GRID_SIZE or column < 0 or column >= GRID_SIZE

    def is_hit(self, guess):
        """
        Check if the guess hits a battleship.

        Args:
            guess (tuple): The (row, column) coordinates of the guess.

        Returns:
            bool: True if the guess hits a battleship, False otherwise.
        """
        row, column = guess
        return (row, column) in self.battleships

    def update_enemy_grid(self, guess, result):
        """
        Update the enemy grid with the result of the guess.

        Args:
            guess (tuple): The (row, column) coordinates of the guess.
            result (str): The result of the guess, either 'Hit' or 'Miss'.
        """
        row, column = guess
        if result == 'Hit':
            self.enemy_grid[row][column] = 'X'
        else:
            self.enemy_grid[row][column] = 'M'

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

        Args:
            grid (list): The grid to be printed.
        """
        for row in grid:
            print(' '.join(row))


def play_game():
    """
    Function to play the Battleships game.
    """
    print("Welcome to Battleships!")
    print("Two players play the Battleships game on separate grids.")
    print("Each player's fleet of battleships is marked on their own grid.")
    print("Guess the locations of the opponent's battleships.")
    print("This is a 2-player turn-based game.")
    print("After your go is over, the board flips to the next player's view.")
    print("Destroy the opponent's fleet by guessing the correct coordinates.")

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
            row = int(guess[0])
            column = int(guess[1])
        except ValueError:
            print("Invalid guess. Please enter two numbers.")
            continue

        if current_player.is_off_grid((row, column)):
            print("Guess is off-grid. Try again.")
            continue

        if current_player.is_hit((row, column)):
            print("Hit!")
            current_player.update_enemy_grid((row, column), 'Hit')
            opponent.update_enemy_grid((row, column), 'Hit')
        else:
            print("Miss!")
            current_player.update_enemy_grid((row, column), 'Miss')
            opponent.update_enemy_grid((row, column), 'Miss')

        if all(cell == 'X' for row in opponent.enemy_grid for cell in row):
            print(f"\n{current_player.name}! You sank all the Battleships.")
            break

        current_player, opponent = opponent, current_player


# Run the game
if __name__ == "__main__":
    play_game()
