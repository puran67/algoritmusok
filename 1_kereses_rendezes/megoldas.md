# Megoldás

1. Összegyűjtöm egy listába a városokat és a felhőket, hogy minden adat egy helyen legyen, ne kelljen többször is végigmenni több listán. Tárolom a városok pozícióját, népességét és indexét, valamint a felhők kezdőpontját és indexét majd a felhő végpontját és a felhő indexét.
2. Sorbarendezem a listát a pozíciók szerint.
3. Végigmegyek a listán:
   - létrehozok egy listát (**cloud_population**), ami tartalmazza majd, hogy ha azt a felhőt távolítjuk el, az mekkora népességet "szabadít fel"
   - létrehozok egy halmazt (**active_clouds**), ami tartalmazza, hogy éppen hány felhő alatt "állok"
   - ha felhő kezdő pozíciójához (_"cloud_start"_) érek, akkor hozzáadom a felhőket tartalmazó halmazhoz a felhő indexét
   - mikor városhoz (_"town"_) érek megnézem, hogy hány felhő takarja
     - ha nem takarja felhő: hozzáadom a már napos népességhez (**sunny_population**)
     - ha 1 felhő takarja: hozzáadom a felhő által takart népességhez (**cloud_population**)
     - ha több felhő takarja: nem csinálok semmit, mert csak egy felhőt tudok eltávolítani
   - ha felhő vég pozíciójához (_"cloud_end"_) érek, akkor eltávolítom a felhőket tartalmazó halmazból a felhőt
4. Megkeresem azt a felhőt, amit eltávolítva a legtöbb embert "szabadítok fel" (**max(cloud_population)**) majd ehhez hozzáadom a már napsütéses népességhez (**sunny_population**).