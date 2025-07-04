import sqlite3
from app.gemini_service import gemini_extract_student_id

def extract_student_id_from_question(question: str) -> str:
    result = gemini_extract_student_id(question)
    return result.get("ma_sinh_vien")

def get_student_info(student_id, db_path="data/students.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "student_id": row[0],
            "diem_chuyen_can": row[1],
            "diem_giua_ky": row[2],
            "diem_bai_tap": row[3],
            "so_mon_da_rot": row[4],
            "GPA": row[5]
        }
    return None
