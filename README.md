# Martynas Švėgžda von Bekker — svetainė

Trikalbis (LT / EN / DE) vieno puslapio pristatymas smuikininkui ir pedagogui
Martynui Švėgždai von Bekker.

## Failai

| Failas | Paskirtis |
| --- | --- |
| `index.html` | **Publikuojama svetainė.** Savarankiškas failas — nuotrauka įdėta kaip data-URI, šriftai iš Google Fonts. Nereikia jokio serverio ar build'o. |
| `artifact.html` | Tas pats turinys peržiūrai Claude aplinkoje. Generuojamas automatiškai. |
| `body.part.html` | **Šaltinis, kurį redaguojame.** Visas turinys, stiliai ir vertimai. |
| `assets/martynas-portrait.jpg` | Portretas (339×511 px, ištrauktas iš CV PDF). |
| `build.py` | Sugeneruoja `index.html` ir `artifact.html` iš šaltinio. |
| `Compact-CV-2018.pdf` | Pirminis šaltinis. |

## Kaip keisti turinį

Visas tekstas gyvena viename JS objekte `body.part.html` faile — `C.lt`, `C.en`, `C.de`, `C.fr`.
Keturios kalbos turi vienodą struktūrą, tad keičiant reikia atnaujinti visas keturias.

Turinys sudėtas iš dviejų CV: lietuviško (2018) ir vokiško (`backup/Kurzer-Lebenslauf.pdf`),
kuris kur kas išsamesnis — iš jo paimta diskografija, Schnittke's premjera, salės,
festivaliai ir stipendijos.

Po redagavimo:

```bash
python3 build.py
```

## Užklausos forma

Puslapio apačioje — forma dviem srautams: **studijos / meistriškumo kursai** ir
**koncerto pasiūlymas**. Pasirinkus tikslą keičiasi žinutės laukelio užuomina,
o laiško tema atitinkamai pažymima, kad būtų galima rūšiuoti.
Yra paslėptas laukas prieš robotus ir laukų tikrinimas visomis trimis kalbomis.

Prieš publikuojant reikia nustatyti gavėją — `body.part.html` viršuje:

```js
var CONTACT_EMAIL = "svegzda.martynas@gmail.com";
var FORM_ENDPOINT = "";   // nebūtina, žr. žemiau
```

Yra du būdai, kaip užklausos pasieks pašto dėžutę:

**1. `mailto:` (paprasčiausias, be registracijų).** Užpildyk tik `CONTACT_EMAIL`.
Paspaudus mygtuką lankytojui atsidaro jo pašto programa su jau suformuotu laišku.
Trūkumas — dalis žmonių laiško taip ir neišsiunčia, o užklausos niekur nesikaupia.

**2. Formos servisas (patikimiau).** Susikūrus paskyrą, pvz. Formspree ar Getform,
įrašyti gautą adresą į `FORM_ENDPOINT`. Tada užklausos siunčiamos tiesiogiai,
lankytojas neišeina iš puslapio, o visos užklausos dar ir kaupiasi serviso skydelyje.
Paskyrą reikia susikurti pačiam — to padaryti negaliu.

Kol nė vienas nenustatytas, forma veikia ir tikrina laukus, bet vietoj siuntimo
parodo nustatymo priminimą.

## Publikavimas

Įjungta: **Settings → Pages → Deploy from a branch → `main` / `root`**.

Dabartinis adresas: **https://tomaslebedevas.photography/vonbekker/**

Adresas toks todėl, kad paskyros GitHub Pages naudoja individualų domeną
`tomaslebedevas.photography`, ir visi projektiniai puslapiai atsiduria po juo.

## Perkėlimas į vonbekker.com

**Prieš darant — įsidėmėti:** `vonbekker.com` šiuo metu veikia ir rodo į `79.98.24.4`
(DNS tvarko `ns1–ns4.serveriai.lt`). Nukreipus įrašus į GitHub, ten esanti svetainė
nustos rodytis. Verta pirma pasidaryti jos kopiją.

Taip pat: nustačius individualų domeną, dabartinis adresas
`tomaslebedevas.photography/vonbekker/` nustos veikti — GitHub ims nukreipinėti
į `vonbekker.com`. Todėl teisinga tvarka yra tokia:

**1. Suvesti DNS įrašus pas registratorių** (serveriai.lt valdymo skyde).

Šakniniam domenui `vonbekker.com` — keturi `A` įrašai:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

Ir, jei palaikoma, keturi `AAAA` įrašai (IPv6):

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

Pačiam `www` — vienas `CNAME` įrašas:

```
www  →  tomlebedev-cloud.github.io
```

Seni `A` įrašai, rodantys į `79.98.24.4`, turi būti pašalinti.

**2. Palaukti, kol įrašai pasklis** (nuo kelių minučių iki kelių valandų).
Patikrinti: `dig +short vonbekker.com` — turi rodyti GitHub adresus.

**3. Pridėti `CNAME` failą** į repozitorijos šaknį, jo turinys — viena eilutė:

```
vonbekker.com
```

Tai automatiškai nustato Custom domain GitHub nustatymuose.

**4. Įjungti Enforce HTTPS** (Settings → Pages). Mygtukas suaktyvėja tik tada,
kai GitHub išduoda sertifikatą naujam domenui — paprastai per 15 minučių–valandą.

## Ką dar verta padaryti

- **Didesnės nuotraukos.** Dabartinė iš PDF yra tik 339 px pločio — tinka portretui, bet ne plačiam vaizdui.
- **„Kišomprė“ konkursas Prancūzijoje** — reikia originalios prancūziškos rašybos.
  Šis pavadinimas neaptinkamas jokiame šaltinyje internete, tad rašyba nepatikrinta;
  svetainėje kol kas paliktas CV variantas. Šaltinyje pažymėta `TODO` (3 vietos — LT, EN, DE).
- ~~„Jaroslav Kozian“~~ → **Jaroslav Kocian** (Ústí nad Orlicí, Čekija) — ištaisyta, pridėtas miestas.
- **Formos servisas.** Šiuo metu veikia `mailto:`. Užsivedus Formspree ir įrašius adresą į
  `FORM_ENDPOINT`, užklausos ateitų tiesiai, be lankytojo pašto programos.
- **Atnaujinti CV** — šaltinis iš 2018 m.
- **Prancūzijos laikotarpis.** 2013 m. interviu Martynas mini šešerius metus Paryžiuje ir
  Prancūzijoje bei grįžimą į Lietuvą 2003 m. — CV to nėra. Verta įtraukti, kai bus patvirtinta.
- Repertuaras, įrašai, artimiausi koncertai — atskiros sekcijos, kai bus turinio.
