#!/bin/sh
set -eux

sed -i 's|<p align="center"><img alt="\(.*\)" src="\(.*\)" width=".*" /></p>|![\1](\2)|g' ../../cours/*/ReadMe.md

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

docker run --rm \
       --volume "$(pwd)/../..:/data" \
       --user "$(id -u):$(id -g)" \
       'pandoc/extra:3.8.2.1' \
       $(echo "$order" | sed 's|.*|cours/&/ReadMe.md|') \
       --pdf-engine 'lualatex' \
       --from 'gfm-yaml_metadata_block+rebase_relative_paths' \
       -V 'geometry:margin=1in' \
       -o 'scripts/pdf/result.pdf'

git restore ../../cours
