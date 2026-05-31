---
name: agent-audio
description: Génère la voix off MP3 d'une vidéo @chronovision.fr via l'API ElevenLabs (voix Sid). À invoquer quand l'utilisateur demande "agent audio", "générer la voix off", "génère l'audio", "ElevenLabs", ou après avoir produit script.md. Lit Outputs/Vidéo_N/script.md, le nettoie, appelle l'API, sauvegarde audio.mp3 et met à jour readme.md.
---

# Agent Audio — Génération voix off ElevenLabs pour @chronovision.fr

Rôle unique : convertir `script.md` en `audio.mp3` via ElevenLabs. Ne touche pas au script original.

## PHASE 0 — Identifier le dossier cible

Lister `Outputs/`. Cibler le dossier le plus récent contenant `script.md` mais **pas** `audio.mp3` (convention : `Vidéo_N` avec accent). Si l'utilisateur précise un numéro, l'utiliser.

## PHASE 1 — Lire et nettoyer script.md

Lire `Outputs/Vidéo_N/script.md`. Produire un texte nettoyé en appliquant ces règles :

- Supprimer toutes les lignes entre crochets `[...]` (ex. `[HOOK — 0-3s]`, `[ANCRAGE]`, etc.)
- Supprimer les lignes commençant par `#`, `**`, `→`, `⭐`, `-`, `>`
- Supprimer toute la section après `## ANALYSE PAR SECTION` (ou tout titre d'analyse)
- Supprimer les lignes de hooks alternatifs (`HOOK A`, `HOOK B`, `HOOK C`) — garder uniquement le hook choisi qui ouvre le script
- Garder le texte brut, les `...` de pause, la ponctuation et émojis éventuels
- Compacter les lignes vides multiples (max 1 ligne vide entre paragraphes)

Sauvegarder dans `Outputs/Vidéo_N/script_clean.txt`. Afficher le texte nettoyé pour validation et le nombre de caractères (`~X crédits ElevenLabs`, limite gratuite 10 000/mois).

## PHASE 2 — Vérifier dépendance Python

Vérifier que `requests` est installé : `python -c "import requests"`. Si erreur, lancer `pip install requests`.

## PHASE 3 — Appel API ElevenLabs

Vérifier que `ELEVENLABS_API_KEY` est définie dans l'environnement. Si absente, arrêter et demander à l'utilisateur de la définir : `export ELEVENLABS_API_KEY="..."` (ou sous Windows `setx ELEVENLABS_API_KEY "..."`).

Écrire un script Python `Outputs/Vidéo_N/_generate_audio.py` (temporaire, à supprimer après) :

```python
import os, sys, requests

api_key = os.environ.get("ELEVENLABS_API_KEY")
if not api_key:
    print("ELEVENLABS_API_KEY missing"); sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f:
    text = f.read().strip()

voice_id = "V8kvppYJoYqSL61Tr8Dn"
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
headers = {"Accept": "audio/mpeg", "Content-Type": "application/json", "xi-api-key": api_key}
payload = {
    "text": text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True}
}

r = requests.post(url, json=payload, headers=headers)
if r.status_code == 200:
    with open(sys.argv[2], "wb") as f:
        f.write(r.content)
    print(f"OK {len(r.content)} bytes")
else:
    print(f"ERROR {r.status_code} {r.text}"); sys.exit(1)
```

L'exécuter : `python _generate_audio.py script_clean.txt audio.mp3` depuis le dossier vidéo.

## PHASE 4 — Vérification et nettoyage

- Vérifier que `audio.mp3` existe et n'est pas vide ; afficher la taille
- Supprimer le script Python temporaire `_generate_audio.py`
- Mettre à jour `readme.md` : ajouter ou mettre à jour la ligne `Audio ElevenLabs : ✅ Généré (audio.mp3)`. Si `readme.md` n'existe pas, ne pas le créer (laisser à agent-output)

## PHASE 5 — Rapport

Afficher :
- ✅ Chemin exact de `audio.mp3`
- Taille du fichier
- Nombre de caractères consommés

## Gestion des erreurs

| Code | Cause | Action |
|---|---|---|
| 401 | Clé invalide | Vérifier `ELEVENLABS_API_KEY` |
| 429 | Crédits épuisés | Stop, prévenir l'utilisateur |
| 422 | Texte trop long | Couper le script en 2 et faire 2 appels |

## Limites

- Ne monte pas la vidéo, ne génère pas les images, ne publie rien
- N'écrase pas `script.md` ni un `audio.mp3` existant sans confirmation
