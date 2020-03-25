#lang racket

;; graph-test.rkt -- Tests for graph.rkt

;; Created by Freddie on Mon Sep 21 21:31:21 2015

;;; Include the code you want to test. 
;;; Be sure to comment out any tests or function calls in that file!
(require "graph.rkt")

;;;; Comment out if testing task 8
(define show identity)

(define map-display
  (lambda (lst)
    (for-each (lambda (i) (displayln (show i))) lst)))

(define (zip . xss)
  (apply map list xss))



;;;;;;;;;;;;;;;;;; Points ;;;;;;;;;;;;;;;;

(define point-test
  (lambda ()

    (define list_of_points 
      (list
       (makePoint 12 -1)
       (makePoint -11 11)
       (makePoint 15 13)
       (makePoint -10 8)
       (makePoint 4 1)
       )
      )
    (newline)
    (displayln "-------- Points ---------")
    (map-display list_of_points)
    (newline)
    (displayln "-- x-coords --")
    (map-display (map X_coord list_of_points))
    (newline)
    (displayln "-- y-coords --")
    (map-display (map Y_coord list_of_points))
    
    (newline)
    (newline)
    (newline)

))

;;; Uncomment to run point-test
(point-test)

;;;;;;;;;;;;;;;;;; Circles ;;;;;;;;;;;;;;;;

(define circle-test
  (lambda ()

    (displayln "----- Circles -----")
    (newline)
    
    (define list_of_circles
      (list
       (makeCircle -5 -9 8)
       (makeCircle 13 2 4)
       (makeCircle -1 12 -12)
       (makeCircle 9 -8 -2)
       (makeCircle 4 5 -1)
       )
      )
    (displayln "-- all circles --")
    (map-display list_of_circles)
    (newline)

    (define origins (map Origo list_of_circles))

    (displayln "-- origins --")
    (map-display origins)
    (newline)
    (displayln "-- origin x-coords --")
    (map-display (map X_coord origins))
    (newline)
    (displayln "-- origin y-coords --")
    (map-display (map Y_coord origins))
    (newline)
    (displayln "-- radii --")
    (map-display (map Radius list_of_circles))
    (newline)
    (newline)
    (newline)
))

;;; Uncomment to run circle-test
;(circle-test)

;;;;;;;;;;;;;;;;;; Rectangles ;;;;;;;;;;;;;;;;

(define rectangle-test
  (lambda ()

    (displayln "------ Rectangles ------")
    
    (define list_of_rectangles
      (list   
       (makeRectangle 2 -4 -2 2)
       (makeRectangle -8 15 0 -3)
       (makeRectangle 13 -10 -9 3)
       (makeRectangle -5 6 -15 -8)
       (makeRectangle 8 -6 4 10)
       (makeRectangle 8 -10 -2 -3)
       (makeRectangle -10 -9 -7 -14)
       (makeRectangle -6 -9 -2 8)
       (makeRectangle 15 -8 -13 -6)
       (makeRectangle 9 -9 -9 -14)
       )
      )
    (newline)
    (displayln "-- list_of_rectangles --")
    (map-display list_of_rectangles)

    (define lls (map Lower_left_corner list_of_rectangles))
    (newline)
    (displayln "-- lls --")
    (map-display lls)

    (define lrs (map Lower_right_corner list_of_rectangles))
    (newline)
    (displayln "-- lrs --")
    (map-display lrs)

    (define uls (map Upper_left_corner list_of_rectangles))
    (newline)
    (displayln "-- uls --")
    (map-display uls)

    (define urs (map Upper_right_corner list_of_rectangles))
    (newline)
    (displayln "-- urs --")
    (map-display urs)

    (newline)
    (displayln "-- all coords --")
    (map-display 
     (map (lambda (lst)
            (zip (map X_coord lst)
                 (map Y_coord lst)))
          (list lls lrs uls urs))
     )
    (newline)
    (newline)
    (newline)
))

;;; Uncomment to run rectangle-test
;(rectangle-test)

;;;;;;;;;;;;;;;;;; Lines ;;;;;;;;;;;;;;;;

(define line-segment-test
  (lambda ()
    
    (displayln "-- Line Segments --")
    (newline)
    
    (define list_of_line_segments 
      (list
       (makeLineSegment 5 6 5 15)
       (makeLineSegment -2 -11 -4 -15)
       (makeLineSegment -5 13 8 -13)
       (makeLineSegment -1 -1 10 1)
       (makeLineSegment 4 -11 -8 -11)
       )
      )
    (displayln "-- all line segments --")
    (map-display list_of_line_segments)
    (newline)

    ;;; This part assumes that you have implemented start/end like I did.
    
    (define start_points 
      (map Startpoint list_of_line_segments))
    (displayln "-- start points --")
    (map-display start_points)
    (newline)

    (define end_points
      (map Endpoint list_of_line_segments))
    (displayln "-- end points --")
    (map-display end_points)
    (newline)

    (displayln "-- all coords --")
    (map-display
     (map (lambda (lst)
            (zip (map X_coord lst)
                 (map Y_coord lst)))
          (list start_points end_points))
     )
    (newline)
    (newline)
    (newline)
))

;;; Uncomment to run line-segment-test
;(line-segment-test)


;;;;;;;;;;;;;;;;;; Pictures ;;;;;;;;;;;;;;;;;;;;;

(define picture-test
  (lambda ()
    (displayln "--- Picts  ---")
    (newline)

    (define the_pict 
  ;;; Comment out components of the picts if it is too large.
      (makePict (list
       (makeRectangle -11 -3 -4 0)
       (makeLineSegment -11 -4 -14 5)
       (makeRectangle -8 -15 -7 -14)
       (makeCircle 9 7 12)
       (makeLineSegment -14 6 11 1)
       (makeCircle 0 2 -5)
       (makePoint -14 15)
       (makeRectangle 12 -10 5 10)
       ))
      )
    (displayln "-- entire picts --")
    (map-display the_pict)
    (newline)


    (define firsts
      (reverse
       (let loop ((lst the_pict) (res null))
         (if (no_more? lst)
             res
             (loop (Rest_of lst) (cons (First_of lst) res))))))

    (displayln "-- firsts --")
    (map-display firsts)
    (newline)


    (define rests
      (reverse
       (let loop ((lst the_pict) (res null))
         (if (no_more? lst)
             res
             (loop (Rest_of lst) (cons (Rest_of lst) res))))))

    (displayln "-- rests --")
    (map map-display rests)
    (newline)
))


;;; Uncomment to run picture-test
;(picture-test)