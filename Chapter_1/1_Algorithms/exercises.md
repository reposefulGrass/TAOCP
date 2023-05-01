
**Exercise 1.** 

To rearrange variables (a, b, c, d) into (b, c, d, a) perform the following:

$
TEMP \leftarrow a \newline
a \leftarrow b \newline
b \leftarrow c \newline
c \leftarrow d \newline
d \leftarrow TEMP \newline
$

**Exercise 2.**

Provided that $m$ and $n$ are positive integers.
If $m \lt n$, then $m = n$, $n = m$ after step E3. Once back at E1, $m \gt n$.
If $m \gt n$, then $r = m \% n$, $m = n$, $n = r$ after step E3. $n \gt m \% n$ by definition of $\%$. Therefore $m \gt n$.  

**Exercise 3.**

I'm not sure it is possible to compute euclid's algorithm without the assignment operation. Recursion still wouldn't work as it uses assignments internally.

**Exercise 4.**

gcd(2166, 6099) = 57

**Exercise 5.**

