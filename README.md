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

In a first attempt, the function *number_one_score* counts the number of ways to obtain a score *n* by taking into account the ordering. 



