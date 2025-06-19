
## Connect4-peli, jossa voit pelata tekoälyä vastaan

# Minkälainen tekoäly on kyseessä?

Tekoäly tulee käyttämään min-max algoritmia, joka on optimoitu alpha-beta pruning tekniikalla. Jos jää aikaa, ajatuksena olisi tehdä eritasoisia tekoälyvastustajia, joista pelaaja voi valita itselleen sopivimman. Lisäksi olisi hienoa suunnitella pelille pygame-käyttöliittymä, mutta se saattaa jäädä kurssin ulkopuolelle.

# Minkä ongelman ratkaiset?

Tekoäly, joka osaa pelata mahdollisimman hyvin Connect4 -peliä

# Mitä ohjelmointikieltä käytät?

Ohjelma tulee olemaan koodattu Pythonilla

# Mitä syötteitä ohjelma saa ja miten niitä käytetään?

Käyttäjä (tai botti) antaa syötteenä pystyrivin numeron ja play funktio laskee, mikä on alin vaakarivi, johon rivillä on mahdollista pelata. Check win käy läpi kaikki ruudut ja tarkastaa voitot. Myöhemmin tähän saattaa tulla optimointia.


# Kerro myös mitä muita kieliä hallitset siinä määrin, että pystyt tarvittaessa vertaisarvioimaan niillä tehtyjä projekteja.

Olen koodannut aiemmin jonkin verran C++:aa,Gota, Javascriptiä ja Haskellia. (+ HTML ja CSS jotka eivät ole oikeastaan ohjelmointikieliä) Luulen kykyneväni vertaisarviomimaan näillä kielillä.

# Tavoitteena olevat aika- ja tilavaativuudet (esim. O-analyysit)

Min-max algoritmin aikavaatiums on O(n^m), jossa n on mahdolliset siirrot ja m puun syvyys. Connect4 pelin tapauksessa Ei siis ole järkevää käydä kaikkia vaihtoehtoja läpi, vaan rajata niitä mahdollisimman paljon alpha-beta pruningilla (eli välttää kokonaan sellaiset haarat, joista tiedetään, ettei niitä ole järkevä tarkastaa)

# Lähteet, joita aiot käyttää.

- https://youtu.be/DV5d31z1xTI?si=vICaqkOYK8VR5vNz

- https://youtube.com/playlist?list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&si=O0Z6BVGOSMm_acJs

- https://www.scaler.com/topics/artificial-intelligence-tutorial/min-max-algorithm/

- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

- https://github.com/KeithGalli/Connect4-Python

- https://en.wikipedia.org/wiki/Minimax


