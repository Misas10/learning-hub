# Teaching Notes

## Learner profile
- **Level:** ~1000 rapid on chess.com. Knows the rules and basics.
- **Motivation:** Rating. Wants to reach "at least intermediate" — 1500 rapid, confirmed 2026-09-30.
- **Time:** ~3–5 h/week, rapid (10+0, 15+10).
- **Self-reported leaks:** no plan in the middlegame; can't convert winning positions / endgames. Did *not* pick "I hang pieces" or "lost out of the opening".

## Teaching preferences
- Carried over from the system-design course (same learner): short lessons, one root fact → derive the consequences, end each lesson with a real fork in the road, seed the ask-teacher box with tempting questions.
- Chess is skills-heavy: every lesson needs boards and a move to choose, not just prose.

## Accounts
- chess.com: `Misas10` (rapid 1080, best 1175; puzzles 1784). Lichess: `Misas_10` (rapid 1380 provisional, 814 games; puzzles 2013 over 8,170 attempts).

## Game data (2026-09-30): what the losses actually are
Engine pass over the 36 most recent chess.com rapid games (all 10+0; 29 from Mar–Apr 2026, 7 from Sep 2026). 17 wins, 17 losses, 2 draws. Shallow search (150k nodes/move), so treat numbers as rough. See [[0002-losses-are-thrown-wins-and-early-blunders]].
- **Thrown wins:** reached +5 or better in 25 games, won 16. The other 9 are half of all non-wins. Self-report of "can't convert" is confirmed.
- **Mechanism is one-move blunders, not technique:** 54 blunders (eval drop of 3+ pawns while still in the game), 1.5 per game; 27 of them made while already +3 or better. Examples: 167760480518 move 12 (Bf7+ gives a bishop away at +6.8, 7 min on clock); 167720614856 move 29 (free queen on d6 not taken, own bishop lost instead).
- **Clock:** both timeout losses came from +9 positions (167731107256: queen hung with 7 s left). Meanwhile 7 losses ended with 5+ minutes unused.
- **Early collapses (not self-reported):** 8 of 17 losses were decided by move 13 by a tactical blunder. Example: 167802513552 move 11, Qxb7 pawn grab.
- **Puzzle gap:** puzzle ratings 700–900 points above rapid. Sees tactics when told one exists; does not look for them unprompted in games.
- **"No plan in the middlegame"**: not visible as a cause of losses in this data. Park it until the blunder rate is down.
- The opponents blunder just as often (59 times); 19 of 64 chances were not punished.

Re-run with `tools/` (needs python-chess and a Stockfish binary; paths inside the scripts point at a scratch directory and must be edited).

## House rules for building lessons
- Every quiz position is checked with Stockfish (and legality with python-chess) before shipping. Say so in the lesson.
- When the engine thinks several options win, say so — the quiz is then about the *easiest* win for a human, and the feedback must admit it.
- Boards are always drawn from White's side; the learner plays White in diagrams unless stated.

## Backlog
- **Blunder check** (checks, captures, threats — for both sides). Confirmed by game data as the top priority. Build it from the learner's own positions (game IDs above).
- **Spending the clock**: slow down at the critical moment, keep a reserve for the conversion.
- **King + pawn vs king** (key squares, opposition) — the endgame every trade-down leads to. Lichess Practice has drills.
- **Basic mates** (K+Q, K+R, ladder) against the clock.
- **"Talk to your pieces" / improve the worst piece** — first answer to "no plan". Blocked on a better source (see RESOURCES gaps).
- **Pawn breaks and open files** — where plans come from.
- **Passed pawns** — make one, push one.
- **Time management in 10+0.**
