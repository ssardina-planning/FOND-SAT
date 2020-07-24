(define (domain no_running_1)

  (:requirements
    :typing :conditional-effects
  )

  (:types Cell)

  (:constants
    c0 c1 c2 - Cell
  )

  (:predicates
  	(left ?c1 ?c2 - Cell)
    (right ?c1 ?c2 - Cell)
    (at ?c1 - Cell)
  )

(:action move-left
:parameters ()
:precondition ()
:effect (and
  (forall (?c1 ?c2 - cell)
    (when (and (at ?c1) (left ?c1 ?c2))
          (and (not (at ?c1)) (at ?c2))
    )
  )
)
)

(:action move-right
:parameters ()
:precondition ()
:effect (and
  (forall (?c1 ?c2 - cell)
    (when (and (at ?c1) (right ?c1 ?c2))
          (and (not (at ?c1)) (at ?c2))
    )
  )
)
)

)