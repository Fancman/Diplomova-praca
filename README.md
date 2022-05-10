# Diplomová práca - Využitie infračerveného žiarenia a termovízie na ochranu verejných priestorov a budov


Cieľom tejto diplomovej práce je preskúmať možnosti využitia infračerveného žiarenia a termovízie pri ochrane priestorov 
s vyššim pohybom osôb prípadne vonkajších priestorov budov. V práci analyzujem prípady použitia IR spektra a temovízie pri monitorovaní priestorov kamerou. 

## Infračervené kamery

Hlavné využitie je v podmienkách s nedostatočným prirodzeným osvetlením. Obyčajné kamery zobrazujú rôzne farby ktoré sú odrážané z objektov po dopade lúčov bieleho svetla. Toto nie je ale možné v noci, kedy ako jediný prirodzený svetelný zdroj je mesačné svetlo alebo umelé osvetlenie pomocou svietidiel. Infračervené svetlo je elektromagnetické žiarenie ktoré vyžaruje každý dosiaľ známy predmet, organizmus alebo vesmírny objekt.

Medzi kamerami ktoré mám k dispozíci, je napríklad ANNKE T200 ktorá podporuje zaznamenávanie termovízie a infračerveného žiarenia. Rozdiel medzi nimi je ten že IR využíva krátke vlny IR žiarenia na oslvetlenie prostredia. Termovízia využíva stredné a dlhé vlny IR a dokážu iba identifikovať teplotu, najčastejšie ako biela - teplo a čierna - zima. Výhoda oproti kátkym vlnám IR je tá že záznam nie je rušený odrazovaným svetlom

# Postup 

Plán implementácie:
- Pripojenie kamery k počítaču a zachytávanie obrazu pomocou OpenCV
- Detekcia narušiteľa priestoru (jeden človek, skupinka ľudí)
- Klasifikácia či je to človek a nie napriklad auto alebo zviera
- Identifikácia človeka podľa tváre

Pre jednotlivé kroky preskúmam existujúce riešenia a navrhnem také, ktoré sa bude najviac hodiť mojím potrebám. V sekcií "Članky" stručne popisujem techniky riešenia krokov z môjho plánu implementácie.

# Články

## An Effective Surveillance System Using Thermal Camera [1]

V článku je predvedený postup zisťovania narušitela objektu. Postup je nasledovný:

- Nastavenie kamery na zachytávanie teploty v rozmädzí 30-40 C.
- Zachytávanie obrázkov ve nekonečnom cykle
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

## Human Detection for Night Surveillance using Adaptive Background Subtracted Image [2]

Navrhnutá metóda využíva nas spracovanie obrázkov HOG (Histogram of Oriented Gradients) čo je technika na extrahovanie príznakov z obrázku. Táto technika je obohatená o adaptívnu extrakciu pozadia. Takto sa nám podarí zredukovať čas spracovania obrázkov a zlepší sa aj presnosť vyhodnocovania. 

V úvode je uvedené že v čase písania článku existovalo málo spôsobov detekcie ľudí v tme. Tie čo existovali buď využívali termovíziu alebo kombináciu termokamery a normalnej kamery na zaznamenávanie denného svetla.

HoG má svoje limitácie a to dlhý čas spracovávania, má vysoký "recall" a nízku "precision". "Precision" je pomer medzi inštanciami ktoré boli správne klasifikované v pozitívnej triede a celkový počet inštancií klasifikovaných v pozitívnej triede. 

    Precision = TruePositive / (TruePositive + FalsePositive)
    
"Recall" vyjadruje ako veľmi sa dá veriť že klasifikátor našiel všetkých členov pozitívnej triedy. 

    Recall = TruePositive / (TruePositive + FalseNegative)
    
Popis navrhovanej metódy pri statickej kamere:

- Zaznamená sa obrázok bez postáv
- Následne je toto pozadie odpočítané pd každého záberu zaznamenaného kamerov
- Výsledok po odčítaní sa spojí s pôvodnou fotografiou z kamery
- Prebehne extrakcia príznakov pomocou HoG
- Príznaky sú odoslané do natrénovaného SVM koré má ako výstup maticu predpovedí

Popis navrhovanej metódy pri dynamickej kamere:

V tomto prípade treba riešiť to že sa pozadie stále mení pri pohybe kamery. V článku je postup rozdelený na dve časti:

### Detekcia vektora posunu

- Záber kamery musí obsahovať objekt ktorý je dostatočne odlíšiteľný od susedných bodov a je statický 
- Objekt by sa mal nachádzať v strede záberu kamery
- Po otočení kamery na ďalšiu pozíciu sa hľadá statický objekt pomocou okna o veľkosti objektu
- Po odčítani x, y bodov pôvodného obrázku a obrázku posunutého pri hľadaní objektu dostaneme vektor posunu
- Získame vektor rozdielov (vzdialenosť a uhol posunu)

### Posun pozadia

Pozadie posunieme pomocou získaného vektora posunu.

Vo výsledkoch je zaznamenaný čas potrebný na spracovanie framu, "precision" a "recall". Testovaný bol samostatný HoG a HoG spolu s extrahovaním pozadia. Recall bol vždy 100%, čiže vždy ak je na zázname človek tak sa záznamená jeho prítomnosť v zábere. "Precision" dosiahla 83% pre statickú kameru a 76% pre dynamickú čo znamená 17% a 24% falošných poplachov keď bola klasifikovaná prítomnosť človeka aj keď na zábere nebol.

Čas spracovania záberú je pri samotnom HoG 1768.29s, HoG s "background subtraction" 23.0047s a pri dynamickej kamere 631.0068s iba s background suntraction a 478.0096 s "adaptive background suntraction"



# Zdroje:

1. [https://ieeexplore.ieee.org/document/5163816](https://ieeexplore.ieee.org/document/5163816)
2. [https://arxiv.org/ftp/arxiv/papers/1709/1709.09389.pdf](https://arxiv.org/ftp/arxiv/papers/1709/1709.09389.pdf)
