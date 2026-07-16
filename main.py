"""Project entry point.

Thin dispatcher so `uv run main.py` (or `python main.py`) does something useful
out of the box. Wire your own commands in as the project grows.

Usage:
    python main.py            # print project info
    python main.py example    # run the example experiment
"""

from __future__ import annotations

import sys

# Make `import ark` work when running this file directly, without an install.
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent / "src"))

from ark import __version__, config, get_logger  # noqa: E402

log = get_logger("main")


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    command = argv[0] if argv else "info"

    if command == "info":
        log.info("agent-research-kit v%s", __version__)
        log.info("seed=%d  log_level=%s", config.seed, config.log_level)
        log.info("Run an experiment with:  python main.py example")
    elif command == "example":
        from experiments.example_experiment import main as run_example

        run_example()
    else:
        log.error("Unknown command: %s (try 'info' or 'example')", command)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
