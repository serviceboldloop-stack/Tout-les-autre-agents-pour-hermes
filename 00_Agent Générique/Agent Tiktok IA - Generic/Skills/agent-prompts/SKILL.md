---
name: agent-prompts
description: Génère tous les prompts images (Freepik) et animations (Kling 2.5) scène par scène pour une vidéo [TON_COMPTE] à partir d'un script existant. À utiliser quand l'utilisateur demande "agent prompts", "générer les prompts", "prompts images", "prompts d'animation", ou après avoir produit un script. Produit outputs/video_N/prompts.md avec 17 à 26 scènes prêtes à copier-coller.
---

# Agent Prompts — Générateur de prompts visuels [TON_COMPTE]

Rôle unique : transformer un script existant en prompts images + animations prêts pour Freepik et Kling 2.5. **N'écrit pas le script, ne génère pas les images, ne fait pas les animations.**

## PHASE 0 — Lecture obligatoire

Avant toute génération, lire en parallèle :
- `Context/style.md` — identité visuelle, suffix universel, negative prompt
- `Context/comptes.md` — règles compte
- `Examples/prompts_exemple.md` — **référence visuelle principale**, à imiter en style et structure
- `Outputs/video_N/script.md` — **le script à illustrer**

Pour identifier le bon dossier `video_N` : lister `Outputs/` et prendre le plus récent qui contient un `script.md` mais pas encore de `prompts.md`. Si ambigu, demander à l'utilisateur.

## PHASE 1 — Découpage du script

- Identifier chaque moment qui nécessite une image
- Règle de découpage :
  - Phrase normale (8-12 mots) → 1 phrase = 1 image
  - Phrases très courtes (1-4 mots) → grouper 2-3 phrases sur 1 image
  - Changement de lieu / personnage / action → toujours nouvelle image
  - Moment d'émotion fort → 1 image dédiée
- Numéroter chaque scène
- Choisir le type de plan optimal pour chaque scène :
  - **POV** : immersion, action physique vécue par un personnage
  - **Wide shot** : plusieurs personnages, établir un lieu, action collective
  - **Medium shot** : action principale d'un personnage, scènes intimes non-POV
  - **Close-up / Detail** : objet crucial, détail révélateur
  - **Split composition** : événements simultanés, avant/après
  - **Extreme slow motion** : WTF moment visuel, impact
- Compter le nombre total : **cible 17-26 scènes pour 60s**

## PHASE 2 — Génération des prompts

Pour chaque scène dans l'ordre :

### Règle fondamentale : IMAGE = PREMIÈRE FRAME
L'image décrit l'état initial figé. L'animation décrit le mouvement qui suit. Jamais de transformation complexe demandée à l'image.

### Prompt image (Freepik)
Format JSON :
```json
{
  "prompt": "[Type de plan] [description précise scène], [description personnage(s)], [décor + époque précise], [éclairage précis], [atmosphère + tension émotionnelle], [SUFFIX UNIVERSEL de style.md]",
  "negative_prompt": "photorealistic, [éléments spécifiques à éviter], cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Suffix universel** (à coller à la fin de CHAQUE prompt image) :
```
dark cinematic illustration style inspired by animated graphic novel,
loose expressive brushstrokes, high contrast deep shadows,
desaturated palette with deep purple violet tones and cold pale moonlight accent,
painterly textured style, vertical 9:16 composition,
no photorealism, no text, no watermark
```

**Negative prompt universel** :
```
photorealistic, bright colors, modern elements, cheerful setting,
cartoonish flat style, blurry, low contrast, flat illustration,
text overlay, watermark, logo
```

### Éclairage selon scène
| Type | Éclairage |
|------|-----------|
| Extérieur nuit / forêt | `cold pale moonlight barely penetrating through dense canopy` |
| Intérieur 1900s | `single weak amber lamp in corner, deep purple violet shadows` |
| Action / tirs | `harsh white muzzle flash briefly illuminating` |
| Scène intime / couture | `warm amber candlelight catching the sparkle` |
| Révélation / twist | `single amber spotlight from above` |
| Mort / deuil | `cold pale moonlight, deep purple violet darkness pressing in` |

### Personnages
- **Principaux** : description complète **identique mot pour mot** dans toutes les scènes. Définir une fois, copier-coller ensuite.
- **Gardes / soldats / antagonistes** : `completely black featureless silhouette [rôle]` — jamais de visage.

### Prompt animation (Kling 2.5)
Format JSON :
```json
{
  "prompt": "[Description du mouvement très précis], [comment les éléments bougent], [ambiance sonore suggérée si utile], no dialogue, [vitesse]",
  "negative_prompt": "fast movement, lip sync, dialogue, robotic movement, glitches, [éléments spécifiques]"
}
```

Mouvements autorisés : `atmospheric`, `slow_zoom_in`, `slow_zoom_out`, `parallax`, `light_shift`, `micro_motion`, `pan_slow`.

Règles :
- **Toujours très lent**, 4-6 secondes par clip
- Exception : flash de tir (bref puis retour au lent)
- **Toujours `no dialogue`** dans le prompt
- Interdits : lip sync, dialogue, mouvements rapides, transitions brusques

## PHASE 3 — Vérification

- ✅ Descriptions des personnages principaux **identiques mot pour mot** d'une scène à l'autre
- ✅ Aucune image ne demande de transformation complexe
- ✅ Toutes les images contiennent le suffix universel
- ✅ Toutes les animations contiennent `no dialogue`
- ✅ Nombre de scènes entre 17 et 26
- ✅ Tous les antagonistes/gardes sont en silhouette noire

## PHASE 4 — Livraison

Sauvegarder dans `Outputs/video_N/prompts.md` (même `N` que le `script.md` lu).

### Format d'output exact

```markdown
# PROMPTS — [SUJET]
## [TON_COMPTE] | [DATE]

---

## DESCRIPTIONS FIXES DES PERSONNAGES
[Descriptions complètes à réutiliser dans toutes les scènes — copier-coller exact]

---

## SCÈNE 1 — [NOM COURT]
**Texte script :** "[phrase(s) illustrée(s)]"
**Plan :** [Type de plan]
**Éclairage :** [Type d'éclairage]

Prompt image :
{
  "prompt": "...",
  "negative_prompt": "..."
}

Prompt animation :
{
  "prompt": "...",
  "negative_prompt": "..."
}

---

## SCÈNE 2 — [NOM COURT]
[etc.]

---

## RÉCAPITULATIF
- Nombre de scènes : [N]
- Durée totale estimée : [N x 5s = Xs]
- Notes de montage : [informations utiles pour CapCut]
```

## Ce que cet agent NE fait PAS
- ❌ N'écrit pas le script (c'est `agent-script`)
- ❌ Ne génère pas les images (Freepik — manuel)
- ❌ Ne fait pas les animations (Kling 2.5 — manuel)
- ✅ Produit uniquement les prompts prêts à copier-coller
