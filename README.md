# Martynas Švėgžda von Bekkeris — svetainė

Trikalbis (LT / EN / DE) vieno puslapio pristatymas smuikininkui ir pedagogui
Martynui Švėgždai von Bekkeriui.

## Failai

| Failas | Paskirtis |
| --- | --- |
| `index.html` | **Publikuojama svetainė.** Savarankiškas failas — nuotrauka įdėta kaip data-URI, šriftai iš Google Fonts. Nereikia jokio serverio ar build'o. |
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

## Kaip publikuoti (GitHub Pages)

Įkėlus repozitoriją į GitHub: **Settings → Pages → Source: Deploy from a branch → `main` / `root`**.
Svetainė atsiras adresu `https://<vartotojas>.github.io/<repo>/`.

Norint prijungti `vonbekker.com` — pridėti `CNAME` failą su domenu ir nukreipti DNS į GitHub Pages.

## Ką dar verta padaryti

- **Didesnės nuotraukos.** Dabartinė iš PDF yra tik 339 px pločio — tinka portretui, bet ne plačiam vaizdui.
- **Patikslinti du pavadinimus** (žr. CV): „Kišomprė“ konkursas Prancūzijoje (originali prancūziška rašyba)
  ir „Jaroslav Kozian“ — greičiausiai Jaroslav **Kocian** konkursas Čekijoje. Svetainėje kol kas naudojama „Kocian“.
- **Atnaujinti CV** — šaltinis iš 2018 m.
- Repertuaras, įrašai, artimiausi koncertai — atskiros sekcijos, kai bus turinio.
