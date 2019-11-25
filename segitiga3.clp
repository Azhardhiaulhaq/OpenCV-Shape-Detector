(defrule generate-garis
	(titik ?x1 ?y1)
	(titik ?x2 ?y2)
	(titik ?x3 ?y3)
	(test (> (sqrt(+(*(- ?x2 ?x1)(- ?x2 ?x1))(*(- ?y2 ?y1)(- ?y2 ?y1)))) 0))
	(test (> (sqrt(+(*(- ?x2 ?x3)(- ?x2 ?x3))(*(- ?y2 ?y3)(- ?y2 ?y3)))) 0))
	(test (> (sqrt(+(*(- ?x3 ?x1)(- ?x3 ?x1))(*(- ?y3 ?y1)(- ?y3 ?y1)))) 0))
	=>
	(assert (garis 1 (sqrt(+(*(- ?x2 ?x1)(- ?x2 ?x1))(*(- ?y2 ?y1)(- ?y2 ?y1))))))
	(assert (garis 2 (sqrt(+(*(- ?x2 ?x3)(- ?x2 ?x3))(*(- ?y2 ?y3)(- ?y2 ?y3))))))
	(assert (garis 3 (sqrt(+(*(- ?x3 ?x1)(- ?x3 ?x1))(*(- ?y3 ?y1)(- ?y3 ?y1))))))
	)

(defrule generate-sudut
	(garis ?identifier1 ?g1)
	(garis ?identifier2 ?g2)
	(garis ?identifier3 ?g3)
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier3 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	=>
	(assert (sudut 1 (rad-deg (acos(/ (+ (* ?g1 ?g1) (- (* ?g2 ?g2)(* ?g3 ?g3))) (* 2 ?g1 ?g2))))))
	(assert (sudut 2 (rad-deg (acos(/ (+ (* ?g3 ?g3) (- (* ?g2 ?g2)(* ?g1 ?g1))) (* 2 ?g3 ?g2))))))
	(assert (sudut 3 (rad-deg (acos(/ (+ (* ?g1 ?g1) (- (* ?g3 ?g3)(* ?g2 ?g2))) (* 2 ?g1 ?g3))))))
	)

(defrule segitiga-lancip
	(sudut ?identifier1 ?s1)
	(sudut ?identifier2 ?s2)
	(sudut ?identifier3 ?s3)
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier3 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	(test (and (< ?s1 89) (and (< ?s2 89) (< ?s3 89))))
	=>
	(assert (segitiga lancip))
	)

(defrule segitiga-tumpul
	(sudut ?identifier1 ?s1)
	(sudut ?identifier2 ?s2)
	(sudut ?identifier3 ?s3)
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier3 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	(test (or (and (> ?s1 91)(< ?s1 180)) (and (> ?s2 91)(< ?s2 180))(and (> ?s3 91)(< ?s3 180))))
	=>
	(assert(segitiga tumpul))
	)

(defrule segitiga-sama-sisi
	(garis ?identifier1 ?g1)
	(garis ?identifier2 ?g2)
	(garis ?identifier3 ?g3)
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier3 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	(test (= ?g1 ?g2 ?g3))
	=>
	(assert (segitiga sama-sisi))
)

(defrule segitiga-siku-siku
	(sudut ?identifier1 ?s1)
	(test (and (> ?s1 89) (< ?s1 91)))
	=>
	(assert (segitiga siku-siku))
)

(defrule segitiga-sama-kaki
	(sudut ?identifier1 ?g1)
	(sudut ?identifier2 ?g2)
	(test (neq ?identifier1 ?identifier2))
	(test(= ?g1 ?g2))
	=>
	(assert (segitiga sama-kaki))
)

(defrule segitiga-sama-kaki-siku-siku
	(segitiga sama-kaki)
	(sudut ?identifier1 ?s1)
	(test(or (> ?s1 89) (< ?s1 91)))
	=>
	(assert (segitiga sama-kaki-siku-siku))
)

(defrule segitiga-samakaki-tumpul
	(segitiga sama-kaki)
	(sudut ?identifier1 ?s1)
	(sudut ?identifier2 ?s2)
	(sudut ?identifier3 ?s3)
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier3 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	(test (or (> ?s1 90) (> ?s2 90) (> ?s3 90)))
	=>
	(assert (segitiga sama-kaki-tumpul)
))

(defrule segitiga-samakaki-lancip
	(segitiga sama-kaki)
	(sudut ?identifier1 ?s1)
	(sudut ?identifier2 ?s2)
	(sudut ?identifier3 ?s3)
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier3 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	(test(and (< ?s1 90) (< ?s2 90) (< ?s3 90)))
	=>
	(assert (segitiga sama-kaki-lancip))
)

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
	(test (or (and (= ?s1 ?s2) (= ?s3 ?s4)) (and (= ?s1 ?s3)(= ?s2 ?s4)) (and (= ?s1 ?s4)(= ?s2 ?s3))))
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

(defrule Segi-Enam
	(sudut ?identifier1 ?s1)
	(sudut ?identifier2 ?s2)
	(sudut ?identifier3 ?s3)
	(sudut ?identifier4 ?s4)
	(sudut ?identifier5 ?s5)
	(sudut ?identifier6 ?s6)
	(test(neq ?identifier1 ?identifier2))
	(test(neq ?identifier1 ?identifier3))
	(test(neq ?identifier1 ?identifier4))
	(test(neq ?identifier1 ?identifier5))
	(test(neq ?identifier1 ?identifier6))
	(test(neq ?identifier2 ?identifier3))
	(test(neq ?identifier2 ?identifier4))
	(test(neq ?identifier2 ?identifier5))
	(test(neq ?identifier2 ?identifier6))
	(test(neq ?identifier3 ?identifier4))
	(test(neq ?identifier3 ?identifier5))
	(test(neq ?identifier3 ?identifier6))
	(test(neq ?identifier4 ?identifier5))
	(test(neq ?identifier4 ?identifier6))
	(test(neq ?identifier5 ?identifier6))
	=>
	(assert (segienam tak-beraturan))
)

(defrule Segi-Enam-Beraturan
	(sudut ?identifier1 ?s1)
	(sudut ?identifier2 ?s2)
	(sudut ?identifier3 ?s3)
	(sudut ?identifier4 ?s4)
	(sudut ?identifier5 ?s5)
	(sudut ?identifier6 ?s6)
	(segienam tak-beraturan)	
	(test (= ?s1 ?s2 ?s3 ?s4 ?s5 ?s6))
	=>
	(assert (segienam beraturan))
)



