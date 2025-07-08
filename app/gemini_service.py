from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
import json
import re

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY!!!!!!!!!!")
genai.configure(api_key=API_KEY)


def gemini_extract_student_id(question: str) -> dict:
    """
    Nhận câu hỏi tự nhiên, trích xuất mã sinh viên bằng Gemini, trả về dict.
    """
    prompt = (
        "Tôi sẽ gửi bạn một câu hỏi của sinh viên. Bạn hãy trích xuất mã sinh viên từ câu hỏi đó. Chỉ trả về kết quả dưới dạng JSON có dạng:\n"
        '{"ma_sinh_vien": "<mã_sinh_viên>"}'"\n"
        "Nếu không tìm thấy mã sinh viên thì trả về:\n"
        '{"ma_sinh_vien": null}'"\n"
        f"Câu hỏi: {question}\n"
        "Không giải thích, không thêm bất kỳ nội dung nào ngoài JSON."
    )
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    # Loại bỏ code block markdown nếu có
    cleaned = response.text.strip()
    if cleaned.startswith('```'):
        cleaned = re.sub(r'^```[a-zA-Z]*', '', cleaned).strip()
        if cleaned.endswith('```'):
            cleaned = cleaned[:-3].strip()
    # Tìm đoạn JSON đầu tiên trong response đã làm sạch
    match = re.search(r'\{.*\}', cleaned, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except Exception:
            return {"error": "Không parse được JSON"}
    return {"error": "Không trích xuất được mã sinh viên"}

def gemini_generate_answer(percent: float, student_id: str = None) -> str:
    """
    Nhận đầu vào là phần trăm dự đoán (từ predict_percent) và mã sinh viên (nếu có), sinh câu trả lời tự nhiên cho client bằng Gemini.
    """
    if student_id:
        prompt = (
            f"Mã sinh viên: {student_id}.\n"
            f"Xác suất rớt môn dự đoán là: {percent}%.\n"
            "Hãy trả lời cho người dùng bằng tiếng Việt, văn phong thân thiện, dễ hiểu. Đưa ra một lời khuyên hoặc kết luận nếu có thể."
        )
    else:
        prompt = (
            f"Xác suất rớt môn dự đoán là: {percent}%.\n"
            "Hãy trả lời cho người dùng bằng tiếng Việt, văn phong thân thiện, dễ hiểu. Đưa ra một lời khuyên hoặc kết luận nếu có thể."
        )
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text.strip()
def gemini_generate_answer_default(question: str) -> str:
    """
    Nhận đầu vào là câu hỏi của sinh viên, sinh câu trả lời tự nhiên cho client bằng Gemini.
    """
    prompt = (
        f"Câu hỏi: {question}\n"
        "Hãy trả lời cho người dùng bằng tiếng Việt, văn phong thân thiện, dễ hiểu"
        "Bạn là một trợ lý ảo của Học Viện Công Nghệ Bưu Chính Viễn Thông, chuyên hỗ trợ sinh viên trong việc học tập và giải đáp thắc mắc về môn học."
        "Bạn có nhiệm vụ chính là cung cấp xac suất rớt môn học dựa trên các thông tin về điểm số và quá trình học tập của sinh viên."
        "Bạn có một model đứng sau để dự đoán xác suất rớt môn học của sinh viên dựa trên các thông tin về điểm số và quá trình học tập của họ."
    )
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text.strip()
