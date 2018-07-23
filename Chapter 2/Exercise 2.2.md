# Exercise 2.2

## Question:
_Bandit example_ Consider a k-armed bandit problem with k = 4 actions, denoted 1, 2, 3, and 4.
Consider applying to this problem a bandit algorithm using ε-greedy action selectioni,
sample average action-value estimates, and initial estimates of Q<sub>1</sub>(a) = 0, for all a. Suppose
the initial sequence of actions and rewards is A<sub>1</sub> = 1, R<sub>1</sub> = 1, A<sub>2</sub> = 2, R<sub>2</sub> = 1, A<sub>3</sub> = 2, R<sub>3</sub> = 2,
A<sub>4</sub> = 2, R<sub>4</sub> = 2, A<sub>5</sub> = 3, R<sub>5</sub> = 0. On some of these time steps the ε case may have ocurred,
causing an action to be selected at random. On which time steps did this definitely occur? On which
time steps could this possibly have occurred.

## Answer:
Estimates @ step 1: (1, 0) (2, 0) (3, 0) (4, 0)
The action selected is _1_. We don't have any information of how ties are broken, so it could have been selected
either randomly or greedily using the tie-breaking strategy.

Estimates @ step 2: (1, 1) (2, 0) (3, 0) (4, 0)
The action selected is _2_. This is a **random** selection as the greedy selection would have been choosing action _1_.

Estimates @ step 3: (1, 1) (2, 1) (3, 0) (4, 0)
The action selected is _2_. Both actions _1_ and _2_ could be the greedy selection, or an ε case.

Estimates @ step 4: (1, 1) (2, 3/2) (3, 0) (4, 0)
The action selected is _2_ which is the greedy choice as well.

Estimates @ step 5: (1, 1) (2, 5/3) (3, 0) (4, 0)
The action selected is _3_ which is a definite ε case, since the greedy action is _2_.

To sum up, the cases where the ε case definitely occurred are steps 2 and 5.
The rest of the cases could be a consequence of a greedy selection or a coincidence with a random choice.

