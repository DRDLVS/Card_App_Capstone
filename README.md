# Flashcard App

## Overview
This is a simple flashcard application built using Python and Tkinter. It helps users learn French vocabulary by displaying random French words and their English translations. The application keeps track of learned words and allows users to practice only the words they have yet to master.

## Features
- Displays a random French word and its English translation after 3 seconds.
- Allows users to mark words as "known" or "unknown".
- Saves progress by removing known words from the learning set.
- Uses CSV files to store vocabulary words.
- Interactive and user-friendly UI with buttons for user interaction.

## How It Works
1. The application loads vocabulary words from `data/french_words.csv`.
2. If a `words_to_learn.csv` file exists, it loads the words from there to continue progress.
3. It selects a random French word and displays it.
4. After 3 seconds, the card flips to show the English translation.
5. The user can:
   - Click the ❌ button to see a new word.
   - Click the ✅ button to mark the word as known, removing it from the list.
6. The updated word list is saved to `words_to_learn.csv`, ensuring progress is retained.

## Installation
### Prerequisites
- Python 3.x
- Required libraries: `tkinter`, `pandas`

### Setup
1. Clone the repository or download the script.
2. Install dependencies using:
   ```sh
   pip install pandas
   ```
3. Run the script:
   ```sh
   python main.py
   ```

## File Structure
```
project-folder/
│-- images/
│   │-- card_front.png
│   │-- card_back.png
│   │-- wrong.png
│   │-- right.png
│-- data/
│   │-- french_words.csv
│   │-- words_to_learn.csv (generated after marking words as known)
│-- main.py
```

## Usage
- Start the program to display a French word.
- Wait 3 seconds to see the English translation.
- Use the ❌ button to skip a word and the ✅ button to mark it as known.
- The application updates the vocabulary list dynamically.

## Notes
- If `words_to_learn.csv` is missing, the program resets the learning progress using `french_words.csv`.
- Ensure that all image files are present in the `images/` directory to avoid UI issues.

---
Happy Learning! 🎓

