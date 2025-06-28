Kun olet ladannut ohjelman koneellesi, lataa ensiksi riippuvuudet seuraavalla komennolla juurikansiossa:

```bash
poetry install
```
Tämän jälkeen aja seuraava komento juurikansiossa

```bash
poetry shell
```
Voit aloittaa ohjelman ajamalla seuraavan komennon
```bash
invoke start
```
Ensin ohjelma pyytää sinua valitsemaan itsellesi pelimerkin, joka tulee näkymään pelilaudalla. Tekoäly näkyy laudalla AI-nimimerkillä. Ihmispelaaja aloittaa aina ja voit jokaisella vuorollasi pelata jollekin pystyriville välillä 1-7.

Tekoälyn vuoron aikana tulostunut tuple kertoo ensimmäisenä mihin pystyriville se on pelannut (1-7) ja toisena arvona uskooko tekoäly ihmispelaajan (positiivinen arvo) vai tekoälyn (negatiivinen arvo) voittavan. Alussa arviot eivät ole kovin luotettavia ja algoritmi palauttaa positiivisen tai negatiivisen arvon riippuen ainoastaan onko haluttu laskentasyvyys parillinen vai pariton. 

Voit halutessasi kokeilla peliä eri laskentasyvyyksillä muuttamalla kohtaa, jossa connect4.py tiedoston game_loop funktio kutsuu minmaxia. Tällä hetkellä maksimi, jolla tekoälyn laskenta-aika on siedettävä on 8-9 syvyyden luokkaa. 