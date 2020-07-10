(define (domain test)

(:requirements :strips)

(:predicates
	(a)
	(b)
	(c)
	(d)
	(e)
)

(:action action_c
	:parameters ()
	:precondition (and
		(a)
		(b)
	)
	:effect (and
		(c)
	)
)

(:action action_e
	:parameters ()
	:precondition (and
		(a)
		(c)
	)
	:effect (and
		(e)
	)
)
)