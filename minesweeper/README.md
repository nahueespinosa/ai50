# Project 1b: Minesweeper

Write an AI to play Minesweeper.

## Video

[![Project 1b: Minesweeper Video](http://img.youtube.com/vi/Asz3K-h0HEw/0.jpg)](https://youtu.be/Asz3K-h0HEw)

## Specification

Complete the implementations of the `Sentence` class and the `MinesweeperAI` class in `minesweeper.py`.

In the `Sentence` class, complete the implementations of `known_mines`, `known_safes`, `mark_mine`, and `mark_safe`.

 - The `known_mines` function should return a set of all of the cells in `self.cells` that are known to be mines.
 - The `known_safes` function should return a set of all the cells in `self.cells` that are known to be safe.
 - The `mark_mine` function should first check to see if `cell` is one of the cells included in the sentence.
    - If `cell` is in the sentence, the function should update the sentence so that `cell` is no longer in the sentence, but still represents a logically correct sentence given that `cell` is known to be a mine.
    - If `cell` is not in the sentence, then no action is necessary.
 - The `mark_safe` function should first check to see if `cell` is one of the cells included in the sentence.
    - If `cell` is in the sentence, the function should update the sentence so that `cell` is no longer in the sentence, but still represents a logically correct sentence given that `cell` is known to be safe.
    - If `cell` is not in the sentence, then no action is necessary.

In the `MinesweeperAI` class, complete the implementations of `add_knowledge`, `make_safe_move`, and `make_random_move`.

- `add_knowledge` should accept a `cell` (represented as a tuple `(i, j)`) and its corresponding `count`, and update `self.mines`, `self.safes`, `self.moves_made`, and `self.knowledge` with any new information that the AI can infer, given that `cell` is known to be a safe cell with `count` mines neighboring it.
    - The function should mark the `cell` as one of the moves made in the game.
    - The function should mark the `cell` as a safe cell, updating any sentences that contain the `cell` as well.
    - The function should add a new sentence to the AI’s knowledge base, based on the value of `cell` and `count`, to indicate that `count` of the `cell`’s neighbors are mines. Be sure to only include cells whose state is still undetermined in the sentence.
    - If, based on any of the sentences in `self.knowledge`, new cells can be marked as safe or as mines, then the function should do so.
    - If, based on any of the sentences in `self.knowledge`, new sentences can be inferred (using the subset method described in the Background), then those sentences should be added to the knowledge base as well.
- `make_safe_move` should return a move `(i, j)` that is known to be safe.
    - The move returned must be known to be safe, and not a move already made.
    - If no safe move can be guaranteed, the function should return `None`.
    - The function should not modify `self.moves_made`, `self.mines`, `self.safes`, or `self.knowledge`.
- `make_random_move` should return a random move `(i, j)`.
    - This function will be called if a safe move is not possible: if the AI doesn’t know where to move, it will choose to move randomly instead.
    - The move must not be a move that has already been made.
    - The move must not be a move that is known to be a mine.
    - If no such moves are possible, the function should return `None`.