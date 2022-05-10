# Diplomová práca - Využitie infračerveného žiarenia a termovízie na ochranu verejných priestorov a budov



Cieľom tejto diplomovej práce je preskúmať možnosti využitia infračerveného žiarenia a termovízie pri ochrane priestorov 
s vyššim pohybom osôb prípadne vonkajších priestorov budov. V práci analyzujem prípady použitia UV a IR spektier pri monitorovaní priestorov kamerou. 

V časti implementácie:
Pripojenie kamery k počítaču a zachýtávanie obrazu pomocou OpenCv
Detekcia narušiteľa priestoru 
Klasifikácia či je to človek a nie napriklad auto alebo zviera
Identifikácia človeka podľa tváre

## Infračervené kamery

Hlavné využitie je v podmienkách s nedostatočným prirodzeným osvetlením. Obyčajné kamery zobrazujú rôzne farby ktoré sú odrážané z objektov po dopade lúčov bieleho svetla. Toto nie je ale možné v noci, kedy ako jediný prirodzený svetelný zdroj je mesačné svetlo alebo umelé osvetlenie pomocou reflektorov. Infračervené svetlo je elektromagnetické žiarenie ktoré vyžaruje každý dosiaľ známy predmet, organizmus alebo vesmírny objekt.

Medzi kamerami ktoré mám k dispozíci, je napríklad ANNKE T200 ktorá podporuje zaznamenávanie termovízie a infračerveného žiarenia. Rozdiel medzi nimi je ten že IR využíva krátke vlny IR žiarenia na oslvetlenie prostredia. Termovízia využíva stredné a dlhé vlny IR a dokážu iba identifikovať teplotu, najčastejšie ako biela - teplo a čierna - zima. Výhoda oproti kátkym vlnám IR je tá že záznam nie je rušený odrazovaným svetlom.

# Články

## An Effective Surveillance System Using Thermal Camera [1]

V článku je predvedený postup zisťovania narušitela objektu. Postup je nasledovný:

- Nastavenie kamery na zachytávanie teploty v rozmädzí 30-40 C.
- Zachytávanie oobrázkov ve nekonečnom cykle
- Rozdelenie jednodtlivých obrázkov na časti o veľkosti m x n pričom všetky časti majú rovnaký počet pixlov
- Zadefinovanie matice pre každý región
- Zadefinovanie premennej Q ktorá bude prahovaá hodnota pre rozdiel medzi súčtami hodnôt R, G, B kanálov po sebe dvoch po sebe zaznamenaných obrázkov
- Zadefinovanie premennej h ktorá bude vyjadrovať početnosť pixlov ktorých rozdiel presiahol prah Q
- Zadefinovanie H ako minimálna hodnota h (počtu pixlov presahujúcich prah h)
- Porovnanie jednotlivých regionov aktuálneho obrázka a predošlého. Ak zmena medzi pixlami regiónov je väčšia ako prah tak sa zapíše 1 inač 0.
- Zadefinovanie F ktoré vyjadruje počet vertikálnych pixlov ktoré sú vedľa seba bez prerušenia a majú hodnotu 1. Ak sú viacere vertikálne množiný, zoberie sa číslo väčšej.
- Ako posledný krok sa nastaví prah G, ktorý ak presiahne F tak sa spustí alarm

Výsledky: 

Vo výsledkoch je zdôvodnené že prečo je rozmädzie snímaných teplot 30-40 C a nie 30-40, je to z dôvodu že osoba môže mať na sebé hrubé oblečenie vďaka ktorému môže mať nižšiu vonkajšiu teplotu. V prípade že by bolo nastavene príliš veľké rozmädzie, napríklad 20-40 C tak by vznikalo veľa falošných poplachov z dôvodu že 20 C je izbová teplota a slnečné svetlo a žiarenie z lámp je tiež snímané IR kamerami. 

Z testovaných 1000 obrázkov bolo úspešné identifikovanie prítomnosti narušiteľa 83.8%.

# Zdroje:

1. [https://ieeexplore.ieee.org/document/5163816](https://ieeexplore.ieee.org/document/5163816)
