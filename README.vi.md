<div align="center">

# 🔬 Agent Research Kit

**Template nghiên cứu chuẩn mực, tái lập được và tích hợp sẵn AI-agent — cho nghiên cứu học thuật & khoa học dữ liệu.**

Clone về, chạy một câu lệnh là bắt đầu nghiên cứu ngay — với cấu trúc dự án gọn
gàng, khả năng tái lập (reproducibility) tích hợp sẵn, khung bài báo LaTeX, và
các kỹ năng (skills) của [Claude Code](https://claude.com/claude-code) đã cài đặt sẵn.

[![CI](https://github.com/tuandang304/agent-research-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/tuandang304/agent-research-kit/actions/workflows/ci.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Use this template](https://img.shields.io/badge/use%20this-template-2ea44f?logo=github)](https://github.com/tuandang304/agent-research-kit/generate)

[English](README.md) · [Tiếng Việt](README.vi.md)

</div>

---

## Vì sao nên dùng template này?

Phần lớn code nghiên cứu bắt đầu từ một notebook lộn xộn và không bao giờ gọn lại
được. Template này cho bạn một **bộ khung chuyên nghiệp ngay từ ngày đầu**, giúp
công việc luôn tái lập được, dễ chia sẻ và dễ chuyển thành bài báo.

- 🧪 **Tái lập mặc định** — một nơi cấu hình duy nhất, một lệnh seed mọi bộ sinh số ngẫu nhiên.
- 📁 **Cấu trúc hợp lý** — `data/ · notebooks/ · experiments/ · results/ · paper/`.
- 📦 **Chạy được ngay** — `uv sync` cài đủ mọi thứ; có sẵn một thí nghiệm mẫu chạy thật.
- 📄 **Sẵn sàng viết báo** — khung LaTeX lấy hình trực tiếp từ `results/`, kèm `CITATION.cff`.
- 🤖 **Sẵn sàng cho AI-agent** — tích hợp sẵn các skill của Claude Code (API, trích dẫn, thiết kế hệ thống...).
- ✅ **Đầy đủ công cụ** — test, linting (ruff), CI, và mẫu issue/PR đã cấu hình sẵn.

## Bắt đầu nhanh (Quickstart)

> Cần [**uv**](https://docs.astral.sh/uv/) (khuyến khích) hoặc `pip` thông thường.

```bash
# 1. Lấy code (hoặc bấm "Use this template" trên GitHub)
git clone https://github.com/tuandang304/agent-research-kit.git
cd agent-research-kit

# 2. Cài mọi thứ vào một môi trường độc lập
uv sync                     # thêm --extra dev để test/lint, --extra notebook cho Jupyter

# 3. Chạy thí nghiệm mẫu — huấn luyện mô hình và lưu hình vào results/figures/
uv run python main.py example
```

Thích dùng pip? `python -m venv .venv && source .venv/bin/activate && pip install -e ".[dev,notebook]"`

Vậy là xong — bạn đã có một dự án nghiên cứu hoạt động và tái lập được.

## Cấu trúc dự án

```
agent-research-kit/
├── src/ark/                # Package tái sử dụng của bạn (config, seed, logging, data IO)
├── experiments/            # Mỗi thí nghiệm một script + file config YAML riêng
├── notebooks/              # Khám phá dữ liệu; 01_exploratory.ipynb đã nối với `ark`
├── data/                   # raw / processed / external  (nội dung bị git bỏ qua)
├── results/                # figures / tables            (tự sinh lại, git bỏ qua)
├── paper/                  # Khung LaTeX + references.bib → dùng results/figures
├── docs/                   # Ghi chú thiết kế, tài liệu dữ liệu, nhật ký thí nghiệm
├── tests/                  # Test kiểm tra nhanh bằng pytest
├── config.yaml             # Cấu hình toàn dự án (seed, log level, khóa của bạn)
├── main.py                 # Điểm chạy chính:  python main.py [info|example]
├── .claude/ · .agents/     # Các skill Claude Code cài sẵn (xem bên dưới)
└── pyproject.toml          # Metadata, dependencies, cấu hình ruff & pytest
```

## Quy ước tái lập (Reproducibility)

Mọi thí nghiệm đều theo ba quy tắc giống nhau, nên kết quả rất dễ tái lập:

```python
from ark import config, get_logger, set_seed

set_seed(config.seed)        # 1. Seed Python, NumPy và PyTorch (nếu có cài)
log = get_logger("my_exp")   # 2. Logging nhất quán, dễ đọc
# 3. Đọc cấu hình từ config.yaml / experiments/configs/*.yaml — không hard-code
```

Đường dẫn được phân giải từ thư mục gốc repo qua `ark.config`, nên cùng một đoạn
code chạy được từ script, notebook hay test — không phải mò `../../`.

## Từ thí nghiệm đến bài báo

Hình lưu vào `results/figures/` được `paper/main.tex` nạp trực tiếp
(`\graphicspath{{../results/figures/}}`). Biên dịch bài báo bằng `latexmk -pdf main.tex`
hoặc đưa thư mục lên [Overleaf](https://overleaf.com). GitHub cũng sẽ hiện nút
**"Cite this repository"** nhờ `CITATION.cff`.

## Các skill Claude Code tích hợp sẵn 🤖

Nếu bạn dùng [Claude Code](https://claude.com/claude-code), các skill này tự nạp
từ `.claude/skills/` (nhân bản trong `.agents/skills/`):

| Skill | Giúp bạn… |
| --- | --- |
| **claude-api** | Lập trình với Claude API trên 8 ngôn ngữ (caching, tools, batches). |
| **bibtex-citation** | Lấy và định dạng BibTeX chuẩn cho `paper/references.bib`. |
| **system-design** | Soạn tài liệu kiến trúc và thiết kế cho `docs/`. |
| **skill-creator / skill-development** | Tự tạo skill riêng cho dự án. |
| **agent-development / plugin-structure** | Xây dựng agent và plugin tùy biến. |
| **memory-management** | Trao cho agent bộ nhớ dự án bền vững. |

Không dùng Claude Code? Các thư mục này vô hại — xóa đi cũng không sao.

## Tùy biến cho riêng bạn

Sau khi bấm **Use this template**, hãy biến nó thành của bạn:

1. Đổi tên package `src/ark/` → `src/<tên_dự_án>` và cập nhật `pyproject.toml`.
2. Điền thông tin tác giả trong `pyproject.toml`, `LICENSE` và `CITATION.cff`.
3. Thêm dependencies vào `pyproject.toml`, rồi `uv sync`.
4. Xóa thí nghiệm mẫu và những phần `paper/`/`.claude/` bạn không cần.

## Đóng góp

Rất hoan nghênh issue và PR — xem [CONTRIBUTING.md](CONTRIBUTING.md). Nếu template
này giúp bạn tiết kiệm thời gian, một ⭐ sẽ giúp người khác tìm thấy nó!

## Giấy phép

[MIT](LICENSE) — miễn phí cho cả mục đích học thuật và thương mại.
