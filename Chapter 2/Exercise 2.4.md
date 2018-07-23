# Exercise 2.4

## Question:
If the step-size parameters, α<sub>n</sub>, are not constant, then the estimate
Q<sub>n</sub> is a weighted average of previously received rewards with a weighting different
from that given by (2.6). What is the weighting on each prior reward for the general
case, analogous to (2.6), in terms of the sequence of step-size parameters?

## Answer:
The equation of Q<sub>(n+1)</sub> = (1-α)<sup>n</sup>\*Q<sub>1</sub> + Σ<sup>n</sup><sub>(i=1)</sub>[α\*(1-α)<sup>(n-i)</sup>\*R<sub>i</sub>] would become
Q<sub>(n+1)</sub> = Π<sup>n</sup><sub>(i=1)</sub>[1-α<sub>i</sub>]\*Q<sub>1</sub> + Σ<sup>n</sup><sub>(i=1)</sub>[α<sub>i</sub>\*Π<sup>i</sup><sub>(j=1)</sub>[1-α<sub>j</sub>]\*R<sub>i</sub>]

Essentially it means that you need to keep a track of the α's used and alter the product
