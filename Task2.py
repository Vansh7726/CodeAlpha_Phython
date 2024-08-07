import tkinter as tk
from tkinter import messagebox
import random
import time

# Define constants
GRID_SIZE = 4
NUM_PAIRS = (GRID_SIZE * GRID_SIZE) // 2
TIME_LIMIT = 60  # Time limit in seconds

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game")

        self.buttons = []
        self.cards = []
        self.first_card = None
        self.second_card = None
        self.flipped_buttons = []
        self.pairs_found = 0
        self.start_time = None

        self.setup_game()
    
    def setup_game(self):
        # Create a list of pairs of numbers
        numbers = list(range(NUM_PAIRS)) * 2
        random.shuffle(numbers)
        self.cards = numbers

        # Create the grid of buttons
        for r in range(GRID_SIZE):
            row_buttons = []
            for c in range(GRID_SIZE):
                button = tk.Button(self.root, width=10, height=5, command=lambda r=r, c=c: self.on_card_click(r, c))
                button.grid(row=r, column=c)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        # Start the timer
        self.start_time = time.time()
        self.root.after(1000, self.check_time)

    def on_card_click(self, r, c):
        if len(self.flipped_buttons) >= 2:
            return
        
        button = self.buttons[r][c]
        index = r * GRID_SIZE + c

        # Show card
        button.config(text=self.cards[index], state="disabled")
        self.flipped_buttons.append((r, c))

        if len(self.flipped_buttons) == 2:
            self.root.after(500, self.check_match)

    def check_match(self):
        r1, c1 = self.flipped_buttons[0]
        r2, c2 = self.flipped_buttons[1]

        index1 = r1 * GRID_SIZE + c1
        index2 = r2 * GRID_SIZE + c2

        if self.cards[index1] == self.cards[index2]:
            self.pairs_found += 1
            if self.pairs_found == NUM_PAIRS:
                self.end_game("Congratulations! You've found all pairs!")
        else:
            # Hide cards
            self.buttons[r1][c1].config(text="", state="normal")
            self.buttons[r2][c2].config(text="", state="normal")
        
        self.flipped_buttons = []

    def check_time(self):
        elapsed_time = time.time() - self.start_time
        remaining_time = TIME_LIMIT - elapsed_time

        if remaining_time <= 0:
            self.end_game("Time's up! Game over.")
        else:
            self.root.after(1000, self.check_time)

    def end_game(self, message):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                self.buttons[r][c].config(state="disabled")

        messagebox.showinfo("Game Over", message)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
