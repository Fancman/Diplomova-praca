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
