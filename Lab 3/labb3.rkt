#lang racket
(require "graph.rkt")

;; Make a new graph
(define makeGraph
  (lambda (type shape)
    (cons type shape)))

;; type of a graph
(define type 
  (lambda (graph) 
    (car graph)))

;; shape of a graph
(define shape 
  (lambda (graph) 
    (cdr graph)))

;; make a point
(define makePoint
  (lambda (x0 y0)
    (makeGraph 'point (list x0 y0))))

;; make a circle
(define makeCircle
  (lambda (x0 y0 radius)
    (makeGraph 'circle (list (makePoint x0 y0) radius))))

;; make a rectangle
(define makeRectangle
  (lambda (x0 y0 x1 y1)
    (define xmax
      (lambda (x0 x1)
      (if (> x0 x1)
          x0
          x1)))
    (define xmin
      (lambda (x0 x1)
      (if (< x0 x1)
          x0
          x1)))
      (define ymax
      (lambda (y0 y1)
      (if (> y0 y1)
          y0
          y1)))
    (define ymin
      (lambda (y0 y1)
      (if (< y0 y1)
          y0
          y1)))
    (makeGraph 'rectangle
               (list (makePoint (xmin x0 x1) (ymax y0 y1))
                     (makePoint (xmax x0 x1) (ymin y0 y1))))))