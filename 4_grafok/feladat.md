# Feladat
A játék n szobából és m alagútból áll. A kezdeti pontszám 0, és minden alagút x-szel növeli a pontszámot, ahol x lehet pozitív vagy negatív is. Egy alagúton többször is át lehet menni.
Az a feladat, hogy az 1-es szobából az n-es szobába sétáljon. Mennyi a maximális pontszám, amit kaphat?

### Bemenet
1. sor: Két n és m egész szám van: a szobák és az alagutak száma. A szobák számozása 1,2,...,n.

Ezután m sor írja le az alagutakat. Minden sor három a, b és x egész számot tartalmaz: az alagút az a helyiségben kezdődik, a b szobában ér véget, és x-szel növeli a pontszámot. Minden alagút egyirányú alagút.
Feltételezheti, hogy az 1-es szobából az n-es szobába el lehet jutni.

### Kimenet
Nyomtasson egy egész számot: a maximális pontszámot, amit kaphat. Ha azonban tetszőlegesen nagy pontszámot tud elérni, nyomtasson -1-et.