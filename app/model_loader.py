
from ultralytics import YOLO

def load_model(weights_path: str, conf_threshold: float):
  
    model = YOLO(weights_path)
    return model