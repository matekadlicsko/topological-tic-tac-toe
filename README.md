# topological-tic-tac-toe

This is a "generalization" of the well-known game tic-tac-toe that is playable in terminal. 
Besides being able to modify the size of the table, you can set it's topology. Possibly the
most well-known example is a torus of which we can think about as the world of Pac-Man. In 
TTTT a torus shaped table would be represented as:
```
````
     1   2   3   
   +---+---+---+
1  |   |   |   | 1
   +---+---+---+
2  |   |   |   | 2
   +---+---+---+
3  |   |   |   | 3
   +---+---+---+
     1   2   3   
```
````

The numbering on the left and on the top denote the index of the corresponding row and col-
oumn respecively, while the numbering on the right and on the coloumn denotes which row/
coloumn the corresponding row/coloumn is identified with. For example in the case of the 
torus walking far east on the table would result in ending up far west in the same coloumn.
