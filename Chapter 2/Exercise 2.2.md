# Exercise 2.2

## Question:
If the step-size parameters, alpha_n, are not constant, then the estimate
Q_n is a weighted average of previously received rewards with a weighting different
from that given by (2.6). What is the weighting on each prior reward for the general
case, analogous to (2.6), in terms of the sequence of step-size parameters?

## Answer:
The equation of Q_(n+1) = (1-alpha)^n*Q_1 + sum^n_(i=1)[alpha*(1-alpha)^(n-i)*R_i] would become
Q_(n+1) = product^n_(i=1)[1-alpha_i]*Q_1 + sum^n_(i=1)[alpha_i*product^i_(j=1)[1-alpha_j]*R_i]

Essentially it means that you need to keep a track of the alphas used and alter the product