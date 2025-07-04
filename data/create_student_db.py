import sqlite3

def create_student_db(db_path="students.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            diem_chuyen_can REAL,
            diem_giua_ki REAL,
            diem_bai_tap REAL,
            so_mon_da_rot INTEGER,
            GPA REAL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_student_db()
    print("Đã tạo xong database students.db với bảng students.")
