CTCI 6.4 Ant on a triangle

Given ants on each vertex of a triangle. If each ant picks a random side to walk into what is the probability of the collion? assume all ants walk at the same speed

There are 9 acts the ants can move

Vertex 1 is left or right, Vertex 2 is left or right, Vertex 3 is left or right.
  | Vertex 1 | Vertex 2 | Vertex 3
1 | left      left        left
2 | left      left        right
3 | left      right       right
4 | left      right       left
5 | right     left        left
6 | right     right       left
7 | right     right       right
8 | right     left        right

the amount of choices is 2^3 = 8
the collision are present when ants walk in opposite direction ie one goes left and one goes right any time the directions are different than a collision happens. A collision with all three ants is impossible.
collisions happen at 2,3,4,5,6,8 the probablity of a collision is 75% chance

on a larger polygon the formula would be n is the number of vertex k is the number of decisions that all are the same

p(n) = (2^n - 2) / (2^n)

how do we calculate k? There are only two occurences of the combination of all ants moving in the same direction
That means the more collisions will happen more often on larger polygons. More vertex more ants that are adjacent to choose opposite directions.

p(5) = (30)/32 = 93.75% chance of collision

