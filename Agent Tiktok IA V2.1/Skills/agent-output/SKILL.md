---
name: agent-output
description: Organise le dossier final d'une vidéo @chronovision.fr — génère description TikTok et readme récapitulatif à partir du script existant. À utiliser quand l'utilisateur demande "agent output", "finaliser la vidéo", "générer la description", "préparer le dossier final", ou après avoir produit le script. Ne touche jamais à script.md, n'écrase jamais un dossier existant.
---

# Agent Output — Organisateur de dossier vidéo @chronovision.fr

Rôle unique : récupérer ce que `agent-script` a produit, générer `description.md` et `readme.md`, livrer un dossier `Outputs/Vidéo_N/` complet et propre.

## PHASE 0 — Lecture obligatoire

Lire en parallèle :
- `Template/description_template.md` — format exact de la caption TikTok
- `Context/tiktok_rules.md` — règles algorithme, CTA, hashtags
- `Outputs/Vidéo_N/script.md` — produit par agent-script (ne pas modifier)

## PHASE 1 — Identification du dossier cible

- Lister `Outputs/` et lire les noms de dossiers existants (convention : `Vidéo_N` avec accent).
- Cibler le dossier le plus récent qui contient `script.md` mais **pas** `description.md` ni `readme.md` → c'est le dossier à finaliser.
- Si aucun dossier de ce type n'existe et qu'il faut en créer un nouveau pour un script à venir : prendre `N = (max existant) + 1`, ou `1` si `Outputs/` est vide.
- **Jamais écraser un dossier existant.** Si `description.md` ou `readme.md` existent déjà dans le dossier cible, demander confirmation à l'utilisateur avant tout écrasement.

## PHASE 2 — Génération de description.md

- Extraire du `script.md` : sujet, hook choisi (A/B/C), CTA final, personnage central.
- Choisir le hashtag variable d'après le personnage/événement (`#jfk`, `#lincoln`, `#raspoutine`, `#tsar`, etc.).
- Choisir l'emoji thématique selon le type de sujet (table emojis du template).
- Rédiger selon `Template/description_template.md` :
  1. Hook reformulé + emoji (garder les chiffres précis)
  2. Phrase résumé mystérieuse (sans spoiler le twist ironique)
  3. CTA enregistrement : "Enregistre cette vidéo, tu vas vouloir la revoir." 💾
  4. CTA partage : "Envoie ça à quelqu'un qui croit encore à la version officielle." 👥
  5. CTA débat : Question ouverte du script dont la réponse n'est PAS dans le script 👇
  6. 4-5 hashtags : `#[variable] #histoire #chronovision #mystere #tiktokfr`
- Vérifier : pas de `#foryou`/`#viral`/`#pourtoi`, pas plus de 5 hashtags, réponse au CTA débat hors du script, pas de spoiler du twist.

### Format `description.md`

```markdown
# DESCRIPTION — [SUJET]
## @chronovision.fr | [DATE]

---

## CAPTION TIKTOK (à copier-coller)

[Ligne 1 — Hook reformulé + emoji]
[Ligne 2 — Phrase résumé mystérieuse]
Enregistre cette vidéo, tu vas vouloir la revoir. 💾
Envoie ça à quelqu'un qui croit encore à la version officielle. 👥
[Ligne 5 — CTA débat — question ouverte dont la réponse n'est PAS dans le script] 👇
[Ligne 6 — Hashtags]

---

## NOTES DE PUBLICATION

- **Horaire recommandé** : 21h00 – 22h30
- **Hashtag variable** : #[sujet]
- **Hook utilisé** : [Rappel du hook choisi]
- **Type de CTA** : [Débat / Théorie / Projection]
```

## PHASE 3 — Génération de readme.md

Récapitulatif complet pour Lucas. Extraire de `script.md` : sujet, angle, hook recommandé, durée estimée, potentiel viral.

### Format `readme.md`

```markdown
# VIDEO [N] — [SUJET EN MAJUSCULES]
## @chronovision.fr | [DATE]

---

## RÉCAPITULATIF

| Élément | Statut |
|---------|--------|
| Script | ✅ Prêt |
| Description TikTok | ✅ Prêt |
| Production visuelle | ⬜ À faire |
| Montage CapCut | ⬜ À faire |
| Publication | ⬜ À faire |

---

## INFORMATIONS CLÉS

- **Sujet** : [Sujet traité]
- **Angle** : [L'angle choisi]
- **Hook recommandé** : [Hook A/B/C + texte]
- **Durée estimée** : [X secondes]
- **Potentiel viral** : [X/10]

---

## CHECKLIST PRODUCTION

- [ ] Produire les visuels (images + animations)
- [ ] Assembler dans CapCut (visuels + voix off + musique cinématique)
- [ ] Vérifier durée finale (cible 55-65s)
- [ ] Copier la description depuis description.md
- [ ] Publier entre 21h00 et 22h30

---

## SUIVI PERFORMANCE (à remplir le lendemain)

| Métrique | Valeur |
|----------|--------|
| Vues | — |
| Likes | — |
| Partages | — |
| Favoris | — |
| Complétion | — |
| Rétention 5s | — |
| Nouveaux abonnés | — |

*Donner ces stats à agent_analyse pour l'analyse de performance.*
```

## PHASE 4 — Vérification finale

- ✅ `Outputs/Vidéo_N/` contient bien les 3 fichiers : `script.md`, `description.md`, `readme.md`
- ✅ `description.md` respecte le template (4 lignes, ≤5 hashtags, CTA question ouverte)
- ✅ Aucun fichier existant n'a été écrasé
- ✅ Afficher à Lucas le récapitulatif : numéro du dossier, sujet, hook utilisé, caption finale.

## Ce que cet agent NE fait PAS

- ❌ Ne réécrit pas le script (c'est `agent-script`)
- ❌ Ne génère pas de visuels ou audio (manuel)
- ❌ Ne publie pas sur TikTok
- ✅ Génère uniquement `description.md` + `readme.md` et livre un dossier propre
