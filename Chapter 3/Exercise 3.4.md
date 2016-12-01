# Exercise 3.4
  
## Question:
Suppose you treated pole-balancing as an episodic task but also used
discounting, with all rewards zero except for -1 upon failure. What then would the
return be at each time? How does this return differ from that in the discounted,
continuing formulation of this task?

## Answer:
The return could be viewed as the negative likelihood of the pole falling.
E.g. a state value of -0.1 means the pole is less likely to fall than
a state value of -0.5, although they won't be equivalent to percentages.

In the discounted, continuing version the external edges of the plot 
would be different, as there will exist a horizon boundary of angles the
pole can be towards the end of the episode where if it continued then 
it would fail. This boundary will approach the breaking point in the limit