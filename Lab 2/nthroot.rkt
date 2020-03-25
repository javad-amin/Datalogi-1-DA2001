#lang racket
(define root
  (lambda (nthroot x)

    (define root-iter
      (lambda (guess nthroot x)
        (if (< (abs (- (expt guess nthroot) x)) 0.0001)
            guess
            (root-iter (/ (+ (* (- nthroot 1) guess) (/ x (expt guess (- nthroot 1))))nthroot) nthroot x))))
    
    
    (root-iter 1.0 nthroot x))
)

(define (root2 y x) (exp( / (log x) y)))
(root 2 7)
(root2 2 7)
