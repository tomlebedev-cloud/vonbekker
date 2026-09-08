# Martynas Švėgžda von Bekkeris — svetainė

Trikalbis (LT / EN / DE) vieno puslapio pristatymas smuikininkui ir pedagogui
Martynui Švėgždai von Bekkeriui.

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

Visas tekstas gyvena viename JS objekte `body.part.html` faile — `C.lt`, `C.en`, `C.de`.
Trys kalbos turi vienodą struktūrą, tad keičiant reikia atnaujinti visas tris.

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
var CONTACT_EMAIL = "";   // gavėjo el. paštas
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

## Kaip publikuoti (GitHub Pages)

Įkėlus repozitoriją į GitHub: **Settings → Pages → Source: Deploy from a branch → `main` / `root`**.
Svetainė atsiras adresu `https://<vartotojas>.github.io/<repo>/`.

Norint prijungti `vonbekker.com` — pridėti `CNAME` failą su domenu ir nukreipti DNS į GitHub Pages.

## Ką dar verta padaryti

- **Didesnės nuotraukos.** Dabartinė iš PDF yra tik 339 px pločio — tinka portretui, bet ne plačiam vaizdui.
- **„Kišomprė“ konkursas Prancūzijoje** — reikia originalios prancūziškos rašybos.
  Šis pavadinimas neaptinkamas jokiame šaltinyje internete, tad rašyba nepatikrinta;
  svetainėje kol kas paliktas CV variantas. Šaltinyje pažymėta `TODO` (3 vietos — LT, EN, DE).
- ~~„Jaroslav Kozian“~~ → **Jaroslav Kocian** (Ústí nad Orlicí, Čekija) — ištaisyta, pridėtas miestas.
- **Nustatyti formos gavėją** — žr. „Užklausos forma“ aukščiau. Kol kas nenustatyta.
- **Atnaujinti CV** — šaltinis iš 2018 m.
- **Prancūzijos laikotarpis.** 2013 m. interviu Martynas mini šešerius metus Paryžiuje ir
  Prancūzijoje bei grįžimą į Lietuvą 2003 m. — CV to nėra. Verta įtraukti, kai bus patvirtinta.
- Repertuaras, įrašai, artimiausi koncertai — atskiros sekcijos, kai bus turinio.
