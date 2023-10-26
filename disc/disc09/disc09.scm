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
(car (cdr (cdr (cdr s))))

#5.3
(define (duplicate lst)
    (if (equal? nil (cdr lst))
        (cons (car lst) (cons (car lst) nil))
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    )
)

#5.4
(define (insert element lst index)
    (define (helper element lst index a)
        (if (= a index)
            (cons element lst)
            (cons (car lst) (helper element (cdr lst) index (+ a 1)))
        )
    )
    (helper element lst index 0)
)