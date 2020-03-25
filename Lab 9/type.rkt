#lang racket

;; Global variabels for allowed operations and allowed operands.
(define allowed_operations '(+ - * / quotient < > =  and or))
(define allowed_operands '(int real bool))

;; Below variabels contain a list of allowed operation according to their result
(define int_result_list '(((int int) + - * quotient)))

(define real_result_list '(((int int) /)
                           ((real real) + - * /)
                           ((int real) + - * /)))

(define bool_result_list '(((int int) < > =)
                           ((real real) < > =)
                           ((int real) < > =)
                           ((bool bool) = and or)))

(require (lib "trace.ss"))


;; Function which takes in a list of operator and two operands as argument returning the result of the operation
(define check
  (lambda (lst)
    (define check_iter
      (lambda (op o1 o2)
        (cond
          ((and (list? o1) (list? o2)) (check_iter op (check o1) (check o2)))
          ((and (list? o1) (not (list? o2))) (check_iter op (check o1) o2))
          ((and (not (list? o1)) (list? o2)) (check_iter op o1 (check o2)))
          ((is_result int_result_list op o1 o2) 'int)
          ((is_result real_result_list op o1 o2) 'real)
          ((is_result bool_result_list op o1 o2) 'bool))))
    (control_input lst)
    (check_iter (car lst) (cadr lst) (caddr lst))))
    
;; Predicate which detects the if an operation belong to one of the result list variabels.
(define is_result
  (lambda (lst op o1 o2)
    (cond
      ((null? lst) #f)
      ((and (and (member o1 (caar lst)) (member o2 (caar lst))) (member op (cdr (car lst)))) #t)
      (else (is_result (cdr lst) op o1 o2)))))
    
  
;; Performs a control on the function check returning any existing error
(define control_input
           (lambda (lst)
           (define check_iter
             (lambda (op o1 o2)
               (cond
                 ((or (integer? op) (integer? o1) (integer? o2))
                  (error "Check needs one operator and two operand types as argument, not numbers."))
                 ((not (member op allowed_operations)) (error op "is not a defined operator."))
                 ((and (not (member o1 allowed_operands)) (not (list? o1))) (error o1 "is not defined operand."))
                 ((and (not (member o2 allowed_operands)) (not (list? o2))) (error o2 "is not  defined operand."))
                 ((only_one_bool o1 o2) (error "Can not make an operation between bool and integer/real."))
                 ((prohibited_bool_operations op o1 o2) (error op "is not defined as an operation for booleans."))
                 ((quotient_error_check op o1 o2) (error "Quotient only works with integers."))
                 ((and_or_prohibited op o1 o2) (error op "is not defined for the operands.")))))
             (if
               (not (= (length lst) 3))
               (error "Check performs type check on two binary operand types and an operator.")
               (check_iter (car lst) (cadr lst) (caddr lst)))))

;; Predicate which checks if only one of the operands is bool
(define only_one_bool
  (lambda (o1 o2)
    (cond
      ((or (list? o1) (list? o2)) #f)
      ((or (eq? o1 'bool) (eq? o2 'bool)) (if (and (eq? o1 'bool) (eq? o2 'bool)) #f #t))
      (else #f))))
                 
;; predicate that ckecks if operation on boolean is prohibited
(define prohibited_bool_operations
  (lambda (op o1 o2)
  (cond
      ((or (list? o1) (list? o2)) #f)
      ((and (eq? o1 'bool) (eq? o2 'bool)) (if (member op '(+ - ' / quotient < >)) #t #f))
      (else #f))))                             

;; Predicate which checks if only one of the operands is bool
(define quotient_error_check
  (lambda (op o1 o2)
    (cond
      ((or (list? o1) (list? o2)) #f)
      ((eq? op 'quotient) (if (not (and (eq? o1 'int) (eq? o2 'int))) #t #f))
      (else #f))))

;; predicate that ckecks if and and or are operaters for prohibited operands
(define and_or_prohibited
  (lambda (op o1 o2)
    (cond
      ((or (list? o1) (list? o2)) #f)
      ((or (eq? op 'and) (eq? op 'or)) (if (and (member o1 '(int real)) (member o2 '(int real))) #t #f))
      (else #f))))

