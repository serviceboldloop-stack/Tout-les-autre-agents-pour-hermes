# PROMPTS EXEMPLE — Script Romanov
## Référence complète : 22 scènes image + animation

---

## SCRIPT DE RÉFÉRENCE
Sujet : Famille Romanov / Nicolas II
Stats : 402 vues | 36% rétention 5s | 63s

---

## DESCRIPTIONS FIXES DES PERSONNAGES
> À réutiliser mot pour mot dans chaque scène où ils apparaissent

**Tsar Nicolas II :**
```
Tsar Nicholas II: tall dignified man with neat dark beard and mustache,
wearing simple early 1900s Russian noble clothing,
serious composed expression, upright aristocratic posture
```

**Famille impériale russe :**
```
Russian imperial family 1918: father tall dignified man with neat dark beard,
mother elegant woman in period dress with hair pinned up,
five children of varying ages in early 1900s Russian clothing,
all rendered with period accurate appearance
```

---

## RÈGLE DE TIMING — PHRASE → IMAGE

| Situation | Règle |
|-----------|-------|
| Phrase normale (8-12 mots) | 1 phrase = 1 image |
| Phrases très courtes (1-4 mots) | Grouper 2-3 phrases sur 1 image |
| Changement de lieu / personnage | Toujours nouvelle image |
| Moment d'action fort | 1 image par action |
| Exemple : "Kennedy s'effondre." + "Sa femme le tient." + "Le sang sur sa robe." | 3 images séparées — chaque détail mérite sa propre image |

---

## LES 22 SCÈNES

### SCÈNE 1 — FAMILLE DANS LA FORÊT LA NUIT
**Texte script :** "Une famille entière a disparu en une nuit."
**Plan :** Wide shot
**Éclairage :** Cold pale moonlight

```json
{
  "prompt": "Wide shot of the Russian imperial family standing together in a dark forest at night, father tall dignified man with neat dark beard in early 1900s Russian noble clothing, mother elegant woman in period dress with hair pinned up, five children of varying ages in early 1900s Russian clothing, all holding hands or standing close together, their figures barely illuminated by a single cold pale moonlight beam through the dark trees above, deep purple violet night forest surrounding them on all sides, their faces barely visible in the darkness, the last moment of a family together, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and cold pale moonlight accent, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, bright colors, modern clothing, cameras or photography equipment, cheerful setting, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The Russian imperial family standing together in the dark forest, all holding hands, the cold pale moonlight beam through the trees shifting very slightly, the family's figures barely moving, the dark forest surrounding them pressing in slowly, no dialogue, very faint cold wind through forest trees, extremely slow atmospheric motion",
  "negative_prompt": "fast movement, bright colors, family separating, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 2 — CORPS RETROUVÉS DANS LA FORÊT
**Texte script :** "On n'a retrouvé les corps que 70 ans plus tard."
**Plan :** Close medium shot
**Éclairage :** Cold pale light from above

```json
{
  "prompt": "Close medium shot of excavation in a dark forest, several white cloth covered forms lying in a dark earthen pit, archaeologists or investigators as completely black featureless silhouettes crouching around the pit, one silhouette carefully brushing away earth from a white covered form, old forest roots and dark earth visible around the pit, cold pale light from above illuminating the discovery, deep purple violet atmospheric forest darkness surrounding the excavation site, the weight of 70 years conveyed in the earth covered forms, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and cold pale light, painterly textured style, vertical 9:16 composition, no photorealism, no graphic gore, no text, no watermark",
  "negative_prompt": "photorealistic, bright colors, faces visible, modern equipment, graphic gore, empty pit, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The black featureless silhouette investigators crouching around the dark earthen pit move very slowly and deliberately, one silhouette carefully brushing earth away from a white covered form with slow methodical strokes, cold pale light from above unchanging, deep purple violet forest darkness completely still around the excavation, slow reverent motion, no dialogue",
  "negative_prompt": "fast movement, bright colors, investigators running, graphic gore, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 3 — EKATERINBOURG 1918
**Texte script :** "17 juillet 1918. Ekaterinbourg. Russie."
**Plan :** Wide establishing shot
**Éclairage :** Overcast grey sky + violet haze

```json
{
  "prompt": "Wide establishing shot of Ekaterinburg Russia in summer 1918, early 20th century Russian provincial architecture with wooden buildings and unpaved streets, a few figures in period clothing visible as dark silhouettes on the street, overcast grey sky above, deep purple violet atmospheric haze over the town, the oppressive tension of revolutionary Russia visible in the empty quiet streets, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and muted grey accent, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, modern buildings, bright colors, cheerful atmosphere, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "Very slow aerial push in descending toward the Ekaterinburg street, the early 20th century Russian buildings growing slightly closer, dark silhouette figures on the street moving very slowly, deep purple violet haze drifting across the town, the oppressive tension conveyed through the slow heavy atmosphere, no dialogue, smooth slow aerial descent",
  "negative_prompt": "fast movement, pulling back, bright colors, cheerful movement, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 4 — LA FAMILLE PRISONNIÈRE
**Texte script :** "Le Tsar Nicolas II est prisonnier depuis un an. Lui. Sa femme. Ses cinq enfants. Enfermés dans une maison sous surveillance constante."
**Plan :** Wide shot intérieur
**Éclairage :** Weak amber lamp + violet shadows

```json
{
  "prompt": "Wide shot inside a sparse 1918 Russian house interior, the Russian imperial family gathered in a bare room, father tall dignified man with neat dark beard in simple clothing, mother elegant woman in period dress, five children of varying ages, all together in the confined space, black featureless silhouette guards visible through windows and doorways surrounding the house, the family visible in the dim interior amber lamp light, deep purple violet shadows pressing in from the guarded perimeters, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and weak amber interior light, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, guards faces visible, bright colors, luxurious interior, family looking free, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The Russian imperial family inside the sparse room, their movements minimal and resigned, the black featureless guard silhouettes visible through windows remaining completely still and watchful, the weak amber lamp inside flickering very slightly, deep purple violet shadows pressing in, no dialogue, faint distant guard footsteps outside, slow confined motion",
  "negative_prompt": "fast movement, guards facing away, bright colors, family trying to escape, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 5 — PORTE QUI SE FERME
**Texte script :** "Enfermés dans une maison sous surveillance constante."
**Plan :** Medium shot — caméra qui recule
**Éclairage :** Lumière qui disparaît

```json
{
  "prompt": "Medium shot of a heavy wooden door slamming shut, viewed from inside a dark sparse 1918 Russian room, the door closing violently with the camera pulling back simultaneously, the last sliver of light from outside disappearing as the door shuts completely, iron bolts and locks visible on the door, deep purple violet darkness consuming the room as the door closes, the family's silhouettes barely visible receding as the camera pulls back from the closing door, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and disappearing amber light crack, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, door opening, bright colors, faces visible, modern door, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The heavy wooden door slams shut in slow motion, the camera simultaneously pulling back as the door closes, the last sliver of amber light from outside shrinking and disappearing as the door seals completely, iron bolts sliding into place with finality, deep purple violet darkness consuming the room, no dialogue, slow heavy door slam and bolts locking, dramatic slow door closing and camera retreat motion",
  "negative_prompt": "fast movement, door opening, bright light remaining, camera not pulling back, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 6 — POV RÉVEILLER LE TSAR À MINUIT
**Texte script :** "Cette nuit-là on les réveille à minuit."
**Plan :** First person POV
**Éclairage :** Cold pale moonlight + weak lamp

```json
{
  "prompt": "First person POV shot looking down at Tsar Nicholas II waking from sleep, tall dignified man with neat dark beard in simple 1918 sleeping clothes, his eyes opening with confusion and alarm, his wife barely visible beside him also waking, the sparse 1918 Russian bedroom interior with bare wooden floor and single weak lamp barely visible, deep purple violet darkness surrounding the bed, cold pale moonlight through a small window barely illuminating the scene, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and weak pale light, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, bright room, tsar standing, modern bedroom, third person view, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The POV looking down at Tsar Nicholas II, his eyes opening slowly with confusion then growing alarm, his wife beside him also stirring awake, their disoriented expressions shifting from sleep to fear, cold pale moonlight through the small window barely illuminating their faces, no dialogue, faint sound of someone being shaken awake then silence, slow disorienting awakening motion",
  "negative_prompt": "fast movement, tsar already standing, bright room, calm expression, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 7 — LA FAMILLE S'HABILLE
**Texte script :** "On leur dit de s'habiller."
**Plan :** Medium wide shot
**Éclairage :** Weak amber lamp

```json
{
  "prompt": "Medium wide shot of the Russian imperial family dressing quickly in their sparse 1918 Russian room, father tall dignified man with neat dark beard pulling on his coat, mother helping the youngest children dress, older children dressing themselves, all moving with confused urgency in the dim light, the bare wooden room barely illuminated by a single weak amber lamp, deep purple violet shadows in the corners, the midnight disruption visible in their disheveled half-dressed state, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and weak amber lamp accent, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, bright colors, family fully dressed, modern clothing, relaxed atmosphere, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The Russian imperial family dresses with confused urgency, father pulling his coat on, mother helping the youngest children, all moving with the disoriented haste of midnight awakening, the weak amber lamp flickering slightly, no dialogue, faint sounds of rustling clothing and children being dressed, slow urgent dressing motion",
  "negative_prompt": "fast movement, family fully dressed already, bright colors, relaxed motion, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 8 — LA FAMILLE TRANSFÉRÉE PAR LES GARDES
**Texte script :** "On leur dit qu'on les transfère pour leur sécurité."
**Plan :** Wide shot — couloir
**Éclairage :** Single weak lamp ahead

```json
{
  "prompt": "Wide shot of the Russian imperial family being escorted through a dark corridor by completely black featureless silhouette guards, father tall dignified man with neat dark beard at the front, mother and five children following, the guard silhouettes surrounding them on all sides, a single weak amber lamp ahead guiding the procession, deep purple violet atmospheric darkness surrounding the group, the false promise of safety in the escort visible in the trusting posture of the family, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and weak amber lamp ahead, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, guard faces visible, bright colors, family resisting, modern corridor, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The Russian imperial family moves slowly forward through the dark corridor escorted by black featureless silhouette guards surrounding them, the single weak amber lamp ahead moving backward as the procession advances, deep purple violet darkness surrounding the group, no dialogue, slow shuffling footsteps on stone floor, slow escorted procession motion",
  "negative_prompt": "fast movement, guard faces visible, bright corridor, family resisting, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 9 — POV TSAR DESCEND AU SOUS-SOL
**Texte script :** "Ils descendent au sous-sol. Onze personnes dans une petite pièce."
**Plan :** First person POV — descente
**Éclairage :** Single weak lamp at bottom

```json
{
  "prompt": "First person POV shot from Tsar Nicholas II's perspective descending stone basement stairs, his hands visible on the rough stone walls for balance as he descends, the stairs going down into a dimly lit basement room below, at the bottom a small bare room with stone walls, a single weak lamp in the corner, eleven people already gathered as dark silhouettes waiting in the confined space, deep purple violet shadows throughout, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and single weak lamp accent below, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, bright basement, empty room, modern stairs, third person view, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The POV slowly descends the stone basement stairs, the hands visible pressing against the rough stone walls moving downward step by step, the small cramped basement room below slowly coming into view, the eleven dark silhouette figures waiting at the bottom becoming more visible with each step, no dialogue, slow footsteps on stone stairs descending, slow deliberate descent motion",
  "negative_prompt": "fast movement, ascending stairs, bright basement, empty room below, third person view, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 10 — LA PORTE SE FERME AU SOUS-SOL
**Texte script :** "La porte se ferme."
**Plan :** Medium shot — finalité
**Éclairage :** Single weak corner lamp

```json
{
  "prompt": "Medium shot of a heavy wooden basement door slamming shut, viewed from inside the small stone basement room, iron bolts sliding into place visible through the crack before it seals completely, the family silhouettes pressing backward as the door closes, the single weak lamp in the corner of the stone basement the only remaining light, deep purple violet darkness pressing in from all sides as the door seals, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and single weak lamp accent, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, door opening, bright colors, modern door, large room, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The heavy wooden basement door slams shut with finality, iron bolts visible sliding into place through the narrowing crack, the last light from outside disappearing completely as the door seals, the single weak amber corner lamp the only remaining light in the sealed stone basement, no dialogue, heavy door slam and bolts locking sound, slow heavy sealing motion",
  "negative_prompt": "fast movement, door staying open, bright light, family moving forward, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 11 — POV TSAR VOIT L'OFFICIER ENTRER
**Texte script :** "Un officier entre."
**Plan :** First person POV
**Éclairage :** Weak amber corner lamp

```json
{
  "prompt": "First person POV shot from Tsar Nicholas II's perspective inside the small stone basement room, looking at the door as it opens and a Soviet military officer enters, the officer rendered as a dark silhouette with his uniform shape barely visible in the weak lamp light, the door open behind him showing only darkness beyond, the family pressed together on both sides of the POV, deep purple violet shadows filling the room, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and weak amber lamp, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, officer face visible, bright basement, modern room, third person view, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The door in the POV slowly opens, the dark silhouette officer stepping through into the cramped stone basement room, his uniform silhouette moving forward deliberately, the darkness beyond the open door visible behind him, the family pressed together on both sides shifting slightly in alarm, no dialogue, slow door opening and deliberate footsteps entering, slow ominous entering motion",
  "negative_prompt": "fast movement, officer face visible, bright basement, family calm, third person view, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 12 — POV OFFICIER LIT L'ORDRE D'EXÉCUTION
**Texte script :** "Il lit un ordre d'exécution. Le Tsar n'a pas le temps de répondre."
**Plan :** First person POV — officier avance
**Éclairage :** Weak amber corner lamp

```json
{
  "prompt": "First person POV shot from the officer's perspective walking slowly into the stone basement room toward the family, a document held in the dark featureless hand in the lower foreground being read, the Russian imperial family visible ahead pressed against the stone wall, father tall dignified man with neat dark beard in front protecting his family, mother and five children behind him, all looking at the approaching figure with growing alarm, cramped stone basement with bare walls and single weak amber corner lamp, deep purple violet shadows throughout, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and weak amber accent, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, faces clearly visible, bright basement, modern room, family relaxed, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The POV moves slowly forward toward the family, the dark featureless hand in the foreground holding the document slightly raised, the Russian imperial family ahead pressed against the stone wall, father stepping slightly forward instinctively to protect his family, their expressions shifting from confusion to understanding to terror, no dialogue, slow footsteps and faint paper sound, slow advancing motion",
  "negative_prompt": "fast movement, family relaxed, bright basement, officer face visible, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 13 — LES SOLDATS TIRENT
**Texte script :** "Les coups de feu commencent."
**Plan :** Dramatic wide shot — muzzle flashes
**Éclairage :** Harsh white flash + violet darkness

```json
{
  "prompt": "Dramatic wide shot inside the small stone basement room, multiple completely black featureless silhouette soldiers in a line raising their rifles and firing toward the family huddled against the far wall, muzzle flashes briefly illuminating the dark cramped room in harsh white light, smoke rising from the rifles, the stone walls visible on all sides, deep purple violet darkness surrounding the brief harsh flash of the shots, no graphic gore just the terrible action of the volley firing, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and harsh white muzzle flash accent, painterly textured style, vertical 9:16 composition, no photorealism, no graphic gore, no text, no watermark",
  "negative_prompt": "photorealistic, soldier faces visible, graphic gore, blood, bright colors, family running, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The black featureless silhouette soldiers raise their rifles in slow unison and fire, multiple muzzle flashes erupting simultaneously in harsh white light briefly illuminating the entire cramped stone basement, smoke rising from the rifles, deep purple violet darkness returning between flashes, no dialogue, multiple simultaneous gunshots echoing in the enclosed stone basement, dramatic slow motion volley firing",
  "negative_prompt": "fast movement, soldier faces visible, graphic gore, blood, bright constant lighting, family running, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 14 — BALLES QUI REBONDISSENT (RALENTI)
**Texte script :** "Les balles rebondissent sur les enfants."
**Plan :** Extreme slow motion
**Éclairage :** Deep purple violet + spark accents

```json
{
  "prompt": "Extreme slow motion cinematic shot of bullets visibly deflecting and ricocheting off the clothing of child figures in the basement, the bullets caught mid-air changing direction in slow motion with visible motion trails, sparks of impact visible at the deflection points on the children's clothing, deep purple violet atmospheric darkness surrounding the impossible slow motion moment, the bullets clearly bouncing off rather than penetrating, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and brief spark accents, painterly textured style, vertical 9:16 composition, no photorealism, no graphic gore, no text, no watermark",
  "negative_prompt": "photorealistic, bullets penetrating, graphic gore, blood, fast motion, bright colors, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "Bullets travel in extreme slow motion toward the children's clothing then visibly deflect and ricochet away at sharp angles, motion trails following each bullet's path and deflection, sparks of impact visible at each deflection point, the bullets clearly changing direction rather than penetrating, multiple deflections happening simultaneously in slow motion, no dialogue, strange metallic ricocheting sounds in slow motion, extreme slow motion deflection",
  "negative_prompt": "fast motion, bullets penetrating, graphic gore, blood, bright colors, single deflection only, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 15 — SOLDATS PANIQUENT
**Texte script :** "Les soldats paniquent. Ils ne comprennent pas."
**Plan :** Medium wide shot
**Éclairage :** Weak amber lamp

```json
{
  "prompt": "Medium wide shot of the black featureless silhouette soldiers in the basement, their formation broken, some stepping backward in confusion and shock, their rifles lowered in disbelief, their body language conveying complete panic and incomprehension, the cramped stone basement room with bare walls and single weak amber corner lamp, deep purple violet shadows throughout, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and weak amber accent, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, soldier faces visible, bright colors, soldiers advancing confidently, modern room, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The black featureless silhouette soldiers break formation slowly, some stepping backward in disbelief, their rifles lowering as their body language shifts from execution to absolute confusion, the weak amber lamp still burning in the corner, no dialogue, confused murmuring sounds, slow panicked disintegrating formation motion",
  "negative_prompt": "fast movement, soldiers advancing, confident posture, bright colors, faces visible, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 16 — POV COUDRE LES DIAMANTS
**Texte script :** "La Tsarine avait cousu des diamants dans les vêtements des enfants."
**Plan :** First person POV — mains qui cousent
**Éclairage :** Warm amber candlelight + diamond sparkle

```json
{
  "prompt": "First person POV shot looking down at elegant hands in early 1900s period clothing carefully sewing small glittering diamonds and precious stones into the lining of a child's garment, the needle and thread visible working around multiple small sparkling gemstones being embedded in the fabric, dozens of tiny diamonds visible already sewn into the garment lining, warm amber candlelight catching the sparkle of each precious stone as it is sewn in, deep purple violet shadows surrounding the close intimate shot, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and warm amber candlelight with diamond sparkle accents, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, modern clothing, bright electric light, few or no diamonds, hands not sewing, third person view, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The elegant hands in the POV slowly and carefully push the needle through the garment fabric around a tiny diamond, pulling the thread through to secure another precious stone into the lining, each stitch slow and deliberate, the dozens of diamonds already sewn catching the warm amber candlelight and sparkling as the hands work, no dialogue, very faint sound of needle through fabric and thread pulling, slow careful sewing motion",
  "negative_prompt": "fast movement, hands stopping, bright electric light, few diamonds, careless sewing, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 17 — ARMURE INVISIBLE DE DIAMANTS
**Texte script :** "Des centaines de pierres précieuses. Qui formaient une armure invisible."
**Plan :** Close medium shot — vêtement ouvert
**Éclairage :** Warm amber candlelight + diamond sparkle

```json
{
  "prompt": "Close medium shot of a child's early 1900s Russian garment laid flat, the fabric cut open to reveal hundreds of tiny glittering diamonds and precious stones sewn densely into every layer of the lining, the gemstones forming a complete invisible armor throughout the entire garment, warm amber candlelight catching every facet of every stone making the opened garment glow with countless points of light, deep purple violet shadows surrounding the opened garment, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and warm amber and diamond sparkle accents throughout, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, empty lining, few diamonds, bright electric light, modern clothing, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The opened child's garment lies completely still, the hundreds of diamonds densely sewn throughout the lining catching warm amber candlelight and creating hundreds of tiny sparkling points of light across the entire garment, the candlelight flickering very slightly causing the diamonds to shimmer more intensely with each flicker, no dialogue, very faint candle crackling, slow sparkling shimmer motion",
  "negative_prompt": "fast movement, few diamonds, bright electric light, garment closed, cartoonish sparkle, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 18 — DRAP SUR LES ENFANTS
**Texte script :** "Les enfants ont survécu aux balles. Mais pas à ce qui a suivi après."
**Plan :** Close medium shot
**Éclairage :** Weak amber corner lamp

```json
{
  "prompt": "Close medium shot of small white cloth covered forms lying still on the cold stone floor of the basement, the shapes clearly those of children of different sizes, completely covered, a black featureless hand just visible at the edge of frame placing the last white cloth over the smallest form, single weak amber lamp in the corner casting final shadows, deep purple violet darkness consuming the stone room, no graphic content just the white covered forms, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and weak amber accent, painterly textured style, vertical 9:16 composition, no photorealism, no graphic gore, no text, no watermark",
  "negative_prompt": "photorealistic, graphic gore, blood, bright colors, forms moving, modern room, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The black featureless hand at the edge of frame slowly lowers the last white cloth over the smallest form on the cold stone basement floor, the white cloth descending in slow motion, the form disappearing beneath it, the other white covered forms already completely still around it, the weak amber corner lamp casting unchanging light, no dialogue, complete silence, agonizingly slow final covering motion",
  "negative_prompt": "fast movement, forms moving, graphic gore, bright colors, forms uncovered, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 19 — POV ENTERRER LES CORPS
**Texte script :** "Les corps ont été cachés. Déplacés deux fois."
**Plan :** First person POV — enterrement
**Éclairage :** Cold pale moonlight

```json
{
  "prompt": "First person POV shot looking down into a dark forest at night, two large rough hands in the foreground holding a shovel digging into dark earth, white cloth covered forms barely visible at the bottom of a shallow pit below, dark forest trees surrounding the excavation at night, cold pale moonlight barely illuminating the scene, deep purple violet night forest darkness surrounding the burial site, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and cold pale moonlight accent, painterly textured style, vertical 9:16 composition, no photorealism, no graphic gore, no text, no watermark",
  "negative_prompt": "photorealistic, bright forest, bodies visible clearly, modern tools, third person view, graphic gore, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The POV looking down into the dark forest, the two large rough hands in the foreground push the shovel into the dark earth slowly and deliberately, lifting earth and depositing it over the white cloth covered forms at the bottom of the pit, each slow shovel movement covering the forms more completely, no dialogue, slow rhythmic sound of shovel in earth, slow deliberate burial motion",
  "negative_prompt": "fast movement, bright forest, third person view, forms not being covered, modern tools, graphic gore, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 20 — DEUX ENDROITS D'ENTERREMENT (SPLIT)
**Texte script :** "Enterrés dans deux endroits différents."
**Plan :** Split composition — deux scènes simultanées
**Éclairage :** Cold pale moonlight — les deux côtés

```json
{
  "prompt": "Wide split composition showing two simultaneous forest burial scenes happening side by side, on the left side black featureless silhouette figures burying forms in a dark forest pit at night, on the right side different black featureless silhouette figures burying different forms in a separate dark forest location at night, both scenes in deep purple violet night forest darkness with cold pale moonlight barely visible, the two separate burials of the separated family remains shown simultaneously, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and cold pale moonlight accent, painterly textured style, vertical 9:16 composition, no photorealism, no graphic gore, no text, no watermark",
  "negative_prompt": "photorealistic, single scene, bright forest, silhouette faces visible, graphic gore, modern elements, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "Both forest burial scenes in the split composition move simultaneously, the black featureless silhouette figures on both sides digging and covering in synchronized slow motion, both scenes in deep purple violet night forest darkness, the two separate burials progressing together at the same pace, no dialogue, faint synchronized digging sounds on both sides, slow synchronized dual burial motion",
  "negative_prompt": "fast movement, single scene only, bright forest, graphic gore, faces visible, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 21 — FORÊT MYSTIQUE 70 ANS PLUS TARD
**Texte script :** "Pendant 70 ans… la famille royale la plus puissante d'Europe gisait dans une forêt inconnue."
**Plan :** Wide atmospheric shot
**Éclairage :** Cold pale moonlight + mist

```json
{
  "prompt": "Wide atmospheric shot of a vast dark Russian forest in deep night, massive ancient trees stretching upward into deep purple violet sky, thick undergrowth covering the forest floor, cold pale moonlight barely penetrating through the dense canopy above creating isolated pools of pale light on the dark forest floor, mist hanging low between the trees, the forest completely silent and still, somewhere beneath the roots and earth the secret of 70 years lies hidden, deeply mysterious and foreboding atmosphere, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and cold pale moonlight accents, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, bright daylight forest, cheerful atmosphere, people visible, modern elements, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The vast dark Russian forest remains almost completely still, only the faintest movement of mist drifting low between the massive trees, isolated pools of cold pale moonlight on the dark forest floor shifting imperceptibly, the absolute silence and stillness of a forest keeping a 70 year secret, no dialogue, complete near silence with only the faintest distant forest wind, almost imperceptible atmospheric mist motion",
  "negative_prompt": "fast movement, bright daylight, people visible, cheerful sounds, lip sync, dialogue, robotic movement, glitches"
}
```

---

### SCÈNE 22 — TRÔNE VIDE
**Texte script :** "Parfois… même les plus puissants disparaissent sans laisser de trace."
**Plan :** Dramatic wide shot
**Éclairage :** Single amber spotlight on empty throne

```json
{
  "prompt": "Dramatic wide shot of an empty ornate throne room, a massive empty throne on a raised platform at the far end, the throne illuminated by a single amber light beam from above, the vast room completely empty around it, imperial decorations and high ceilings stretching into deep purple violet darkness above, the floor leading to the throne completely empty, the absence of power more powerful than its presence, the throne abandoned and alone, dark cinematic illustration style inspired by animated graphic novel, loose expressive brushstrokes, high contrast deep shadows, desaturated palette with deep purple violet tones and single amber spotlight on empty throne, painterly textured style, vertical 9:16 composition, no photorealism, no text, no watermark",
  "negative_prompt": "photorealistic, person on throne, bright colors, modern room, cartoonish, blurry, flat illustration, text overlay, watermark"
}
```

**Animation :**
```json
{
  "prompt": "The massive empty throne in the vast ornate room sits completely alone, the single amber light beam from above holding steady on it, dust particles floating almost imperceptibly in the beam of light, the deep purple violet darkness above and around the throne completely still and empty, the silence of absolute abandoned power growing more profound, no dialogue, complete silence, almost imperceptible dust particle floating motion",
  "negative_prompt": "fast movement, person appearing on throne, bright colors, room filling with people, lip sync, dialogue, robotic movement, glitches"
}
```
