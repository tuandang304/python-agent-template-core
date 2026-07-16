# Contributing

Thanks for your interest in improving **Agent Research Kit**! 🎉

## Ways to contribute

- **Report bugs / request features** via [Issues](https://github.com/tuandang304/agent-research-kit/issues).
- **Improve docs** — typos, clarifications, and better examples are always welcome.
- **Submit code** via pull request (see below).

## Development setup

```bash
git clone https://github.com/tuandang304/agent-research-kit.git
cd agent-research-kit
uv sync --extra dev        # or: pip install -e ".[dev]"
pre-commit install         # optional: format & lint on commit
```

## Before opening a PR

```bash
ruff format .              # format
ruff check . --fix         # lint
pytest                     # tests must pass
```

Keep changes focused and match the existing style. For anything non-trivial,
open an issue first so we can align on the approach.

## Code of conduct

Be respectful and constructive. We want this to be a welcoming project for
researchers and students of all levels.
