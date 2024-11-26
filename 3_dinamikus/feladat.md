# Feladat

Tekintsünk egy n érméből álló pénzrendszert. Minden érmének pozitív egész értéke van. 
Számítsa ki, hány különböző rendezett módon lehet előállítani egy x pénzösszeget a rendelkezésre álló érmék felhasználásával.

Például, ha az érmék {2,3,5}, és a kívánt összeg 9, akkor 3 módja van:
 - 2+2+5
 - 3+3+3
 - 2+2+2+3

### Bemenet
1. sor: Két **n** és **x** egész szám van: az érmék száma és a kívánt pénzösszeg.
2. sor: **n** különböző egész számot tartalmaz c<sub>1</sub>,c<sub>2</sub>,...,c<sub>n</sub>: az egyes érmék értéke.

### Kimenet
Egy egész szám nyomtatása: a módok száma modulo 10<sup>9</sup>+7.