#lang racket

(require "list.rkt")

;;;;;;;;;;;;;;;;;;
;; Changes 19 sept 2015 by Alex Loiko:
;;    * renamed "*.scm" -> "*.rkt", added "#lang racket"
;;    * modularized tests into list-tests.rkt
;;    * added short automated tests for all assignments. In particular:
;;          - (list-ops-auto-test)

;;;;;;;;;;
;; Test of list functions (supplied by course team)

;; list-test -- run list test with an (initially) empty list
(define list-test
  (lambda ()
    (list-edit (list-create))))

;; list-edit -- interactively test list manipulation functions
(define list-edit
  (lambda (lst)
    (display "Edit operation (insert/delete/print/nth/first/rest/end): ")
    (let ((oper (read)))
      (cond ((or (eq? oper 'insert)
                 (eq? oper 'i))
             (list-edit (list-insert (read-element "Element to insert: ")
                                     lst)))
            ((or (eq? oper 'delete)
                 (eq? oper 'd))
             (list-edit (list-delete (read-element "Element to delete: ")
                                     lst)))
            ((or (eq? oper 'nth)
                 (eq? oper 'n))
             (elem-print (list-nth (read-element "Element number: ")
                                   lst))
             (newline)
             (list-edit lst))
            ((or (eq? oper 'print)
                 (eq? oper 'p))
             (list-print lst)
             (list-edit lst))
            ((or (eq? oper 'rest)
                 (eq? oper 'r))
             (list-print (list-rest lst))
             (list-edit lst))
            ((or (eq? oper 'first)
                 (eq? oper 'f))
             (elem-print (list-first lst))
             (newline)
             (list-edit lst))
            ((or (eq? oper 'end)
                 (eq? oper 'e)) lst)
            (else (display "Unknown operation")
                  (newline)
                  (list-edit lst))))))

;; Uses the interface in "list.rkt" to convert the list
;; from your representation to ordinary Scheme lists
(define (your-list-to-scm-list your-list)
  (if (list-empty? your-list)
      '()
      (cons (list-first your-list)
            (your-list-to-scm-list (list-rest your-list)))
      )
  )

(define (run-tests test-name err-actual-expected-lst)
  (map (curry apply
        (lambda (msg your-answer expected)
          (check-actual-expected test-name msg (your-list-to-scm-list your-answer) expected)
          ))
       err-actual-expected-lst )
  (displayln (format "~a: All tests OK" test-name)))
  
  
       
;; Automated test function. Tests whether list operations work correctly.
(define (list-ops-auto-test)
  (let* ((new-list (list-create))      ;; define actual/expected answer pairs
         (singleton-42-list (list-insert 42 new-list))
         (two-el-list (list-insert 0 singleton-42-list))
         (three-el-list (list-insert 42 two-el-list))
         (four-el-list (list-insert 1 three-el-list))
         (remove-42-list (list-delete 42 four-el-list))
         (insert-len-list (list-insert (list-len four-el-list) remove-42-list))
         (insert-len-len-list (list-insert (list-len new-list) insert-len-list))
         (singleton-nth-1 (list-insert (list-nth 1 singleton-42-list) insert-len-len-list))
         (list-nth-5 (list-insert (list-nth 4 singleton-nth-1) singleton-nth-1))
         )

    (run-tests
     'list-ops-auto-test
     (list                    ;; each element has the format ("info error message" actual expected)
      (list "list-create should produce empty list" new-list '())
      (list "single insert should produce singleton" singleton-42-list '(42))
      (list "list-first should return last inserted " two-el-list '(0 42))
      (list "list-delete should remove all occurances and not reverse the list" remove-42-list '(1 0))
      (list "4-element lists should have length 4" insert-len-list '(4 1 0))
      (list "0-element lists should have length 0" insert-len-len-list '(0 4 1 0))
      (list "list-nth is 1-indexed and works on singleton lists" singleton-nth-1 '(42 0 4 1 0))
      (list "list-nth is 1-indexed and works on 4:th elements of length-5 lists" list-nth-5 '(1 42 0 4 1 0))
      )
     )
    )
  )


(define (do-to-each-test)
  (run-tests
   'do-to-each-test
   (list
    (list "map of 0-element list" ((do-to-each-proc (curry + 1)) (list-create)) '())
    (list "map of 1-element list" ((do-to-each-proc (curry + 1)) (list-insert 1 (list-create))) '(2))
    ))
  )

(define (accumulate-test)
  (run-tests
   'accumulate-test
   (list
    (list "accumulate of 1-element list (should return that single element)"
          (list-insert
           ((accumulate-proc + 0) (list-insert 1 (list-create)))
           (list-create)
           )
          '(1)
          )
    (list "accumulate of 2-element list, correct order of arguments to proc"
          (list-insert
           ((accumulate-proc cons null) (list-insert 2
                                              (list-insert 1 (list-create))))
           (list-create)
           )
          '((2 1))
          )
    )
   )
  
  (void )
  )

(define (add-n-test)
  (let ( (actual (map add-n (list -42 -1 0 1 2 17511751 )))
         (expected (map (curry +) (list -42 -1 0 1 2 17511751 )))
         )
    (check-actual-expected 'add-n-test "(add-n k) should produce a procedure that adds k to its input"
                           (map (lambda (f) (f 17511705.5)) actual)
                           (map (lambda (f) (f 17511705.5)) expected)
                           )
    (displayln (format "~a: All tests OK" 'add-n-test))
    ))

(define (even-odd-test)
  (let ( (simple-fkn (even-odd (const 10) (const 'hej)))
         (less-simple-fkn (even-odd sqr sqrt))
         )
    (check-actual-expected 'add-n-test "even-odd should work with simple fkns that don't care about input"
                           (map simple-fkn (list -3 -2 -1 0 1 2 3333333333))
                           (list 'hej 10 'hej  10 'hej 10 'hej)
                           )
    (check-actual-expected 'add-n-test "even-odd should work with any functions"
                           (map less-simple-fkn (list -4 0 1 2 3333333333))
                           (list (sqr -4) (sqr 0) (sqrt 1) (sqr 2) (sqrt 3333333333))
                           )
    (displayln (format "~a: All tests OK" 'even-odd-test))
    )
  )

(define (choose-test)
  (let ( (simple-fkn (choose even? (const 10) (const 'hej)))
         (less-simple-fkn (choose list? length sqr))
         )
    (check-actual-expected 'add-n-test "choose should work with simple fkns that don't care about input"
                           (map simple-fkn (list -3 -2 -1 0 1 2 3333333333))
                           (list 'hej 10 'hej  10 'hej 10 'hej)
                           )
    (check-actual-expected 'add-n-test "choose should work with any functions"
                           (map less-simple-fkn (list (list 1 2) (list 3 4) -4 0 1 2 3333333333))
                           (list 2 2 (sqr -4) (sqr 0) (sqr 1) (sqr 2) (sqr 3333333333))
                           )
    (displayln (format "~a: All tests OK" 'choose-test))
    )
  )

(define (all-tests)
  (list-ops-auto-test)
  (do-to-each-test)
  (accumulate-test)
  (add-n-test)
  (even-odd-test)
  (choose-test)
  )


;; compares actual with expected and prints error information
(define (check-actual-expected err-symbol err-info actual expected)
  (if (equal? actual expected)
      (void)
      (error err-symbol "~a\ngot ~a, expected ~a" err-info actual expected)
      )
  )

;; read-element -- prompt the user with the given string, then
;; return the answer
(define read-element
  (lambda (operation)
    (display operation)
    (read)))

;; list-print -- print each element in the given list, separated
;; by " "
(define list-print
  (lambda (lst)
    (cond ((list-empty? lst) (newline))
          (else (display (list-first lst))
                (display " ")
                (list-print (list-rest lst))))))

;; elem-print -- print the given element
(define elem-print
  (lambda (elem)
    (display elem)))

