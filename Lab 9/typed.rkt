
#lang typed/racket

;; typed.rkt -- Några funktioner i typad Racket

;;; Addera två tal
(: add (Real Real -> Real))
(define (add x y)
  (+ x y))

;;; Addera alla tal i en lista
(: sumlist ((Listof Real) -> Real))
(define (sumlist lst)
  (if (empty? lst)
      0
      (add (car lst) (sumlist (cdr lst)))))

;;; Addera godtyckligt många argument (överkurs)
(: sum (Real * -> Real))
(define (sum . args)
  (if (empty? args)
      0
      (add (car args) (apply sum (cdr args)))))


;;; Fakultetsfunktionen, med svansrekursion
(: factorial (Integer -> Integer))
(define (factorial n)
  (: factorial-iter (Integer Integer -> Integer))
  (define (factorial-iter n p)
    (if (= n 0)
        p
        (factorial-iter (- n 1) (* p n))))
  (factorial-iter n 1))

;;; Fibonacci-funktionen
(: fibonacci (Integer -> Integer))
(define (fibonacci n)
  (: fibonacci-iter (Integer Integer Integer -> Integer))
  (define (fibonacci-iter a b n)
    (if (= n 0)
        b
        (fibonacci-iter (+ a b) a (- n 1))))
  (fibonacci-iter 1 0 n))