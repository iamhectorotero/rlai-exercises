# Exercise 1.4: Learning from Exploration   

## Question
Suppose learning updates occurred after all moves, including exploratory
moves. If the step-size parameter is appropriately reduced over time, then the state values would converge to a set
of probabilities. What are the two sets of probabilities computed when we do, and when we do not, learn from
exploratory moves? Assuming that we do continue to make exploratory moves, which set of probabilities might be
better to learn? Which would result in more wins?

## Answer:
With the step size parameter appropriately reduced, and assuming the exploration rate is fixed, the probability set
with no learning from exploration is the value of each state given the optimal action from then on is taken, whereas
with learning from exploration it is the expected value of each state including the active exploration policy.
Using the former is better to learn, as it reduces variance from sub-optimal future states (e.g. if you can win a
game of chess in one move, but if you perform another move your opponent wins, that doesn't make it s bad state)
The former would result in more wins all other things being equal