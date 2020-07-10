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
	:precondition (and
		(a)
	)
	:effect (and
		(when (b)
			(c))
		(when (c)
			(e))
			
	)
)
)