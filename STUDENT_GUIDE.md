# Student Guide to fleet-symmetry-analyzer

## What is this?

Analyzes symmetry groups in ternary sequences and their musical counterparts.```python\nfrom lib.analyzer import find_symmetry_groups\nfind_symmetry_groups([1,0,-1,1,0,-1,1,1])```

## Why does it matter in the fleet?

All 15 MIDI fleet repos connect through the ternary⇄music bridge. This repo
handles one specific aspect of that bridge. Start here, explore outward.

## Next Steps

After understanding this repo, explore:
- fleet-ternary-music (the core theory)
- fleet-midi-text2midi (text→MIDI using this theory)
- fleet-music-theorist (analyze what you build)
