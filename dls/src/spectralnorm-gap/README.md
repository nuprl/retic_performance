spectralnorm-gap
===

Directory with 2 spectralnorm configurations:
- `0.py.retic` is fully-typed
- `28.py.retic` is less-typed

Both programs are retic-transpiled code.
"Strangely", `28.py` runs slower than `0.py`, by about `1/2` second

The gap is due to `check_type_float` getting put inside the loops in
- `part_A_times_u`
- `part_At_times_u`
