# Exercise 3.6
  
## Question:
Imagine that you are a vision system. When you are first turned on for 
the day, an image floods into your camera. You can see lots of things, 
but not all things. You can't see objects that are occluded, and
of course you can't see objects that are behind you. After seeing that 
first scene, do you have access to the Markov state of the environment? 
Suppose your camera was broken that day and you received no images at 
all, all day. Would you have access to the Markov state then?

## Answer:
It depends on what your task is. The Markov state is based on what
information provides a complete state of the information necessary to
make decisions. For any environment there are assumptions made about the
possible changes, so as long as the environment continues to operate
under those assumptions then you can have a Markov state.

If the camera was broken you wouldn't necessarily be able to determine 
the next reward you received (again, dependent on the task). In general
this would not be considered the Markov state