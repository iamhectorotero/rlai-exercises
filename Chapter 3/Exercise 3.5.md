# Exercise 3.5
  
## Question:
Imagine that you are designing a robot to run a maze. You decide
to give it a reward of +1 for escaping from the maze and a reward of zero at all
other times. The task seems to break down naturally into episodes - the successive
runs through the maze - so you decide to treat it as an episodic task, where the goal
is to maximize expected total reward (3.1). After running the learning agent for a
while, you find that it is showing no improvement in escaping from the maze. What
is going wrong? Have you effectively communicated to the agent what you want it
to achieve?

## Answer:
This is likely an exploration issue where the agent is unable to find
the exit the first time and therefore doesn't know there's anything
better than 0 as a reward. Potential solutions include having each
non-goal state be worth -1, and/or extending the episode length. This
would mean states the agents visits a lot (particularly around the start)
will get worse and worse values so it will want to move away from there
and eventually find the goal (essentially reaching the goal stops it
being in pain)