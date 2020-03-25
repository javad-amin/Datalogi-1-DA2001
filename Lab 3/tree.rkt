#lang racket

;; tree.rkt -- Another test figure

(require "graph.rkt")

;;;;;;;;;;;;
;; Another test figure.
(start 800 800)
(begin
  (clear)
  (define FIRST_BRANCH_ANGLE 0.2)
  (define FIRST_JOINT_SIZE 1.0)
  (define SECOND_JOINT_SIZE 0.5)
  (define FIRST_SUBLEAF_SIZE (/ 1 1.5))
  (define SECOND_SUBLEAF_SIZE (/ 1 2.5))
  (define FIRST_SUBLEAF_ANGLE 1.1)
  (define SECOND_SUBLEAF_ANGLE 0.8)
  
  (define LEAF_ORIGIN_X 200)
  (define LEAF_ORIGIN_Y 700)
  (define LEAF_SIZE 300)
  (define LEAF_ANGLE -1.5)
  (define NUMBER_OF_SUBLEAF_LEVELS 6)
  (define FRUIT_SIZE 3)
  
  (define point+
    (lambda (p1 p2)
      (makePoint (+ (X_coord p1) (X_coord p2))
                 (+ (Y_coord p1) (Y_coord p2)))))

  (define point*scalar
    (lambda (point factor)
      (makePoint (* (X_coord point) factor)
                 (* (Y_coord point) factor))))
  

  ;; Grafik-test. En fraktal som föreställer en kvist.
  ;; Tar en punkt (point) där bilden börjar, en storlek i pixlar,
  ;; och antal sub-nivåer. Hur bilden ser ut beror på konstanter som BRANCH_ANGLE definierade ovan.
  (define leaf-graph-list
    (lambda (start_point size angle_rad iters)
      
      (if (= iters 0)

          ;; Basfall, bara ett löv (liten cirkel)
          (list (makeCircle (X_coord start_point)
                            (Y_coord start_point) FRUIT_SIZE))

          ;; Rekursions-fall, en gren med små löv
          (let* ((unit_ang (makePoint (cos angle_rad)
                                      (sin angle_rad)))
                 (unit_ang_rot (makePoint (cos (+ angle_rad FIRST_BRANCH_ANGLE)) 
                                          (sin (+ angle_rad FIRST_BRANCH_ANGLE))))
                 (branch1 (point+ start_point (point*scalar unit_ang size)))
                 
                 (branch2 (point+ branch1 
                                  (point*scalar unit_ang_rot (* size SECOND_JOINT_SIZE)))))
            
            (append (list 
                     ;; sträckan från kvistens början till första förgreningspunkten
                     (makeLineSegment (X_coord start_point) (Y_coord start_point)
                                      (X_coord branch1) (Y_coord branch1))

                     ;; sträckan från första till 2:a förgreningspunkten
                     (makeLineSegment (X_coord branch1) (Y_coord branch1)
                                      (X_coord branch2) (Y_coord branch2))
                     )

                    ;; Rekursivt anrop, första förgreningspunkten
                    (leaf-graph-list branch1 
                                     (* size FIRST_SUBLEAF_SIZE)
                                     (+ angle_rad FIRST_SUBLEAF_ANGLE)   (- iters 1))

                    ;; rekursivt anrop andra förgreningspunkten
                    (leaf-graph-list branch2 
                                     (* size SECOND_SUBLEAF_SIZE)
                                     (+ angle_rad SECOND_SUBLEAF_ANGLE)  (- iters 1))
                    )))))

  ;; Huvudanrop
  (drawGraph (makePict (cons
                        (makeRectangle 100 100 700 700)
                        
                        (leaf-graph-list (makePoint LEAF_ORIGIN_X LEAF_ORIGIN_Y) LEAF_SIZE
                                         LEAF_ANGLE
                                         NUMBER_OF_SUBLEAF_LEVELS))))
  )