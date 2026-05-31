# STYLE — [TON_HANDLE]
## Guide visuel pour la génération d'images et d'animations

> ⚠️ Remplis la Section 1 avec ton identité visuelle.
> Les Sections 2-4 contiennent les règles techniques universelles — ne pas modifier.

---

## 1. IDENTITÉ VISUELLE (à remplir)

- **Nom du style** : [Ex: Dark Violet Cinematic / Flat Illustration Colorée / Réaliste Sombre]
- **Ambiance** : [Ex: Mystérieux et dramatique / Énergique et positif / Sobre et pro]
- **Référence** : [Ex: style @maratrium / style documentaire / style dessin animé sombre]

### Palette de couleurs

| Élément | Couleur hex | Usage |
|---------|-------------|-------|
| Couleur dominante | #[XXX] | [Usage] |
| Lumière principale | #[XXX] | [Usage] |
| Accent | #[XXX] | [Usage] |

**Exemple rempli (niche histoire sombre) :**
| Fond / ombres | `#2D1B4E` deep purple | Couleur dominante |
| Lumière froide | `#C8D8E8` cold moonlight | Éclairage nocturne |
| Lumière chaude | `#8B6040` amber | Lampes, bougies |

### Prompt suffix universel
*(Le texte à coller à la fin de CHAQUE prompt image)*
```
[TON SUFFIX — ex:]
dark cinematic illustration style inspired by animated graphic novel,
loose expressive brushstrokes, high contrast deep shadows,
desaturated palette with deep purple violet tones and cold pale moonlight accent,
painterly textured style, vertical 9:16 composition,
no photorealism, no text, no watermark
```

### Negative prompt universel
```
[TON NEGATIVE PROMPT — ex:]
photorealistic, bright colors, modern elements, cheerful setting,
cartoonish flat style, blurry, low contrast, text overlay, watermark, logo
```

---

## 2. RÈGLES UNIVERSELLES POUR LES IMAGES

- **Ratio** : 9:16 vertical (TikTok)
- **Texte dans les images** : JAMAIS
- **Personnages principaux** : description identique mot pour mot dans toutes les scènes
- **Personnages secondaires / antagonistes** : silhouettes noires sans visage (plus rapide à générer, cohérent)
- Viser 17-26 images pour 60s (1 image par phrase / changement de scène)

### Ce qu'est une bonne image
- Illustre fidèlement le script à ce moment précis
- Crée une sensation forte — le viewer ne peut pas détourner les yeux
- Ne ressemble pas à une image IA générique — doit paraître dessinée / peinte

---

## 3. RÈGLES D'ANIMATION (Kling 2.5 / Runway / Pika)

**Principe** : l'animation prolonge l'émotion de l'image — elle ne change pas la scène

**Format économique (économise 70% de tokens) :**
```
"Continue from generated image — [mouvement à ajouter]"
```
❌ Ancien : redécrire toute la scène (300+ mots)
✅ Nouveau : `Continue from generated image — slow zoom in, atmospheric mist rising` (~10 mots)

### Mouvements autorisés
| Type | Description |
|------|-------------|
| `atmospheric` | Brume, lumière, vent subtil, nuages |
| `slow_zoom_in` | Très lent rapprochement caméra |
| `slow_zoom_out` | Très lent éloignement caméra |
| `parallax` | Légère séparation premier/arrière-plan |
| `light_shift` | Variation subtile de lumière |
| `micro_motion` | Respiration, regard, cheveux dans le vent |
| `pan_slow` | Balayage très lent de la caméra |

### Interdits animation
- ❌ Lip sync ou mouvements de bouche
- ❌ Dialogue
- ❌ Mouvements rapides / caméra agitée
- ❌ Transitions brusques

**Durée cible** : 4-6 secondes par clip | **Vitesse** : toujours très lente

---

## 4. ÉCLAIRAGE PAR TYPE DE SCÈNE

| Scène | Éclairage recommandé |
|-------|---------------------|
| Extérieur nuit | `cold pale moonlight barely penetrating` |
| Intérieur ancien | `single weak amber lamp, deep shadows` |
| Action / violence | `harsh white flash briefly illuminating` |
| Révélation / twist | `single spotlight from above` |
| Mort / deuil | `cold pale moonlight, deep darkness pressing in` |
| [Ta scène type] | [Ton éclairage] |
