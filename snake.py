import random
import time

# Define snakes (head: tail) and ladders (bottom: top)
SNAKES = {
    99: 54,
    88: 24,
    70: 55,
    52: 42,
    25: 2
}

LADDERS = {
    6: 25,
    11: 40,
    46: 90,
    60: 85,
    17: 69
}

# Creative Twist: Mystery tiles that trigger random good or bad events!
MYSTERY_TILES = [15, 33, 49, 64, 78, 92]


def get_players():
    """Ask for the number of players and their custom names."""
    print("==========================================")
    print("🐍🪜  WELCOME TO MYSTERY SNAKE & LADDER!  🪜🐍")
    print("==========================================")

    while True:
        try:
            num_players = int(input("\nHow many players want to play? (2-4): "))
            if 2 <= num_players <= 4:
                break
            print("⚠️ Please enter a number between 2 and 4.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number (2, 3, or 4).")

    players = []
    tokens = ["P1", "P2", "P3", "P4"]

    print("\n--- Enter Player Names ---")
    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1} (or press Enter for 'Player {i + 1}'): ").strip()
        if not name:
            name = f"Player {i + 1}"
        players.append({
            "name": name,
            "token": tokens[i],
            "pos": 0
        })

    return players


def trigger_mystery(player):
    """Apply a random creative event when landing on a '?' tile."""
    events = [
        ("🚀 Rocket Boost! Jump ahead 7 spaces!", 7),
        ("🌀 Time Warp! Slide back 5 spaces!", -5),
        ("🍀 Lucky Charm! Move forward 4 spaces!", 4),
        ("🍌 Banana Peel! Slip back 3 spaces!", -3)
    ]
    message, shift = random.choice(events)
    print(f"   🎁 MYSTERY TILE! {message}")
    new_pos = max(1, min(99, player["pos"] + shift))  # Keep between 1 and 99
    return new_pos


def display_board(players):
    """Render a live 10x10 board showing all players, snakes, ladders, and mystery tiles."""
    print("\n" + "=" * 61)
    for row in range(9, -1, -1):
        row_cells = []
        for col in range(10):
            # Zig-zag numbering from 1 to 100
            num = row * 10 + (10 - col) if row % 2 == 1 else row * 10 + (col + 1)

            # Check which players are on this square
            here = [p["token"] for p in players if p["pos"] == num]

            if len(here) > 1:
                cell = f"*{len(here)}P* "  # Shows *2P*, *3P*, etc. if multiple players share a tile
            elif len(here) == 1:
                cell = f" [{here[0]}]"
            elif num in SNAKES:
                cell = f"S->{SNAKES[num]:02d}"
            elif num in LADDERS:
                cell = f"L->{LADDERS[num]:02d}"
            elif num in MYSTERY_TILES:
                cell = "  ?  "
            else:
                cell = f" {num:3d} "
            row_cells.append(cell)
        print("|" + "|".join(row_cells) + "|")
    print("=" * 61)

    # Live Scoreboard
    status = " | ".join([f"{p['name']} ({p['token']}): {p['pos']}" for p in players])
    print(f"📊 Standings -> {status}\n")


def take_turn(player):
    """Handle dice rolling, bonus rolls on 6, movement, and special tiles."""
    while True:
        input(f"👉 {player['name']}'s turn ({player['token']}) — Press Enter to roll...")
        dice = random.randint(1, 6)
        print(f"🎲 {player['name']} rolled a {dice}!")

        if player["pos"] + dice > 100:
            print(f"   🚫 Overshot 100! {player['name']} stays at {player['pos']}.")
        else:
            old_pos = player["pos"]
            player["pos"] += dice
            print(f"   👣 Moved from {old_pos} -> {player['pos']}")

            # Check Snakes, Ladders, or Mystery Tiles
            if player["pos"] in SNAKES:
                dest = SNAKES[player["pos"]]
                print(f"   🐍 CHOMP! Bitten by a snake at {player['pos']}! Sliding down to {dest}...")
                player["pos"] = dest
            elif player["pos"] in LADDERS:
                dest = LADDERS[player["pos"]]
                print(f"   🪜 CLIMB! Found a ladder at {player['pos']}! Climbing up to {dest}...")
                player["pos"] = dest
            elif player["pos"] in MYSTERY_TILES:
                player["pos"] = trigger_mystery(player)
                print(f"   📍 {player['name']} is now at {player['pos']}.")

        # Check for win condition immediately
        if player["pos"] == 100:
            return True

        # Creative Rule: Rolling a 6 grants a bonus roll!
        if dice == 6:
            print(f"   🔥 BONUS ROLL! {player['name']} rolled a 6 and gets to go again!")
            time.sleep(0.6)
        else:
            return False


def play_game():
    """Main game loop."""
    players = get_players()
    print("\nLegend: [P1] = Player Token | S->XX = Snake | L->XX = Ladder | ? = Mystery Tile")
    display_board(players)

    while True:
        for player in players:
            won = take_turn(player)
            display_board(players)
            if won:
                print("🎉" * 20)
                print(f"🏆 CONGRATULATIONS {player['name'].upper()}! YOU WON THE GAME! 🏆")
                print("🎉" * 20)
                return
            time.sleep(0.4)


if __name__ == "__main__":
    play_game()
