import os
import joblib

model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'du_doan_rot_mon.pkl')
model = joblib.load(model_path)

def predict_percent(data):
    """
    Nhận vào dữ liệu đầu vào (list hoặc numpy array), trả về xác suất dự đoán (phần trăm).
    """
    # Nếu model là binary/classification, dùng predict_proba
    proba = model.predict_proba([data])[0][1]  # Xác suất lớp 1
    return round(proba * 100, 2)

