# Megoldás

1. lépés: Létrehozok egy listát (**db**), ahol **db[i]** azokat a lehetséges módokat tárolja, ahogyan az **i** összeg kifizethető a rendelkezésre álló érmékkel. _(A dp[0] legyen 1, mivel egy módon lehet elérni a 0 összegú pénzt úgy, hogy nem fizetünk semmit.)_
2. lépés: Minden érmét végigveszünk. Ha egy _coin_ értékű érmét hozzáadunk egy már elért összeghez (**i**), akkor az új összeg (**i + coin**) is elérhető. Azaz, ha **dp[i]** módon lehet elérni **i** összeget, akkor **dp[i + coin]**-ot növeljük d**p[i]** értékével. Mivel ez nagy számokat is eredményezhet, minden lépésnél az értékeket modulo 10<sup>9</sup>+7 vesszük.
3. lépés: Visszaadjuk a kívánt összeg elérhetőségének módjait: **db[x]**