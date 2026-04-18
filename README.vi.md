# Project Template (Mẫu Dự Án)

Đây là một template dự án được thiết kế với cấu trúc chuẩn mực, giúp bạn tiết kiệm thời gian và không phải thiết lập từ đầu mỗi khi bắt đầu một dự án Python, Data Science, Machine Learning hay AI Agent mới.

## 📂 Cấu trúc thư mục

- **`data/`**: Thư mục dùng để chứa dữ liệu (raw, processed, external,...). Cần đảm bảo dữ liệu lớn hoặc nhạy cảm đã được xử lý trong `.gitignore`.
- **`docs/`**: Thư mục chứa các tài liệu liên quan đến dự án, báo cáo, file thiết kế hệ thống.
- **`src/`**: Nơi chứa mã nguồn chính (core logic) của dự án. Gói gọn các module con (ví dụ: data_processing, training, utils) vào thư mục này để code luôn module-hóa, dễ tái sử dụng.
- **`.agents/` / `.claude/`**: Các thư mục cấu hình dành riêng cho hệ thống AI Agent hoặc các workflow của Claude.

## 📄 Các tệp tin quan trọng

- **`baseline.ipynb`**: File Jupyter Notebook chuẩn bị sẵn cho quá trình EDA (Exploratory Data Analysis) và xây dựng mô hình/giải pháp baseline đầu tiên rất nhanh chóng.
- **`main.py`**: File chạy chính (entry point) của dự án. Dùng để liên kết các module và khởi chạy chương trình (như pipeline huấn luyện mô hình, chạy ứng dụng,...).
- **`pyproject.toml`**: File cấu hình dự án, lưu trữ metadata và quản lý các thư viện phụ thuộc (dependencies) thay thế cho `requirements.txt` theo tiêu chuẩn hiện đại.
- **`.python-version`**: Định nghĩa chuẩn phiên bản Python của dự án (hiện tại `3.14`), giúp các công cụ như `pyenv` hoặc `uv` tự động chọn đúng môi trường.
- **`CLAUDE.md`**: File chỉ dẫn hành vi (Guidelines) cho AI Agent cài đặt sẵn những nguyên tắc cần tuân thủ về tư duy và coding khi làm việc trong project này.
- **`skills-lock.json`**: Tập tin khoá kỹ năng, giúp ghi nhớ các công cụ đã cấu hình để dự án hoạt động đồng nhất.
- **`.gitignore`**: Chứa danh sách các thư mục/file không được push lên Git để giữ repo gọn nhẹ và bảo mật.

## 🚀 Hướng dẫn bắt đầu (Getting Started)

1. **Khởi tạo môi trường ảo và cài đặt thư viện:**
   Dựa vào `pyproject.toml` và `.python-version` để setup môi trường (khuyến khích dùng `uv`, `poetry`, hoặc `venv`).
   
2. **Setup dữ liệu ban đầu:**
   Lưu trữ các tập dataset sử dụng trong quá trình làm việc vào thư mục `data/`.
   
3. **Phân tích với Notebook:**
   Mở `baseline.ipynb` để khám phá dữ liệu, lên ý tưởng phương pháp phân tích và xây dựng baseline.

4. **Module hóa logic:**
   Đưa các đoạn code đã kiểm chứng ở baseline vào các file `.py` riêng trong thư mục `src/`, và chỉ xuất kết quả ra từ tập lệnh điều khiển `main.py`.

*Chúc bạn đạt kết quả thật tốt và code ít bug!*
