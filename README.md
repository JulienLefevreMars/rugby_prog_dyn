# Some words about rugby_scores

We are interested here to compute and enumerate the number of ways to obtain *n* points, given the rugby rules: 
* 3 pts for a penalty, 
* 5 pts for a try 
* 7 pts for a converted try

First we have to know wether the order is taken into account or not. For instance, we can obtain 10 from 3 ways:
* 2 tries
* 1 converted tries + 1 penalty
* 1 penalty + 1 converted tries
So, calling *A(n)* (*C(n)*) the number of ways to obtain *n* with (without respectively) ordering, we will have *A(10)=3* and *C(10)=2*. 

## With ordering

In a first attempt, the function *number_one_score* counts the number of ways to obtain a score *n* by taking into account the ordering. 

This can be obtained through dynamic programming and the recursive formula:
*A(n) = A(n-3) + A(n-5) + A(n-7)*

If one wants to find the asymptotic behavior of *A(n)* one can fit the evolution of *log A(n)* w.r.t *n* that follows approximately a line. 
In parallel it suggests to find a solution of the previous equation on the form *A(n) = r^n* which leads to find a root of the polynomial *X⁷-X⁴-X²-1*

## Without ordering

In a second attempt, it is possible to find *C(n)* by enumerating the set *{ (a,b,c) / 3a + 5b + 7c = n}*.
For instance, for *C(20)*, we enumerate starting from the converted tries then only the tries and so on
* 20 = 2 * 7 + 2 * 3 
* 20 = 1 * 7 + 2 * 5 + 1 * 3
* 20 = 4 * 5
* 20 = 1 * 5 + 5 * 3

It can be done with three nested loops, at the cost of *O(n⁴)* computation. 

It suggests also a recursive formula 
*C(n,list[1:k]) = C(n,list[1:k-1]) + C(n-list[k],list[1:k])* 
where list = [3,5,7] and it is related to the Coin problem (see here https://medium.com/@bharatkulratan/coin-change-problem-57ea55fade76 ).

## Future questions

* It is easy to see that *A(n) ~ r^n* with *r=1.2637...* but is there a simple asymptotic formula for *C(n)* ? Preliminary fit suggest *C(n) = O(n^a)* with *a ~ 1.2* slightly increasing with *n*. Could it be possible that the exponent equals r ??

* Instead of the values 3, 5, 7 we could be interested  to generalize the results to any sequence of integers, whose gcd could be 1 or possibly greater than 1.






