# Experiments

One script per experiment. Each run should be **reproducible**: seed everything
via `set_seed(config.seed)`, read settings from a file in `configs/`, and write
outputs to `results/`.

- `example_experiment.py` — a complete, runnable example (trains a classifier,
  saves a confusion-matrix figure).
- `configs/` — one YAML per experiment, committed to git for a clear record.

Run the example:

```bash
uv run python experiments/example_experiment.py
# or
python main.py example
```
