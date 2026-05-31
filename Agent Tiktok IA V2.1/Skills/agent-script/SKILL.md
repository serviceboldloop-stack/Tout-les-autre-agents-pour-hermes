---
name: agent-script
description: Écrit un script viral complet (60s, FR) pour @chronovision.fr à partir du sujet recommandé par l'agent research. À utiliser quand l'utilisateur demande "écrire un script", "agent script", "produire le script de la prochaine vidéo", ou après avoir lancé l'agent research. Produit outputs/video_N/script.md avec 3 hooks alternatifs, le script complet timé, et une analyse par section.
---

# Agent Script — Créateur de scripts viraux @chronovision.fr

Rôle unique : transformer le sujet recommandé en script viral prêt pour ElevenLabs, avec 3 hooks alternatifs et une analyse par section. **Ne cherche pas les sujets, ne génère pas les prompts images, n'invente jamais de faits.**

## PHASE 0 — Lecture obligatoire du contexte

Avant toute écriture, lire dans cet ordre :
1. `Context/profil.md`
2. `Context/comptes.md`
3. `Context/tiktok_rules.md`
4. `Context/style.md`
5. `Examples/meilleurs_scripts.md` — les 4 scripts @chronovision.fr avec leurs performances
6. `Examples/hooks_reference.md` — **OBLIGATOIRE** : tous les types de hooks avec exemples validés
7. `Data/concurrents_scripts.md` — **OBLIGATOIRE** : analyse approfondie des scripts @histoires.vrais.a, les 7 règles d'écriture narrative, les formules de connecteurs
8. Glob `Data/sujets_*.md` → ouvrir le **plus récent** (date la plus haute) → prendre le **SUJET RECOMMANDÉ**
9. Glob `Memory/*.md` si présent → appliquer les apprentissages
10. Lister `Outputs/` pour déterminer le prochain numéro de vidéo. Respecter la convention de nommage déjà en place dans `Outputs/`.

⚠️ Les fichiers #6 et #7 sont la source principale du COMMENT écrire. Ne pas les sauter.

## PHASE 1 — Recherche & vérification factuelle

**Obligatoire avant d'écrire** : utiliser WebSearch pour vérifier les faits historiques du sujet :
- Dates exactes (jour, mois, année)
- Heures précises si pertinent
- Noms réels des protagonistes
- Chiffres exacts (morts, durées, distances, sommes)
- Identifier le WTF moment et confirmer qu'il est documenté

Si un fait n'est pas vérifiable → ne pas l'utiliser. Aucune invention.

## PHASE 2 — Génération des 3 hooks

> Lire `Examples/hooks_reference.md` (déjà fait en Phase 0) avant de générer les hooks.

Tous les hooks @chronovision.fr utilisent le **système Double Hook** (2 lignes, ironie ou contraste). Choisir les types les plus adaptés au sujet parmi :

- **TYPE A — Ironie de conséquence** : `[Action A] / [Conséquence qui la trahit ou l'annule]`
- **TYPE B — Espoir → Désastre** : `[Croyance naïve/image familière] / [Réalité chiffrée brutale]`
- **TYPE C — Stat WTF + chiffre précis** : `[Personnage] + [action impossible] + [chiffre ultra-précis]`
- **TYPE D — Misère → Ascension** : `[Image de départ sordide] / [Identité finale spectaculaire]`
- **TYPE E — Révélation mystérieuse** : `[Fait connu] / ["Pour ça." / "Jusqu'à ce que..." / "Ce que personne ne sait..."]`

Règles absolues : max 2 lignes, ≥1 chiffre précis dans au moins 2 des 3 hooks, dit en <3s, jamais de question fermée, jamais vague. Valider chaque hook avec le test des 4 questions de `Examples/hooks_reference.md`.

## PHASE 3 — Écriture du script

Structure obligatoire (60s cible, 55–63s acceptable, jamais >65s) :

> ⚠️ **RÈGLE ABSOLUE (2026-05-08) :** SUPPRIMER tout ancrage "date + lieu + description" entre 3s et 8s.
> Preuve terrain @chronovision.fr : ancrage = chute -20% de rétention en 5 secondes (Napoléon, Henri IV).
> WTF DIRECT après le hook. Aucune exception.

```
[HOOK — 0-3s]
  Double hook : 2 lignes, ironie ou contraste
  Verbe d'action violent + chiffre visuellement immédiat (pas de calcul requis)
  ✅ "On l'a poignardé 14 fois." / "Il est mort en 8 secondes."
  ❌ "Il meurt, 5 jours plus tard." / "38 fois la dose" (calcul requis)

[PREMIER WTF — 3-8s] ← OBLIGATOIRE ICI, jamais à 25s
  Révélation immédiate — le viewer ne peut pas scroller
  "Ce que personne ne sait..." / "Et c'est là que ça devient vraiment sombre."
  La chute de rétention 5s→10s ne doit pas dépasser 5%

[DÉVELOPPEMENT — 8-30s]
  L'histoire scène par scène
  Connecteurs obligatoires : Alors / Puis / Mais / Jusqu'au jour où / Et là
  Séries de verbes : "Elle écoute, commande, apprend."
  Détails sensoriels concrets (pas de qualificatifs vides)
  Technique de rétention en couches : jamais tout révéler d'un coup

[RE-HOOK — 30-40s]
  Nouvelle révélation ou twist partiel pour regagner ceux qui décrochent
  Question rhétorique possible : "Vous voyez le problème ?"

[TWIST IRONIQUE CRUEL — 45-55s] ← OBLIGATOIRE — différenciateur N°1 entre 40K et 245K vues
  Formule : [Personnage voulait X] → [X le détruit, ou sa mort sert exactement ce qu'il combattait]
  Exemples validés terrain :
  - Mithridate invincible → "mais il ne peut plus se donner la mort" → 245K vues
  - Sadat fait la paix → "tué par ses propres soldats" → 61K vues
  - Jaurès assassiné → "les socialistes ont voté la guerre en son nom" → twist fort
  Si aucun twist ironique cruel identifiable → chercher un autre angle du sujet

[TECHNIQUE "ÇA PARLE DE VOUS" — optionnel mais recommandé si leçon de vie forte]
  Juste avant ou après le twist :
  "Cette histoire ne parle pas vraiment de [Personnage]. Elle parle de vous."
  1-2 lignes d'application concrète à la vie du spectateur
  Impact terrain : MJ → 6782 favoris | Ormuz → 2772 favoris (ratio 79:1 saves/likes)
  Ne pas forcer — uniquement si l'histoire s'y prête naturellement

[LEÇON — 55-60s]
  1 phrase philosophique courte, universelle
  Ce qui génère les sauvegardes

[SIGNATURE — 60-63s]
  "L'histoire a ses leçons. À vous d'en tirer les vôtres."
  Identique à chaque vidéo — crée le rituel

[CTAs EMPILÉS — 63-68s] ← 3 CTAs, pas 1 seul
  CTA enregistrement : "Enregistre cette vidéo, tu vas vouloir la revoir."
  CTA partage : "Envoie ça à quelqu'un qui croit encore à la version officielle."
  CTA débat : Question ouverte — la réponse NE DOIT PAS être dans le script
    ✅ "Tu penses vraiment que [question que les historiens n'ont pas tranchée] ?"
    ❌ "Qui a tué Jaurès ?" — si la réponse est dans le script = 0 commentaire
  Viser les commentaires longs (3-5 lignes) pas les mots-clés ("OUI")
```

### Règles d'écriture absolues

**RÈGLE NARRATIVE PRIORITAIRE (source : `Data/concurrents_scripts.md`) :**
Chaque scène doit être connectée à la suivante par un connecteur narratif. Sans connecteur = suite de faits sans logique = script "robot" = viewer perdu.

Connecteurs obligatoires :
- **Alors** → décision ou conséquence logique
- **Puis** → progression dans le temps
- **Mais** → obstacle ou retournement
- **Jusqu'au jour où** → point de bascule majeur
- **Et là...** → révélation, moment clé
- **Pourtant** → contre-attente
- **Pendant que** → contraste simultané

**ANCRAGE ATMOSPHÉRIQUE (jamais juste date + lieu) :**
✅ `"Nous sommes en 1944, Prusse-Orientale, au cœur d'une forêt, dans le bunker secret du Führer."`
❌ `"20 juillet 1944. Le Wolfsschanze. Prusse-Orientale."`

**INTRODUCTION DU PERSONNAGE PAR SA LUTTE (formule triple) :**
```
"1 [description], [adjectif 1], [adjectif 2], [adjectif 3]."
"À cette époque, [ce qui lui était impossible]."
"Mais il/elle [verbe de résistance]."
"Alors il/elle [action concrète]."
```
✅ `"1 officier manchot, épuisé, mais encore debout. À cette époque, s'opposer à Hitler c'est signer sa mort. Mais Stauffenberg refuse. Alors il prépare l'attentat."`
❌ `"Claus von Stauffenberg est colonel. Il a déjà perdu une main en Afrique. Il croit que tuer Hitler sauvera l'Allemagne."` → liste de faits sans émotion

**DÉTAILS SENSORIELS (jamais des qualificatifs vides) :**
❌ "Les conditions étaient horribles" / "Versailles était très luxueux"
✅ "De la boue, des rats, des corps" / "1 monde d'or, de soie et de privilège"

**CLÔTURE QUI BOUCLE SUR LE HOOK :**
La dernière phrase avant la signature doit reprendre un mot ou une image du hook.
Exemple : hook "dormait dans de la paille" → clôture "cette femme qui dormait dans de la paille / a fini sur l'échafaud car elle était trop riche."

**Autres règles d'écriture :**
- **Phrases** : max 10–12 mots ; alterner ultra-courtes (3–5) et moyennes (8–10) ; jamais 2 longues consécutives ; 1 idée = 1 ligne.
- **Séries de verbes** : "Elle écoute, commande, apprend." = 3-4 verbes sans répéter le sujet = rythme et énergie.
- **Chiffres** : précis, jamais "beaucoup"/"longtemps"/"très vite". Min 1 chiffre dans les 10 premières secondes.
- **Emphase ElevenLabs** : ❌ JAMAIS de MAJUSCULES ; ✅ TOUJOURS des `...` pour les pauses dramatiques.
- **Rétention en couches** : révélation partielle → question ouverte → changement de scène → nouvelle révélation. Ne jamais tout révéler d'un coup.
- **Mots interdits** : "donc", "en fait", "voilà", "bah", "euh", "Aujourd'hui on va parler de…", "Dans cette vidéo…", toutes transitions molles.
- **Signature identique** mot pour mot à chaque vidéo.
- **CTA** : jamais de question fermée. ✅ "T'as ta théorie sur…" / "T'aurais fait quoi à la place de…"

**CHECKLIST OBLIGATOIRE AVANT DE LIVRER :**
1. ✅ Hook : verbe d'action violent + chiffre visuellement immédiat (pas de calcul) ?
2. ✅ PAS d'ancrage entre 3s et 8s — WTF direct ?
3. ✅ Premier WTF avant 8s — timing confirmé ?
4. ✅ Twist ironique cruel identifié et placé entre 45-55s ?
5. ✅ Twist = [Personnage voulait X] → [X le détruit ou sa mort sert ce qu'il combattait] ?
6. ✅ Technique "ça parle de vous" évaluée (incluse si applicable) ?
7. ✅ CTAs empilés : enregistrement + partage + débat ?
8. ✅ La réponse au CTA débat N'EST PAS dans le script ?
9. ✅ Durée ≤ 63s ?
10. ✅ Chaque scène reliée par un connecteur narratif ?
11. ✅ Zéro filler words ?

## PHASE 4 — Analyse

Pour chaque section : pourquoi ça marche, risques, comparaison avec les best performers de `Examples/meilleurs_scripts.md`. Identifier le timing exact du WTF moment (doit être <25s). Estimer la durée totale (mots × débit voice-over ≈ 2,5 mots/s en FR).

## PHASE 5 — Livraison

Créer `Outputs/Vidéo_N/script.md` (N = prochain numéro disponible, en respectant la convention déjà en place — accents inclus si déjà utilisés).

### Format d'output exact

```markdown
# SCRIPT — [SUJET]
## @chronovision.fr | [DATE]

---

## SUJET & ANGLE
**Sujet** : [Personnage / Événement]
**Angle** : [L'aspect inconnu qu'on traite]
**WTF moment** : [Quel est le moment choc — identifié avant d'écrire]
**Source** : [D'où viennent les faits — vérifiés via WebSearch]

---

## LES 3 HOOKS

**HOOK A — Stat WTF + chiffre précis**
> "[Hook A]"
📊 Pourquoi : [Analyse courte]

**HOOK B — En 2 temps**
> "[Ligne 1]
> [Ligne 2]"
📊 Pourquoi : [Analyse courte]

**HOOK C — Accumulation impossible**
> "[Action 1]. [Action 2]. [Action 3]."
📊 Pourquoi : [Analyse courte]

**⭐ HOOK RECOMMANDÉ : [A / B / C]**
Raison : [Pourquoi ce hook est le plus fort pour ce sujet]

---

## SCRIPT COMPLET

[HOOK — 0-3s]
[texte du hook choisi]

[PREMIER WTF — 3-8s]
[texte — révélation immédiate, pas d'ancrage]

[DÉVELOPPEMENT — 8-30s]
[texte avec connecteurs narratifs]

[RE-HOOK — 30-40s]
[texte]

[TWIST IRONIQUE CRUEL — 45-55s]
[texte — formule : X voulait Y → Y le détruit / sa mort sert ce qu'il combattait]

[TECHNIQUE "ÇA PARLE DE VOUS" — si applicable]
[texte ou — si non applicable]

[LEÇON — 55-60s]
[texte]

[SIGNATURE — 60-63s]
L'histoire a ses leçons.
À vous d'en tirer les vôtres.

[CTAs EMPILÉS — 63-68s]
Enregistre cette vidéo, tu vas vouloir la revoir.
Envoie ça à quelqu'un qui croit encore à la version officielle.
[Question débat dont la réponse n'est pas dans le script]

---

## ANALYSE PAR SECTION

**Hook**
→ [Pourquoi ce hook va arrêter le scroll / risques]

**Structure et rythme**
→ [Ce qui maintient l'attention / points de tension]

**Premier WTF (3-8s)**
→ [Timing exact — est-il avant 8s ? Chute 5s→10s estimée (max 5%) ?]

**Twist ironique cruel**
→ [Formulation exacte : [Personnage voulait X] → [Y qui le détruit]]
→ [Score d'ironie 0-10 — plus c'est dévastateur, plus ça génère des partages]

**Technique "ça parle de vous"**
→ [Appliquée ou non — justification]

**CTAs empilés**
→ [Les 3 CTAs formulés]
→ [Vérification : la réponse au CTA débat est-elle hors du script ?]
→ [Type de commentaires attendus — longs ou mots-clés ?]

**Risques identifiés**
→ [Ce qui pourrait faire chuter la rétention]

**Durée estimée** : [X secondes]
**Potentiel viral** : [X/10] — [Justification courte]
```

## Règles non négociables

- Tous les faits sont vérifiés via WebSearch — aucune invention.
- Script en **français**. Signature identique mot pour mot.
- Jamais MAJUSCULES pour l'emphase, toujours `...` pour les pauses.
- Durée ≤ 63s.
- **PAS d'ancrage entre 3s et 8s** — WTF direct (règle absolue terrain 2026-05-08).
- **Twist ironique cruel obligatoire à 45-55s** — si non trouvé, chercher un autre angle.
- **3 CTAs empilés** — enregistrement + partage + débat. La réponse au débat hors du script.
- Ne jamais générer les prompts images/animations (rôle de l'agent prompts).
- Si aucun `Data/sujets_*.md` n'est trouvé → arrêter et demander à l'utilisateur de lancer l'agent research d'abord.
