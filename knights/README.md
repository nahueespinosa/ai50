# Project 1a: Knights

Write a program to solve logic puzzles.

## Video

[![Project 1a: Knights Video](http://img.youtube.com/vi/NagQUqtGMt8/0.jpg)](https://youtu.be/NagQUqtGMt8)

## Background

In 1978, logician Raymond Smullyan published “What is the name of this book?”, a book of logical puzzles. Among the puzzles in the book were a class of puzzles that Smullyan called “Knights and Knaves” puzzles.

In a Knights and Knaves puzzle, the following information is given: Each character is either a knight or a knave. A knight will always tell the truth: if knight states a sentence, then that sentence is true. Conversely, a knave will always lie: if a knave states a sentence, then that sentence is false.

The objective of the puzzle is, given a set of sentences spoken by each of the characters, determine, for each character, whether that character is a knight or a knave.

For example, consider a simple puzzle with just a single character named A. A says “I am both a knight and a knave.”

Logically, we might reason that if A were a knight, then that sentence would have to be true. But we know that the sentence cannot possibly be true, because A cannot be both a knight and a knave – we know that each character is either a knight or a knave, but not both. So, we could conclude, A must be a knave.

That puzzle was on the simpler side. With more characters and more sentences, the puzzles can get trickier! Your task in this problem is to determine how to represent these puzzles using propositional logic, such that an AI running a model-checking algorithm could solve these puzzles for us.

## Specification

Add knowledge to knowledge bases `knowledge0`, `knowledge1`, `knowledge2`, and `knowledge3` to solve the following puzzles.

- Puzzle 0 is the puzzle from the Background. It contains a single character, A.
    - A says “I am both a knight and a knave.”
- Puzzle 1 has two characters: A and B.
    - A says “We are both knaves.”
    - B says nothing.
- Puzzle 2 has two characters: A and B.
    - A says “We are the same kind.”
    - B says “We are of different kinds.”
- Puzzle 3 has three characters: A, B, and C.
    - A says either “I am a knight.” or “I am a knave.”, but you don’t know which.
    - B says “A said ‘I am a knave.’”
    - B then says “C is a knave.”
    - C says “A is a knight.”

In each of the above puzzles, each character is either a knight or a knave. Every sentence spoken by a knight is true, and every sentence spoken by a knave is false.

Once you’ve completed the knowledge base for a problem, you should be able to run `python puzzle.py` to see the solution to the puzzle.