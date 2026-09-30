# Losses are thrown wins and early blunders, not missing plans

An engine pass over 36 recent rapid games (2026-09-30) showed the learner reaches a winning position (+5 or better) in most games and fails to win 9 of those 25, almost always through a single-move blunder or the clock rather than poor technique. Another 8 losses were decided by a tactical blunder by move 13. This confirms the self-reported conversion problem, changes its cause, and demotes "no middlegame plan" as a priority.

## Evidence
Stockfish at 150k nodes per move over all 36 games; details and game IDs in NOTES.md. Puzzle ratings (1784 chess.com, 2013 Lichess) sit far above the rapid rating, so the tactical knowledge exists and is not being applied in games.

## Implications
Teach the habit of checking before moving (checks, captures, threats for both sides) and clock use before any strategy. Use the learner's own positions as quiz material. The 1500 rapid target was confirmed the same day.
