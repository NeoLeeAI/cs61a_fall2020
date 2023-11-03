(define (filter-lst fn lst)
  (if (null? lst)
      '()
      (if (eq? #t (fn (car lst)))
          (cons (car lst) (filter-lst fn (cdr lst)))
          (filter-lst fn (cdr lst))
      )
  )
)

; ;; Tests
(define (even? x) (= (modulo x 2) 0))

(filter-lst even? '(0 1 1 2 3 5 8))

; expect (0 2 8)
(define (interleave first second)
  (if (and (null? first) (null? second))
      ()
      (if (null? first)
          (cons (car second) (cdr second))
          (if (null? second)
              (cons (car first) (cdr first))
              (cons (car first)
                    (cons (car second)
                          (interleave (cdr first) (cdr second))
                    )
              )
          )
      )
  )
)

(interleave (list 1 3 5) (list 2 4 6))

; expect (1 2 3 4 5 6)
(interleave (list 1 3 5) nil)

; expect (1 3 5)
(interleave (list 1 3 5) (list 2 4))

; expect (1 2 3 4 5)
(define (accumulate combiner start n term)
  (if (= 1 n)
      (combiner start (term n))
      (accumulate combiner
                  (combiner start (term n))
                  (- n 1)
                  term
      )
  )
)

(define (no-repeats lst) 

    )
