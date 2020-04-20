# Project 6a: Parser

Write an AI to parse sentences and extract noun phrases.

```
$ python parser.py
Sentence: Holmes sat.
        S
   _____|___
  NP        VP
  |         |
  N         V
  |         |
holmes     sat

Noun Phrase Chunks
holmes
```

## Video

[![Project 6a: Parser Video](http://img.youtube.com/vi/tBSRlNXgnog/0.jpg)](https://youtu.be/tBSRlNXgnog)

## Background

A common task in natural language processing is parsing, the process of determining the structure of a sentence. This is useful for a number of reasons: knowing the structure of a sentence can help a computer to better understand the meaning of the sentence, and it can also help the computer extract information out of a sentence. In particular, it’s often useful to extract noun phrases out of a sentence to get an understanding for what the sentence is about.

In this problem, we’ll use the context-free grammar formalism to parse English sentences to determine their structure. Recall that in a context-free grammar, we repeatedly apply rewriting rules to transform symbols into other symbols. The objective is to start with a nonterminal symbol `S` (representing a sentence) and repeatedly apply context-free grammar rules until we generate a complete sentence of terminal symbols (i.e., words). The rule `S -> N V`, for example, means that the `S` symbol can be rewritten as `N V` (a noun followed by a verb). If we also have the rule `N -> "Holmes"` and the rule `V -> "sat"`, we can generate the complete sentence `"Holmes sat."`.

Of course, noun phrases might not always be as simple as a single word like `"Holmes"`. We might have noun phrases like `"my companion"` or `"a country walk"` or `"the day before Thursday"`, which require more complex rules to account for. To account for the phrase `"my companion"`, for example, we might imagine a rule like:

```
NP -> N | Det N
```

In this rule, we say that an `NP` (a “noun phrase”) could be either just a noun (`N`) or a determiner (`Det`) followed by a noun, where determiners include words like `"a"`, `"the"`, and `"my"`. The vertical bar (`|`) just indicates that there are multiple possible ways to rewrite an `NP`, with each possible rewrite separated by a bar.

To incorporate this rule into how we parse a sentence (`S`), we’ll also need to modify our `S -> N V` rule to allow for noun phrases (`NP`s) as the subject of our sentence. See how? And to account for more complex types of noun phrases, we may need to modify our grammar even further.

## Specification

Complete the implementation of `preprocess` and `np_chunk`, and complete the context-free grammar rules defined in `NONTERMINALS`.

- The `preprocess` function should accept a `sentence` as input and return a lowercased list of its words.
    - You may assume that `sentence` will be a string.
    - You should use `nltk`’s `word_tokenize` function to perform tokenization.
    - Your function should return a list of words, where each word is a lowercased string.
    - Any word that doesn’t contain at least one alphabetic character (e.g. `.` or `28`) should be excluded from the returned list.
- The `NONTERMINALS` global variable should be replaced with a set of context-free grammar rules that, when combined with the rules in `TERMINALS`, allow the parsing of all sentences in the `sentences/` directory.
    - Each rules must be on its own line. Each rule must include the `->` characters to denote which symbol is being replaced, and may optionally include `|` symbols if there are multiple ways to rewrite a symbol.
    - You do not need to keep the existing rule `S -> N V` in your solution, but your first rule must begin with `S ->` since `S` (representing a sentence) is the starting symbol.
    - You may add as many nonterminal symbols as you would like.
    - Use the nonterminal symbol `NP` to represent a “noun phrase”, such as the subject of a sentence.
- The `np_chunk` function should accept a `tree` representing the syntax of a sentence, and return a list of all of the noun phrase chunks in that sentence.
    - For this problem, a “noun phrase chunk” is defined as a noun phrase that doesn’t contain other noun phrases within it. Put more formally, a noun phrase chunk is a subtree of the original tree whose label is `NP` and that does not itself contain other noun phrases as subtrees.
        - For example, if `"the home"` is a noun phrase chunk, then `"the armchair in the home"` is not a noun phrase chunk, because the latter contains the former as a subtree.
    - You may assume that the input will be a `nltk.tree` object whose label is `S` (that is to say, the input will be a tree representing a sentence).
    - Your function should return a list of `nltk.tree` objects, where each element has the label `NP`.
    - You will likely find the documentation for `nltk.tree` helpful for identifying how to manipulate a `nltk.tree` object.

You should not modify anything else in `parser.py` other than the functions the specification calls for you to implement, though you may write additional functions and/or import other Python standard library modules. You will need to modify the definition of `NONTERMINALS`, but you should not modify the definition of `TERMINALS`.