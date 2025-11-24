#!/bin/sh

if ! git status '../../cours' '../../ReadMe.md' | grep -q 'nothing to commit, working tree clean'; then
  echo 'Veuillez lancer ce script uniquement quand les fichiers du cours ne sont pas modifiés... désolé.'
  exit 1
fi

if git clean -xfdn '../../cours' | grep -q 'Would remove'; then
  echo 'Veuillez lancer ce script uniquement quand les fichiers du cours ne sont pas modifiés... désolé (Utilisez git clean).'
  exit 2
fi

if ! which rsvg-convert >'/dev/null'; then
  echo 'Veuillez installer rsvg-convert (package librsvg2-bin sur Ubuntu par exemple).'
  exit 3
fi

if ! docker version >'/dev/null'; then
  echo 'Veuillez installer et lancer Docker.'
  exit 4
fi

# On pourrait utiliser `ls` mais on préfère avoir les cours dans l'ordre.
order="$(cat <<- EOF
Introduction
Infrastructure
Conception
Tests
Exigences
Débuggage
Performance
GUIs-et-APIs
Équipe
EOF
)"

# Commençons par créer une intro en enlevant la table des matières
sed -i '/## Contenu/,$d' '../../ReadMe.md'
sed -i "s|](documentation|](https://github.com/sweng-epfl/turing/tree/main/documentation|g" '../../ReadMe.md'

# Le markdown du cours utilise du HTML pour afficher les images à une échelle raisonnable.
# `pandoc` ne supporte pas ça en combinaison avec `rebase_relative_paths` (seuls les images Markdown sont supportées par cette extension).
# Donc on les convertit, adieu l'échelle...
sed -i 's|<p align="center"><img alt="\(.*\)" src="\(.*\)" width=".*" /></p>|![\1](\2)|g' '../../cours/'*'/ReadMe.md'

# Pandoc gère mal les SVGs, c.f. https://github.com/jgm/pandoc/issues/8176
# Donc on les transforme en PDF à l'avance
for c in $order; do
  for i in "../../cours/$c/images/"*.svg; do
    [ -f "$i" ] || break # ignorer les dossiers dans lesquels il n'y a pas de SVG
    rsvg-convert -f 'pdf' --dpi-x '300' --dpi-y '300' -o "$i.pdf" "$i"
  done
  sed -i 's|.svg)|.svg.pdf)|g' "../../cours/$c/ReadMe.md"
done

# On veut aussi que les liens vers les exercices soient absolus
for c in $order; do
  sed -i "s|](exercices|](https://github.com/sweng-epfl/turing/tree/main/cours/$c/exercices|g" "../../cours/$c/ReadMe.md"
done

# la commande `sed` ajoute un suffixe et un préfixe à chaque nom, pour obtenir les chemins vers les fichiers Markdown
# `gfm` = GitHub-Flavored Markdown
# `-yaml_metadata_block` = ne pas interpréter `---` comme des séparateurs de métadonnées
# `+rebase_relative_paths` = utiliser le chemin de chaque .md comme base pour les liens/images
# `margin=1in` = marges raisonnables, par défaut elles sont énormes
# `colorlinks=true` = liens en couleur (sinon on ne se rend pas compte que ce sont des liens)
docker run --rm \
       --volume "$(pwd)/../..:/data" \
       --user "$(id -u):$(id -g)" \
       'pandoc/extra:3.8.2.1' \
       'ReadMe.md'  $(echo "$order" | sed 's|.*|cours/&/ReadMe.md|') \
       --pdf-engine 'lualatex' \
       --from 'gfm-yaml_metadata_block+rebase_relative_paths' \
       -V 'geometry:margin=1in' \
       -V 'colorlinks=true' \
       -o 'scripts/pdf/GénieLogiciel.pdf'

git restore '../../cours' '../../ReadMe.md'
git clean -xfd '../../cours' >'/dev/null'
