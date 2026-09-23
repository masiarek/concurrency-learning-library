# 05 — Message passing

The alternative to sharing memory is to send it. A channel carries a value from one thread to another, and with it three questions that every design has to answer: does the sender wait for the receiver, how does a receiver learn that no more values will come, and who owns the value afterwards. Go and Rust built the channel into the language and the standard library and answer the third question oppositely; the other four have queues, and this chapter shows what the queue leaves out.

Every lesson in this chapter is a **stub**: the question, the expected answer per language and what the programs will have to show, waiting for the programs. A stub becomes a lesson when its examples run in CI and its table is replaced by what they printed.

| Lesson | The one thing |
|---|---|
| [Who owns a value after it has been sent?](sending_a_value_moves_it/README.md) | *stub* — a Rust send moves the value; every other language sends an alias |
| [Does a send return before anyone receives?](an_unbuffered_send_waits/README.md) | *stub* — the unbuffered send is the rendezvous; buffered sends run ahead; Rust's channel is unbounded |
| [What stops a fast producer from filling memory?](a_bounded_queue_pushes_back/README.md) | *stub* — a bound makes the fast producer wait; no bound makes memory grow with the rate difference |
| [How does a receiver learn that no more values will come?](closing_a_channel/README.md) | *stub* — Go closes, Rust drops the last sender, the queue languages send a poison pill |
| [How does one thread wait on several channels at once?](waiting_on_several_channels/README.md) | *stub* — Go's `select` takes the first ready at random; the others fan everything into one channel |
| [How do three stages run at once on one stream of values?](a_pipeline_of_stages/README.md) | *stub* — each stage on its own thread with a channel between; the speedup is the number of stages, bounded by the slowest |
| [How does one stream split across workers and merge back?](fan_out_fan_in/README.md) | *stub* — N workers on one input, N outputs merged into one — and the merged order is the finish order |
| [How do N workers share one queue of jobs?](a_worker_pool/README.md) | *stub* — fan-out made permanent: N workers, one job channel, one results channel, and how the pool learns it is done |
| [What if only one thread is allowed to touch the data?](one_owner_receives_the_numbers/README.md) | *stub* — give the data to one thread and send it the updates: no lock, no race, the actor model |
| [How does one event reach every subscriber?](publish_and_subscribe/README.md) | *stub* — a channel delivers to one receiver; a broadcast needs a queue per subscriber and a policy for the slow one |
