# Exercise 1.2: Symmetries   

## Question 
Many tic-tac-toe positions appear different but are really the same because of symmetries.
How might we amend the reinforcement learning algorithm described above to take advantage of this?
In what ways would this improve it? Now think again. Suppose the opponent did not take advantage of symmetries.
In that case, should we?
Is it true, then, that symmetrically equivalent positions should necessarily have the same value?

## Answer:
For tic-tac-toe it is possible to use 4 axis of symmetry to essentially fold the board down to a quarter of the size
This would dramatically increase the speed/reduce the memory required.
If the opponent did not take advantage of symmetries then it could result in a worse overall performance, for example,
if the opponent always played correct except for 1 corner, then using symmetries would mean you never take advantage
of that information. This means symmetrically equivalent positions don't always hold the same value in a
multi-player game
