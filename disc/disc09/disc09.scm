#4.1
(define (factorial x)
    (if (= x 1)
        1
        (* x (factorial (- x 1)))
    )
)

#4.2
(define (fib n)
    (if (= n 0)
        0
        (if (= n 1)
            1
            (+ (fib (- n 1)) (fib (- n 2))) 
        )
    )
)

#5.1
(define (my-append a b)
    (if (equal? nil (cdr a))
        (cons (car a) b)
        (cons (car a) (my-append (cdr a) b))
    )
)

#5.2
