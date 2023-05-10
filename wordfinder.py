"""Word Finder: finds random words from a dictionary."""

import random
"""Imports python random library."""

class WordFinder:
    """Finds random words fron a txt file provided.
    >>> w = WordFinder("testwords.txt")
    4 words read

    >>> w.random() in ["Milk", "Cheese", "Bread", "Eggs"]
    True

    >>> w.random() in ["Milk", "Cheese", "Bread", "Eggs"]
    True
    """
    
    def __init__(self, file_path):
        """Reads words file and prints the number of words."""
        
        word_file = open(file_path)
        self.words = self.parse_file(word_file)
        print(f'{len(self.words)} words read')
        
    def parse_file(self, word_file):
        """Parses the word_file."""
        return [word.strip() for word in word_file]
    
    def random(self):
        """Returns a random word from the word_file."""
        return random.choice(self.words)
    
    
class SpecialWordFinder(WordFinder):
    """Finds random words fron a txt file provided, but will not include comments starting with '#' or blank lines.
    >>> w = SpecialWordFinder("words2.txt")
    4 words read

    >>> w.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> w.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """
    
    def parse_file(self, word_file):
        """Parses the word file ignoring comments starting with '#' and blank lines."""
        return [word.strip() for word in word_file if word.strip() and not word.startswith('#')]