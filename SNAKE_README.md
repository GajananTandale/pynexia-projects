# 🐍🪜 Mystery Snake & Ladder (Python)

A creative, terminal-based multiplayer **Snake & Ladder** game built in Python. Beyond the classic 1–100 grid rules, this version features custom player profiles, bonus turns, and unpredictable **Mystery Tiles** that can boost you forward or send you slipping backward.

---

## ✨ Features

* **Multiplayer Support (2–4 Players):** Choose the number of players at the start of the game.
* **Custom Player Names:** Enter custom names for each player (with automatic defaults like `Player 1` if left blank).
* **Live 10×10 ASCII Game Board:** Displays a zig-zag 1–100 grid in the terminal that updates after every turn, including multi-player tile indicators (`*2P*`, `*3P*`) when players share a square.
* **Classic Snakes & Ladders:** Automatic coordinate updates when landing on a snake head (`S->XX`) or ladder base (`L->XX`).
* **Mystery Tiles (`?`):** Landing on a `?` square triggers a random event:
  * 🚀 **Rocket Boost:** Jump ahead 7 spaces
  * 🍀 **Lucky Charm:** Move forward 4 spaces
  * 🍌 **Banana Peel:** Slip back 3 spaces
  * 🌀 **Time Warp:** Slide back 5 spaces
* **Bonus Roll on 6:** Rolling a `6` grants an immediate extra turn.
* **Exact Finish Rule:** Players must roll the exact number needed to land on square `100` to win.

---

## 🛠️ Prerequisites

* **Python 3.6+**
* No external libraries required (uses Python's built-in `random` and `time` modules).

---

## 🚀 How to Run

1. **Clone or download** the project file (`creative_snake_ladder.py`).
2. **Open your terminal** or command prompt and navigate to the project folder:
   ```bash
   cd path/to/project
   ```
3. **Run the script:**
   ```bash
   python creative_snake_ladder.py
   ```

---

## 🎮 How to Play

1. Enter the number of players (**2 to 4**).
2. Type in a name for each player (or press **Enter** to use default names).
3. Press **Enter** on your turn to roll the 6-sided die.
4. Watch the live board and standings update automatically until the first player reaches **100**!

### Board Legend

| Symbol | Meaning |
| :--- | :--- |
| `[P1]` – `[P4]` | Individual player token |
| `*2P*` / `*3P*` | Multiple players on the same square |
| `S->XX` | Snake head (slides down to square `XX`) |
| `L->XX` | Ladder bottom (climbs up to square `XX`) |
| `?` | Mystery tile (triggers a random boost or trap) |

---

## 📂 Project Structure

```text
snake-and-ladder/
├── creative_snake_ladder.py   # Main game logic, board renderer, and player loop
└── README.md                  # Project documentation
```

