

# Yksikkötestauksen kattavuusraportti.


#  Mitä on testattu, miten tämä tehtiin?

On testattu, että voitontarkistusfunktio osaa tarkistaa voiton jokaiseen suuntaan, koska tämä on kenties tärkein asia. Ensin on testattu, että play funktio päivittää laudalta halutun ruudun tyhjästä ("  ") ja pelatun symbolin mukaiseksi ("X ") sekä, että check_win_cell palauttaa Falsen, jos ruutu on tyhjä. Tämän jälkeen on pelattu play funktion avulla neljän pelinappulan pysty, vaaka, ja vinottain ylös ja alaspäinosottavat rivit. Tämän jälkeen on tarkastettu unittestin assertEqual funktion avulla, että check_win_cell palauttaa Truen kaikissa näissä tapauksissa. 

Laudan pisteenlaskuun liittyvistä funktioista ei ole testejä, koska ajattelin sen olevan turhan hankalaa. Käyttöliittymää en testannut.

# Minkälaisilla syötteillä testaus tehtiin?


# Miten testit voidaan toistaa?

Tämä lukee jo Readmessä

# Ohjelman toiminnan mahdollisen empiirisen testauksen tulosten esittäminen graafisessa muodossa. (Mikäli sopii aiheeseen)

