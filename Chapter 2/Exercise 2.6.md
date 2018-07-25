# Exercise 2.6

## Question:
The results shown in Figure 2.3 should be quite reliable because they
are averages over 2000 individual, randomly chosen 10-armed bandit 
tasks. Why, then, are there oscillations and spikes in the early part 
of the curve for the optimistic method? In other words, what might 
make this method perform particularly better or worse, on average, 
on particular early steps?

## Answer:
The oscillations in the early stage are likely to be caused as the
algorithm reduces the Q values for the poorly performing options.
To start off with it's going to think all of the bad options are good
and has to try each multiple times before it realises they're actually
bad. This will depend on how quickly these bad options drop below the
best option (once that occurs on exploration will reduce them to their
correct values over time but at a much more reduced rate)



