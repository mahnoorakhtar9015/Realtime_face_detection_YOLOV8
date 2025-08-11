# 🖥 Real-Time Face Detection with YOLOv8

This project implements **real-time face detection** using the **YOLOv8** deep learning model.  
It captures live webcam feed, processes each frame, and detects faces with bounding boxes and confidence scores.

---

## 🚀 Features
- **Real-time detection** from webcam using OpenCV.
- Fine-tuned **YOLOv8** model for face detection.
- High accuracy and fast inference on both **CPU** and **GPU**.
- Modular codebase for easy extension to other YOLO versions.
- Option to switch between **YOLOv5** and **YOLOv8** for performance comparison.

---

## 📂 Project Structure
face_detection_app/

├── app/

│ ├── model_loader.py # Load YOLO models

│ ├── inference.py # Run inference on webcam frames

├── yolov5/ # YOLOv5 repo for v5 comparison

├── main.py # Entry point for real-time detection

├── best_v5.pt # Fine-tuned YOLOv5 weights

├── best_yolov8.pt # Fine-tuned YOLOv8 weights

├── yolov5_metrics.csv # YOLOv5 final metrics

├── yolov8_metrics.csv # YOLOv8 final metrics

└── requirements.txt # Required dependencies



## 📊 YOLOv8 vs YOLOv5 (on same dataset)
| Model   | Precision | Recall | mAP50 | mAP50-95 |
|---------|-----------|--------|-------|----------|
| YOLOv5  | 0.886     | 0.823  | 0.892 | 0.579    |
| YOLOv8  | **0.89**  | **0.81** | **0.88** | **0.588** |


📁 **Source:** [`yolov5_metrics.csv`](yolov5_metrics.csv) & [`yolov8_metrics.csv`](yolov8_metrics.csv)


*Why YOLOv8?**
- Actively maintained and updated by Ultralytics.
- Anchor-free design → better adaptability.
- Faster inference with better accuracy.
- Cleaner API for training, validation, and export.

---


**YOLOv8 Real-Time Detection Example**
![YOLOv8 Detection](assets/1.jpg) 


## ⚙️ Installation
```bash
# Clone this repository
git clone https://github.com/mahnoorakhtar9015/face-detection-yolov8.git
cd face-detection-yolov8

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🏃 Usage

```bash
python main.py


```
Press q to quit the live detection.