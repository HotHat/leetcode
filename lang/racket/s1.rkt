#lang racket

(define/contract (two-sum nums target)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  (letrec ([hs (make-hash)]
           [itr (lambda (lst target idx)
                  (if (null? lst)
                      '()
                      (if (hash-has-key? hs (car lst))
                          '(1  idx)
                          (begin
                            (hash-set! hs (- target (car lst)) idx)
                            (itr (cdr lst) target (+ 1 idx))))))])


    (itr nums target 0))

  )


(two-sum '(2 7 11 15) 9)