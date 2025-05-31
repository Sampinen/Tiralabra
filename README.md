# Connect 4 solver
[Määrittelydokumentti](https://github.com/Sampinen/Tiralabra/blob/main/dokumentaatio/maarittelydokumentti.md)
## Releaset

[viikon 3 release](https://github.com/Sampinen/Tiralabra/releases/tag/viikko3)

[viikon 2 release](https://github.com/Sampinen/Tiralabra/releases/tag/viikko2)

[viikon 1 release](https://github.com/Sampinen/Tiralabra/releases/tag/viikko1)

## Viikkoraportit
[viikon 3 raportti](https://github.com/Sampinen/Tiralabra/blob/main/dokumentaatio/viikkoraportti3.md)

[viikon 2 raportti](https://github.com/Sampinen/Tiralabra/blob/main/dokumentaatio/viikkoraportti2.md)

[viikon 1 raportti](https://github.com/Sampinen/Tiralabra/blob/main/dokumentaatio/viikkoraportti1.md)



## Komennot, joilla sovellusta käytetään

Aja seutavat komennot juurikansiossa, voit myös ajaa ensiksi poetry shell ja sen jälkeen ajaa komennot ilman poetry run osaa

### Riippuvuuksien asentaminen:

```bash
poetry install
```

### Sovelluksen käynnistäminen

```bash
poetry run invoke start
```
### Testit
```bash
poetry run invoke test
```
### Testikattavuus
(Komento poikkeaa hieman ohjeesta, koska alaviivan kanssa komentokehote ei tunnista sitä)
```bash
poetry run invoke coverage-report
```
### Pylint

```bash
poetry run invoke lint
```
