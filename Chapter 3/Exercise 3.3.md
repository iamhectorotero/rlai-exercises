# Exercise 3.3
  
## Question:
Consider the problem of driving. You could define the actions in
terms of the accelerator, steering wheel, and brake, that is, where your body meets
the machine. Or you could define them farther out - say, where the rubber meets the
road, considering your actions to be tire torques. Or you could define them farther
in - say, where your brain meets your body, the actions being muscle twitches to
control your limbs. Or you could go to a really high level and say that your actions
are your choices of where to drive. What is the right level, the right place to draw
the line between agent and environment? On what basis is one location of the line
to be preferred over another? Is there any fundamental reason for preferring one
location over another, or is it a free choice?

## Answer:
The limit of the actions should be at the functional point, being the 
point at which is the agent makes the decision to take an action that
the action always occurs in the same way every time. Above that point
it is better to think of the agent as having sub-goals and goals, where
something like walking to the door is a goal with the sub-goals of 
moving the legs, with the action of applying hydraulic pressure to
particular points.

However this does depend on the reliability of the system, and what
reliability you require. If 99% of sub-goals are successful then it may
be easy to convert them into actions. Abstracting in this way makes
reaching larger goals easier as it dramatically reduces the
action-space needed to explore.