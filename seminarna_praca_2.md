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

## Thermal Imaging Dataset for Person Detection [3]

Článok popisuje vytváranie datasetu obrázkov za realistického počasia. Expiremnet bol vykonávaný vždy v noci, za pekného počasia, hmly a počas silného dažďa. Ľudia na fotkách napodobňovali ľudí, ktorý sa úmyselne snažia dostať na monitorované územie bez autorizácie, teda v rôznych vzdialenostiach od kamery, rôznymi rýchlosťami a pozíciami tela ako sú plazenie po rukách a nohách, skrývanie sa, zhrbená chôdza a behanie. 

#### Snímanie za pekného počasia

Prebehlo na lúke s malým lesíkom, čiže bolo možné vyskúšať záznamenávanie ľudí ako sa schvávajú z kríkmi a stromami. Lokalita v zábere má približne 180m na šírku a teplota bolo približne 2 C. Testovaná bola vzdialenosť 110 až 165m pričom sa používali dva typy šošoviek, jedna obučajná a jedná určná na vytváranie sústredených dialkových fotiek. Keď sa postavy vzďalovali od kamery do vzdialenosti 165m tak ich nebolo možné vidieť ľudským zrakom ani pomoocu obyčajných šošoviek. Na všetkých zachytených fotografiach je vidieť obrysy ľudí.

#### Snímanie za hmly

Vzhľadom na vysokú hustotu čiastočiek vody vo vzduchu sú dlhé vlny IR (LWIR) vysoko rozptýlené, čiže viditeľnosť pomocou termovízie je značne obmedzená. V tomto počasí bolo možné zachytiť obrysy človeka len do 30m obyčajnou šošovkou ad do 50m diaľkovou.

#### Snímanie za ťažkého dažďa

Pri snímaní sa vyskúšali vzdialenosti rovnaké ako pri peknom počasí a to 30, 70, 110, 140, 170, 180 a 215m a vo vštkých pózach ako pri preknom počasí. Pri vzdialenosti 215m bolo možné zachytiť obrysy človeka iba ďialkovými šošovkami.

### Spracovanie údajov

Po natáčaní a preprocessingu bolo získaných 20 minút za pekného počasia, 13 minút hmly a 15 minút ťažkého dažďa. Videa bolo postrihané a rozdelené podľa predefinovaných scenárov. Následná bola extrakcia snímkov pomocou Matlabu. Výsledkom bolo 11900 snímkov o veľkosti 1280x960 pre pekné počasie, 4905 hmlu a 7030 pre ťažký dažď. Následne sa rerezentatívne snímky pooznačovali anotáciami podľa rôznych aktivít, z rôzných vzdialenosti a rôzneho počasia. Výsledných bolo 7412 anotovaných snímkov.

Na anotácie bol použitý program Yolo BBox Annotation Tool kde sa postavy dajú ohraničovať pomocou bounding boxu a je spomenuté že výber programu na vytváranie anotácií záleží od metódy ktorá bude použitá na trénovanie modelu. Kontkrétne tento program podpruje YOLO, VOC, a MSCOCO formáty.

## Real-Time Human Detection with Thermal Camera Feed using YOLOv3 [4]

V tomto článku je predstavená implementácia algoritmu YOLOv3 na presnú detekciu ľudského tela v reálnom čase a podmienkých kedy obyčajná kamera určená pre viditeľné svetlo zlyháva. Na trénovanie a testovanie bolo použitých 47650 termálnych snímkov. Počas experimentov bolo možné identifikovať človeka už za 17 milisekúnd a precision 95.5%.

Spomínané sú spôsoby detekcie osôb pomocou klasifikácie na základe príznkov ktoré sú zadefinované človekom a to (Histogram of Oriented Gradients) HoG ktorý bol spomenutý v prvom článku, Aggregated Channel Features (ACF) a Integral Channel Features (ICF) ktorú sú spomenuté ako najpopulárnejšie spôsoby klasifikácie. 

Ďalej sú spomenuté klasifikácie pomocou CNN.  Region Proposal Network (RPN) s predtrénovanými váhami z ImageNet datasetu a potrebuje ako vstup termálny snímok a obyčajný. YOLOv2 ktorá používa 4 kanály RGB+T (T ako thermal).  Spomínané je spojenie snímku s viditeľným svetlom a termo snímku využité ResNet-152 ktoré využíva encoder a decoder. Zvyčajne sú rýchlejšie jedno prechodové detekčné techniky z ktorých sú najpopulárnejšie SSD a YOLO. YOLOv3 ma podobný výkon ako DSSD pričom DSSD he 3x rýchlejšie ako SSD. YOLOv3 má lepšiu "precision" pre menšie objekty ako technológie s dvoma prechodovými stupňami ktor= vyuýívajú regresiu, ResNET. FPN, G-RMI a TDM.

Preto si vybrali YOLOv3 vzhľadom k tomu že využíva RGB obrázky, a má vyrovnáný kompromismedzi presnosťou a rýchlosťou.

### YOLO detektor

Je vhodný na použitie v reálnom čase a pri potrebé nízkej straty na presnosti. Algorimtus detekuje lokality s objektami spolu s zaradením do triedy. Snimka je rozdelená na menšie časti a pre každú sú vyhladané objekty a klasifikujú sa do tried spolu s výpočtom confidence score. YOLOv3 je vylepšená verzia YOLOv2 a má 53 vrstiev, 3x3 a 1x1 filtre trénovaná je na ImageNet datasete. Bounding box prediction je vylepšená aplikovaním 1x1 kernelov on troch odlišných miestách v sieti pre detekciu.Klasifikácia je vykonávaná pomocou logistickej regressie.

Z 95 000 obrázkov sa vybral subset so 742 snímkov s ľudmi ktoré sú zozbierané preskakovaním 20 snímkov pre tréning spolu s 30 snímkov s chodcami. Postavy boli pooznačované bounding boxami s programom LabelImg.

#### Tréning

Na vyriešenie toho že CNN potrebuje na natrénovanie a väčšie datasety ako Microsoft COCO, Caltech, ImageNet nemajú veľké množstvo snímok zachytených termo kamerou. Používa preto predtrénované vahy podľa COCO a je dodatočne dotrénovaná pomocou "Transfer learning"-u čo znamená že posledné vrstvy v CNN modeli natrénujeme datasetom nasších obrázkov. Myšlienka je za tym taká že nižšie vrstvy aj tak využívajú iba low level príznaky ktoré sú spoločné naprieč datasetmi. 

V tomto prípade sa zoberú váhy po natrénovaní pre triedu "human" po 1000 iteráciach a model sa odtestuje. Pre model by mala optimálne vyjsť "loss" menšia 2.

#### Výsledky

Detekcia je vykonaná v reálnom čase s použitím GPU trvá 17ms a pomocou CPU 7-8 sekúnd. "Average precision" vyšla 95.15% V porovnaní o ostatnými technikami sa rapídne znížil missrate.

![image](https://user-images.githubusercontent.com/5480663/167900624-87a4a989-df01-4a15-8344-3126c10410ea.png)

## Thermal Imaging Dataset for Person Detection [5]

Algoritmus na hľadanie tváre používa OpenCV knižnicu spolu s knižnicou mpi4py ktorá umožnuje používať paralelizmus. Ako vžpočtové zdroje boli použité 4 Dell servery, každý s 12 GB RAM. Aplikácia má detekovať tvár v reálnom čase.

### Dataset

Snímky postavy su zaznamenané v rôznych vzdialenostiach od kamery, dokopy ich je 500. Pozadie je homogenne s nízkou teplotou. Postup je modifikovaná verzia od in=ho výskumníka ktorá funguje tak že sa nájde hlava, krk, najviac vpravo a najviac vľavo bod.

Algorimtus je rozdelený do troch častí: preprocesing, výpočet koordinácií pre extrakciu príkazov a vykreslenie stvorca okolo tváre.

#### Preprocesing 

- Vstup je obrázok s RGB kanálmi
- R kanál je odstránený a vznikne 2D matica
- Obrázok je skonvertovaný na čierno biely pomocou techniky zvanej thresholding
- Použijú sa filtre s morfologickými operáciami ako je otváranie a zatváranie. Sú použité kvôli vyostreniu hrán
- Hranice objektu su nájdené a uložené

#### Výpočet koordinácií pre extrakciu príznakov

- Zistenie počtu dôležitých pixelov v každom riadku alebo stĺpci
- Headpoint (bod od ktorého začína hlava) sa hľadá postupným prechádzaním riadkov binárnej verzie obrázka a v prvom kde narazí na 1 je headpoint
- Spraví sa histogram vertikálných pozícií pixlov a akumulované intenzity pixelov 
- Náhla zmena vo vertikálnych intenzitách pixelov znamená že sme narazili na miesto kde sa hlava stretáva s ramenami - krk
- Najviac pravý bod a najviac lavý bod sa nachádza medzi head point a neck point. Oba body sú na hrane ohraničujúceho obdĺžnika
- Pomocou euklidovskej vzdialenosti sú vypočítané ďalšie body ohraničujúceho obžnika

Výsledky:

Hľadanie ohraničenia tváre trvalo priemerne 20 sekúnd.


# Zdroje:

1. [An Effective Surveillance System Using Thermal Camera](https://ieeexplore.ieee.org/document/5163816)
2. [Human Detection for Night Surveillance using Adaptive Background Subtracted Image](https://arxiv.org/ftp/arxiv/papers/1709/1709.09389.pdf)
3. [Thermal Imaging Dataset for Person Detection](https://ieeexplore.ieee.org/document/8757208)
4. [Real-Time Human Detection with Thermal Camera Feed using YOLOv3](https://ieeexplore.ieee.org/document/9342089)
5. [Detection of Human Face by Thermal Infrared Camera Using MPI model and Feature Extraction Method](https://ieeexplore.ieee.org/document/8777581)


Transfer learning - https://towardsdatascience.com/transfer-learning-with-convolutional-neural-networks-in-pytorch-dd09190245ce
