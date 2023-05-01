
**Algorithm E** (Euclids algorithm)
1. Divide $m$ by $n$ and let $r$ be the remainder. ($0 \le r \lt n$)
2. if $r = 0$, then the algorithm terminates; $n$ is the answer.
3. Set $m \leftarrow n$, $n \leftarrow r$ and go back to E1.

A formal definition of algorithm E can we written as seen below. 

$
f((n)) = (n); \newline
f((m, n)) = (m, n, 0, 1); \newline
f((m, n, r, 1)) = (m, n, m \% n, 2); \newline
f((m, n, r, 2)) = (n) \text { if } r = 0 \text{, otherwise } (m, n, r, 3); \newline
f((m, n, p, 3)) = (n, p, p, 1).
$

