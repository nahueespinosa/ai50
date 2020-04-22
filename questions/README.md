# Project 6b: Questions

Write an AI to answer questions.

```
$ python questions.py corpus
Query: What are the types of supervised learning?
Types of supervised learning algorithms include Active learning , classification and regression.

$ python questions.py corpus
Query: When was Python 3.0 released?
Python 3.0 was released on 3 December 2008.

$ python questions.py corpus
Query: How do neurons connect in a neural network?
Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers.
```

## Video

[![Project 6b: Questions Video](http://img.youtube.com/vi/kv9RDo-eDzo/0.jpg)](https://youtu.be/kv9RDo-eDzo)

## Background

Question Answering (QA) is a field within natural language processing focused on designing systems that can answer questions. Among the more famous question answering systems is Watson, the IBM computer that competed (and won) on Jeopardy!. A question answering system of Watson’s accuracy requires enormous complexity and vast amounts of data, but in this problem, we’ll design a very simple question answering system based on inverse document frequency.

Our question answering system will perform two tasks: document retrieval and passage retrieval. Our system will have access to a corpus of text documents. When presented with a query (a question in English asked by the user), document retrieval will first identify which document(s) are most relevant to the query. Once the top documents are found, the top document(s) will be subdivided into passages (in this case, sentences) so that the most relevant passage to the question can be determined.

How do we find the most relevant documents and passages? To find the most relevant documents, we’ll use tf-idf to rank documents based both on term frequency for words in the query as well as inverse document frequency for words in the query. Once we’ve found the most relevant documents, there many possible metrics for scoring passages, but we’ll use a combination of inverse document frequency and a query term density measure (described in the Specification).

More sophisticated question answering systems might employ other strategies (analyzing the type of question word used, looking for synonyms of query words, lemmatizing to handle different forms of the same word, etc.) but we’ll leave those sorts of improvements as exercises for you to work on if you’d like to after you’ve completed this project!

## Specification

Complete the implementation of `load_files`, `tokenize`, `compute_idfs`, `top_files`, and `top_sentences` in `questions.py`.

- The `load_files` function should accept the name of a `directory` and return a dictionary mapping the filename of each `.txt` file inside that directory to the file’s contents as a string.
    - Your function should be platform-independent: that is to say, it should work regardless of operating system. Note that on macOS, the `/` character is used to separate path components, while the `\` character is used on Windows. Use `os.sep` and `os.path.join` as needed instead of using your platform’s specific separator character.
    - In the returned dictionary, there should be one key named for each `.txt` file in the directory. The value associated with that key should be a string (the result of reading the corresonding file).
    - Each key should be just the filename, without including the directory name. For example, if the directory is called `corpus` and contains files `a.txt` and `b.txt`, the keys should be `a.txt` and `b.txt` and not `corpus/a.txt` and `corpus/b.txt`.
- The `tokenize` function should accept a `document` (a string) as input, and return a list of all of the words in that document, in order and lowercased.
    - You should use `nltk`’s word_tokenize function to perform `tokenization`.
    - All words in the returned list should be lowercased.
    - Filter out punctuation and stopwords (common words that are unlikely to be useful for querying). Punctuation is defined as any character in `string.punctuation` (after you `import string`). Stopwords are defined as any word in `nltk.corpus.stopwords.words("english")`.
    - If a word appears multiple times in the `document`, it should also appear multiple times in the returned list (unless it was filtered out).
- The `compute_idfs` function should accept a dictionary of `documents` and return a new dictionary mapping words to their IDF (inverse document frequency) values.
    - Assume that `documents` will be a dictionary mapping names of documents to a list of words in that document.
    - The returned dictionary should map every word that appears in at least one of the documents to its inverse document frequency value.
    - Recall that the inverse document frequency of a word is defined by taking the natural logarithm of the number of documents divided by the number of documents in which the word appears.
- The `top_files` function should, given a `query` (a set of words), `files` (a dictionary mapping names of files to a list of their words), and `idfs` (a dictionary mapping words to their IDF values), return a list of the filenames of the the `n` top files that match the query, ranked according to tf-idf.
    - The returned list of filenames should be of length `n` and should be ordered with the best match first.
    - Files should be ranked according to the sum of tf-idf values for any word in the query that also appears in the file. Words in the query that do not appear in the file should not contribute to the file’s score.
    - Recall that tf-idf for a term is computed by multiplying the number of times the term appears in the document by the IDF value for that term.
- The `top_sentences` function should, given a `query` (a set of words), `sentences` (a dictionary mapping sentences to a list of their words), and `idfs` (a dictionary mapping words to their IDF values), return a list of the `n` top sentences that match the query, ranked according to IDF.
    - The returned list of sentences should be of length `n` and should be ordered with the best match first.
    - Sentences should be ranked according to “matching word measure”: namely, the sum of IDF values for any word in the query that also appears in the sentence. Note that term frequency should not be taken into account here, only inverse document frequency.
    - If two sentences have the same value according to the matching word measure, then sentences with a higher “query term density” should be preferred. Query term density is defined as the proportion of words in the sentence that are also words in the query. For example, if a sentence has 10 words, 3 of which are in the query, then the sentence’s query term density is `0.3`.

You should not modify anything else in `questions.py` other than the functions the specification calls for you to implement, though you may write additional functions, add new global constant variables, and/or import other Python standard library modules.