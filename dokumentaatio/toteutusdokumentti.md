# Toteutusdokumentti

## Ohjelman yleisrakenne

Ohjelman arkkitehtuurinen rakenne on isoilta linjoiltaan seuraava. Tarkemmin luokkia, metodeita ja parametreja kannattaa tutkia suoraan lähdekoodista.

![Kaavio](https://github.com/Juboskar/pakkausalgoritmit/blob/main/dokumentaatio/kuvat/arkkitehtuuri.png)

Käyttäjän kanssa kommunikointiin on toteutettu graafinen käyttöliittymä (UI). Käyttöliittymä viestii controller-servicen kanssa, jonka toiminnan ytimen muodostavat Lempel-Ziv ja Huffman -pakkaamisesta ja purkamisesta vastaavat luokat. Tiedostojen tallentaminen ja lukeminen toteutetaan omassa luokassa, joka kommunikoi controller-luokan kanssa. 

## Algritmien suorituskyvyn vertailu

67kt kokoinen tiedosto pakkautui 36kt kokoiseksi Huffmanilla ja 26kt kokoiseksi Lempel-Zivillä. Lempel-Ziv pakkaa kuitenkin käytettäessä hitaammin siten, että käyttäjä joutuu pari sekuntia odottelemaan, kun taas Lempel-Ziv pakkaa käyttäjän näkökulmasta ilman viivettä. 

## Käytettyjä lähteitä:

- https://engineering.purdue.edu/ece264/17au/hw/HW13?alt=huffman [luettu 1.2.2022-10.2.2022]
- https://en.wikipedia.org/wiki/Huffman_coding [luettu 1.2.2022-10.2.2022]
- https://www.youtube.com/watch?v=JsTptu56GM8 [luettu 1.2.2022-10.2.2022]
- https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch [luettu 28.2.2022-10.2.2022]
- https://en.wikipedia.org/wiki/LZ77_and_LZ78 [luettu 28.2.2022-10.2.2022]
