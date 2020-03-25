#lang racket
(define cuberoot
  (lambda (x)

    (define cuberoot-iter
      (lambda (guess x)
        (if (< (abs (- (* guess guess guess) x)) 0.0001)
            guess
            (cuberoot-iter (/ (+ (* 2 guess) (/ x (expt guess 2)))3) x))))
    
    
    (cuberoot-iter 1 x))
)

