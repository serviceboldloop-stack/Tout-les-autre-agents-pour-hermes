# STYLE — @chronovision.fr
## Guide complet pour la génération d'images et d'animations

---

## 1. IDENTITÉ VISUELLE

- **Nom du style** : Dark Violet Cinematic Graphic Novel
- **Référence** : Style Mara — cartoon semi-abstrait, expressif, sombre
- **Ambiance** : Mystérieux, dramatique, oppressant, cinématique
- **Format** : 9:16 vertical (TikTok)
- **Texte dans les images** : JAMAIS

### Ce qu'est une bonne image sur ce compte
Une bonne image est une image qui :
- Illustre fidèlement ce que dit le script à ce moment précis
- Crée une sensation de malaise ou d'étrangeté — le viewer se pose des questions
- Est "chamboulante" — visuellement forte, pas neutre
- Maintient l'attention par sa composition et son atmosphère
- Ne ressemble PAS à une image IA générique — doit avoir l'air dessinée à la main

---

## 2. PALETTE DE COULEURS

| Élément | Couleur | Usage |
|---------|---------|-------|
| Fond / ombres | Deep purple violet `#2D1B4E` | Couleur dominante partout |
| Atmosphère | Desaturated purple `#4A3060` | Brume, air, distance |
| Lumière froide | Cold pale moonlight `#C8D8E8` | Éclairage nocturne principal |
| Lumière chaude | Weak amber `#8B6040` | Lampes, bougies, intérieurs |
| Flash | Harsh white `#F0F0F0` | Coups de feu, éclairs |
| Accents | Diamond sparkle `#E0E8FF` | Pierres précieuses, reflets |

**Règle absolue** : jamais de couleurs vives, saturées ou joyeuses. Palette toujours sombre et désaturée.

---

## 3. PROMPT SUFFIX UNIVERSEL
> À coller à la fin de CHAQUE prompt image sans exception.

```
dark cinematic illustration style inspired by animated graphic novel,
loose expressive brushstrokes, high contrast deep shadows,
desaturated palette with deep purple violet tones and cold pale moonlight accent,
painterly textured style, vertical 9:16 composition,
no photorealism, no text, no watermark
```

## NEGATIVE PROMPT UNIVERSEL
> À coller dans le champ négatif de CHAQUE image.

```
photorealistic, bright colors, modern elements, cheerful setting,
cartoonish flat style, blurry, low contrast, flat illustration,
text overlay, watermark, logo
```

---

## 4. FRÉQUENCE DES IMAGES

- **Règle** : une image par phrase ou par changement de scène / personnage / action
- **Volume cible** : 17 à 26 images pour une vidéo de 60 secondes
- **Principe** : illustrer TOUT — chaque phrase, chaque moment clé, chaque transition
- **Objectif** : rendre la vidéo la plus dynamique possible pour que le viewer ne se lasse jamais

> Une image = une idée du script. Quand l'idée change → nouvelle image.

---

## 5. TYPES DE PLANS

| Plan | Nom anglais | Quand l'utiliser |
|------|------------|-----------------|
| Vue d'ensemble | `Wide shot` | Établir un lieu, montrer un groupe |
| Plan moyen | `Medium shot` | Action principale, émotions |
| Gros plan | `Close-up` | Détail crucial, objet important |
| Vue subjective | `First person POV` | Immersion maximale (descendre, réveiller, marcher) |
| Par dessus l'épaule | `Over shoulder` | Confrontation, dialogue |
| Vue aérienne | `Aerial shot` | Villes, espaces, cartes |
| Détail | `Detail shot` | Objet, texture, mains |
| Double scène | `Split composition` | Deux événements simultanés |
| Ralenti extrême | `Extreme slow motion` | WTF moment visuel |

---

## 6. RÈGLES DE PERSONNAGES

### Personnages principaux
- Décrits en **détail complet et identique** dans chaque scène où ils apparaissent
- La description doit être copiée mot pour mot d'une scène à l'autre pour la cohérence

### Template personnage historique
```
[Nom] : [taille/stature], [description physique distinctive],
wearing [tenue d'époque précise], [expression/posture],
[détail caractéristique unique]
```

### Exemple validé — Tsar Nicolas II
```
Tsar Nicholas II: tall dignified man with neat dark beard and mustache,
wearing simple early 1900s Russian noble clothing,
serious composed expression, upright aristocratic posture
```

### Personnages secondaires / antagonistes / gardes / soldats
- **Silhouettes noires featureless** — jamais de visage, jamais de détail
- Corps lisibles mais sans identité
- Toujours décrits comme : `completely black featureless silhouette [rôle]`

---

## 7. ÉCLAIRAGE PAR TYPE DE SCÈNE

| Type de scène | Éclairage |
|---------------|-----------|
| Extérieur nuit | Cold pale moonlight, venant d'en haut |
| Intérieur | Weak amber lamp in corner, ombres denses |
| Action / choc / tir | Harsh white flash brutal |
| Scènes intimes | Warm amber candlelight, cercle de lumière serré |

---

## 8. SCÈNES TYPES — TEMPLATES DE PROMPT

### Scène de forêt nuit
```
dark night forest, massive ancient trees, thick undergrowth,
cold pale moonlight barely penetrating through dense canopy,
isolated pools of pale light on dark forest floor,
mist hanging low between trees, deep purple violet sky
```

### Scène d'intérieur 1900s
```
sparse [époque] Russian interior, bare wooden floor,
single weak amber lamp in corner, stone or wooden walls,
deep purple violet shadows in corners and ceiling
```

### Scène de sous-sol / cave
```
cramped stone basement room, bare stone walls and low ceiling,
single weak amber corner lamp, iron bolts on doors,
deep purple violet darkness pressing in from all sides
```

### Scène de rue historique
```
early 20th century [pays] architecture, unpaved streets,
figures as dark silhouettes, overcast grey sky,
deep purple violet atmospheric haze over the buildings
```

---

## 9. FORMAT D'UN PROMPT IMAGE COMPLET

```json
{
  "prompt": "[Type de plan] de [description de la scène], [description du/des personnage(s) si présent(s)], [éléments du décor précis + époque], [éclairage précis], [atmosphère + tension], [prompt suffix universel]",
  "negative_prompt": "photorealistic, [éléments à éviter spécifiques à la scène], cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

---

## 10. RÈGLES D'ANIMATION (Kling 2.5)

### Principe fondamental
> L'animation prolonge l'émotion de l'image — elle ne change pas la scène.

### ⚠️ RÈGLE CRITIQUE — IMAGE = PREMIÈRE FRAME UNIQUEMENT
- Le prompt image décrit la scène au démarrage, figée
- Le prompt animation décrit le MOUVEMENT qui va se passer ensuite
- Ne jamais demander à l'image une transformation complexe
- Pour une transformation : l'image montre le point de départ, l'animation fait la transition

**Exemple :**
- ❌ Image : "A needle in hay that transforms into Earth" → bugs garantis
- ✅ Image : "A needle in a pile of golden hay, warm amber light"
- ✅ Animation : "The hay slowly dissolves and transforms into the shape of the Earth"

### Vitesse
- **Toujours très lente** — jamais de mouvement rapide
- Exception : flash de coup de feu (bref et brutal, puis retour au lent)
- Durée cible : **4 à 6 secondes par clip**

### Mouvements autorisés
| Type | Description |
|------|-------------|
| `atmospheric` | Brume, lumière, vent subtil, nuages |
| `slow_zoom_in` | Très lent rapprochement caméra |
| `slow_zoom_out` | Très lent éloignement caméra |
| `parallax` | Légère séparation premier/arrière-plan |
| `light_shift` | Variation subtile de lumière, bougie qui vacille |
| `micro_motion` | Respiration, regard, cheveux dans le vent |
| `pan_slow` | Balayage très lent de la caméra |

### Interdits animation
- ❌ Lip sync ou mouvements de bouche
- ❌ Dialogue
- ❌ Actions rapides ou violentes directes
- ❌ Transitions brusques
- ✅ Toujours finir avec `no dialogue` dans le prompt

### Negative prompt animation universel
```
fast movement, lip sync, dialogue, robotic movement, glitches,
bright colors, sudden changes, fast cuts
```

---

## 11. FORMAT D'UN PROMPT ANIMATION COMPLET

```json
{
  "prompt": "[Description du mouvement très précis de l'image], [comment les éléments bougent], [atmosphère sonore suggérée si utile], no dialogue, [vitesse du mouvement]",
  "negative_prompt": "fast movement, lip sync, dialogue, robotic movement, glitches, [éléments spécifiques à éviter]"
}
```

---

## 12. CE QU'ON NE FAIT JAMAIS

- ❌ Appareils photo ou caméras dans les scènes historiques
- ❌ Éléments modernes dans des scènes d'époque
- ❌ Gore graphique — suggérer sans montrer
- ❌ Visages des gardes / soldats / antagonistes
- ❌ Couleurs vives ou lumière ambiante homogène
- ❌ Style cartoon plat ou bande dessinée classique
- ❌ Texte dans les images
- ❌ Fond blanc ou neutre
- ❌ Photorealisme

---

## 13. VARIATIONS DE STYLE

Le style de base est sombre et violet. Pour diversifier sans perdre l'identité :

| Variation | Quand l'utiliser | Modification du suffix |
|-----------|-----------------|----------------------|
| Style de base | Scènes nocturnes, mort, mystère | Aucune |
| Variation ambre | Scènes intimes, révélation douce | Remplacer "cold pale moonlight" par "warm amber candlelight" |
| Variation rouge sang | Coups de feu, violence suggérée | Ajouter "deep crimson accent" |
| Variation gris guerre | Batailles, conflits | Remplacer violet par "cold grey ash tones" |

---

## 14. PARAMÈTRES FREEPIK RECOMMANDÉS

- **Ratio** : 9:16 (Portrait — TikTok vertical)
- **Style** : Illustration / Digital Art
- **Qualité** : Maximum
- **Seed** : Garder le même seed pour les scènes avec les mêmes personnages (cohérence visuelle)
