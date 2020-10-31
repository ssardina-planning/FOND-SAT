(define (domain test)

    (:requirements :adl)

    (:predicates
        (a)
        (b)
        (c)
        (d)
        (e)
    )

    (:action action
        :parameters ()
        :precondition (a)
        :effect (oneof
            (when (b)(c))
            (when (c)(e))
        )
    )

    (:action actionA
        :parameters ()
        :precondition (not (a))
        :effect (a)
    )
)