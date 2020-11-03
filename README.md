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



