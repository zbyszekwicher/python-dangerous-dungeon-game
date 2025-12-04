Dangerous Dungeon - Python Push Your Luck Dungeon Crawler CLI Game



Core Gameplay:



Dangerous Dungeon is a text-based, push-your-luck RPG where the goal is to get the highest score (treasure value) while staying alive.



The further you delve:

&nbsp;- Foes are stronger

&nbsp;- Loot is more valuable.

&nbsp;- Your character levels up, resetting and increasing combat power.



The game is a test of risk management:

&nbsp;- If your character dies in combat, the game is over and your score will not be saved.

&nbsp;- Players can type `esc` before any encounter to safely escape the dungeon with the gathered loot. This value is then saved to the high score board.

The objective is to know when to retreat to achieve the highest possible score!



Hall of Fame

&nbsp;- Highest Recorded Score: 64

&nbsp;- Achieved by character called POLSKA FOREWER, on Level 4.

This means no one ever got as far as level 5.



Project Context \& Status



&nbsp;- Development Origin: The core gameplay loop was initially developed on a phone during a trip in 2020, with some functions and dual-language support added later.

&nbsp;- Settings: The game includes a starting menu to adjust difficulty, language and fight speed. The default speed (`delay`) is 7 (0.7 seconds between combat actions).



Known Issues (Legacy Code)



This project is presented as is to showcase early architectural design and game logic. If you run the game, you may encounter the following known bugs:



&nbsp;- File I/O Stability: The high score tracking occasionally fails due to file input/output errors when trying to read or write to the external `highscores` file.

&nbsp;- Legacy Code Errors: Minor display bugs or crashes may occur due to changes in variable handling across Python versions since 2020.



File Architecture \& Setup



The project is structured across five interdependent modules and includes English and Polish localization.



Files

&nbsp;- `Dangerous\_Dungeon\_Game.py`: Main entry point and settings menu.

&nbsp;- `script01.py` / `script1\_polski.py`: Core combat logic.

&nbsp;- `script2.py` / `script2\_polski.py`: English/Polish gameplay, story, monster lists, and loot tables.

&nbsp;- `highscores` (empty file): Required for score persistence.



Running the Game



1\.  Clone the Repository:

&nbsp;   ```bash

&nbsp;   git clone https://github.com/zbyszekwicher/python-dangerous-dungeon-game.git

&nbsp;   cd python-dangerous-dungeon-game

&nbsp;   ```

2\.  Run the Main File:

&nbsp;   ```bash

&nbsp;   python Dangerous\_Dungeon\_Game.py

&nbsp;   ```

