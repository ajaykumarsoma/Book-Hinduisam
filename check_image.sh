#!/bin/bash
cd /Users/amac/MechInterpLab/Book-Hinduisam
echo "=== Checking if image file exists ==="
ls -lh docs/images/chapter_09/nataraja_agni_linga.png
echo ""
echo "=== Checking if image is tracked by git ==="
git ls-files docs/images/chapter_09/nataraja_agni_linga.png
echo ""
echo "=== Git status ==="
git status docs/images/chapter_09/
