# Python Project Template

This is a meticulously structured project template designed to save you time and eliminate the need to set up from scratch every time you start a new Python, Data Science, Machine Learning, or AI Agent project.

## 📂 Directory Structure

- **`data/`**: Directory dedicated to data storage (raw, processed, external, etc.). Ensure that large or sensitive data files are properly handled in `.gitignore`.
- **`docs/`**: Directory containing project-related documentation, reports, and system design files.
- **`src/`**: The core source code of the project. Organize sub-modules (e.g., `data_processing`, `training`, `utils`) within this directory to maintain modular and reusable code.
- **`.agents/` / `.claude/`**: Configuration directories specific to AI Agent systems or Claude workflows.

## 📄 Key Files

- **`baseline.ipynb`**: A ready-to-use Jupyter Notebook for Exploratory Data Analysis (EDA) and rapidly building the initial baseline model/solution.
- **`main.py`**: The main entry point of the project. Used to orchestrate modules and run the application (e.g., model training pipeline, app execution).
- **`pyproject.toml`**: The project configuration file, storing metadata and managing dependencies, replacing the traditional `requirements.txt` with modern standards.
- **`.python-version`**: Defines the standard Python version for the project (currently `3.14`), allowing tools like `pyenv` or `uv` to automatically select the correct environment.
- **`CLAUDE.md`**: Behavioral guidelines for pre-installed AI Agents, outlining principles and coding standards to follow within this project.
- **`skills-lock.json`**: A skills lock file that remembers configured skills and tools to ensure consistent project operation.
- **`.gitignore`**: Specifies files and directories that should not be pushed to Git, keeping the repository clean and secure.

## 🚀 Getting Started

1. **Initialize Virtual Environment and Install Dependencies:**
   Check `pyproject.toml` and `.python-version` to set up your environment (using `venv`, `poetry`, or `uv`).

2. **Setup Initial Data:**
   Store any datasets you intend to use into the `data/` directory.

3. **Analyze with Notebook:**
   Open `baseline.ipynb` to explore data, brainstorm analytical methods, and build a baseline.

4. **Modularize Logic:**
   Move verified code snippets from the baseline notebook into separate `.py` files within the `src/` directory, and output results via the `main.py` control script.

*Good luck and happy coding!*
