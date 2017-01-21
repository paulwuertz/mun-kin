import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

monstroj={
	"Nivelo 1":5,
	"Nivelo 2":5,
	"Nivelo 4":4,
	"Nivelo 6":4,
	"Nivelo 8":4,
	"Nivelo 10":3,
	"Nivelo 12":3,
	"Nivelo 14":3,
	"Nivelo 16":3,
	"Nivelo 18":2,
	"Nivelo 20":1,
}

klaso  = "Klaso" 
klasoj = ["Klaso 1","Klaso 2","Klaso 3","Klaso 4"]
kras_kvant = 	 3

raso  = "Raso"
rasoj = ["Raso 1","Raso 2","Raso 3"]
			
malbenoj = 		19
tuj_kartoj = 	 8
supermun = 		 4
migramon = 		 3
veturiloj = 	 7
trompi = 		 2

gajni_niv = 9
unufoj = [4,3,2,2] #2,3,4,5
ras_nur = [2,2,1]
klas_nur = [2,2,2,1]
#ras_ne = 1 po do 7

vestag=[{"Ŝuoj":3},{"Unumane":5},{"Dumane":3},{"Torso":3},{"Kesto":3}]
aliaj=12
#+	pordoj		64 40
#+	monstroj	37 x
#+	trezoroj	67 9
#______________168

db = create_engine('sqlite:///visualalchemist.db')
db.echo = False  # Try changing this to True and see what happens
Session = sessionmaker(bind=db)

# create a Session
session = Session()

kartaro=Kartaro(nomo="Esperanĉkin")
session.add(kartaro)

bild=Bildo(nomo="Test",loko="test.jpg")
session.add(bild)

for mon in monstroj:
	for i in range(monstroj[mon]):
		nivel, trezor=""," Trezoro"
		if monstroj[mon] > 15:
			nivel+="2 Niveloj"
		if monstroj[mon] > 3:
			trezor+="j"
		if not monstroj[mon] in [14,16,18]:
			trezor = str(6-monstroj[mon])+trezor
		else:
			trezor = str(7-monstroj[mon])+trezor

		obj=Karto(supra_top=mon,supra="Nomo de Monstro",  klarigo_eta_teksto="Dummy tekst kio ripetas "*6, piedo_dekstra=trezor ,piedo_maldekstra=nivel, bildo_id=1, bildo=bild, kartaro_id=1, kartaro=kartaro)
		session.add(obj)  

for ras in rasoj:
	for i in range(kras_kvant):			
		obj=Karto(supra=ras,  klarigo_eta_teksto="Dummy tekst kio ripetas "*5, piedo_dekstra=raso, bildo_id=1, bildo=bild, kartaro_id=1, kartaro=kartaro)
		session.add(obj)  

for klas in klasoj:
	for i in range(kras_kvant):			
		obj=Karto(supra=klas,  klarigo_eta_teksto="Dummy tekst kio ripetas "*5, piedo_dekstra=klaso, bildo_id=1, bildo=bild, kartaro_id=1, kartaro=kartaro)
		session.add(obj)  

for gajn in range(gajni_niv):
	obj=Karto(supra="Stultaj ideoj",  klarigo_ega_teksto="Akiru nivelon", bildo_id=1, bildo=bild, kartaro_id=1, kartaro=kartaro)
	session.add(obj)  

for beno in range(malbenoj):
	obj=Karto(supra="Malbeno!",  klarigo_eta_teksto="Bene, bene, benite! "*5, bildo_id=1, bildo=bild, kartaro_id=1, kartaro=kartaro) 
	session.add(obj)  

for rol in klasoj+rasoj:
	for i in range(kras_kvant):
		obj=Karto(supra=rol,  klarigo_eta_teksto="Rasa, klasa, afabla... "*5, bildo_id=1, bildo=bild, kartaro_id=1, kartaro=kartaro) 
		session.add(obj)  

session.commit() 
session.flush()