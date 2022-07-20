# CTCI 6.1

# The heavypill

You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams. Given a scale that provides an exact measurement, how would you find the heavy bottle? You can only use the scale once.

How do we measure out weight with one use of the scale?

Buy more microtransactions to use the scale another time... Just kidding

We can divide the pill bottles into groups of 10. This would only get us 10 choices closer to choosing the right pill bottle.
Its a scale not a double balanced scale.
How would we measure this?
I can only use the scale once what if that once was one time on?

Do all the bottles have the same amount of pills?
If i put one pill at a time from each bottle onto the scale and read the output I could tell when the heavier pill was put on and what bottle the pill came from. Would this be using the scale more than once?

You put multiples of pills all of different ammounts up to 19 pills. (sum(1-20) - weight) / 0.1grams.

Remember the only contraints to these problems are the ones the question states.