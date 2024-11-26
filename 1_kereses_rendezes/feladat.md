# Feladat

A kolumbiai Quibdó azon városok közé tartozik, ahol a legtöbb csapadék esik a világon.
Egész évben felhők borítják a várost. A városnak sok városa van, amelyek egydimenziós vonalon helyezkednek el. Az egyes városok helyzetét és lakosságát a számegyenesen ismeri. Minden felhő lefedi az összes várost, amelyek bizonyos távolságra vannak tőle. Egy városról azt mondják, hogy sötétben van, ha létezik legalább egy felhő, így a város a felhő hatókörén belül van. Egyébként állítólag süt a nap.

A városi tanács megállapította, hogy van elég pénzük pontosan egy felhő eltávolítására a legújabb technológiájukkal. Így akarják eltávolítani a felhőt úgy, hogy a legkevesebb ember maradjon sötétben a felhő eltávolítása után. Legfeljebb hány ember tartózkodhat egy napsütötte városban pontosan egy felhő eltávolítása után?

*Megjegyzés: Ha egy várost nem takar felhő, akkor már naposnak számít, és a végső válaszban ennek a városnak a lakosságát is bele kell számítani.*

### Beviteli formátum:
   1. sor: egyetlen egész számot tartalmaz, a városok számát
   2. sor: szóközzel elválasztott egész számokat tartalmaz. Az ebben a sorban szereplő egész szám a város lakosságát jelöli
   3. sor: szóközzel elválasztott egész számokat tartalmaz, amelyek a város helyét jelölik az egydimenziós egyenesen
   4. sor: egyetlen egész számból áll, amely a várost borító felhők számát jelöli
   5. sor: szóközzel elválasztott egész számokat tartalmaz, amelyek a felhő elhelyezkedését jelölik a koordinátatengelyen
   6. sor: szóközzel elválasztott egész számokból áll, amelyek a felhő tartományát jelölik

*Megjegyzés: Az egyes felhők hatótávolságát a helyük szerint számítják ki, azaz a felhő a pozíciójában helyezkedik el, és minden tőle távolabb eső várost lefed. Más szóval, a felhő minden olyan várost beborít, amely a tartományban található.*

### Kimeneti formátum
Nyomtasson ki egy egész számot, amely jelöli a napfényes városban tartózkodó emberek maximális számát úgy, hogy pontosan egy felhőt távolít el.