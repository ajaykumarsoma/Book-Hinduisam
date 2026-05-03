#!/usr/bin/env python3
"""Compact spacing in chapter 09 by reducing multiple blank lines."""

# Read the file
with open('docs/chapters/chapter_09_shiva_purana_linga_truth.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace multiple consecutive newlines with maximum 2 newlines
# This preserves paragraph breaks but removes excessive spacing
import re

# Replace 3+ newlines with 2 newlines
compacted = re.sub(r'\n\n\n+', '\n\n', content)

# Write back
with open('docs/chapters/chapter_09_shiva_purana_linga_truth.md', 'w', encoding='utf-8') as f:
    f.write(compacted)

# Calculate reduction
original_lines = content.count('\n')
compacted_lines = compacted.count('\n')
reduction = original_lines - compacted_lines

print(f"Original lines: {original_lines}")
print(f"Compacted lines: {compacted_lines}")
print(f"Reduced by: {reduction} lines ({100*reduction/original_lines:.1f}%)")
print("✅ Spacing compacted successfully!")
