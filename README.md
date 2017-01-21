# Ekzemplo

http://www.p4w5.eu/munchkin

# Kio estas?

Ilo por memfari Munĉkinkartaro enrete per grupo. Estas tutfuŝe farite, ĉar mi ne estas retprogramisto kaj verŝajne nek estas sekure nek bele, sed devus simple funkscii.

# Kiel uzi

Ĉar mi ne uzas uzantojn kaj volas nur elektitajn homojn kunlabori mi kombinias ĝin kun .htpasswd kaj Deamon, kiu faras intersavaĵojn...
Estas pli rapidaĉfarite ol uzemfarite por savaĝa reto ;)
Konsideru ĝin uzi lokale eble, aû klopodu blibonigajn ŝanĝojn ;)  

'''bash
mkvirtualenv munchkin && cd munchkin
source bin/activate

git clone https://github.com/paulwuertz/mun-kin
cd mun-kin

pip install -r requirements.txt

python models.py && python tests/populate.py # ekkreas modeloj kaj 
python app.py
'''
