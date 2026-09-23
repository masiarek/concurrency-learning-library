# Cache coherence

**Category:** [Parallelism](../README.md) · **Status:** stub

**One line:** Keeping several cached copies of the same data consistent when one of them is written — done in hardware between a CPU's cores, at a cost that false sharing exposes.

Also called: cache invalidation, write-back.

## How it connects


- **See also:** [False sharing](../../hazards/false_sharing/README.md), [NUMA](../numa/README.md)

## Where to read more

- **In this library:** [Can one thread see another's writes out of order?](../../../02_Shared_State/reordering_and_the_memory_model/README.md)
- **In this library:** [Why are eight threads writing eight different variables slow?](../../../07_Parallelism/false_sharing/README.md)
- **Notes:** [Cache coherence ↗](https://docs.google.com/document/d/11AUT-9ZiaDLML1DHaKz41nj_dmzj0-fSXxHyxMGj_4U/edit?tab=t.0)
- **Notes:** [cache invalidation ↗](https://docs.google.com/document/d/1DHSM56i69dzhauCUMym3o5DfyA1RJkichLYl4KFKn9Q/edit?tab=t.0)
- **Notes:** [write-back with invalidation ↗](https://docs.google.com/document/d/1MYeif5pOPcuarLG0aae17yq8oqPFZwY3_y9j17h-NFU/edit?tab=t.0)
- **Notes:** [shared data across different caches ↗](https://docs.google.com/document/d/1JSbyd8pdLLMCtMUdosY1amPrzgdJu_6uHIGQGSkL9YA/edit?tab=t.0)
- **Reference:** [Wikipedia: Cache coherence ↗](https://en.wikipedia.org/wiki/Cache_coherence)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
