# FIFA-World-Cup-2022-Predictor

This repository contains a Python program to predict and calculate points for players' predictions in the FIFA World Cup 2022.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The FIFA World Cup 2022 Predictor is a Python program that allows users to make predictions for the FIFA World Cup 2022 matches. The program calculates the points for each player based on their predictions and the actual results of the matches. It provides a tabulated summary of each player's points for different stages of the competition.

## Installation

1. Clone the repository to your local machine
2. Install the required Python packages

3. Place the prediction files in the appropriate folders as described below

## Usage

1. Prepare the prediction files:
- Create a directory for each player (e.g., Player1, Player2).
- In each player's directory, create text files for their predictions for each stage of the competition:
  - `PlayerX - group prediction.txt` (Group stage prediction)
  - `PlayerX - round of 16 prediction.txt` (Round of 16 prediction)
  - `PlayerX - quarter final prediction.txt` (Quarter-final prediction)
  - `PlayerX - semi final prediction.txt` (Semi-final prediction)
  - `PlayerX - final prediction.txt` (Final prediction)

Note: The file names should be in the format mentioned above, replacing "PlayerX" with the respective player's name.

2. Run the program: python main.py
3. The program will generate a table with the following columns:
- Player: The player's name
- Stage: The stage of the competition (Group Stage, Round of 16, Quarter Finals, Semi Finals, Finals)
- Points in Phase: The points earned by the player in that phase
- Total Points: The total points accumulated by the player throughout the competition

4. The table will be saved as `Table.txt` in the repository directory, and the same table will be displayed on the console.

## Output example
![image](https://github.com/8Altair/FIFA-World-Cup-2022-Predictor/assets/109831705/3b794a45-8abd-457d-9b2a-b958d40a42b3)


## License
This project is licensed under the [MIT License](LICENSE).


