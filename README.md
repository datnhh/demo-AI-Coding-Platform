# textkit — repo mẫu Python

Nhánh này là **repo thứ hai** của AI Coding Platform (P3-T02), tồn tại để chứng minh ADR-004:
thêm một hệ sinh thái chỉ tốn một file `.agent/repo.yml`, không tốn dòng code nào của
orchestrator.

Nó độc lập hoàn toàn với nhánh `main` (dự án .NET): khác trình quản lý gói (`pip` thay vì
`nuget`), khác cách build, và khác định dạng kết quả test.

## Chạy tay

```bash
pip install -r requirements.txt
pytest -q
```

## Quy ước

- Mã nguồn ở `src/textkit/`, test ở `tests/`.
- Mỗi hàm public đều có docstring và test cho cả trường hợp `None`.
- Không sửa `.agent/` — đó là cấu hình của platform.
