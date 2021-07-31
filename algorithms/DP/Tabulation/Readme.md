# Tabulation (Bottom Up approach)
Tabulation is the strategy which uses bottom-up approach which transitions from the base case and reaches its destination state the nth state. It uses a table to store all the values uptil nth state.
<br>

<!-- # Memoization Recipe
1. Make it work.
    * visualize the problem as a tree
    * implement the tree using recursion
    * test it
2. Make it efficient
    * add a memo object 
    * add a base case to return memo values
    * store return values into the memo
<br/> -->

## Fibonacii memoization
### Q. Write a funtion ```fib(n)``` that takes in a number as arguement. The function should return the n-th number of the fibonacii sequence.
The code initializes the base cases which is 0 and 1 and the iterates through all the n elements adding the ith value to i+1 element and i+2 element.
<p align="center">
<img src="./imgs/fibexp1.png" alt="Image" width="300">
</p>
<p align="center">
<img src="./imgs/fibexp2.png" alt="Image" width="300">
</p>
Finally the final table will look something like this
<p align="center">
<img src="./imgs/fib.png" alt="Image" width="300">
</p>

``` 
```
<br/>

<!-- ## Grid-Traveler Problem <br/>
### Q. Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. You may only move down right or left. In how many ways can you travel to the goal on a grid with dimensions m*n? <br/>
So, the ques can be soved easily with a time-complexity of O(n+m) using the memoization technique. We will store the grids that we have already calculated in a HashMap and use them to calculate the no. of ways of the bigger grids eg. for a  2,3 grid given in the image we can see that there are many grids that are repeating for eg. (1,2) so we can calculate the no. of ways of that grid once and store it in the HashMap. This method brings down the complexity from O(2^(n*m)) to O(n+m).
<p align="center">
<img src="./imgs/gt.png" alt="Image" width="300">
</p>

The hashMap will look something like this
```
d{
    "1,2": 1
}
```
<br/>

## CanSum Memoization
### Q. Write a function ```canSum(targeSum, numbers)``` that takes in a targetSum and an array of numbers as arguements.
The function should return boolean indicating true wether or not it is possible to generate the targetSum using numbers from the array. <br/><br/>
You may use an element of the array as many times as needed. <br/><br/>You may assume that all input numbers are non-negative.

<br/>

## HowSum Memoization
### Q. Write a function ```howSum(howSum, numbers)``` that takes in a targetSum and an array of numbers as arguements.
The function should return an array containing any combination of elemnts that add up to exactly the targetSum. If there is no combination that adds up to the targetSum, then return null.
So, as you can see using the memoization the time-complexity changes from O((n^m)*m), so here the time-complexity is (n^m)*m because the number of recursion calls = n^m and the it takes m-time to copy the old list and add an new element to O(n*m^2 ), here the it takes only n*m recursion calls and space complexity changed from O(m) to O(m^2), here m^2 is because the HashMap holds m keys with a list.

<br/>

## BestSum Memoization
### Q. Write a function ```bestSum(howSum, numbers)``` that takes in a targetSum and an array of numbers as arguements.
The function returns the shortest combination of numbers that add up to exactly the targetSum.


<br/>

## canConstruct Memoization
### Q. Write a function ```canConstruct(target, a)``` that takes in a target string and an array of strings as arguements.
The function should return boolean indicating true wether or not it is possible to generate the target string using the array of strings.
So the time-complexity of the code without using memoization is O((n^m)*m) and space complexity is O(m^2). After using meoization the time-complexity changes to O((n*m)*m) and space-complexity remains the same.
<br/>

## countConstruct Memoization
### Q. Write a function ```countConstruct(target, a)``` that takes in a target string and an array of strings as arguements.
The function should return the number of ways that the target can be constructed by concatenating elements of the array of elements.
So the time-complexity of the code without using memoization is O((n^m)*m) and space complexity is O(m^2). After using meoization the time-complexity changes to O((n*m)*m) and space-complexity remains the same.
<br/>

## allConstruct Memoization
### Q. Write a function ```allConstruct(target, a)``` that takes in a target string and an array of strings as arguements.
The function should return all the ways that the target can be constructed by concatenating elements of the array of elements.
<p align="center">
<img src="./imgs/allconstruct.png" alt="Image" width="300">
</p>
Let m be the height of the tree and n be the no. of elements in the array. So the total no. of combinations will be equal to n^m. So, we'll have n^m sub-arrays as output. So the time-complexity will be O(n^m) and space complexity will be O(m). -->