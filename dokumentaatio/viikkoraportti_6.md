# Viikko 6

Aikaa käytetty 8 tuntia, josta 2 tuntia vertaisarviota.

Viikolla 6 viimeistelty Lempel-Ziv, eli sovellus on nyt viimein 
ydintoiminnoiltaan periaatteessa täysin valmis. Seuraavalla viikolla tarkastelussa, 
saisiko luokkien rakennetta hieman refaktoroitua järkevämmäksi ja 
olisiko esimerkiksi syytä piiottaa private metodeiksi osa metodeista ja muutenkin
vähän yleistä koodin laatua ja käytäntöjä voisi höylätä.

Lempel-Ziv tallettaa tällä hetkellä tiedostoon mukaan listan 
merkeistä, jotka käytössä tiedostossa. 
Huomasin, että tämän voisi toteuttaa staattisella listalla, jota ei tarvitsisi tallettaa, jossa mukana ascii-merkit. Toisaalta listan tallentaminen binääriin ei vie ihan mahdottomasti
tilaa osuutena isoissa tiedostoissa ja Huffmanin puolella joutuu myös tallettamaan puun.
Katson ensi viikolla tarkemmin, tuleeko muutosta.

Lisäksi kirjoitettu testejä ja tyylikorjauksia pylintin pohjalta.
CI passing.

Ensi viikolla pääsee sitten dokumentaatiopuolta urakoimaan viimein kunnolla ja kirjoittamaan lisää testejä.
Tällä hetkellä testit ovat enimmäkseen oikeastaan vain rivikattavuuden kattamiseksi ja aika perustapauksia
varten, mutta katsotaan ensi viikolla olisiko syytä hieman spesiaalimpia testejä toteuttaa erilaisilla
(ehkä jopa satunnaisilla) syötteillä ja isoilla tiedostoilla.

Käyttöliittymään tulossa pieniä muutoksia, joilla sovellusta tulee olemaan helpompi käyttää.