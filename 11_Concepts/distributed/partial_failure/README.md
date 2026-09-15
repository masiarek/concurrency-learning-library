# Partial failure

**Category:** [Distributed systems](../README.md) · **Status:** stub

**One line:** In a distributed system one component can fail while the others continue, and a caller often cannot tell a slow peer from a dead one.

## How it connects


- **See also:** [Consensus](../consensus/README.md), [Distributed computing](../distributed_computing/README.md), [Durable execution](../durable_execution/README.md), [Idempotency](../idempotency/README.md), [Remote procedure call](../rpc/README.md), [Timeout](../../async/timeout/README.md)

## In each language

| | |
|---|---|
| Erlang and Elixir | [`monitor_node` ↗](https://www.erlang.org/doc/apps/erts/erlang.html#monitor_node/2) monitors the status of another node |
| Elsewhere | gRPC [deadlines ↗](https://grpc.io/docs/guides/deadlines/): once the deadline has passed, the client gives up and fails the call with `DEADLINE_EXCEEDED` |

## Where to read more

- **Reference:** [Dominik Tornow: Distributed Async Await (NDC talk) ↗](https://www.youtube.com/watch?v=lfSIunYUsSg)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
