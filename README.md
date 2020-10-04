<!!> For having the images (and particulary our class diagram, please read the html file)

For this project, we have decided to focus on a bot based on the game **"Wondev woman"**. 
Here is a link of the game for further explanations : https://www.codingame.com/multiplayer/bot-programming/wondev-woman


## The game 

#### Presentation 

This game for two players consists in winning a maximum of points in an initialized board. Each player has 2 units which are put randomly in the beginning of the game. During each turn, the player can move one of its unit to an adjacent cell (diagonal moves are allowed) and, after his move, build on one of the adjacent cell. Building on a cell will increase the "height" of the cell by 1. For winning points, your units have to move on cells of height 3.

#### Rules : 

- An unit can only move to cells which have at most one height of difference. For example, if your unit is based on an unit of height 0, you can not move to an adjacent cell of height 3. The inverse is also true. 
- If you build on a cell of height 3 , the cell is blocked and nobody can go on it during all the game. 
- If you move on a cell which is already occupied by an ennemy's unit, your unit will push its unit.
- One rule proper to the challenge for fairness and optimization : our algorithm can not take more than 50 ms for taking a decision.


This game is quite similar to a more famous one : **Santorini**.

## How to install / use it

This section will be detailed once our files are merged and compacted.

## Our approach 

During the first week, we have decided to get used to the game and the environment proposed by the site. After this, we have decided to work on the following architecture which presents our classes and the main methods : 

< check it on the html file > 


- The class **Cell** represents one cell of the board, it contains the position and the cell and actual height.
- The subclasses **DeadCell** and **ValidCell** represent the cells that do not have a height of level 4 or cells that are outside the board.
- The subclass **Position** permits to compute distance between two cells. We have implemented the chebyshev distance. 
- The class **Unit** represents the units of the players. It contains the position (the cell in which the unit is based on), the player, and the index (because each player has 2 units)
- The class **Action** represents the actions that our unit is going to do. We have two types of action : Move&Build and Push&Build when we want to push out an ennemy player. We have decided to represent these 2 types of actions in 2 separated subclasses. 
- The class **Node** handles the tree exploration and our bot decision making. The feature state contains all the information about the game for our exploration.

## Algorithms implemented 

#### Negamax  search with alpha-beta pruning

The core of our bot's decision making is a derivation of minimax implementation called **negamax**. Globally, minimax algorithm tries on one hand thanks to the maximizer to get the highest score, while the minimizer tries to get the lowest score by trying to counter moves. In this algorithm, we assume that the opponent is playing optimally. In the case of negamax, for the ennemy player, the minimax score is a negation of its negamax score. 

Because we are **time-limited** (remember that we can not exceed 50ms for having a decision), we need to optimize our search depth for having better decisions in the same time. For this, we implemented **negamax search algorithm with alpha-beta pruning**. It cuts some branches in the trees which permit to avoid some "useless" computations. 

## What could've been done / didn't work

- The initial game has a **fog of war**. It means that we do not see all the board and we might not know exactly the position of ennemy's units. We did not focus on this feature. But trying to find the ennemy despite the fog could've been an interesting approach.

- Implementing **Voronoi algorithm** : pushing the enemy into a smaller area than yours is achieved by the Voronoi heuristic which involves counting the cells you can reach before your opponent. This algorithm helps to have a better **board control** by computing the areas that you own and the areas that the ennemy owns. Moreover, it "seems" that having an aggressive gameplay permits to go more in depth during the tree exploration and permits more computations. 