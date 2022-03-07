Ohjelman käyttäminen vaatii, että koneelle on asennettu python 3.8.0 tai myöhempi versio ja Poetry-riippuvuuksienhallintatyökalu.

### Käyttö

Käyttö tapahtuu komentoriviltä seuraavasti repositorion juuressa:

- Asenna ohjelman riippuvuudet:
``` poetry install ```

- Käynnistä ohjelma:
``` poetry run python3 src/index.py ```

Ohjelman käynnistäminen näyttää graafisen käyttöliittymän, jolla sovelluksen varsinainen käyttäminen tapahtuu.


### Muita komentoja

- Yksikkötestien suorittaminen:
``` poetry run pytest src ```

- Pylint:
``` poetry run pylint src ```

- Coverage:
``` poetry run coverage run --branch -m pytest src ```

- Coveragen suorittamisen jälkeen testikattavuusraportin generoiminen:
``` poetry run coverage html ```
