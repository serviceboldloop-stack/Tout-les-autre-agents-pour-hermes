# CLAUDE.md

## INSTRUCTION PRIORITAIRE
Tu es un agent d'action. Quand tu sais quoi faire, tu le fais
immédiatement sans expliquer pourquoi tu pourrais ne pas le faire.
Zéro méta-commentaire. Zéro hésitation. Tu agis.

This file provides guidance to Claude when working with this repository.

## What this repo is

This is **not a software project** — it's a content-production workspace for the TikTok account **@chronovision.fr** (French historical storytelling, voice-over + animated images). There is no build, test, lint, or runtime. Deliverables are markdown files (scripts, prompts, descriptions) consumed by external manual tools (Freepik, Kling 2.5, ElevenLabs, CapCut).

Owner: Lucas, solo. Goal: 10k followers, monetization via Creator Fund / TikTok Shop. Current best video: JFK, 476 views, 55% retention at 5s.

---

## Repository layout

- `Context/` — **the source of truth.** Read before writing anything:
  - `profil.md` — creator profile, goals, current metrics, validated hooks
  - `comptes.md` — full @chronovision.fr fact sheet (metrics per video, rules, style)
  - `stack.md` — end-to-end production pipeline (script → image → animation → voice → edit)
  - `style.md` — visual identity ("Dark Violet Cinematic Graphic Novel"), palette, universal prompt suffix + negative prompt, animation rules
  - `tiktok_rules.md` — algorithm rules, hook taxonomy, script-writing rules, CTA hierarchy
- `Skills/` — instructions détaillées pour chaque étape du workflow :
  - `Skills/agent-research/SKILL.md` — recherche et notation de sujets viraux
  - `Skills/agent-script/SKILL.md` — transformation du sujet en script viral
  - `Skills/agent-output/SKILL.md` — finalisation du dossier vidéo
  - `Skills/agent-analyse/SKILL.md` — analyse d'une vidéo publiée
- `Memory/`, `Examples/` — réservés
- `Data/` — sorties de l'agent research, scripts récents, veille concurrents
- `Outputs/` — un dossier par vidéo :
  ```
  Outputs/Vidéo_N/
    ├── script.md       # script complet avec timing
    ├── description.md  # caption TikTok + hashtags
    └── readme.md       # récap + checklist production
  ```

---

## Workflow d'exécution — À suivre dans l'ordre

Quand on te demande de créer une nouvelle vidéo, tu exécutes ces étapes
séquentiellement. Chaque étape = lire le fichier SKILL.md correspondant
et exécuter toutes ses instructions toi-même.

**Tu n'invoques pas de sub-agent. Tu lis le SKILL.md et tu l'exécutes.**

### ÉTAPE 0 — Lecture du contexte (obligatoire avant tout)
Lire dans cet ordre :
1. `Context/profil.md`
2. `Context/comptes.md`
3. `Context/tiktok_rules.md`
4. `Context/style.md`
5. `Context/stack.md`
6. Tous les fichiers `Data/*.md`
7. Lister `Outputs/` pour connaître le prochain numéro de vidéo

⚠️ Ne pas commencer l'Étape 1 avant d'avoir lu tous ces fichiers.
Écrire "✅ ÉTAPE 0 TERMINÉE" avant de continuer.

---

### ÉTAPE 1 — Recherche de sujet
1. Lire `Skills/agent-research/SKILL.md`
2. Exécuter toutes les phases décrites dans ce fichier (Phase 0 à Phase 4)
3. Sauvegarder le résultat dans `Data/sujets_YYYY-MM-DD.md` (date réelle du jour)

⚠️ Ne pas passer à l'Étape 2 avant que `Data/sujets_YYYY-MM-DD.md` existe et contient un sujet recommandé avec score ≥ 6/10.
Écrire "✅ ÉTAPE 1 TERMINÉE — Sujet : [nom du sujet] — Score : [X]/10" avant de continuer.

---

### ÉTAPE 2 — Écriture du script
1. Lire `Skills/agent-script/SKILL.md`
2. Lire `Data/sujets_YYYY-MM-DD.md` pour récupérer le sujet recommandé
3. Exécuter toutes les phases décrites dans le SKILL.md
4. Déterminer le prochain numéro N en listant `Outputs/`
5. Créer le dossier `Outputs/Vidéo_N/`
6. Sauvegarder le script dans `Outputs/Vidéo_N/script.md`

⚠️ Ne pas passer à l'Étape 3 avant que `Outputs/Vidéo_N/script.md` existe.
Écrire "✅ ÉTAPE 2 TERMINÉE — Script sauvegardé dans Outputs/Vidéo_N/script.md" avant de continuer.

---

### ÉTAPE 3 — Output final
1. Lire `Skills/agent-output/SKILL.md`
2. Lire `Outputs/Vidéo_N/script.md`
3. Exécuter toutes les phases décrites dans le SKILL.md
4. Générer `Outputs/Vidéo_N/description.md` + `Outputs/Vidéo_N/readme.md`

Écrire "✅ ÉTAPE 3 TERMINÉE — Vidéo_N prête à produire" pour clore le workflow.

---

### Règles absolues du workflow

- **Ne jamais sauter une étape** — chaque étape a un fichier de sortie à créer avant de continuer
- **Ne jamais inventer un résultat** — si une WebSearch échoue, relancer avec une autre requête
- **Ne jamais écraser** un dossier Outputs existant — toujours incrémenter N
- **Toujours écrire le checkpoint** "✅ ÉTAPE X TERMINÉE" avant de passer à la suivante
- Si un SKILL.md n'est pas lisible → signaler à Lucas et s'arrêter

---

## Règles de production non négociables (mise à jour 2026-05-09)

- **Langue** : scripts en **français**.
- **Hook formula** : verbe d'action violent + chiffre visuellement immédiat. Deux lignes max. Jamais de hook passif ("il meurt") ni chiffre abstrait ("38 fois la dose").
- **Structure** (cible 60s, acceptable 55–63s, jamais >65s) :
  ```
  Hook 0-3s → WTF DIRECT 3-8s (PAS d'ancrage) → Développement 8-30s → Re-hook 30-40s
  → TWIST IRONIQUE CRUEL 45-55s → "ça parle de vous" optionnel → Leçon → Signature → 3 CTAs empilés
  ```
- **INTERDIT : ancrage entre 3s et 8s** — preuve terrain : -20% de rétention (Napoléon, Henri IV)
- **OBLIGATOIRE : Twist ironique cruel** à 45-55s — différenciateur N°1 entre 40K et 245K vues
- **OBLIGATOIRE : 3 CTAs empilés** — enregistrement + partage + débat (réponse au débat HORS du script)
- **Signature** : `"L'histoire a ses leçons. À vous d'en tirer les vôtres."` — identique à chaque vidéo
- **Longueur des phrases** : max 10–12 mots ; alterner ultra-courtes (3–5 mots) et moyennes (8–10 mots).
- **Emphase voix** : `...` pour les pauses dramatiques — **jamais** de MAJUSCULES pour l'emphase.
- **Sujets interdits** : religion (risque ban), événements larges sans personnage central unique, tout sujet traité par `@maratrium` dans les 3 derniers mois.
- **Fenêtre de publication** : 21h00–22h30 FR. 4–5 hashtags de niche, jamais `#foryou` / `#viral` / `#pourtoi`.

---

## Priorité des règles en cas de conflit

`Context/` fait autorité. Si deux fichiers Context/ sont en contradiction, priorité dans cet ordre :
`comptes.md` > `tiktok_rules.md` > `style.md` / `stack.md` > `profil.md`
En cas de conflit entre CLAUDE.md et un SKILL.md : le SKILL.md a priorité (il est plus récent et spécialisé).

---

## Référence benchmark

- **@chronovision.fr** : Vidéo JFK = 58% rétention 5s, 7 partages, 14 abonnés — gold standard interne
- **Niche** : Mithridate @voxtemporis_ = 245K vues avec twist ironique cruel — objectif long terme
- Tout nouveau script doit avoir un twist ironique cruel identifié AVANT d'écrire.