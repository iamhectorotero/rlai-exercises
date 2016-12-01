# Exercise 1.5: Other Improvements   

## Question:
Can you think of other ways to improve the reinforcement learning player?
Can you think of any better way to solve the tic-tac-toe problem as posed?

## Answer:
If the player was adapting over time decaying the old updates could speed up the improvement.
Altering the exploration rate/learning based on the variance in the opponents actions. If the opponent is
always making the same moves and you are winning from it, then e-greedy with 10% exploration is just going to
lose you games. Even though tic-tac-toe is a solvable game doing that may not result in the highest result
with a sub-optimal opponent.
