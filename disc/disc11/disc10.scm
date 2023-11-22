#1.1
(+ 1 2 3 4)

(+ 1 (* 2 3))

#1.2
p = Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil), Pair(6, Pair(8, nil))))))
p.rest
p.first  .rest.first.first
the first operand - p.first

#1.3