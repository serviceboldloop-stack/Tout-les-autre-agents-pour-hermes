# stack.md — Comment utiliser Agent Sport V1

> Guide d'utilisation du système pour Lucas.

---

## Démarrage rapide

1. **Ouvrir Claude Code** dans le dossier `Agent Sport V1/`
2. **Dire ce que tu veux** — l'agent route automatiquement vers le bon coach

## Exemples de commandes

### Nutrition
- `"nutrition"` → Active le coach nutrition
- `"qu'est-ce que je mange ce soir pour la séance de demain ?"` → Plan pré-workout
- `"j'ai pas atteint mes calories aujourd'hui, qu'est-ce que j'ajoute ?"` → Solution rapide
- `"donne-moi un petit-dej prise de masse"`

### Musculation
- `"muscu"` ou `"séance du lundi"` → Programme PUSH complet du jour
- `"je suis en semaine 3 du cycle, donne-moi ma séance"` → RIR adapté automatiquement
- `"j'ai fait développé couché à 25kg × 10/10/10/9"` → Analyse + recommandation prochaine séance
- `"j'ai mal à l'épaule, qu'est-ce que j'évite ?"` → Adaptations

### Football
- `"foot"` → Active le coach football
- `"séance technique ce soir"` → Séance solo 60 min structure complète
- `"j'ai un match demain"` → Préparation mentale + nutrition + muscu léger ou pas
- `"RSA aujourd'hui"` → Protocole selon poste

### Questions mixtes
- `"je stagne depuis 3 semaines"` → Diagnostic croisé (nutrition + muscu + récup)
- `"check semaine"` → Récap de tout (entraînements faits, nutrition on track ?)
- `"j'ai un match samedi, est-ce que je fais legs vendredi ?"` → Décision coordinée

---

## Mise à jour des infos

Pour que l'agent soit précis, mettre à jour ces infos régulièrement :

| Info | Comment | Fichier |
|---|---|---|
| Charges muscu | "note mes perfs : développé couché 27,5kg × 10/10/10/10" | `Data/progression.md` |
| Semaine du cycle RIR | "je suis en semaine 4 du cycle" | `Context/programme_muscu.md` |
| Niveau football | "je me réévalue : contrôle 3/5, cardio 2/5..." | `Context/profil.md` |
| Nouveau équipement | "j'ai acheté un banc" | `Context/profil.md` + `Context/programme_muscu.md` |
| Profil foot | Lors du 1er onboarding foot | `Context/profil.md` |

---

## Recherche web

Si une question n'est pas couverte par la base de connaissances :
→ L'agent dit "Je fais une recherche web"
→ Effectue la recherche
→ Synthétise et cite les URLs sources

Déclencher manuellement : `"cherche sur le web [sujet]"`

---

## Structure des réponses

L'agent répond toujours avec des **chiffres concrets** :
- Charges, séries, reps, temps de repos — jamais vague
- Calories, grammes de protéines — jamais "mange plus"
- Durées de séance, nombre de répétitions d'exercice

Ton : **direct, dense** — pas de blabla, pas de recap inutile.

---

## Connexion avec d'autres agents

Ce système est connecté à :
- **Mon Bro Cerveau** — wiki de connaissances de Lucas (documentation complète des agents)
- **Agent Marketing V1** — si une question touche le business de Lucas

Pour accéder au Cerveau : `C:\Users\chapo\Documents\Mon Bro Cerveau\`
