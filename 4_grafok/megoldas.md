# Megoldás

1. Gráf felépítése:
    - A bemeneti adatok alapján két gráfot építünk: a normál gráfot (**graph**) és a fordított gráfot (**reverse_graph**).
    - **graph[a]** egy listát tartalmaz, amely az a szobából kiinduló alagutakat tárolja. (Minden alagutat a célja (**b**) és a súlya (**x**) **(b, x)** párosaként tároljuk.)
    - A **reverse_graph[b]** az alagutak fordított irányú változatait tartalmazza, hogy a visszafelé történő elérhetőséget is ellenőrizhessük.
2. lépés: _Bellman-Ford_ algoritmus használata
   - A **dist** lista tartalmazza az összes szoba pontszámát: **dist[i]** a legnagyobb pontszámot jelenti az **i** szobából elérve.
   - Kezdetben a **dist[1] = 0**, hiszen az 1-es szobából indulunk, a többi szoba pontszámát pedig -∞-re (vagyis elérhetetlen) állítjuk be.
   - Minden iterációban a gráf minden élét (a **graph[a]** listán keresztül) végigjárjuk, és ha a **dist[a] + x > dist[b]**, akkor frissítjük **dist[b]**-t.
3. lépés:  A Bellman-Ford algoritmus befejezése után egy extra lépést végzünk, hogy azokat a csúcsokat (**in_cycle**) megjelöljük, amelyek elérhetők egy pozitív ciklussal.
   - Ha egy csúcs pontszámát a végén még tovább lehet növelni, akkor ez azt jelzi, hogy a csúcs pozitív ciklus része.
   - Ezt a ciklust az **in_cycle** lista (_True_ vagy _False_) értékeivel jelöljük.
4. lépés: A **reachable(start, targets, graph)** függvénnyel ellenőrizzük, hogy a pozitív ciklusban érintett szobák elérhetők-e az 1-es szobából (**graph**), illetve visszafelé is elérhetők-e az _n_-es szobából (**reverse_graph**).
   - Ha bármelyik pozitív ciklusban lévő szoba nem elérhető az 1-es szobából, vagy nem vezet vissza az _n_-es szobába, akkor nem érhetünk el végtelen pontszámot.
5. lépés: Eredmény
   - Ha van elérhető pozitív ciklus, akkor a válasz -1, mivel végtelen pontszámot lehetne elérni.
   - Ha nincs, akkor a **dist[n]** értékét adjuk vissza, amely a legnagyobb pontszámot jelenti az _n_-es szobából elérve.