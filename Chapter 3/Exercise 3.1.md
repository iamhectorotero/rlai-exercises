# Exercise 3.1 
  
## Question:
Devise three example tasks of your own that fit into the MDP framework, identifying for each its states, actions,
and rewards. Make the three examples as _different_ from each other as possible. The framework is abstract and
flexible and can be applied in many different ways. Stretch its limits in some way in at least one of your examples.

## Answer:
Example 1: Hairdresser agent

- States: the state of the hair and the desired cut of the client. The state of the hair and desired cut could be
encoded as arrays of the length of the hair in a set of predetermined areas the head is divided in.
- Actions: using the scissors or the clipper (and what accessory) and the area to be cut.
- Rewards: negative rewards for the client complaints or imprecisions in the cut and positive rewards for tips.

Example 2: DJ agent

- States: a measure of how much people are dancing and singing to the song being played and the song currently playing.
- Actions: given a setlist of 5000 songs, selecting the next song to be played (or a combination of them) and a type of
transition between the songs.
- Rewards: negative rewards given by people leaving the club faster than expected, positive rewards given by the level
of danciness/_singiness_ in the club.

Example 3: Texas Hold'em Poker player agent

- States: The two cards in its hand and the cards showing in the table.
- Actions: Check, call, raise, or fold.
- Rewards: The money obtained or lost after playing one hand.
