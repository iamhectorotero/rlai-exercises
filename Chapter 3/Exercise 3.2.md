# Exercise 3.2 
  
## Question:
Is the MDP framework adequate to usefully represent *all* goal-directed learning tasks?
Can you think of any clear exceptions?

## Answer:
We can try to think about it in terms of the limitations a finite MDP imposes in a problem definition and whether any
approximations could exist within the framework.

1) The Markov property, if not only the previous state and action selected influence which will be the next state. An
example of this could be a modified game of chess where the order in which the pieces were moved affects the possible
moves. This could be encoded within the MDP, an state would be composed of the position of the pieces and when
they have been moved (skyrocketing the amount of available states making it a more difficult learning environment).
If the sequence information wasn't available (or only partially available) at the time of making a decision,
information from the past that can affect the next state would be missing, breaking the Markov property.

2) The action and state sets must be finite. Any problem with infinite available actions or states would need
alternative representations, such as grouping them into subsets and use these sets. An example of this could be a
problem where the states are the natural numbers and we have to define intervals (e.g. negative numbers, numbers in the
range 0-25, 25-200, and 200-∞) or where the actions can be a string of any size and we restrict it to a discrete number
of lengths (e.g. only generate strings with length 3, 5, 8, 13, 21 and 34).

3) Rewards must be numerical. If the rewards the environment gives back are not numerical we would need to encode them
as numbers. This can be a highly difficult task as the rewards may not translate naturally to numbers. For example,
if the rewards were your family's verbal feedback on how good the meal you prepared was, it would be difficult to
convert it into a number and capture correctly its intensity (e.g. What's a better feedback? "It was really good" or
"I have enjoyed the meal a lot"). If we opt for a simpler reward encoding, distinguishing only negative, neutral and
positive comments, this may not capture perfectly the information given.

The first example is, as far as I understand, a clear exception of the MDP-framework not being an appropriate
representation. Apart from this, some of the points mentioned (or their combination) may difficult largely the task for
an agent, making it really hard to learn anything valuable from the environment.
