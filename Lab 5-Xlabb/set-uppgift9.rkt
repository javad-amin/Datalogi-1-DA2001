#lang racket

(require (lib "trace.ss"))


;; Assignment 1


;; make-object -- constructor for making diffrent types of objects.
(define make-object
  (lambda (type value)
    (cons type value)))


;; type -- selector for the type of an object
(define type
  (lambda (procedure)
    (car procedure)))

;; value -- selector for the value of an object
(define value
  (lambda (procedure)
    (cdr procedure)))

;;set? -- Predicate which checks if the argument/object is a set
(define set?
  (lambda (set)
    (cond
      ((null? set) #f)
      ((list? set) (if (eq? (type set) 'set) #t #f))
      (else #f))))

;; empty? -- Predicate that checks if an object is empty or not
(define empty?
  (lambda (set)
    (cond
      ((set? set) (if (null? (value set)) #t #f))
      (else (if (null? set) #t #f)))))

;; del-dup -- procedure for removing all of the dupplicates in an object
(define del-dup
  (lambda (obj)
    (define iter
      (lambda (obj result)
        (cond
          ((empty? obj) result)
          ((member? (first obj) (rest obj)) (iter (rest obj) result))
          (else (iter (rest obj) (cons (first obj) result))))))
    
    (cond
      ((or (empty? obj) (empty? (rest obj))) obj)
      (else (reverse (iter obj '()))))))


(define make-set
  (lambda (lst)
    (remove-duplicates (map (lambda (x)
                              (if (set? x)
                                  (remove-duplicates (make-set x) same-elem?)
                                  x)) lst) same-elem?)))
                

(define make-set-from-elems
  (lambda x
    (make-set x)))

;; insert -- procedure that inserts an element in the begginging of a list or set
(define insert
  (lambda (el set)
    (cond ((set? set) (make-set (cons el (value set))))
          (else (cons el set)))))

;; first -- returns the first element of a list or set
(define first
  (lambda (set)
    (if (set? set) (car (value set))
        (car set))))

;; rest -- returns all of the elements other than the first on from a list or set
(define rest
  (lambda (set)
    (if (set? set) (cdr (value set))
        (cdr set))))

;; set-length -- length of a list or set
(define set-length
  (lambda (set)
    (define helper
      (lambda (set result)
        (cond
          ((empty? set) result)
          (else (helper (rest set) (+ 1 result))))))
    (helper set 0)))

;; set-delete -- delete an element from a set
(define set-delete
  (lambda (element set)
    (define helper
      (lambda (element set result)
        (cond
          ((empty? set) result)
          ((same-elem? element (first set)) (helper element (rest set) result))
          (else (helper element (rest set) (insert (first set) result))))))
    (helper element set (the-empty-set))))

;; the-empty-set -- returns an empty set
(define the-empty-set
  (lambda ()
    (make-set '())))

;; Uppgift 2

;; member? -- predicate which checks if an element is a member of a set or not
(define member?
  (lambda (el set)
  (ormap (lambda (x) (same-elem? el x)) set)))

;; subset? -- predicate which controls if all element in set1 are included in set2
(define subset?
  (lambda (set1 set2)
    (andmap (lambda (x) (member? x set2)) set1)))


;; same-set? -- predicate which checks if all the element between two sets are the same
(define same-set?
  (lambda (set1 set2)
    (if (and (subset? set1 set2) (subset? set2 set1)) #t
        #f)))

;; same-elem? -- predicate which checks if two elements are the same
(define same-elem?
  (lambda (e1 e2)
    (cond
      ((and (set? e1) (set? e2) (same-set? e1 e2)) #t)
      ((and (symbol? e1) (symbol? e2) (eq? e1 e2)) #t)
      ((and (number? e1) (number? e2) (= e1 e2)) #t)
      ((and (vector? e1) (vector? e2) (equal? e1 e2)) #t)
      (else #f))))

;; Uppgift 4

;; set-only? -- predicate that makes sure a list contains only sets and nthing else
(define set-only?
  (lambda (lst)
    (cond
      ((empty? lst) #t)
      ((set? (first lst)) (set-only? (rest lst)))
      (else #f))))
            
;; union -- procedure which returns a new set made of union of two sets
(define union
  (lambda (set1 set2)
    (if (empty? set2) set1
        (union (insert (first set2) set1) (rest set2)))))

;; union* -- procedure which returns a new set made of union of multiple sets sets
(define union*
  (lambda rest-id

    (define helper
      (lambda (lst first-time result)
        (cond
          ((not (set-only? lst)) (error "Union takes in sets as argument."))
          ((empty? lst) result)
          ((= first-time 1) (helper (rest lst) 0 (first lst)))
          (else (helper (rest lst) 0 (union (first lst) result))))))
    (helper rest-id 1 (the-empty-set))))
      

;; intersection -- procedure which returns a new set made of intersection of two sets
(define intersection
  (lambda (set1 set2)
    (filter (lambda (x) (member? x set2)) set1)))

;; intersection* -- procedure which returns a new set made of intersection of multiple sets
(define intersection*
  (lambda rest-id

    (define helper
      (lambda (lst first-time result)
        (cond
          ((not (set-only? lst)) (error "intersection takes in sets as argument."))
          ((empty? lst) result)
          ((= first-time 1) (helper (rest lst) 0 (first lst)))
          (else (helper (rest lst) 0 (intersection (first lst) result))))))
    
    (helper rest-id 1 (the-empty-set))))

;; difference -- procedure which returns a new set made of difference between two sets
(define difference
  (lambda (set1 set2)
    (filter (lambda (x) (not (member? x set2))) set1)))

;; cartesian-product - procedure that takes in two sets as argument and returns a list of cartesian product of the elements
;; of the sets in pairs
(define (cartesian-product set1 set2)
  (apply append
         (map (lambda (x)
                (map (lambda (y)
                       (vector x y))
                     set2))
              set1)))


;(cartesian-product (make-set '((A) (B) (C) (D) (E))) (make-set '((A) (B) (C) (D) (E) (A) (B))))

;;   Tests
;; Define myset
(define myset
  (make-set '(a (a b b (c b) 3) 5 5.0 (e s) (s e s))))
;(make-set '(s e s))
;; Uppgift 1
;(set? myset)
;(empty? myset)
;(insert 1 myset)
;(insert (make-set '(f b)) myset)
;(first myset)
;(first (insert (make-set '(f b)) myset))
;(rest myset)
;(set-length myset)

;(member? 5 myset)
;(member? 'a myset)
;(member? (make-set '(1 2)) (make-set '(1 2 3)))
;(member? 'x (make-set '(1 2 3 x)))
;(member? (make-set '((x) 2)) (make-set '(4 2 (x))))
;(subset? (make-set '((x) 2)) (make-set '(4 2 (x))))
;(subset? (make-set '((x) 2 3)) (make-set '(4 2 (x))))
;(member? (the-empty-set) (make-set '(a b c)))
;(member? (make-set '(1)) (the-empty-set))
;(member? (make-set '(1 2)) (make-set '((1 2) 3)))
;(member? (make-set '(1)) (make-set '((1 2) 3)))
;(member? (make-set '(1 (b))) (make-set '(3 2 ((b) 1))))
;(member? (make-set '(1 2)) (make-set '(y (2 1))))
;(same-set? (make-set '(1 2 a)) (make-set '(2 a 1)))
;(same-set? (the-empty-set) (the-empty-set))
;(same-set? (make-set '((1 2) 2 3)) (make-set '(2 3 (2 1))))
;(same-set? (make-set '((2 3) a b)) (make-set '(2 3 (a b))))
;(same-set? (make-set '(2 (b (z)) 4)) (make-set '(3 5 (z) (x))))

;;Uppgift 4
;(union (make-set '(1 2 (x (y 3) 4)))
;         (make-set '(b 1 (a (r)))))

;(intersection (make-set '(1 (2 (1)) 3 (1 2)))
;           (make-set '(((1) 2) 3 4 (2 3))))

;(difference (make-set '(1 (2 3) b)) (make-set '(b 1)))

;(cartesian-product (make-set '(1 2 3)) (make-set '(a b)))


(provide (all-defined-out))