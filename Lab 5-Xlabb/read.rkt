#lang racket

;; read.rkt -- Read test cases

;; Created by Freddie on Fri Sep 25 20:11:35 2015
;; Modified by Alex on Mon Oct 05 22:17:00 2015
;;     (added the threaded printing of dots (isn't it nice?),
;;      )

(provide (all-defined-out))

(define (from-file filename)
  (call-with-input-file filename read))


(define (test-pairs-with-proc proc filename)
  (let ((lines (from-file filename)))
    (for-each (lambda (line)
                (displayln (apply proc line)))
              lines)))

(define thing 0)

(define (make-dot-printing-thread)
  (thread (lambda ()
            (let loop ()
              (sleep 0.75)
              (display ". ")
              (display thing)
              (display " ")
              (flush-output)
              (loop)
              )
            ))
  )



(define (make-problem-counting-thread)
  (thread (lambda ()
            (let loop ()
              ;(sleep 2)
              (set! thing (thread-receive))
              ;(display (thread-receive))
              ;(display " ")
              ;(flush-output)
              (loop)
              )
            ))
  )

                     
(define (compare-output same-set? operation operation-name infile outfile)
  (displayln (format "   Testing '~A'" operation-name))
  (displayln "************************")
  (displayln "************************")
  (newline)
  (define dot-printer (make-dot-printing-thread))
  (define prob-counter (make-problem-counting-thread))
  (define result
    (if 
     (let loop ((row 1) (all-passed #t)
                (input-lines (from-file infile))
                (expected-output (from-file outfile)))
       (if (empty? input-lines)
           (begin (displayln "") all-passed)
           (let* ((i (car input-lines))
                  (o (apply operation i))
                  (e (car expected-output))
                  (this-passed 
                   (if (same-set? o e)
                       #t
                       (let ()
                         (displayln (format "Incorrect answer at row ~A. Test was:" row))
                         (displayln "-------------------------------------")
                         (displayln (format "~A" (cons operation-name i)))
                         (displayln (format "Suggested answer:\n~A\nbut your result was:\n~A" e o))
                         (displayln "*************************************")
                         #f))))
             (thread-send prob-counter row)
             (loop (+ row 1) (and this-passed all-passed)
                   (cdr input-lines)
                   (cdr expected-output)))))
     "Tests passed!"
     "Tests failed."))
  (kill-thread dot-printer)
  (kill-thread prob-counter)
  result
  )

