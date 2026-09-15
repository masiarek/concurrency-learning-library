# Remote procedure call

**Category:** [Distributed systems](../README.md) · **Status:** stub

**One line:** Calling a function that runs on another machine as though it were local — convenient until the network fails in a way no local call can.

Also called: RPC, RMI, remote method invocation.

## How it connects


- **See also:** [Distributed computing](../distributed_computing/README.md), [Partial failure](../partial_failure/README.md)

## In each language

| | |
|---|---|
| Go | [`net/rpc` ↗](https://pkg.go.dev/net/rpc), frozen and not accepting new features |
| Java | [RMI ↗](https://docs.oracle.com/en/java/javase/25/docs/api/java.rmi/java/rmi/package-summary.html): an object in one Java virtual machine invokes methods on an object in another |
| Python | [`xmlrpc` ↗](https://docs.python.org/3/library/xmlrpc.html), remote procedure calls as XML over HTTP |
| C# | [gRPC on ASP.NET Core ↗](https://learn.microsoft.com/en-us/aspnet/core/grpc/) |
| Erlang and Elixir | [`erpc` ↗](https://www.erlang.org/doc/apps/kernel/erpc.html), enhanced remote procedure calls to functions on other nodes |
| Elsewhere | [gRPC ↗](https://grpc.io/docs/what-is-grpc/core-concepts/): services described in Protocol Buffers, with a deadline on each call |

## Where to read more

- **Notes:** [remote method invocation (RMI) - general ↗](https://docs.google.com/document/u/0/d/18c4ILIWpWmSuCYbKzNUWd_y_EkJDkcnWhpGIvXHcxqA/edit)
- **Reference:** [Wikipedia: Remote procedure call ↗](https://en.wikipedia.org/wiki/Remote_procedure_call)

<!-- Generated above this line by tools/build_concepts.py from TOML data — edit the data, not the page. Hand-written notes go below it and are kept. -->
