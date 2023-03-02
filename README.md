# Wordle Copilot

This repository contains a Python program that helps users solve the popular word-guessing game, Wordle. The program provides a list of best starting words and assists the user in filtering a list of five words in the English language. The user can filter words based on certain criteria, corresponding to the colors in the Wordle game. The program then prints the remaining words to assist the user in their next guess.

## Getting Started

### Prerequisites

- Python 3.x
- Git (optional)

### Installing

Clone this repository to your local machine using the following command:

```bash
git clone git@github.com:YigitEkin/wordle-copilot.git
```

Alternatively, you can download the repository as a ZIP file and extract it.

## Running the Program

To run the program, open a terminal or command prompt and navigate to the directory where the repository is located. Then run the following command:

```bash
cd src
cd copilot
python3 copilot.py
```

The program will provide a list of best starting words for the user. After the user has made their initial guess, the program will prompt the user to enter the letters that were correct and in the correct position (green), correct but in the wrong position (yellow), or incorrect (gray). Based on the user's input, the program will filter the list of possible words and provide a new list for the user's next guess.

The program will continue prompting the user for their guesses and providing filtered lists until the correct word is guessed or the user runs out of guesses.
