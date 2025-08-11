from app.model_loader import load_model
from app.inference import run_inference
import cv2
import time

def start_realtime(weights_path, conf_threshold=0.25):
    model = load_model(weights_path, conf_threshold)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        start = time.time()
        result = run_inference(model, frame, conf_threshold)
        fps = 1 / (time.time() - start)
        cv2.putText(result, f" FPS: {fps:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Face Detection", result)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    weights = "best_yolov8.pt" 
    start_realtime(weights)