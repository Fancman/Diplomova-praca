# Články

## An Infrared Array Sensor-Based Approach for Activity Detection, Combining Low-Cost Technology with Advanced Deep Learning Techniques [1]

V článku je predvedený postup rozpoznávania ľudských aktivít pomocou inračerveného senzora. Pripojený je na Raspberry Pi počítač a umiestnený je na strop miestnosti.
Senzor zachytáva viaceré rozlíšenia 24x32 12x16 a 6x8. Aktiviry ktoré je možné rozpoznať sú beh, chodenie, padanie, státie, ležanie a zmena aktivity.
Na zlpšenie presnosti detekcie sa použili techniky super resolution a denoising. Vďaka zväčšeniu rozlíšenia je detekcia viac citlivá na zmeny teploty a znižuje mieru rušenia. 
Následne sú data poslane do neuronovej siete ktorá zistí približné odhady aktivit a váhy. Výstup je nasledne poslaný do LSTM siete ktora prevedia robustnejšiu klasifikáciu aktivít. Z dúvodu použitia vlastnej architektury siete ktora nie je predtrenovana, majú nedostatok udajov v datasete a tak ich vygenerujú pomocou datovej augumentacie prostrednictvom siete typu CGAN (Conditional Generative Adversarial Networks )

FSRCNN -  Fast Super-Resolution Convolutional Neural Network - 1. extrakcia priznakov, 2. redukcia demenzií priznakov na zniženie vypočtovej naročnosti 3. nelineárne mapovanie príznakov na príznaky z vyššej dimenzie, je zodpovedná za vytvorenie dostatočného kontextu na rekonštrukciu obrazu s vysokým rozlíšením 4. expanzia dimenzí dát 4 dekonvolucia - opačna akcia konvolucie, vytvori presnešiu reprezentáciu dát z predošlej vrstvy 5. aktivačná funkcia PReLU odlišná od Relu kde je threshold 0 a tu je naučeny pri trenovani

Denoising - obnovenie obrazu do pôvodneho stavu, ktorý bol kontaminovaný prídavným šumom. Použitá sieť DIP ktora obnovuje štruktúru degradovaného obrazku, nie je nutný trenovaci dataset učí sa sama zisťovanim ze čo vytvára šum a obrazove body su uzitocne

LSTM - Long short-term memory - sa prevažne používajú na učenie, spracovanie a klasifikáciu sekvenčných údajov, pretože tieto siete sa dokážu naučiť dlhodobé závislosti medzi časovými krokmi údajov. Medzi bežné aplikácie LSTM patrí analýza nálad, modelovanie jazyka, rozpoznávanie reči a analýza videa

Výsledky: 

V tomto článku navrhli systém detekcie aktivity pomocou IR snímača s nízkym rozlíšením a pokročilých techník hlbokého učenia počítačového videnia. Pomocou jedného snímača umiestneného na strope uskutočnili rôzne experimenty v ktorých zbierali údaje za rôznych podmienok počas nepretržitého časového obdobia s rôznym rozlíšením (t. j. 24 × 32, 12 × 16 a 6 × 8). Na identifikáciu aktivity účastníkov spustili klasifikáciu, ktorá ako vstupné údaje berie snímky vytvorené snímačom a predpovedá aktivitu. Na ďalšie zlepšenie klasifikácie použili tri pokročilé techniky hlbokého učenia: SR, denoizáciu a CGAN. V tomto prípade bolo kľúčovým cieľom zvýšiť presnosť klasifikácie údajov s nízkym rozlíšením. Prostredníctvom výsledkov sme zistili, že aplikácia týchto techník pomohla zlepšiť presnosť klasifikácie obrazov s nízkym rozlíšením zo 78,32 % na 84,43 % (rozlíšenie 6 × 8) a z 90,11 % na 94,54 % (rozlíšenie 12 × 16).

## Automated Detection of Firearms and Knives in a CCTV Image [2]

Po analýze záznamov z CCTV kamier bolo zistené že majú prevažne nizke rozlišenie, zlú kvalitu kvôli rozmazavaniu, kompresii a lacným kamerám
Z toho plynie prva podmienka bay alogrimtus dokazal pracovat aj s datami ktore maju nizke rozlisenie. Druha podmienka bola aby boli falosne alarmy čo najmenej časté.

#### Detekcia noža 

Navrhli algoritmus detekcie nožov založený na vizuálnych deskriptoroch a strojovom učení. Na rozdiel od pôvodného posuvného okna hľadali nože len v blízkosti ľudskej siluety a  vtedy, keď sa na obrázku objaví aspoň jedna ľudská silueta. Okrem toho je detekcia noža držaného v ruke v obmedzenej časti obrazu rýchlejšia a navyše ruka držiaca nôž má viac charakteristických vizuálnych znakov ako nôž samotný, takže môžu očakávať lepšie výsledky. V obraze rozlíšili dve oblasti: jednu v blízkosti potenciálneho páchateľa a druhú v blízkosti potenciálnej obete. V týchto oblastiach môžu očakávať zobrazenie noža vzhľadom na všeobecnú dynamiku útoku nožom.

Kvôli špecifickým vzorom nožov použili dva descriptori na získanie príznakov a to hranovy histrogram a homogenne textury. Prvy ma informácie o rôznych hranách v obrázku, dokopy ich je 8 typov. Druhy popisuje specificke obrazove vzory ak su smer, drsnosť a pravidelnosť vzorov v obraze. Dva deskriptory poskytujú komplexné informácie o vlastnostiach charakteristických pre nože (hrana, vrchol a oceľový povrch čepele)

Na nájdenie najlepších parametrov pre SMV použili simple grid search algorithm s krížovoou validáciou.

#### Detekcia pištole 

Ako prvé je získanie pozadia a následne jeho odčítanie od ďalších snímkov. Na vžstup použili detektor hrán Canny ktorý prevedie obrázok na set htán a nasledne pomocou anlýzy posuvným oknom ktoré mení svoju veľkosť hľadá pištol v okolí siluety ruky.

#### Trénovacie a testovacie datasety

Dataset nozov bol získaný z CCTV záznamov, obrázky boli orezané na veľkosť 100x100px. Obsahuje dve triedy obrázkov: Pozitívne príklady - nôž je vidteľný v ruke, nož držaný v ruke je považovný za indikátor nebezpečenstva. Nôž ktorý nie je držaný v ruke považujú na menej nebzepečný
Negatívne príklady nôž nie je držaný v ruke

Dataset zbraní získali že natáčali herca pri fingovanej krádeži.

#### Výsledky - nôž

Príznaky z histogramu hrán mali lepšie výsledky pri dtekcií noža a to 81 accuracy, homogenne textury maly accuracy 52. Riešenie problému detekcie nožov sa zaoberá nízkou kvalitou a nízkym rozlíšením obrazu; to je dôležité vzhľadom na skutočnosť, že v živom vysielaní sa môže objaviť niekoľko video artefaktov aplikácií, ktoré ovplyvňujú detekciu osôb


#### Výsledky - pištol

Detekcia prebiehala na snímkoch z videí a nie je viditeľna celý čas, miestami je skrytá. nameraná bola až 99 uspečnosť pri true positive ale bolo zachytených aj približne 50 falošných alarmov.

## Automatic Detection of Knives in Complex Scenes [3]

Po preskúmaní vyzdvihli to že vznikajú problemy pri detekcií nožov z dôvodu že majú rôzne tvary, vzhľady, veľkosti a podmienky osvetlenia ktoré často negatívne ovplyňujú výsledky.
Popisujú sieť YOLO ktorá je jednúrovňová a je určená na detekciu objektov v obraze. Je rýchlejsiša ako dôjstupnove siete ale na úkor presnosti. Tradične je natrénovaná na COCO datasete ktorý obsahuje bežné objekty ako triedy.

Výsledky detekcie závisia od kvality vstupných údajov. Uvádzajú ako problém že je málo verejne dostupných datasetov z CCTV kamier. Použili DaSCI knives dataset ktorý je súčasťou ineho datasetu obsahujuceho zbrane. Nože sú na nich umiestené v rôznych scénach, sú rôznych typov, pričom na neiktorych obrázkoch sú aj viaceré. Ako problém uvádzaju to že nože zaberajú malý priestor pomerom na veľkosť obrázka. Ako druhy dataset použili MS COCO ktorý obsahuje aj nože

#### Processing

Yolo sieť prijíma obrázky veľkosti 416x16 a preto museli byť obrázky v datasetoch zmenené na túto veľkosť. Ako prvú metódu na zmenu veľkosti použili bilineárnu interpoláciu. Počíta nové interpalačné body na zaklade na základe váženého priemeru ich okolitých bodov (štyri v pôvodnom obraze). Váha priradená každému susednému bodu je na základe jeho vzdialenosti od nového bodu. Následne je hodnota nového bodu ovplyvnená najmä hodnotami bližších susedov.

Druhá metóda je SRGAN sieť s učiteľom, používa generatívnu sieť na vytvorenie obrázkov s väčším rozlíšením aby boli podobné originálnym  obrázkom. Diskriminativna siet rozhoduje o tom ci vysledny obrazok vyzera ako pravy alebo ako falosny. SRGAN bola natrenovana na ImageNet datasete.

Obrázky v dataset su v rôznych prostrediach a to: vonku kde je výraznejšie osvetlenie, vnútri kde je slabšie osvetlenie, nôž je čiastočne skryty, nôž je plne viditeľný.

#### Transfer learning

Pouťitý bol transfer learning čo ja použitie zamrazených váh po naučení z ineho datasetu a následne účenie na nami dodanými datami a triedami. V tomto pripade použili dataset Pascal VOC ktorý ale neobsahuje triedu nožov.

#### Vysledky

Vykonali 4 merania a to kombinacie ci bol pouzity transfer learning alebo nebol pouzity a dva typu preprocessingu. Najlepšie výsledky namerali pri nepouzity transfer learningu a ako preprocesing ked bol pouzity SRGAN

Výsledky ukázali, že použitie algoritmu predspracovania superrozlíšenia podporuje lepšie výsledky len vtedy, ak nie je v kombinácii s prenosovým učením. Okrem toho použitie navrhovaného transferového učenia techniky znížilo celkový výkon našich modelov YOLOv4.

# Zdroje:

1. [An Infrared Array Sensor-Based Approach for Activity Detection, Combining Low-Cost Technology with Advanced Deep Learning Techniques](https://www.mdpi.com/1424-8220/22/10/3898)
2. [Automated Detection of Firearms and Knives in a CCTV Image](https://www.mdpi.com/1424-8220/16/1/47)
3. [Automatic Detection of Knives in Complex Scenes](https://www.researchgate.net/publication/363407966_Automatic_Detection_of_Knives_in_Complex_Scenes)
