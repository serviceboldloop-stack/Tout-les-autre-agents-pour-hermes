# TIKTOK RULES — Règles universelles de l'algorithme
## Référence pour tous les agents — [TON_COMPTE]

---

## 1. CE QUE TIKTOK MESURE (par ordre d'importance)

| Signal | Poids | Objectif [TON_COMPTE] |
|--------|-------|--------------------------|
| Watch time / rétention | ⭐⭐⭐⭐⭐ | > 60% à 5s, > 20% complétion |
| Sauvegardes | ⭐⭐⭐⭐ | > 3% des vues |
| Partages | ⭐⭐⭐⭐ | > 1% des vues |
| Commentaires | ⭐⭐⭐ | Débat, pas juste "cool" |
| Likes | ⭐⭐ | Signal secondaire — ne pas optimiser pour ça |

**Règle absolue** : 10 000 vues + 75% complétion > 10 000 vues + 2 000 likes + 40% complétion.
Ne jamais sacrifier la rétention pour gonfler les likes.

### Ce que l'algo n'utilise PAS
- ❌ Nombre d'abonnés — un compte à 0 peut faire des millions de vues
- ❌ Performances passées — chaque vidéo repart de zéro
- ❌ Pays / langue — poids faible

---

## 2. COMMENT TIKTOK DISTRIBUE UNE VIDÉO

```
Étape 1 — Batch test (200-500 viewers non-abonnés)
         ↓ rétention faible → vidéo enterrée
         ↓ rétention forte → Étape 2

Étape 2 — Distribution élargie
         → Couches successives jusqu'à saturation
```

### Les 3 paliers de distribution (validé terrain 2026-05-09)

| Palier | Signal N°1 | Signal N°2 | Seuil critique |
|--------|------------|------------|----------------|
| 0 → 300 vues | Taux de complétion > 20% | Rétention 5s > 50% | < 20% complétion = vidéo enterrée |
| 300 → 1 000 vues | Commentaires longs + partages | Rétention continue | 0 CTA actif = bloqué à 300 |
| 1 000 → 10 000 vues | CTR miniature + watch time | Abonnements | Dépend de la niche |

**Erreur fréquente :** Hook excellent (65% à 5s) + zéro CTA = bloqué à 300 vues. L'algo teste l'engagement actif au palier 2, pas seulement la rétention passive.

### "200-view jail"
Phénomène courant : la vidéo stagne après 200 vues.
Cause = rétention insuffisante dans le batch initial.
Solution = retravailler le hook des 3 premières secondes.

### La première heure est critique
Si partages + commentaires arrivent dans les 60 premières minutes → TikTok pousse plus fort.
Si les gens scrollent sans s'arrêter → la décision algo est déjà prise.

---

## 3. LA RÈGLE DES 3 SECONDES

Les 3 premières secondes déterminent tout. Si le viewer scroll avant 3s, la vidéo est morte.

### Ce qui se passe seconde par seconde

```
0-3s   → HOOK : arrêter le scroll. Une seule priorité.
3-8s   → PREMIER WTF : révélation immédiate — OBLIGATOIRE (règle absolue 2026-05-08)
8-12s  → DÉVELOPPEMENT SERRÉ : zéro temps mort — chute 5s→10s max 5%
12-30s → SUITE : nourrir la curiosité, tension maintenue, connecteurs narratifs
30-40s → RE-HOOK : nouvelle révélation ou twist partiel
45-55s → TWIST IRONIQUE CRUEL : la révélation qui retourne tout → génère partages
55-60s → LEÇON + SIGNATURE
60s+   → CTAs : enregistrement + partage + commentaire débat (voir section 6)
```

> ⚠️ **SUPPRIMER tout ancrage "date + lieu + description sensorielle"** entre 3s et 8s.
> Preuve terrain : ancrage = chute -20% en 5 secondes (Napoléon, Henri IV). Aller directement au WTF.

### Où les viewers partent — diagnostics

| Moment de drop | Cause | Solution |
|----------------|-------|---------|
| 0-3s | Hook trop faible | Réécrire avec verbe violent + chiffre visuel |
| 3-8s | Ancrage descriptif au lieu de WTF | Supprimer l'ancrage, WTF direct |
| 8-12s | Temps mort après le WTF | Développement serré, zéro filler |
| 30s | Perte de tension | Re-hook obligatoire ici |
| 50s | Trop long | Couper les phrases non essentielles |

**Pattern interrupt** : changer visuellement ou verbalement toutes les 3-5 secondes.

---

## 4. RÈGLES DES HOOKS

### Double hook — système validé par Lucas
```
Hook 1 (ligne 1) → fait choc / chiffre précis → arrête le scroll
Hook 2 (ligne 2) → tease la fin de façon abstraite → force à rester pour comprendre
```
Le viewer doit AVOIR BESOIN de regarder la fin pour résoudre la tension créée par les 2 lignes.

### Les 6 types de hooks classés par efficacité (niche histoire)

**TYPE 1 — STAT WTF + CHIFFRE PRÉCIS** ⭐⭐⭐⭐⭐
```
"[Personnage] est mort en [X secondes/jours/heures]."
```
Validé terrain : "Le président le plus puissant du monde est mort en 8 secondes." → 55% rétention 5s

**TYPE 2 — IRONIE / CONTRASTE** ⭐⭐⭐⭐⭐
```
"Il [accomplissement]. Il [chute ironique]."
"Le président qui a aboli l'esclavage. Tué 5 jours après sa victoire."
```

**TYPE 3 — LISTE D'ACTIONS IMPOSSIBLES** ⭐⭐⭐⭐
```
"On l'a empoisonné. Noyé. Fusillé."
```

**TYPE 4 — RÉVÉLATION MYSTÉRIEUSE** ⭐⭐⭐⭐
```
"[Fait connu]. Ce que personne ne sait..."
```

**TYPE 5 — DATE + LIEU + TENSION** ⭐⭐⭐⭐
```
"21 janvier 1793. Paris. Dans quelques heures, le roi de France va mourir."
```

**TYPE 6 — PARADOXE COURT** ⭐⭐⭐
```
"Il ne respectait aucune loi, sauf la sienne."
```

### Règles absolues pour tout hook
- ✅ Maximum 2 lignes
- ✅ Minimum 1 chiffre précis si possible
- ✅ La ligne 2 crée une tension avec la ligne 1
- ✅ Se dit en < 3 secondes à l'oral
- ❌ Jamais "Bonjour", "Salut", "Aujourd'hui on va voir"
- ❌ Jamais de question fermée (réponse oui/non)
- ❌ Jamais de hook vague sans élément concret

---

## 5. RÈGLES D'ÉCRITURE DU SCRIPT

### Longueur des phrases
- Max 10-12 mots par phrase
- Alterner ultra-courtes (3-5 mots) et moyennes (8-10 mots)
- Jamais deux longues phrases consécutives

**Bon rythme :**
```
Les coups de feu commencent.
Mais quelque chose d'impossible se passe.
Les balles rebondissent sur les enfants.
Les soldats paniquent.
Ils ne comprennent pas.
```

**Mauvais rythme :**
```
Alors que les soldats commencèrent à tirer sur les membres de la famille
qui se trouvaient dans le sous-sol, quelque chose d'absolument impossible
et complètement inattendu se produisit.
```

### Mots et structures qui retiennent
- Chiffres précis (pas "beaucoup" → "47", pas "longtemps" → "12 ans")
- Noms propres (crédibilité + mémorabilité)
- Verbes d'action au présent (pas passé composé)
- Phrases nominales sans verbe ("Un père. Une mère. Cinq enfants.")
- Répétitions rythmiques ("Il mange. Il boit. Il chante. Rien.")
- Ellipses de tension ("...")

### Filler words interdits
- "donc", "en fait", "voilà", "bah", "euh"
- "Aujourd'hui on va parler de...", "Dans cette vidéo..."
- "Et donc comme je vous le disais", "Pour continuer..."
- "Il faut savoir que", "Vous savez que"
- Toutes les transitions molles

### Emphase pour la voix IA (ElevenLabs)
- ❌ JAMAIS les MAJUSCULES pour l'emphase
- ✅ TOUJOURS les "..." pour les pauses dramatiques

| Effet voulu | Comment écrire |
|-------------|---------------|
| Emphase | `"Il a... tout perdu."` |
| Pause dramatique | `"Et là... tout s'arrête."` |
| Phrase isolée forte | `"Il ment."` seul sur sa ligne |
| Mot traîné | `"Un silence... interminable."` |

---

## 6. RÈGLES DES CTAs

### CTAs par signal visé (validé 2026-05-09)

| Signal visé | CTA | Impact algo |
|-------------|-----|-------------|
| **Enregistrement** (sauvegarde) | "Enregistre cette vidéo, tu vas vouloir la revoir." | ⭐⭐⭐⭐ |
| **Partage** | "Envoie ça à quelqu'un qui croit encore à la version officielle." | ⭐⭐⭐⭐⭐ |
| **Commentaire débat** | "Tu penses vraiment que [X] ? Les historiens se déchirent encore là-dessus." | ⭐⭐⭐⭐⭐ |
| **Commentaire projection** | "T'aurais fait quoi à la place de [Personnage] ?" | ⭐⭐⭐⭐ |
| **Commentaire connaissance** | "Tu savais pour [fait rare] ?" | ⭐⭐⭐ |
| **Abonnement direct** | "Abonne-toi pour la suite" | ⭐⭐ |

### Règles CTA qualité (CRITIQUE pour le palier 300→1000)

**Règle N°1 — La réponse ne doit PAS être dans le script.**
Si la question débat a une réponse évidente dans le script → zéro commentaire.
❌ "Qui a vraiment tué Jaurès ?" — la réponse (Raoul Villain) est dans le script.
✅ "Tu penses vraiment qu'une seule mort pouvait empêcher la Première Guerre mondiale ?" — débat ouvert, les historiens s'opposent.

**Règle N°2 — Viser les commentaires LONGS, pas les mots-clés.**
"Commente OUI si tu savais pas" → commentaires d'un mot, poids algo faible.
Une vraie question de débat → commentaires argumentés de 3-5 lignes → poids algo x3-5.

**Règle N°3 — Utiliser 2-3 CTAs empilés (enregistrement + partage + commentaire).**
```
"Enregistre cette vidéo, tu vas vouloir la revoir."
"Envoie ça à quelqu'un qui croit encore à la version officielle."
"Et toi — tu penses vraiment que [question débat] ?"
```

- Ne JAMAIS demander le like
- Les commentaires d'inconnus ont plus de poids que ceux d'abonnés

---

## 7. PUBLICATION

### Horaires validés par Lucas
- **Créneau optimal** : 21h00 – 22h30 (heure française)
- **Créneau secondaire** : 20h00 – 23h00
- Plus c'est tard dans la soirée, mieux c'est selon ses observations

### Fréquence
- Cible : 1 à 3 vidéos par jour
- **Règle** : une bonne vidéo > trois vidéos moyennes. Ne jamais sacrifier la qualité pour le volume.

---

## 8. HASHTAGS ET DESCRIPTION

### Hashtags validés [TON_COMPTE]
- 4 à 5 hashtags max — ultra-ciblés niche
- ✅ `#histoire` `#histoirevraie` `#[TON_COMPTE]` `#mystere` `#storytelling`
- ❌ `#foryou` `#viral` `#pourtoi` — hashtags génériques inutiles
- Ajouter 1 hashtag lié au sujet de la vidéo (#jfk, #lincoln, #raspoutine...)

### Format de description validé
```
[Hook reformulé — 1 ligne]
[1 phrase résumé mystérieuse — tease sans révéler]
[CTA — question courte]
[Hashtags]
```
Exemple JFK :
```
Le président le plus puissant du monde. Mort en 8 secondes. 🇺🇸
Ce qui s'est vraiment passé ce jour-là.
T'as ta théorie sur qui a vraiment tué JFK ? 👇
#jfk #histoire #[TON_COMPTE] #mystere #tiktokfr
```

---

## 9. SUJETS ET ANGLES

### Angles qui percent
1. Personnage connu — angle totalement inconnu
2. Injustice documentée → partages élevés
3. Personnage quasi-immortel (survie improbable)
4. Secrets d'État / complots prouvés
5. "Ce que personne ne te dit" sur un fait connu
6. Twist hypothétique ("Et si X avait survécu ?") → ragebait naturel = commentaires
7. Sujet d'actualité qui a fait beaucoup de bruit récemment

### Règle des personnages
**TOUJOURS un seul personnage central par vidéo.**
Le viewer s'attache à une personne, jamais à un événement ou un mouvement.

### Angles à éviter
- ❌ Religion (risque shadowban)
- ❌ Sujets trop obscurs (pas de curiosité préexistante)
- ❌ Guerres entières ou événements trop larges
- ❌ Sujets traités par @maratrium dans les 3 derniers mois

---

## 10. DIAGNOSTICS — LIRE LES PERFORMANCES

### Signaux positifs (vidéo qui va bien performer)
- Rétention 5s > 50% dans les 2 premières heures
- Commentaires d'inconnus dans les 30 premières minutes
- Sauvegardes > 2% dans les premières 24h
- La vidéo continue à faire des vues après 48h

### Signaux d'alerte
| Symptôme | Problème | Solution |
|----------|----------|---------|
| Stagnation à 200 vues | Hook trop faible | Réécrire avec chiffre précis |
| Likes élevés, sauvegardes faibles | Divertissement sans valeur perçue | Ajouter une leçon / twist |
| Vues élevées, 0 nouveaux abonnés | Sujet sans fidélisation | Sujet trop généraliste |
| Watch time < 40% | Script qui ne retient pas | Avancer le WTF moment, raccourcir |
| Peu de partages | Twist pas assez fort | Rendre le "et si" plus clivant |

---

## 11. LES 10 RÈGLES À NE JAMAIS OUBLIER

1. Les 3 premières secondes sont tout — si le hook ne retient pas > 50%, la vidéo est morte
2. Le watch time surpasse tout autre signal — optimise pour la rétention, pas les likes
3. Un chiffre précis vaut mille adjectifs — "8 secondes" > "très rapidement" (et le viewer doit le visualiser sans calcul)
4. Un seul personnage central par vidéo — jamais un événement en général
5. **Le WTF moment doit tomber entre 3 et 8 secondes — pas à 25s (règle absolue 2026-05-08)**
6. Phrases courtes, toujours courtes — max 12 mots, souvent 5-7
7. **Le CTA génère des commentaires LONGS — la question ne doit pas avoir de réponse dans le script**
8. Les sauvegardes = signal de valeur long terme — twist ironique + "ça parle de vous" = +300% favoris
9. Un compte à 0 abonné peut faire des millions — l'algo ignore les abonnés
10. **Hook excellent + 0 CTA = bloqué à 300 vues — l'engagement actif est obligatoire au palier 2**

---

## 12. TWIST IRONIQUE CRUEL ET "ÇA PARLE DE VOUS"

Ces deux techniques sont les différenciateurs principaux entre 40K et 245K vues.
Source : analyse corpus 10 scripts concurrents, 2026-05-09.

### Twist ironique cruel — OBLIGATOIRE pour dépasser 100K vues

Le twist ironique est la révélation qui retourne la situation dans le sens le plus dévastateur possible.
Sans twist ironique/cruel : script 40-50K maximum. Avec : 100K+ possible.

**Formule :**
```
[Personnage cherche à accomplir X]
→ Twist : X le détruit, ou sa mort sert exactement ce qu'il combattait
```

| Exemple | Type d'ironie |
|---------|--------------|
| Mithridate invincible au poison → ne peut plus se suicider | L'outil de survie devient l'outil de sa chute |
| Les socialistes votent la guerre au nom de Jaurès qui la combattait | La mort de la victime légitime ce qu'elle refusait |
| Sadat fait la paix → tué par ses propres soldats | Le geste noble entraîne la mort |

**Où placer le twist :** entre 45s et 55s, après le développement.

**Checklist twist ironique :**
- Le personnage voulait X → il obtient l'inverse de X ? ✅
- Sa mort a-t-elle servi exactement ce qu'il combattait ? ✅
- Le twist crée-t-il une ironie cruelle et inattendue ? ✅
- → Si oui à 2/3 : inclure le twist. Sinon : chercher un autre angle.

### "Ça parle de VOUS" — technique Mara pour doubler les favoris

À mi-script, basculer du personnage historique vers le spectateur.
Transforme une anecdote historique en miroir personnel → engagement ×3-5 sur les favoris.

**Formule :**
```
"[Ce moment dans l'histoire]...
il ne parle pas vraiment de [Personnage].
Il parle de vous.
[Application concrète à la vie du spectateur en 1-2 lignes.]"
```

**Exemples validés (corpus 2026-05-09) :**
- MJ (6 782 favoris) : "cette scène-là / elle ne parle pas vraiment de Michael Jackson / elle parle de vous"
- Ormuz (2 772 favoris) : "vous ce matin en faisant votre plein / vous payez la fermeture d'un détroit"

**Règle :** N'utiliser que si l'histoire se prête naturellement à une projection personnelle. Ne pas forcer.
**Quand l'utiliser :** scripts avec leçon de vie claire ou valeur éducative forte.
**Impact sur les favoris :** peut doubler ou tripler les enregistrements → signal fort pour l'algo.
