# Speed Typing Test

Welcome to the Speed Typing Test project! This is a terminal-based typing speed test application implemented in Python using the `curses` library for terminal handling and `wonderwords` to generate random sentences for typing practice.

## Features

- Welcome screen with instructions.
- Generates random test sentences dynamically using the `wonderwords` package.
- Displays real-time typing accuracy with color-coded feedback:
  - Green for correct characters
  - Red for incorrect characters
- Calculates and displays Words Per Minute (WPM) live.
- Supports backspace for corrections.
- Allows exit anytime by pressing the Escape key.

## Installation

1. Clone the repository:
git clone https://github.com/kartik1280/WPM-Typing-Test
cd speed-typing-test

2. Install dependencies:
pip install wonderwords

3. (For Windows users) You may need to install `windows-curses` for curses support:
pip install windows-curses

## Usage

Run the typing test with Python 3:
python main.py

- Upon launch, you will see a welcome screen. Press any key to start.
- A random sentence will appear. Type the sentence exactly as displayed.
- Characters typed correctly appear in green; mistakes appear in red.
- Your WPM (words per minute) updates as you type.
- Complete the sentence to finish the test.
- After completion, press any key to try another sentence or press Escape to exit.

## Notes

- The average word length assumed for WPM calculation is 5 characters.
- The program runs entirely in the terminal using curses for smooth input and display control.
- Backspace works with manual handling due to curses input behavior.
- Color rendering may vary depending on your terminal emulator.

## License
This project is for learning purposes. Feel free to use and modify it with proper credit.

## Author
Kartik Sharma

