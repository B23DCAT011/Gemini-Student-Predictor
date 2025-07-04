from flask import Blueprint, request, jsonify, render_template, send_from_directory
from app.core import extract_student_id_from_question, get_student_info
from app.models import predict_percent
from app.gemini_service import gemini_generate_answer
import os

router = Blueprint('router', __name__)

@router.route("/")
def serve_index():
    # Phục vụ file frontend/index.html khi truy cập root
    return send_from_directory(os.path.join(os.path.dirname(__file__), '../frontend'), 'index.html')

@router.route("/process", methods=["POST"])
def process():
    try:
        # Nhận dữ liệu từ form hoặc fetch (application/x-www-form-urlencoded hoặc application/json)
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form
        question = data.get("question")
        if not question:
            return jsonify({"error": "Câu hỏi không được cung cấp"}), 400
        # Trích xuất mã sinh viên
        student_id = extract_student_id_from_question(question)
        if not student_id:
            return jsonify({"error": "Không tìm thấy mã sinh viên trong câu hỏi"}), 404
        # Lấy thông tin sinh viên từ DB
        info = get_student_info(student_id)
        if not info:
            return jsonify({"error": f"Không tìm thấy thông tin cho mã sinh viên {student_id}"}), 404
        # Dự đoán xác suất rớt môn
        input_data = [
            info["diem_chuyen_can"],
            info["diem_giua_ky"],
            info["diem_bai_tap"],
            info["so_mon_da_rot"],
            info["GPA"]
        ]
        percent = predict_percent(input_data)
        # Sinh câu trả lời tự nhiên bằng Gemini
        answer = gemini_generate_answer(percent, student_id)
        return jsonify({
            "ma_sinh_vien": student_id,
            "percent": percent,
            "answer": answer
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


