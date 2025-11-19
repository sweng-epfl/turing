# Conversion en PDF

Ce script convertit les notes de cours en un gros PDF.

Leur ordre est défini en dur dans le script, à changer donc si l'ordre change.

**Bugs actuels**:
- Les caractères chinois et arabes (c.f. fin de la page 2 dans l'intro par exemple) ne sont pas affichés
  - Il est possible de donner à pandoc un nom de police à utiliser, mais cela cause des problèmes de chargement d'une police japonaise...
- Le texte dans les images SVG ne s'affiche pas
