# Exercise 3.8
  
## Question:
The Bellman equation (3.12) must hold for each state for the value
function v_pi shown in Figure 3.5b. As an example, show numerically that this equation
holds for the center state, valued at +0.7, with respect to its four neighboring states,
valued at +2.3, +0.4, -0.4, and +0.7. (These numbers are accurate only to one
decimal place.)

## Answer:
Because it's using an equiprobable random policy the chance of each state being
selected is the same, meaning the average reward is the sum of the possible future
states divided by the number of future states.

(delta^1*sum)/outcomes = (0.9 * 3.0) / 4 ~= 0.7