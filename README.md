# Cheat Sheet – Git og GitHub for Gruppe 14

## Arbeidsflyt: Slik gjør du det hver gang

### 1. Oppdater main og lag ny branch

```bash
git checkout main
git pull origin main
git checkout -b navn-på-ny-del
```

### 2. Skriv i VSCode og lagre

Bruk `Cmd + S` (Mac) eller `Ctrl + S` (Windows).

### 3. Commit og push

```bash
git add .
git commit -m "Beskrivelse av hva du la til"
git push -u origin navn-på-ny-del
```

`-u origin navn-på-ny-del` trenger du bare første gang for en ny branch. Etter det holder det med `git push`.

### 4. Lag pull request på GitHub

- Gå til repoet på github.com
- Klikk **Compare & pull request** på repo-siden (gul boks øverst)
- Skriv en kort beskrivelse
- Legg til en reviewer fra gruppen
- Klikk **Create pull request**

### 5. Reviewer godkjenner

- Fanen **Pull requests** → åpne PR-en
- Klikk **Files changed** for å se endringer
- Klikk **Review changes** → skriv kommentar → velg **Approve** → **Submit review**

### 6. Merge til main

- Klikk **Merge pull request**
- Klikk **Confirm merge**
- Klikk **Delete branch** for å rydde opp

### 7. Alle henter oppdatert main

```bash
git checkout main
git pull origin main
```

---

## Nyttige Git-kommandoer

| Kommando | Hva den gjør |
|----------|--------------|
| `git status` | Viser hva som er endret og hvilken branch du er på |
| `git branch` | Lister alle lokale brancher (stjernen viser hvor du er) |
| `git log --oneline` | Viser commit-historikk kort og oversiktlig |
| `git checkout <branch>` | Bytter til en annen branch |
| `git pull` | Henter siste endringer fra GitHub |
| `git add .` | Legger alle endringer klar til commit |
| `git commit -m "melding"` | Lagrer endringene lokalt med en beskrivelse |
| `git push` | Sender endringer opp til GitHub |

---

## Markdown-syntaks

```markdown
# Hovedoverskrift
## Underoverskrift
### Under-underoverskrift

**fet tekst** og *kursiv tekst*

- Punktliste
- Punkt to

1. Nummerert liste
2. Punkt to

> Blokksitat for viktige poeng

[Lenketekst](https://url.no)

`kode eller tekniske begreper`
```

Tips: Bruk [stackedit.io](https://stackedit.io/) for å se hvordan markdown-en ser ut mens du skriver.

---

## Viktige regler

- **Aldri commit direkte til main** – alt skal gjennom en branch og pull request
- **Kjør `git pull origin main`** før du lager en ny branch, så du jobber med siste versjon
- **Commit ofte med tydelige meldinger** – det ser bra ut i historikken
- **Bruk din egen GitHub-bruker** – sensor sjekker at alle har bidratt aktivt
- **Koordiner i gruppechatten** hvis flere jobber på samme fil samtidig, for å unngå merge-konflikter
- **Sjekk `Insights → Contributors`** på GitHub før innlevering, så alle navn er der med commits
