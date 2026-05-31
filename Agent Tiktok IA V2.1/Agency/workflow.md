# WORKFLOW — Équipe d'agents @chronovision.fr
## Architecture de collaboration et phases de production

---

## ARCHITECTURE DE L'ÉQUIPE

```
┌─────────────────────────────────────────────────────────┐
│                    LUCAS (chef de projet)                │
│         Lance le pipeline / donne les stats             │
└──────────────────────┬──────────────────────────────────┘
                       │
         ┌─────────────▼─────────────┐
         │      PHASE 1 — PARALLÈLE  │
         │  Research + Memory check  │
         └──────┬────────────────────┘
                │
         ┌──────▼──────────────────────┐
         │   PHASE 2 — REVUE CROISÉE   │
         │  Research valide le script  │
         └──────┬──────────────────────┘
                │
         ┌──────▼──────────────────────┐
         │   PHASE 3 — PRODUCTION      │
         │   Script → Prompts          │
         └──────┬──────────────────────┘
                │
         ┌──────▼──────────────────────┐
         │   PHASE 4 — LIVRAISON       │
         │   Output assemble tout      │
         └──────┬──────────────────────┘
                │
         ┌──────▼──────────────────────┐
         │   PHASE 5 — ANALYSE         │
         │   (lendemain — après pub)   │
         └─────────────────────────────┘
```

---

## PHASE 1 — RECHERCHE ET MÉMOIRE (parallèle)

**Qui travaille :** Agent Research + lecture de memory/ en simultané
**Objectif :** Trouver les sujets ET récupérer tous les apprentissages récents

### Agent Research
```
STATUT : 🔄 EN COURS
- Lire data/ et examples/meilleurs_scripts.md
- Lire data/concurrents_scripts.md
- Chercher les sujets viraux (TikTok + web search)
- Produire data/sujets_YYYY-MM-DD.md avec 5 sujets notés
STATUT : ✅ TERMINÉ → passer à Phase 2
```

### Lecture mémoire (en parallèle)
```
STATUT : 🔄 EN COURS
- Lire memory/base_memory.md
- Extraire les 3 règles prioritaires du moment
- Les noter pour les transmettre à l'agent script
STATUT : ✅ TERMINÉ → prêt pour Phase 2
```

**Condition de passage à Phase 2 :**
Les 5 sujets sont notés ET les règles mémoire sont extraites.

---

## PHASE 2 — REVUE CROISÉE RESEARCH → SCRIPT

**Qui travaille :** Agent Research relit la liste de sujets avant de la soumettre
**Objectif :** Valider que le sujet recommandé est vraiment le meilleur avant d'écrire le script

### Checklist de validation (agent research)
```
□ Le sujet recommandé a un WTF moment clairement identifiable ?
□ Le sujet n'a pas été traité récemment par @maratrium ?
□ Le sujet n'a pas déjà été traité sur @chronovision.fr ?
□ Un hook avec chiffre précis est possible sur ce sujet ?
□ Le score est > 6/10 ?

Si une case est ❌ → passer au sujet suivant dans la liste
Si toutes les cases sont ✅ → soumettre à agent script
```

### Rapport de validation
```
Agent Research → Agent Script :
"Sujet validé : [NOM]
Score : [X]/10
WTF moment identifié : [description]
Hook possible : [idée de hook]
Règles mémoire à appliquer : [3 règles prioritaires du moment]
Feu vert pour écriture."
```

**Condition de passage à Phase 3 :**
Agent Research a validé le sujet ET transmis le rapport.

---

## PHASE 3 — PRODUCTION (séquentielle)

**Qui travaille :** Agent Script → puis Agent Prompts
**Objectif :** Produire le script complet + tous les prompts visuels

### Agent Script
```
STATUT : 🔄 EN COURS
- Lire le rapport de validation de Phase 2
- Lire context/ complet
- Lire examples/meilleurs_scripts.md
- Lire data/concurrents_scripts.md
- Appliquer les 3 règles mémoire prioritaires
- Écrire le script avec 3 hooks alternatifs
- Produire video_N/script.md
STATUT : ✅ TERMINÉ
```

### Auto-vérification script (avant de passer aux prompts)
```
□ Durée estimée ≤ 63 secondes ?
□ Hook contient un chiffre précis ?
□ WTF moment avant 25 secondes ?
□ CTA invite au débat (pas question fermée) ?
□ Zéro filler words ?
□ Signature présente ?

Si une case est ❌ → corriger avant de passer à Agent Prompts
Si toutes les cases sont ✅ → passer à Agent Prompts
```

### Agent Prompts
```
STATUT : 🔄 EN COURS
- Lire video_N/script.md
- Lire context/style.md
- Lire examples/prompts_exemple.md
- Découper le script scène par scène
- Générer tous les prompts images + animations
- Produire video_N/prompts.md
STATUT : ✅ TERMINÉ
```

### Auto-vérification prompts
```
□ Nombre de scènes entre 17 et 26 ?
□ Descriptions des personnages identiques d'une scène à l'autre ?
□ Suffix universel sur chaque image ?
□ "no dialogue" sur chaque animation ?
□ Aucune image ne demande une transformation complexe ?

Si une case est ❌ → corriger
Si toutes les cases sont ✅ → passer à Phase 4
```

**Condition de passage à Phase 4 :**
script.md ✅ + prompts.md ✅ + toutes les cases cochées.

---

## PHASE 4 — LIVRAISON

**Qui travaille :** Agent Output
**Objectif :** Assembler le dossier final et livrer à Lucas

### Agent Output
```
STATUT : 🔄 EN COURS
- Lire video_N/script.md et video_N/prompts.md
- Générer video_N/description.md
- Générer video_N/readme.md avec checklist production
- Vérifier que les 4 fichiers sont présents
STATUT : ✅ TERMINÉ
```

### Rapport final à Lucas
```
═══════════════════════════════════════
✅ VIDEO [N] PRÊTE — [SUJET EN MAJUSCULES]
═══════════════════════════════════════

📁 Dossier : outputs/video_[N]/
📄 script.md       ✅
📄 prompts.md      ✅ ([N] scènes)
📄 description.md  ✅
📄 readme.md       ✅

🎯 Hook recommandé : [Hook choisi]
⏱️ Durée estimée : [X]s
🎬 Nombre de scènes : [N]
📊 Potentiel viral : [X]/10

🔜 PROCHAINE ÉTAPE POUR LUCAS :
1. Coller le script dans ElevenLabs
2. Générer les [N] images dans Freepik
3. Animer dans Kling 2.5
4. Monter dans CapCut
5. Publier entre 21h et 22h30
═══════════════════════════════════════
```

---

## PHASE 5 — ANALYSE (lendemain)

**Qui travaille :** Agent Analyse
**Objectif :** Apprendre de la vidéo publiée et améliorer le système

### Déclenchement
Lucas donne les stats au format standard :
```
video_[N]
[durée]s ; [vues] vue ; [likes] like ; [commentaires] commentaire ;
[partages] partage ; [favoris] favoris ;
temps de visionnage moyen de [X] seconde ;
[X]% ont regardé toute la vidéo ; [X] nouveau followers ;
après 5s il reste [X]% ; après 10s il reste [X]% ;
après 20s il reste [X]% ; après 30s il reste [X]% ;
après 40s il reste [X]% ; après 50s il reste [X]% ;
après 60s il reste [X]%
```

### Agent Analyse
```
STATUT : 🔄 EN COURS
- Lire les stats données par Lucas
- Lire video_N/script.md
- Lire memory/base_memory.md
- Construire la courbe de rétention
- Diagnostiquer les chutes
- Formuler 3-5 recommandations concrètes
- Sauvegarder video_N/analyse.md
- Mettre à jour memory/base_memory.md
STATUT : ✅ TERMINÉ
```

### Rapport d'amélioration à Lucas
```
═══════════════════════════════════════
📊 ANALYSE VIDEO [N] — [SUJET]
═══════════════════════════════════════

Score global : [X]/10

Points forts :
✅ [Ce qui a bien marché]

Points à améliorer :
⚠️ [Priorité 1]
⚠️ [Priorité 2]

Pour la prochaine vidéo :
→ [Règle concrète 1]
→ [Règle concrète 2]

Mémoire système mise à jour. ✅
═══════════════════════════════════════
```

---

## GESTION DES BLOCAGES

### Si un agent est bloqué
```
❌ BLOQUÉ — [NOM AGENT]
Problème : [Description précise]
Besoin : [Ce qu'il faut pour débloquer]
```
→ Signaler à Lucas immédiatement. Ne pas continuer sans résoudre.

### Si les agents sont en désaccord
Exemple : Research propose un sujet que Script considère trop difficile à traiter.
→ Research et Script exposent leurs arguments
→ Lucas tranche
→ Pipeline reprend

### Si un sujet ne passe pas la validation Phase 2
→ Passer au sujet #2 de la liste
→ Si aucun sujet ne passe → relancer agent_research avec de nouvelles recherches

---

## SUIVI DE PRODUCTION GLOBAL

```
outputs/
├── video_1/   ✅ Publié | [date] | [vues] vues | Analysé ✅
├── video_2/   ✅ Publié | [date] | [vues] vues | Analysé ✅
├── video_3/   🎬 En production
└── video_4/   ⬜ À lancer
```
