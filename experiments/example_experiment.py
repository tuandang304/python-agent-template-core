"""A complete, runnable example experiment.

It trains a small classifier on a built-in dataset, prints metrics, and saves a
confusion-matrix figure to ``results/figures/``. Copy this file to start a new
experiment; it demonstrates the reproducibility + logging + paths conventions.

    uv run python experiments/example_experiment.py
"""

from __future__ import annotations

from ark import config, get_logger, set_seed
from ark.config import FIGURES_DIR, PROJECT_ROOT

log = get_logger("experiment")


def main() -> None:
    set_seed(config.seed)
    log.info("Running example experiment (seed=%d)", config.seed)

    # Lazy imports so the package itself stays import-light.
    import matplotlib

    matplotlib.use("Agg")  # headless-safe backend
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_wine
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
    from sklearn.model_selection import train_test_split

    X, y = load_wine(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=config.seed, stratify=y
    )

    model = RandomForestClassifier(n_estimators=200, random_state=config.seed)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    log.info("Test accuracy: %.3f", acc)

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    fig_path = FIGURES_DIR / "example_confusion_matrix.png"
    ConfusionMatrixDisplay.from_predictions(y_test, preds)
    plt.title(f"Wine — RandomForest (acc={acc:.2f})")
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    log.info("Saved figure -> %s", fig_path.relative_to(PROJECT_ROOT))


if __name__ == "__main__":
    main()
