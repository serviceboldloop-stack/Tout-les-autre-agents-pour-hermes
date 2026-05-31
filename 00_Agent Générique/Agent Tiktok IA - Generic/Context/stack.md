# STACK — Pipeline de production [TON_COMPTE]
## Outils et workflow complet

---

## 1. LES OUTILS

| Outil | Rôle | Usage |
|-------|------|-------|
| **Claude (cet agent)** | Scripts + prompts | Génère le script, les prompts images et les prompts animations |
| **Freepik AI** | Génération d'images | Crée les images à partir des prompts |
| **Kling 2.5** | Animation | Anime les images générées (via Freepik) |
| **ElevenLabs** | Voix off | Convertit le script en voix narrative |
| **CapCut** | Montage final | Assemble images animées + voix + musique + sous-titres |

---

## 2. WORKFLOW COMPLET (étape par étape)

```
ÉTAPE 1 — SUJET
└── Trouver un sujet viral (agent recherche ou choix manuel)
    → Critères : personnage connu, angle inconnu, WTF moment identifiable

ÉTAPE 2 — SCRIPT (Agent script)
└── Génération du script complet
    → Hook double (ligne 1 choc + ligne 2 tease)
    → Structure optimale 60s
    → Signature + CTA débat

ÉTAPE 3 — PROMPTS (Agent prompts)
└── Génération des prompts images + animations
    → 1 prompt image par phrase / changement de scène
    → 17 à 26 images pour 60s
    → 1 prompt animation par image
    → Suffix universel + negative prompt sur chaque image

ÉTAPE 4 — GÉNÉRATION IMAGES (Manuel — Freepik)
└── Lucas génère chaque image sur Freepik
    → Ratio 9:16, style Illustration, qualité max
    → Garder le même seed pour les scènes avec mêmes personnages

ÉTAPE 5 — ANIMATION (Manuel — Kling 2.5 via Freepik)
└── Lucas anime chaque image avec le prompt animation
    → Durée cible : 4-6 secondes par clip
    → Vitesse toujours lente

ÉTAPE 6 — VOIX OFF (Manuel — ElevenLabs)
└── Lucas colle le script dans ElevenLabs
    → Voix narrative cinématique
    → Les "..." dans le script créent les pauses automatiquement

ÉTAPE 7 — MONTAGE (Manuel — CapCut)
└── Assemblage final
    → Images animées synchronisées avec la voix off
    → Musique cinématique dramatique en fond (pas de musique tendance)
    → Sous-titres si nécessaire
    → Durée finale cible : 55-65 secondes

ÉTAPE 8 — PUBLICATION
└── Post sur [TON_COMPTE]
    → Horaire cible : 21h00 – 22h30
    → Description = hook reformulé + 1 phrase résumé + CTA + hashtags
    → 4-5 hashtags max (#histoire #histoirevraie #[TON_COMPTE] #mystere + 1 sujet-spécifique)
```

---

## 3. OUTPUT PAR VIDÉO

Chaque vidéo produit un dossier dans `outputs/` :

```
outputs/
└── video_N/
    ├── script.md       → Script complet avec timing
    ├── prompts.md      → Tous les prompts images + animations numérotés
    ├── description.md  → Caption TikTok + hashtags
    └── video.mp4       → Vidéo finale montée (après production)
```

---

## 4. RÈGLES DE PRODUCTION

- **Qualité > vitesse** : ne jamais publier une vidéo avec un hook faible pour tenir la cadence
- **Seed cohérent** : garder le même seed Freepik pour toutes les scènes avec le même personnage
- **Image = première frame** : le prompt image décrit l'état initial, l'animation fait le mouvement
- **Musique** : cinématique dramatique — jamais de musique tendance incompatible avec le style historique
- **Voix** : les "..." dans le script = pauses ElevenLabs — ne jamais les retirer du script avant de coller dans ElevenLabs

---

## 5. TEMPS DE PRODUCTION ESTIMÉ PAR VIDÉO

| Étape | Temps estimé |
|-------|-------------|
| Script (agent) | ~2 minutes |
| Prompts (agent) | ~3 minutes |
| Génération images (Freepik) | ~30-45 minutes |
| Animations (Kling) | ~20-30 minutes |
| Voix off (ElevenLabs) | ~5 minutes |
| Montage (CapCut) | ~30-45 minutes |
| **Total estimé** | **~1h30 – 2h par vidéo** |

Objectif à terme avec l'agent : réduire les étapes 1-2-3 à moins de 10 minutes.
