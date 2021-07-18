# Dynamic Programing
Dynamic problem is an algorithm technique based on reccurent formula, it is an algorithm which helps to solve overlapping sub-problems. Sometimes these sub-problems in dp are known as states. A good example of a dp problem is fibonacii series. A good trick or strategy to solve dp questions is to use memoization.
<br>

# Memoization
Memoization is the strategy where we calculate the states and store them so that we don't have to calculate them again and again because a state can be present in many different parts of the solution of the problem.
<br>


### Fibonacii memoization
<p align="center">
<img src="./imgs/fib6.png" alt="Image" width="50">
</p>

As you can see, the time complexity changes from O(2^N) to O(N)
and our HashMap which stores the states will look something like this
``` 
d{
    3: 2,
    4: 3,
    5: 5
}
```

# Grid-Traveler Problem <br/>
## Q. Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. You may only move down right or left. <br/>
## In how many ways can you travel to the goal on a grid with dimensions m*n?
So, the ques can be soved easily with a time-complexity of O(n+m) using the memoization technique. We will store the grids that we have already calculated in a HashMap and use them to calculate the no. of ways of the bigger grids eg. for a  2,3 grid given in the image we can see that there are many grids that are repeating for eg. (1,2) so we can calculate the no. of ways of that grid once and store it in the HashMap. This method brings down the complexity from O(2^(n*m)) to O(n+m).
<p align="center">
<img src="./imgs/gt.png" alt="Image">
</p>

The hashMap will look something like this
```
d{
    "1,2": 1
}
```