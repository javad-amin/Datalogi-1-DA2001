

#lang racket

;; GRAPH.SCM
;;
;; Graph is a simple graphics package in scheme.
;;
;; revision made by Alex Loiko and Fredrika Agestam 2015-08-07
;;;; to update drawGraph to work in more Racket dialects and
;;;; to draw another picture.
;; revision made by Serafim Dahl 2009-09-18
;;;; to make graph.scm independent of simple-draw
;;;; by including the content of simple-draw in
;;;; this file
;; revision made by Per Sedholm 2008-09-15
;; revision made by Serafim Dahl 2005-08-29
;; revision made by Marco Wesselgren 1997-09-14
;; Many thanks

;; ------------------------------------------------
;; Rör inte -- Behövs för att drawGraph ska fungera
(provide start clear)
(provide (all-defined-out))

(require (lib "draw.ss" "htdp")
	 (lib "posn.ss" "lang"))

(define draw-a-point
  (lambda (X_coord Y_coord . color) 
    (if (null? color)
	(draw-solid-disk (make-posn X_coord Y_coord) 1)
	(draw-solid-disk (make-posn X_coord Y_coord) 1 (car color)))))

(define draw-a-line-segment
  (lambda (X_coord_1 Y_coord_1 X_coord_2 Y_coord_2 . color)
    (if (null? color)
	(draw-solid-line (make-posn X_coord_1 Y_coord_1)
			 (make-posn X_coord_2 Y_coord_2))
	(draw-solid-line (make-posn X_coord_1 Y_coord_1)
			 (make-posn X_coord_2 Y_coord_2)
			 (car color)))))

(define draw-a-circle
  (lambda (X_coord Y_coord radius . color)
    (if (null? color)
	(draw-circle (make-posn X_coord Y_coord) radius)
	(draw-circle (make-posn X_coord Y_coord) radius (car color)))))

(define clear clear-all)

;;; -----------------------------------------------------------------
;;; ---------- allt härovanför måste vara intakt, rör INTE ----------

;; Här börjar det som man kan (ska) ändra i

;; makeGraph -- constructor for graphical units.
(define makeGraph
  (lambda (type shape)
    (cons type shape)))

;; type -- selector for the type of a graphical unit
(define type
  (lambda (graph)
    (car graph)))

;; shape -- selector for the shape of a graphical unit
(define shape
  (lambda (graph)
    (cdr graph)))

;;;;;;;;;;
;; Constructors for the various graphical units.
;;
;; TODO: Delete the quoted text and write your code in its place.

;; makePoint -- constructor for 'point
(define makePoint
  (lambda (x0 y0)
    (makeGraph 'point (list x0 y0))))

;; returnera X koorinaten
;;(define X_coord
 ;; (lambda (point)
  ;;  (cadr point)))

;; returnera Y koorinaten
;;(define Y_coord
;;  (lambda (point)
;;    (caddr point)))

;; make a circle
(define makeCircle
  (lambda (x0 y0 radius)
    (makeGraph 'circle (list (makePoint x0 y0) radius))))

;; makeLine -- constructor for 'line_segment
(define makeLineSegment
  (lambda (x0 y0 x1 y1)
    (makeGraph 'line_segment
               (list (makePoint x0 y0)
                     (makePoint x1 y1)))))

;; makeRectangle -- constructor for 'rectangle
(define makeRectangle
  (lambda (x0 y0 x1 y1)
    (makeGraph 'rectangle
               (list (makePoint (min x0 x1) (max y0 y1))
                     (makePoint (max x0 x1) (min y0 y1))))))
               

;; makePict -- constructor for 'pict
(define makePict
  (lambda (picts)
    (makeGraph 'pict picts)))

;;;;;;;;;;
;; Help functions for safer selectors

;;(define Radius           ;; Re-defined later; see below
 ;; (lambda (circle)
  ;;  (if (eq? (type circle) 'circle)
     ;;   (cadr (shape circle))
    ;;    (errormessage "this does not work with" circle))))

;; errormessage -- report an error.
;;   ``string'' is the error message
;;   ``object'' is the object that caused the error.
(define errormessage
  (lambda (string object)
    (error (string-append string
                          " "
                          (symbol->string (type object))))))

;;;; Assignment 5: Comment out the previous definition of `X_coord`
;;;; and uncomment this one.
;; (define X_coord          ;; Re-defined later; see below
;;   (lambda (point)
;;     (if (eq? (type point) 'point)
;;         (car (shape point))
;;         (errormessage "this does not work with" point))))



;;;;;;;;;;
;; Selectors for the various graphical units.
;;
;; NB: Some of these replaces previous versions. Normally, the code
;;     for the previous versions should be removed. In this case, we
;;     (the assistants) may want to look at them, so it's best to
;;     simply leave them in place.

;;;; Assignment 6: Comment out the previous definitions of `X_coord`
;;;; and `Y_coord` and uncomment these ones.

;; ;; X_coord -- select the X coordinate from the given 'point
;; (define X_coord
;;   (lambda (point)
;;     (retrieve point 'point car)))

;; A funnction in order to select and retrieve data from the graph
(define retrieve
  (lambda (graph expected-type selection)
    (if (eq? (type graph) expected-type)
        (if (null? (shape graph)) '()
            (selection (shape graph)))
        (errormessage "this does not work with" graph))))

;; radius of circle
(define Radius
  (lambda (circle)
    (retrieve circle 'circle cadr)))

;; x-coord of point
(define X_coord
  (lambda (point)
    (retrieve point 'point car)))

;; ;; Y_coord -- select the Y coordinate from the given 'point
;; y-coord of point
(define Y_coord
  (lambda (point)
    (retrieve point 'point cadr)))

;; Lower_left_corner -- select the lower left (or south west) corner
;; of the given 'rectangle
(define Lower_left_corner
  (lambda (rectangle)
    (retrieve rectangle 'rectangle car)))

;; Upper_right_corner -- select the upper right (or north east) corner
;; of the given 'rectangle
(define Upper_right_corner
  (lambda (rectangle)
    (retrieve rectangle 'rectangle cadr)))

;; Lower_right_corner -- select the lower right (or south east) corner
;; of the given 'rectangle
(define Lower_right_corner
  (lambda (rectangle)
    (makePoint (X_coord (Upper_right_corner rectangle))
                (Y_coord (Lower_left_corner rectangle)))))

;; Upper_left_corner -- select the upper left (or north west) corner
;; of the given 'rectangle
(define Upper_left_corner
  (lambda (rectangle)
    (makePoint (X_coord (Lower_left_corner rectangle))
                (Y_coord (Upper_right_corner rectangle)))))

;; Origo -- select the center of the given 'circle
(define Origo
  (lambda (circle)
    (retrieve circle 'circle car)))

;;;; In Assignment 6: Comment out the previous version of `Radius`
;;;; and uncomment this one
;; ;; Radius -- select the radius of the given 'circle
;; (define Radius
;;   (lambda (circle)
;;     (retrieve circle 'circle cadr)))

;; Startpoint -- select the first point of the given 'line_segment
(define Startpoint
  (lambda (line_segment)
    (retrieve line_segment 'line_segment car)))

;; Endpoint -- select the second (last) point of the given 'line_segment
(define Endpoint
  (lambda (line_segment)
    (retrieve line_segment 'line_segment cadr)))

;; Graphs -- select the list of graphical units from the given 'pict
(define Graphs
  (lambda (graph)
    (list (retrieve graph 'pict car) (retrieve graph 'pict cdr))))

    


;; First_of -- select the first of the graphical units from the given
;; 'pict
(define First_of
  (lambda (graphs)
    (retrieve graphs 'pict car)))

;; Rest_of -- create a new 'pict with the second through last (i.e.
;; all except the first) of the graphical units of the given 'pict
(define Rest_of
  (lambda (graphs)
    (makePict (retrieve graphs 'pict cdr))))

;; no_more? -- predicate to determine whether the given 'pict has any
;; graphical units. Returns #t if the list of graphical units is empty,
;; #f otherwise.
(define no_more?
  (lambda (graphs)
    (if (null? (retrieve graphs 'pict car)) #t #f)))
               

;; Assignment 7: Comment out this function to draw objects in color, when they have a color attribute.
(define color (lambda (object) 'black))

;; drawGraph can be used to draw the graphical units on the computer
;; screen.
(define (drawGraph object)
  (if (null? object) null
      (let ((color (color object)))
  (cond ((equal? 'point (type object))
         (draw-a-point (X_coord object)
                       (Y_coord object)
                       color))

        ((equal? 'circle (type object))
         (draw-a-circle (X_coord (Origo object))
                        (Y_coord (Origo object))
                        (Radius object)
                        color))

        ((equal? 'line_segment (type object))
         (draw-a-line-segment (X_coord (Startpoint object))
                      (Y_coord (Startpoint object))
                      (X_coord (Endpoint object))
                      (Y_coord (Endpoint object))
                      color))

        ((equal? 'rectangle (type object))
         (draw-a-line-segment (X_coord (Lower_left_corner object))
                      (Y_coord (Lower_left_corner object))
                      (X_coord (Upper_left_corner object))
                      (Y_coord (Upper_left_corner object))
                      color)
         (draw-a-line-segment (X_coord (Upper_left_corner object))
                      (Y_coord (Upper_left_corner object))
                      (X_coord (Upper_right_corner object))
                      (Y_coord (Upper_right_corner object))
                      color)
         (draw-a-line-segment (X_coord (Upper_right_corner object))
                      (Y_coord (Upper_right_corner object))
                      (X_coord (Lower_right_corner object))
                      (Y_coord (Lower_right_corner object))
                      color)
         (draw-a-line-segment (X_coord (Lower_right_corner object))
                      (Y_coord (Lower_right_corner object))
                      (X_coord (Lower_left_corner object))
                      (Y_coord (Lower_left_corner object))
                      color))

        ((equal? 'pict (type object))
         (if (not (no_more? object))
             (begin
               (drawGraph (First_of object))
               (drawGraph (Rest_of object)))
             null))))))

;;;;;;;;;;
;; Test figure
(define test-figure
  (lambda ()
    (start 400 400)
    (begin
      (clear)
      (define r 100)
      (define x0 200)
      (define y0 200)
      (define PI (* 4 (atan 1)))
      (define x/2 (* (/ (sqrt 3) 2) r))
      (define fig
        (makePict (list
                   (makePoint x0 y0)
                   (makeRectangle (- x0 r) (- y0 r) (+ x0 r) (+ y0 r))
                   (makeCircle x0 y0 r)
                   (makePict (list (makeLineSegment x0         (- y0 r)
                                                    (- x0 x/2) (+ y0 (/ r 2)))
                                   (makeLineSegment x0         (- y0 r)
                                                    (+ x0 x/2) (+ y0 (/ r 2)))
                                   (makeLineSegment (- x0 x/2) (+ y0 (/ r 2))
                                                    (+ x0 x/2) (+ y0 (/ r 2))))))))
      (drawGraph fig)
      )
    ))



;;     Test

(define mypoint (makePoint 100 100))
(define myrectangle (makeRectangle 50 350 350 50))
(define mycircle (makeCircle 200 200 50))
(define myline (makeLineSegment 300 300 200 200))
(define mypic (makePict (list myline mycircle mypoint myrectangle)))
;;(start 400 400)
;;(drawGraph mypic)

;;(define myrectangle (makeRectangle 1 7 3 2))
;;(Upper_left_corner myrectangle) (Upper_right_corner myrectangle) (Lower_right_corner myrectangle) (Lower_left_corner myrectangle)
