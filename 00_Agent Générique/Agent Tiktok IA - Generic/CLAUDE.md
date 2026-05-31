# CLAUDE.md — Agent TikTok IA

## INSTRUCTION PRIORITAIRE
Tu es un agent d'action. Quand tu sais quoi faire, tu le fais immédiatement.
Zéro méta-commentaire. Zéro hésitation. Tu agis.

---

## Ce qu'est ce projet

Workspace de création de contenu TikTok IA — format **voix off + images IA, sans face cam**.
Livraisons : fichiers markdown (scripts, prompts, descriptions) utilisés avec des outils externes (ElevenLabs, Freepik/Midjourney, Kling/Runway, CapCut).

### Avant de commencer — Setup utilisateur
Lire `Context/profil.md` et `Context/comptes.md`. Si les champs sont encore en [crochets], demander à l'utilisateur de les remplir avant de produire quoi que ce soit.

---

## Structure du dossier

- `Context/` — **source de vérité** — lire avant tout :
  - `profil.md` — profil créateur, niche, objectifs, stack
  - `comptes.md` — données du compte, journal analytics, règles validées terrain
  - `tiktok_rules.md` — règles algorithme TikTok, hooks, structure script, CTAs
  - `style.md` — identité visuelle, suffix prompt, règles animation
  - `stack.md` — pipeline de production complet
- `Skills/` — workflows détaillés à exécuter :
  - `Skills/agent-research/SKILL.md` — recherche et notation de sujets viraux
  - `Skills/agent-script/SKILL.md` — transformation sujet → script viral complet
  - `Skills/agent-prompts/SKILL.md` — génération prompts images + animations
  - `Skills/agent-output/SKILL.md` — finalisation dossier vidéo
  - `Skills/agent-analyse/SKILL.md` — analyse vidéo publiée + mise à jour mémoire
- `Memory/base_memory.md` — règles validées + journal analytics du compte
- `Data/` — sujets recherchés, analyse concurrents
- `Examples/` — références de scripts, hooks, prompts
- `Outputs/` — un dossier par vidéo produite

---

## Workflow — Création d'une nouvelle vidéo

**Tu n'invoques pas de sub-agent. Tu lis le SKILL.md et tu l'exécutes toi-même.**

### ÉTAPE 0 — Lecture contexte (obligatoire avant tout)
1. `Context/profil.md`
2. `Context/comptes.md`
3. `Context/tiktok_rules.md`
4. `Context/style.md`
5. `Context/stack.md`
6. Tous les `Data/*.md`
7. Lister `Outputs/` pour le prochain numéro de vidéo
8. `Memory/base_memory.md`

Écrire **"✅ ÉTAPE 0 TERMINÉE"** avant de continuer.

### ÉTAPE 1 — Recherche de sujet
Lire et exécuter `Skills/agent-research/SKILL.md`.
Sauvegarder dans `Data/sujets_YYYY-MM-DD.md` (score ≥ 6/10 requis).
Écrire **"✅ ÉTAPE 1 TERMINÉE — Sujet : [X] — Score : [X]/10"** avant de continuer.

### ÉTAPE 2 — Script
Lire et exécuter `Skills/agent-script/SKILL.md`.
Sauvegarder dans `Outputs/Vidéo_N/script.md`.
Écrire **"✅ ÉTAPE 2 TERMINÉE"** avant de continuer.

### ÉTAPE 3 — Output final
Lire et exécuter `Skills/agent-output/SKILL.md`.
Générer `Outputs/Vidéo_N/description.md` + `Outputs/Vidéo_N/readme.md`.
Écrire **"✅ ÉTAPE 3 TERMINÉE — Vidéo_N prête à produire"**.

---

## Règles absolues du workflow

- Ne jamais sauter une étape
- Ne jamais inventer un résultat (si WebSearch échoue → relancer)
- Ne jamais écraser un dossier Outputs existant — toujours incrémenter N
- Toujours écrire le checkpoint avant de passer à l'étape suivante

---

## Règles de production non négociables

- **Hook** : verbe d'action violent + chiffre visuellement immédiat. Jamais passif, jamais chiffre abstrait.
- **Structure** (60s cible, 55-63s acceptable, jamais > 65s) :
  ```
  Hook 0-3s → WTF DIRECT 3-8s (PAS d'ancrage) → Développement 8-30s → Re-hook 30-40s
  → TWIST IRONIQUE CRUEL 45-55s → "ça parle de vous" optionnel → Leçon → Signature → 3 CTAs
  ```
- **INTERDIT** : ancrage descriptif entre 3s et 8s (= -20% rétention, validé terrain)
- **OBLIGATOIRE** : Twist ironique cruel à 45-55s (différenciateur N°1 entre 40K et 245K vues)
- **OBLIGATOIRE** : 3 CTAs empilés — enregistrement + partage + débat (réponse au débat hors du script)
- **Phrases** : max 10-12 mots, alterner ultra-courtes (3-5) et moyennes (8-10)
- **Emphase ElevenLabs** : `...` pour pauses — JAMAIS de MAJUSCULES
- **Hashtags** : 4-5 max, niche ciblée — jamais #foryou / #viral / #pourtoi

---

## Priorité des règles en cas de conflit

`Context/` fait autorité : `comptes.md` > `tiktok_rules.md` > `style.md` > `profil.md`
SKILL.md > CLAUDE.md (plus récent et spécialisé)

---

## Benchmarks de référence (niche historique, validés terrain)

| Référence | Résultat | Ce que ça prouve |
|-----------|----------|-----------------|
| Mithridate (@voxtemporis_) | 245K vues | Twist ironique cruel = multiplicateur N°1 |
| Boudica (même compte) | 20K vues | Sans twist ironique = plafond 40-50K |
| Ormuz (@maratrium) | 198K, 2772 saves | "Ça parle de vous" = saves massifs |
| MJ (@maratrium) | 234K, 6782 saves | Leçon de vie + "ça parle de vous" = record saves |
