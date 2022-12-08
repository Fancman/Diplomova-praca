# Diplomová práca - Využitie infračerveného žiarenia a termovízie na ochranu verejných priestorov a budov


Cieľom tejto diplomovej práce je preskúmať možnosti využitia infračerveného žiarenia a termovízie pri ochrane priestorov 
s vyššim pohybom osôb prípadne vonkajších priestorov budov. V práci analyzujem prípady použitia IR spektra a temovízie pri monitorovaní priestorov kamerou. 

## Infračervené kamery

Hlavné využitie je v podmienkách s nedostatočným prirodzeným osvetlením. Obyčajné kamery zobrazujú rôzne farby ktoré sú odrážané z objektov po dopade lúčov bieleho svetla. Toto nie je ale možné v noci, kedy ako jediný prirodzený svetelný zdroj je mesačné svetlo alebo umelé osvetlenie pomocou svietidiel. Infračervené svetlo je elektromagnetické žiarenie ktoré vyžaruje každý dosiaľ známy predmet, organizmus alebo vesmírny objekt.

Medzi kamerami ktoré mám k dispozíci, je napríklad ANNKE T200 ktorá podporuje zaznamenávanie termovízie a infračerveného žiarenia. Rozdiel medzi nimi je ten že IR využíva krátke vlny IR žiarenia na osvetlenie prostredia. Termovízia využíva stredné a dlhé vlny IR a dokážu iba identifikovať teplotu, najčastejšie ako biela - teplo a čierna - zima. Výhoda oproti kátkym vlnám IR je tá že záznam nie je rušený odrazovaným svetlom

# Postup 

Plán implementácie:

- Zachytávanie snímok pomocou OpenCV
- Vyskúšanie rôznych techník detekcie pohybujúcich sa objektov v zábere kamery
- Porovnanie Accuracy, Precision, vzdialeností, podmienok
- Klasifikácia či je to človek, a nie zviera alebo auto
- Detekcia tváre a uloženie na spracovanie


Pre jednotlivé kroky preskúmam existujúce riešenia a navrhnem také, ktoré sa bude najviac hodiť mojím potrebám. V sekcií "Članky" stručne popisujem techniky riešenia krokov z môjho plánu implementácie.

Naštudované članky:

[Seminárna práca 1](./seminarna_praca_1.md)

[Seminárna práca 2](./seminarna_praca_2.md)

[Prezentácia 2](./prezentacia_2.pdf)

[Návod na spustenie](./src/README.md)

Progres:

* 