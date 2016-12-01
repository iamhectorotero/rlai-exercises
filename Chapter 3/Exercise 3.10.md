# Exercise 3.10
  
## Question:
Now consider adding a constant c to all the rewards in an episodic
task, such as maze running. Would this have any effect, or would it leave the task
unchanged as in the continuing task above? Why or why not? Give an example.

## Answer:
If the was an upper limit to the number of steps in an episode then v_c would decrease
(and thus G(t) would decrease) as the episode progresses because the maximum point
in the series would be the episode length - t rather than infinite.

I don't believe this would change the task assuming a basic exploration strategy
like e-greedy (something that explored via relative values like softmax would
be affected)