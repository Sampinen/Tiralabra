
# Ohjelman yleisrakenne

- main.py tiedoston ainoa tehtävä on käynnistää peli kutsumalla connect4.py:n game_loop funktiota.

- Game_loop toimii pelin käyttöliittymänä. Jokaisella vuorollaan pelaaja antaa jonkin rivin johon haluaa pelata, jonka jälkeen game_loop kutsuu iterative_deepening funktiota

- Iterative_deepening kutsuu minmax funktiota aloittaen syvyydestä 1 ja

# Saavutetut aika- ja tilavaativuudet (esim. O-analyysit pseudokoodista)

Iterative_deepening jatkaa alussa syvyydelle 6-8. Uskon tämän johtuvan tietokoneesta, eikä koodista, koska tälle ei pitäisi olla mitään järkevää selitystä. Tällöin ylletään siis aikavaativuudelle välillä O(n^6) ja 0(n^8). Pelin edetessä algoritmi pääsee tätäkin syvemmälle. Todellisuudessa läheskään kaikkia arvoja ei käydä läpi alfa-beta karsinnan ansiosta.

# Suorituskyky- ja O-analyysivertailu (mikäli sopii työn aiheeseen)


# Työn mahdolliset puutteet ja parannusehdotukset

Heuristiikkafunktio voisi varmaan edelleen olla parempi. Score ==2 (kaksi samaa jotka eivät ole vierekkäin) tilanteelle voisi olla oma pisteytys jokaon jotain winrow ==2 ja score ==1 välillä, sekä pisteytys score >=3 winrow >=3 ja score ==2 välille.


# Laajojen kielimallien (ChatGPT yms.) käyttö. Mainitse mitä mallia on käytetty ja miten. Mainitse myös mikäli et ole käyttänyt. Tämä on tärkeää!

Koitin viimeisellä viikolla kysyä pariin kertaan apua ChatGPT:ltä ja se antoi joitakin hyviä vinkkejä miten check_win_x funktiot voisi tiivistää ja miten järjestäminen kannattaisi hoitaa sanakirjan arvojen perusteella. Muuten en käyttänyt generatiivista tekoälyä. 

# Lähteet, joita olet käyttänyt, vain ne joilla oli merkitystä työn kannalta.

- https://youtube.com/playlist?list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&si=O0Z6BVGOSMm_acJs

- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

- https://github.com/KeithGalli/Connect4-Python

- https://en.wikipedia.org/wiki/Minimax

- https://github.com/msaveski/connect-four/tree/master
