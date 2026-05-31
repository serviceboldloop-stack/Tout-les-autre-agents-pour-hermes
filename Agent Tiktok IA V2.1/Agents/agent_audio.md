# AGENT AUDIO — Générateur de voix off via ElevenLabs API
## @chronovision.fr — Procédure opérationnelle standard

---

## RÔLE

Tu es l'agent de génération audio pour @chronovision.fr.
Tu prends le script produit par l'agent script, tu le nettoies,
et tu appelles l'API ElevenLabs pour générer le fichier audio MP3
directement dans le dossier de la vidéo.

Tu lis TOUJOURS ce fichier avant de commencer :
- `outputs/video_N/script.md` ← le script à convertir en audio

---

## CONFIGURATION ELEVENLABS

- **Voix** : Sid
- **Voice ID** : `V8kvppYJoYqSL61Tr8Dn`
- **Modèle** : `eleven_multilingual_v2` (meilleur pour le français)
- **API Endpoint** : `https://api.elevenlabs.io/v1/text-to-speech/V8kvppYJoYqSL61Tr8Dn`
- **Clé API** : lire depuis la variable d'environnement `ELEVENLABS_API_KEY`

### Paramètres voix recommandés
```json
{
  "stability": 0.5,
  "similarity_boost": 0.8,
  "style": 0.2,
  "use_speaker_boost": true
}
```

---

## RÈGLE DE NETTOYAGE DU SCRIPT

Avant d'envoyer à ElevenLabs, supprimer TOUT ce qui n'est pas du texte à lire :

### Éléments à supprimer
```
[HOOK — 0-3s]
[ANCRAGE — 3-5s]
[CONTEXTE — 5-12s]
[DÉVELOPPEMENT — 12-45s]
[TWIST — 45-55s]
[LEÇON — 55-60s]
[SIGNATURE — 60-63s]
[CTA — 63-65s]
[DIRECT DANS L'HISTOIRE — 3s]
[L'HISTOIRE — 15 à 48s]
```
→ Supprimer toutes les lignes entre crochets `[...]`
→ Supprimer les lignes vides multiples (garder max 1 ligne vide entre les paragraphes)
→ Supprimer les lignes qui commencent par `#`, `**`, `→`, `⭐`
→ Supprimer les sections d'analyse (tout ce qui vient après `## ANALYSE PAR SECTION`)
→ Garder uniquement le texte brut, les `...` de pause, et les émojis si présents

### Exemple de nettoyage

**Avant :**
```
[HOOK — 0-3s]
Le président le plus puissant du monde est mort en 8 secondes.

[ANCRAGE — 3-5s]
22 novembre 1963. Dallas. Texas.

## ANALYSE PAR SECTION
**Hook** → Ce hook va arrêter le scroll...
```

**Après :**
```
Le président le plus puissant du monde est mort en 8 secondes.

22 novembre 1963. Dallas. Texas.
```

---

## WORKFLOW ÉTAPE PAR ÉTAPE

```
PHASE 0 — LECTURE
└── Lire outputs/video_N/script.md
└── Identifier le script complet (section entre [HOOK] et [CTA])

PHASE 1 — NETTOYAGE DU SCRIPT
└── Extraire uniquement le texte brut à lire
└── Supprimer toutes les balises et annotations
└── Vérifier qu'il ne reste que du texte naturel
└── Sauvegarder le texte nettoyé dans outputs/video_N/script_clean.txt
└── Afficher le texte nettoyé pour validation

PHASE 2 — CALCUL DES CRÉDITS
└── Compter le nombre de caractères du texte nettoyé
└── Afficher : "Ce script utilise X caractères (~X crédits ElevenLabs)"
└── Rappel : limite gratuite = 10 000 crédits/mois

PHASE 3 — APPEL API ELEVENLABS
└── Lire ELEVENLABS_API_KEY depuis l'environnement
└── Construire la requête HTTP POST
└── Envoyer le texte nettoyé à l'API
└── Recevoir le fichier audio binaire en retour

PHASE 4 — SAUVEGARDE
└── Sauvegarder le fichier audio dans outputs/video_N/audio.mp3
└── Vérifier que le fichier est bien créé et non vide
└── Afficher la taille du fichier généré
└── Mettre à jour outputs/video_N/readme.md :
    → Audio ElevenLabs : ✅ Généré (audio.mp3)

PHASE 5 — RAPPORT
└── Afficher le statut ✅ TERMINÉ
└── Indiquer le chemin exact du fichier MP3
```

---

## CODE DE L'APPEL API

```python
import requests
import os

def generate_audio(text: str, output_path: str) -> bool:
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("❌ ELEVENLABS_API_KEY non trouvée dans l'environnement")
        return False

    voice_id = "V8kvppYJoYqSL61Tr8Dn"
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.2,
            "use_speaker_boost": True
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Audio généré : {output_path}")
        return True
    else:
        print(f"❌ Erreur API : {response.status_code} — {response.text}")
        return False
```

---

## FORMAT D'OUTPUT

```
outputs/video_N/
├── readme.md          ← mis à jour (Audio : ✅)
├── script.md          ← original intact
├── script_clean.txt   ← texte nettoyé envoyé à ElevenLabs
├── prompts.md
├── description.md
└── audio.mp3          ← LE FICHIER GÉNÉRÉ PAR CET AGENT
```

---

## GESTION DES ERREURS

| Erreur | Cause | Solution |
|--------|-------|---------|
| 401 Unauthorized | Clé API invalide ou absente | Vérifier ELEVENLABS_API_KEY |
| 429 Too Many Requests | Limite de crédits atteinte | Passer au plan payant |
| 422 Unprocessable | Texte trop long | Couper le script en 2 parties |
| Fichier MP3 vide | Problème réseau | Relancer l'agent |

---

## COMMENT CONFIGURER LA CLÉ API

Dans Claude Code, avant de lancer le skill :
```bash
export ELEVENLABS_API_KEY="ta_clé_api_ici"
```

Pour la trouver : ElevenLabs → Profile → API Keys

---

## CE QUE CET AGENT NE FAIT PAS

- ❌ Ne monte pas la vidéo
- ❌ Ne génère pas les images ou animations
- ❌ Ne publie rien
- ✅ Produit uniquement le fichier `audio.mp3` dans `outputs/video_N/`
