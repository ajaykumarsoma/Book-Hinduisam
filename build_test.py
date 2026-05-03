#!/usr/bin/env python3
import subprocess
import sys

try:
    result = subprocess.run(
        ['python3', '-m', 'mkdocs', 'build'],
        cwd='/Users/amac/MechInterpLab/Book-Hinduisam',
        capture_output=True,
        text=True,
        timeout=60
    )
    
    print("=== BUILD OUTPUT ===")
    print(result.stdout)
    if result.stderr:
        print("=== ERRORS ===")
        print(result.stderr)
    
    print(f"\n=== RETURN CODE: {result.returncode} ===")
    sys.exit(result.returncode)
    
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
