# Distributed computing

**Category:** [Distributed systems](../README.md) · **Status:** stub

**One line:** Tasks on separate machines that communicate over a network: their events are only partially ordered, and one part can fail while the rest keeps running.

Also called: distributed systems, distributed platform.

## How it connects

```mermaid
flowchart LR
  n_concurrency["Concurrency"]
  n_distributed_computing["Distributed computing"]
  n_concurrency ---|vs| n_distributed_computing
  classDef center stroke-width:3px
  class n_distributed_computing center
  classDef outside stroke-dasharray: 4 3
  class n_concurrency outside
```

- **Often confused with:** [Concurrency](../../foundations/concurrency/README.md)
- **See also:** [Partial failure](../partial_failure/README.md), [Remote procedure call](../rpc/README.md)

## In each language

| | |
|---|---|
| Erlang and Elixir | [distributed Erlang ↗](https://www.erlang.org/doc/system/distributed.html): runtime systems called nodes connect, and message passing, links and monitors work across nodes when pids are used |

## Where to read more

- **Notes:** [Distributed Systems - main ↗](https://docs.google.com/document/d/1YlfP2Lu-Wep_E_gzJqM3BzxdFW0bSpIAtkE04vmkdCo/edit?tab=t.0)
- **Notes:** [distributed async and await - distributed platform ↗](https://docs.google.com/document/d/16iIMo9Rtp_BFFnUHh8wgww6z7Rc5EN-zmAPnBfDxfA8/edit?tab=t.0)
- **Reference:** [Wikipedia: Distributed computing ↗](https://en.wikipedia.org/wiki/Distributed_computing)
- **Reference:** [Dominik Tornow: Distributed Async Await (NDC talk) ↗](https://www.youtube.com/watch?v=lfSIunYUsSg)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
