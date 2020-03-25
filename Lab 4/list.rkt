#lang racket

;; list.rkt
;;
(require (lib "trace.ss"))
;;;;;;;;;;
;; Assignment 1



;; list-create -- create an empty list 
(define list-create
  list)
  

;; list-empty -- procedure that checks if a list is empty or not
(define list-empty?
  (lambda (lst)
    (if (empty? lst) #t
        #f)))

;; list-insert -- procedure that inserts an element in the begginging of a list
(define list-insert
  (lambda (el lst)
    (cons el lst)))

;; list-delete -- procedure that removes all of the occurrences of a number in a list
(define list-delete
  (lambda (el lst)
    (if (null? lst) '()
        (if (eq? el (car lst)) (list-delete el (cdr lst))
            (list-insert (car lst) (list-delete el (cdr lst)))))))

;; list-first -- returns the first element of a list
(define list-first
  (lambda (lst)
    (car lst)))

;; list-rest -- returns all of the elements other than the first on from a list
(define list-rest
  (lambda (lst)
    (cdr lst)))

;; list-len -- length of a list
(define list-len
  (lambda (lst)
    (cond
      ((list-empty? lst) 0)
      (else (+ 1 (list-len (list-rest  lst)))))))

;; list-nth -- returns the n-th element of a list
(define list-nth
  (lambda (n lst)
    (if (or (> n (list-len lst)) (< n 1))
        (error "Make sure that n is within the list!")
        (if (eq? n 1)
            (list-first lst)
            (list-nth (- n 1) (list-rest  lst))))))
    

;;;;;;;;;;
;; Assignment 2

;; add one (1) to the argument
(define add-one
  (lambda (x)
    (+ 1 x)))

;; Does the same procedure to all of the elements of a list
(define do-to-each
  (lambda (proc lst)
    (if (list-empty? lst) '()
        (list-insert (proc (list-first lst)) (do-to-each proc (list-rest  lst))))))

;; Does the same procedure to all of the elements of a list "Svansrekursiv"
(define do-to-each-svans
  (lambda (proc lst)
    (define helper
      (lambda (lst result)
        (if (list-empty? lst) (reverse result)
            (helper (list-rest lst) (list-insert (proc (list-first lst)) result) ))))
    (trace helper)
    (helper lst '())))



;; add n to the argument
(define add-n
  (lambda (n)
    (lambda (x)
      (+ x n))))

;; multiply n with the argument
(define mul-n
  (lambda (n)
    (lambda (x)
      (* x n))))

;; Divide n with the argument
(define div-n
  (lambda (n)
    (lambda (x)
      (/ x n))))

;; Power n to the argument
(define power-n
  (lambda (n)
    (lambda (x)
      (expt x n))))

;; a procedure that returns a diffrent procedure on an argument depending on if the element is odd or an even number
(define even-odd
  (lambda (proc-even proc-odd)
    (lambda (x)
      (if (even? x) (proc-even x)
          (proc-odd x)))))
;; same as above with the diffrence of being able to choose the pridicate
(define choose
  (lambda (predicate proc-1 proc-2)
    (lambda (x)
      (if (predicate x) (proc-1 x)
          (proc-2 x)))))

;; Applies a procedure between all of the elements of a list
(define accumulate
  (lambda (proc id lst)
    (cond
      ((list-empty? lst) (error "Does not work on an emtly list"))
      ((list-empty? (list-rest  lst)) (proc (list-first lst) id))
      ((proc (list-first lst) (accumulate proc id (list-rest  lst)))))))

;;Another versoin of accumulate which takes a list as an argument and returns a procedure.
(define accumulate-proc
  (lambda (proc id)
    (lambda (lst)
      (cond
        ((list-empty? lst) (error "Does not work on an emtly list"))
        ((list-empty? (list-rest  lst)) (proc (list-first lst) id))
        ((proc (list-first lst) (accumulate proc id (list-rest  lst))))))))


;; a do to each function which returns a procedure which takes a list as an argument.
(define do-to-each-proc
  (lambda (proc)
    (lambda (lst)
      (if (list-empty? lst) '()
          (list-insert (proc (list-first lst)) (do-to-each proc (list-rest  lst)))))))


;;Tests, Uncomment to test all the functions
(define lst (list-create 1 2 3 4 3 6 3))
lst
;"(list-empty? lst)" (list-empty? lst)
;"(list-empty? '())" (list-empty? '())
;"(list-insert 99 lst)" (list-insert 99 lst)
;"(list-delete 3 lst)" (list-delete 3 lst)
;"(list-first (list-insert 99 lst))" (list-first (list-insert 99 lst))
;"(list-rest (list-insert 99 lst))" (list-rest (list-insert 99 lst))
;"(list-len lst)" (list-len lst)
;"(list-nth 4 lst)" (list-nth 4 lst)
;"(do-to-each add-one lst)" (do-to-each add-one lst)
;"(do-to-each add-one '())" (do-to-each add-one '())
;"(define add-two (add-n 2))" (define add-two (add-n 2))
;"(add-two 3)" (add-two 3)
;"(define half (div-n 2))" (define half (div-n 2))
;"(define double (mul-n 2))" (define double (mul-n 2))
;"(define half-double (even-odd half double))" (define half-double (even-odd half double))
;"(do-to-each half-double mylist)" (do-to-each half-double lst)
;"(define half-double-2 (choose even? half double))" (define half-double-2 (choose even? half double))
;"(do-to-each half-double-2 lst)" (do-to-each half-double-2 lst)
;"(accumulate + 0 lst)" (accumulate + 0 lst)
;"(accumulate * 1 lst)" (accumulate * 1 lst)
;"(accumulate cons '() lst)" (accumulate cons '() lst)
;"(define sum (accumulate-proc + 0))" (define sum (accumulate-proc + 0))
;"(sum lst)" (sum lst)
;"(define sq-list (do-to-each-proc sqr))" (define sq-list (do-to-each-proc sqr))
;"(sq-list mylist)" (sq-list lst)
;(trace do-to-each-svans)
;"(do-to-each-svans add-one '(7 2 7 8))" (do-to-each-svans add-one '(7 2 7 8))

(provide (all-defined-out))