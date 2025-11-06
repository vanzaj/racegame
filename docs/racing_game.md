# 🎲 Emerson’s Car Racing Game

A fun way to learn about technical debt and legacy code

## Setup

1. Players join by scanning the QR code on the big screen.
2. Each player's car starts at the beginning line with 0 damage.
3. The finish line is at 20 steps away.


## What You See

- Big Screen (shared + organizer control):
  - Shows the race track, all cars, and their positions.
  - Displays the QR code for new players.
  - Organizer uses it to start each round.
- Player Screen (on your phone):
  - Buttons to pick your move (Normal or Super).
  - Shows your dice roll, base step, damage, and final movement.


## How to Play (Each Round)

1. Organizer starts a round.
2. Each player chooses:
   - *Normal*: safer, no extra damage.
   - *Super*: faster, but +1 damage.
3. Dice are rolled (1–6).
   - If you chose Normal:
     - Even roll (2, 4, 6) → base step = 2
     - Odd roll (1, 3, 5) → base step = 1
     - If you chose Super:
       - Base step = the dice number (1–6)
       - Damage increases by 1
4. Final movement = base step – current damage (minimum 0).
5. Move your car forward by the final movement.


## Winning

- The first player to reach or pass the finish line wins.
- Once a winner is declared, the game ends.


## Example Moves
- Normal, 0 damage, roll 2 → base step 2 – 0 = 2 steps
- Normal, 1 damage, roll 3 → base step 1 – 1 = 0 steps
- Super, 0 damage, roll 4 → base step 4 – 1 = 3 steps (damage becomes 1)
- Super, 1 damage, roll 2 → base step 2 – 2 = 0 steps (damage becomes 2)

-----

✅ Simple formula: Final movement = base step – damage (never negative).
✅ Works with 3 to 100 players.
✅ Fun to watch on the big screen, fun to play on your phone.

