
# Ohjelman yleisrakenne

- main.py tiedoston ainoa tehtävä on käynnistää peli kutsumalla connect4.py:n game_loop funktiota.

- Game_loop toimii pelin käyttöliittymänä. Jokaisella vuorollaan pelaaja antaa jonkin rivin johon haluaa pelata, jonka jälkeen game_loop kutsuu minmax funtiota.

# Saavutetut aika- ja tilavaativuudet (esim. O-analyysit pseudokoodista)

Minmaxin maksimiaikavaatimus on aina O(n^m), 

# Suorituskyky- ja O-analyysivertailu (mikäli sopii työn aiheeseen)


# Työn mahdolliset puutteet ja parannusehdotukset

Heuristiikkafunktio voisi varmaan edelleen olla parempi. En saanut muistiominaisuutta kovin pitkälle, enkä ole varma kuinka monimutkainen muistin olisi pitänyt olla, mutta algoritmi osaa nyt päivittää pystyrivijärjestyksen sen perusteella, kuinka syvälle algoritmi on mennyt kyseisessä pystyrivissä edellisellä kerralla. Koodi voisi myös olla siistimpää jossakin kohdissa.


# Laajojen kielimallien (ChatGPT yms.) käyttö. Mainitse mitä mallia on käytetty ja miten. Mainitse myös mikäli et ole käyttänyt. Tämä on tärkeää!

Koitin viimeisellä viikolla kysyä pariin kertaan apua ChatGPT:ltä ja se antoi joitakin hyviä vinkkejä miten check_win_x funktiot voisi tiivistää ja miten järjestäminen kannattaisi hoitaa sanakirjan arvojen perusteella. Muuten en käyttänyt generatiivista tekoälyä.

# Lähteet, joita olet käyttänyt, vain ne joilla oli merkitystä työn kannalta.

- https://youtube.com/playlist?list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV&si=O0Z6BVGOSMm_acJs

- https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

- https://github.com/KeithGalli/Connect4-Python

- https://en.wikipedia.org/wiki/Minimax

- https://github.com/msaveski/connect-four/tree/master
