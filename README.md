# PredAI Gemini - Dự đoán rớt môn và sinh câu trả lời tự động

## Mô tả
Dự án Flask kết hợp AI Gemini để dự đoán xác suất rớt môn của sinh viên và sinh câu trả lời tự nhiên cho người dùng dựa trên dữ liệu điểm số.

## Cấu trúc chính
- `app/` : Backend Flask, xử lý API, truy vấn DB, gọi model, tích hợp Gemini
- `frontend/` : Giao diện web chat đơn giản (HTML/JS)
- `models/du_doan_rot_mon.pkl` : File model dự đoán (joblib)
- `students.db` : Database SQLite lưu thông tin sinh viên

## Cài đặt
1. Tạo virtualenv và cài đặt thư viện:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
2. Tạo database và thêm dữ liệu mẫu:
   ```sh
   python create_student_db.py
   python insert_sample_data.py
   ```
3. Đặt API key Gemini vào biến môi trường `GEMINI_API_KEY` hoặc sửa trực tiếp trong `app/gemini_service.py`.

## Chạy ứng dụng
```sh
python app.py
```
Truy cập [http://127.0.0.1:5000/](http://127.0.0.1:5000/) để sử dụng giao diện chat.

## Gửi câu hỏi qua API
```sh
curl -X POST http://127.0.0.1:5000/process -H "Content-Type: application/json" -d "{\"question\": \"Cho tôi biết xác suất rớt môn của sinh viên 20231234?\"}"
```

## Liên hệ
- Tác giả: Lưu Đức Anh
- Email: ducanhluuSt@gmail.com
