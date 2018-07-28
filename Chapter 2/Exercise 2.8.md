# Exercise 2.8

## Question:
Suppose you face a 2-armed bandit task whose true action values change randomly from time step
to time step. Specifically, suppose that, for any time step, the true values of action 1 and 2
are respectively 0.1 and 0.2 with probability 0.5 (case A), and 0.9 and 0.8 with probability 0.5
(case B). If you are not able to tell which case you face at any step, what is the best expectation
of success you can achieve and how should you behave to achieve it? Now suppose that on each step
you are told whether you are facing case A or case B (although you still don't know the true action
values). This is an associative search task. What is the best expectation of success you can
achieve in this task, and how should you behave to achieve it?

## Answer:

For the first scenario, you cannot hold individual estimates for the case A and B. Therefore,
the best approach is to select the action that has best value estimate in combination. In this case,
the estimates of both actions the same. So the best expectation of success is 0.5 and it can be
achieved by selecting an action randomly at each step.


A<sub>1</sub> = 0.5 \* 0.1 + 0.5 \* 0.9 = 0.5

A<sub>2</sub> = 0.5 \* 0.2 + 0.5 \* 0.8 = 0.5

For the second scenario, you can hold independent estimates for the case A and B, thus we can learn
the best action for each one treating them as independent bandit problems. The best expectation
of success is 0.55 obtained from selecting A<sub>2</sub> in case A and A<sub>1</sub> in case B.

0.5 \* 0.2 + 0.5 \* 0.9 = 0.55




