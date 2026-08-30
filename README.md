# demo-AI-Coding-Platform

Repo dùng để chạy thử [AI Coding Platform](https://github.com/datnhh) trên một dự án thật.

Nội dung cố ý nhỏ nhất có thể: một thư viện và một bộ test. Mục đích không phải là bản thân
đoạn code, mà là để platform có một thứ **build được và test được** để làm việc lên.

## Cấu trúc

| Đường dẫn | Là gì |
|---|---|
| `src/Demo` | Thư viện. Chỗ agent thêm code |
| `tests/Demo.Tests` | Test. Agent phải thêm test cho mọi thay đổi |
| `.agent/repo.yml` | Bản mô tả cho platform: ảnh container, lệnh build/test |

## Quy ước

- Mỗi thay đổi phải kèm test. Test là thứ duy nhất platform dùng để tự kết luận đúng/sai.
- Không sửa `.agent/` — đó là cấu hình của platform, đã khai trong `protected_paths`.

## Chạy cục bộ

```bash
dotnet test tests/Demo.Tests/Demo.Tests.csproj
```
