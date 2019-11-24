(defrule generate-garis
	(titik ?identifier1 ?x1 ?y1)
	(titik ?identifier2 ?x2 ?y2)
	(titik ?identifier3 ?x3 ?y3)
	(titik ?identifier4 ?x4 ?y4)
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier3 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	(test(neq ?identifier1 ?identifier4))
	(test(neq ?identifier3 ?identifier4))
	(test(neq ?identifier2 ?identifier4))
	=>
	(assert (garis 1 (sqrt(+(*(- ?x2 ?x1)(- ?x2 ?x1))(*(- ?y2 ?y1)(- ?y2 ?y1))))))
	(assert (garis 2 (sqrt(+(*(- ?x2 ?x3)(- ?x2 ?x3))(*(- ?y2 ?y3)(- ?y2 ?y3))))))
	(assert (garis 3 (sqrt(+(*(- ?x3 ?x4)(- ?x3 ?x4))(*(- ?y3 ?y4)(- ?y3 ?y4))))))
	(assert (garis 4 (sqrt(+(*(- ?x4 ?x1)(- ?x4 ?x1))(*(- ?y4 ?y1)(- ?y4 ?y1))))))
	)

(defrule Jajar-Genjang
	(garis ?identifier1 ?g1)
	(garis ?identifier2 ?g2)
	(garis ?identifier3 ?g3)
	(garis ?identifier4 ?g4)
	(test (and (= ?g1 ?g3)(= ?g2 ?g4)))
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier3 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	(test(neq ?identifier1 ?identifier4))
	(test(neq ?identifier3 ?identifier4))
	(test(neq ?identifier2 ?identifier4))
	=>
	(assert (segiempat Jajar-Genjang))
)

(defrule Jajar-Genjang-Beraturan
	(garis ?identifier1 ?g1)
	(garis ?identifier2 ?g2)
	(garis ?identifier3 ?g3)
	(garis ?identifier4 ?g4)
	(segiempat Jajar-Genjang)
	(test (= ?g1 ?g2 ?g3 ?g4))
	=>
	(assert (segiempat Jajar-Genjang-Beraturan))
)

(defrule Jajar-Genjang-Layang-Layang
	(sudut ?identifier1 ?s1)
	(sudut ?identifier2 ?s2)
	(sudut ?identifier3 ?s3)
	(sudut ?identifier4 ?s4)
	(segiempat Jajar-Genjang)
	(test (or (and (= ?s1 ?s2) (= ?s3 s4)) (and (= ?s1 s3)(= ?s2 ?s4)) (and (= ?s1 ?s4)(= ?s2 ?s3))))
	=>
	(assert (segiempat Jajar-Genjang-Layang-Layang))
)

(defrule Trapesium
	(garis ?identifier1 ?g1)
	(garis ?identifier2 ?g2)
	(garis ?identifier3 ?g3)
	(garis ?identifier4 ?g4)
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier3 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	(test(neq ?identifier1 ?identifier4))
	(test(neq ?identifier3 ?identifier4))
	(test(neq ?identifier2 ?identifier4))
	=>
	(assert (segiempat Trapesium))
)

(defrule Trapesium-Sama-Kaki
	(segiempat Trapesium)
	(garis ?identifier1 ?g1)
	(garis ?identifier2 ?g2)
	(garis ?identifier3 ?g3)
	(garis ?identifier4 ?g4)
	(test (or (= ?g1 ?g2)(= ?g1 ?g3)(= ?g1 ?g4)(= ?g2 ?g3) (= ?g2 ?g4) (= ?g3 ?g4)))
	=>
	(assert (segiempat Trapesium-Sama-Kaki))
)

(defrule Trapesium-Siku-Siku
	(segiempat Trapesium)
	(sudut ?identifier1 ?s1)
	(test (= ?s1 90))
	=>
	(assert (segitempat Trapesium-Siku-Siku))
)