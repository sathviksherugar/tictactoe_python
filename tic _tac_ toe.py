class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        print("\n")
        for row in self.grid:
            print(" | ".join(row))
            print("-" * 5)

    def make_move(self, row, col, symbol):
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # Rows & Columns
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)) or \
               all(self.grid[j][i] == symbol for j in range(3)):
                return True
        # Diagonals
        if all(self.grid[i][i] == symbol for i in range(3)) or \
           all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell in ["X", "O"] for row in self.grid for cell in row)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self):
        print("Welcome to Tic Tac Toe!")
        self.board = Board()
        self.player1 = Player(input("Enter name for Player 1 (X): "), "X")
        self.player2 = Player(input("Enter name for Player 2 (O): "), "O")
        self.current_player = self.player1

    def switch_turn(self):
        self.current_player = (
            self.player1 if self.current_player == self.player2 else self.player2
        )

    def play(self):
        while True:
            self.board.display()
            print(f"{self.current_player.name}'s turn ({self.current_player.symbol})")
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid position. Try again.")
                continue

            if not self.board.make_move(row, col, self.current_player.symbol):
                print("Cell is already occupied. Try another.")
                continue

            if self.board.check_winner(self.current_player.symbol):
                self.board.display()
                print(f"🎉 {self.current_player.name} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break

            self.switch_turn()
# Run the game
if __name__ == "__main__":
    game = Game()
    game.play()
