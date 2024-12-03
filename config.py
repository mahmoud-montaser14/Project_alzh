import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_really_secure_key'
    UPLOAD_FOLDER = 'static/uploads/'
    MODEL_PATH = r'D:\api\model.tflite'  # Adjust path as needed
