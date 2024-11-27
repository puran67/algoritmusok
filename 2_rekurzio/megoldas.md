# Megoldás

1. lépés: Ha a tömb egy elemből áll (**left == right**), akkor a maximum részösszeg maga az elem, mivel nincs más választási lehetőség.
2. lépés: Rekurzió
   - A tömböt két részre osztom középen:
      - Az első rész a **left**-től a **mid** indexig tart.
      - A második rész a **mid+1**-től a **right** indexig tart.
   - Meghívom a **max_subarray_sum** függvényt a bal majd a jobb oldali részre, ezzel kiszámítom a _bal_ és *jobb részösszeg*eket.
   - A _középső részösszeget_ külön kiszámolom, mivel a maximum lehet olyan részszakasz is, ami átnyúlik a két rész között. (**max_crossing_sum**)
   - Mikor eléri az alapesetet (_1. lépés_) akkor visszalép, a _három részösszeg_ közül a legnagyobbat adjom vissza.