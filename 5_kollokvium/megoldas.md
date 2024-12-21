# Megoldás

A megoldás során _KMP_ algoritmus használatával keresünk egy mintát egy szövegben.

1. Bemenet feldolgozása:
    - Mivel több tesztesetet kell kezelni, a bemeneti adatokat egyszerre olvassuk be a standard bemenetről. Az adatokat soronként dolgozzuk fel.
    - Minden teszteset három sorból áll:
      - Az első sorban a minta (**needle**) hosszát olvassuk be (bár ezt nem használjuk közvetlenül, de a bemenet struktúrájában szükséges).
      - A második sorban található a keresett minta (**needle**).
      - A harmadik sorban található a szöveg (**haystack**), amiben keresünk. 
    - Mivel több teszteset is lehet, a bemenetet egy ciklusban dolgozzuk fel, és minden teszteset után kiírjuk a megfelelő eredményt.
2. lépés: Prefix függvény kiszámítása
   - A **compute_prefix_function** függvény lépései:
     - Kezdetben a prefix függvény minden értékét nullára állítjuk.
     - A mintában végigiterálunk, és minden karakterhez kiszámítjuk, hogy a korábbi karakterek közül melyek alkotnak olyan prefixet, ami megegyezik a minta egy részével.
     - Az így kapott prefix függvény segíti majd a keresést.
3. lépés:  A minta keresése a szövegben
   - A **kmp_search** függvény lépései:
     - Kezdjük a szöveg első karakterével, és a minta karaktereivel próbálunk egyezést találni.
     - Ha találunk egy egyezést, tovább lépünk, és ha a teljes mintát megtaláljuk, hozzáadjuk az aktuális pozíciót a találatok listájához.
     - Ha nem találunk egyezést, a prefix függvény segítségével megtudjuk, hogy hová ugorjunk a mintában, és folytatjuk a keresést anélkül, hogy újra ellenőriznénk már biztosan nem egyező karaktereket.
     - Az összes találatot tároljuk a matches listában.
4. lépés:  Eredmények kiírása
   - Minden tesztesethez kiírjuk a minta előfordulásainak kezdőpozícióit.
     - Ha találtunk előfordulásokat, kiírjuk azok kezdőpozícióit.
     - Ha nem találtunk előfordulást, akkor semmi sem kerül kiírásra, de az egyes tesztesetek között üres sorokat hagyunk.