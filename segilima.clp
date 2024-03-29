(defrule Segi-Lima
	(sudut ?identifier1 ?s1)
	(sudut ?identifier2 ?s2)
	(sudut ?identifier3 ?s3)
	(sudut ?identifier4 ?s4)
	(sudut ?identifier5 ?s5)
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	(test(neq ?identifier1 ?identifier4))
	(test(neq ?identifier1 ?identifier5))
	(test(neq ?identifier2 ?identifier3))
	(test(neq ?identifier2 ?identifier4))
	(test(neq ?identifier2 ?identifier5))
	(test(neq ?identifier3 ?identifier4))
	(test(neq ?identifier3 ?identifier5))
	(test(neq ?identifier4 ?identifier5))
	=>
	(assert (segilima tak-beraturan))
)

(defrule Segi-Lima-Beraturan
	(sudut ?identifier1 ?s1)
	(sudut ?identifier2 ?s2)
	(sudut ?identifier3 ?s3)
	(sudut ?identifier4 ?s4)
	(sudut ?identifier5 ?s5)
	(segilima tak-beraturan)	
	(test (= ?s1 ?s2 ?s3 ?s4 ?s5))
	=>
	(assert (segilima beraturan))
)