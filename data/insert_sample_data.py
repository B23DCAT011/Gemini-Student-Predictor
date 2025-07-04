import sqlite3

def insert_sample_data(db_path="students.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    data = [
        ("20231234", 8.0, 7.5, 9.0, 0, 3.2),
        ("20231235", 6.5, 5.0, 7.0, 1, 2.8),
        ("20231236", 9.0, 8.5, 10.0, 0, 3.7),
        ("20231237", 4.0, 3.5, 5.0, 2, 2.0),
        ("20231238", 7.0, 6.0, 8.0, 1, 2.9),
        ("20231239", 4.0, 3.5, 2.0, 8, 1.0)
    ]
    cursor.executemany("""
        INSERT OR REPLACE INTO students (student_id, diem_chuyen_can, diem_giua_ki, diem_bai_tap, so_mon_da_rot, GPA)
        VALUES (?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()
    print("Đã thêm dữ liệu mẫu vào students.db")

if __name__ == "__main__":
    insert_sample_data()
