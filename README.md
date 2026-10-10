# Gerçek Zamanlı İnsan Tespiti 🎯

YOLO11 ile eğitilmiş, gerçek zamanlı insan tespiti yapan derin öğrenme modeli.

## 📊 Sonuçlar
| Metrik | Değer |
|--------|-------|
| mAP@50 | %91.3 |
| Precision | %81.6 |
| Recall | %87.0 |
| Hız | 1.8ms/resim |
| Eğitim Süresi | 0.644 saat |

## 🛠️ Kullanılan Teknolojiler
- Python 3.13
- PyTorch 2.6 (CUDA 12.4)
- Ultralytics YOLO11
- OpenCV
- NVIDIA RTX 4050 GPU

## 📁 Proje Yapısı
```
yolo-detector/
├── detect.py      # Gerçek zamanlı kamera tespiti
├── train.py       # Model eğitimi
├── data.yaml      # Veri seti konfigürasyonu
└── README.md
```

## ⚙️ Kurulum
```bash
pip install ultralytics opencv-python
```

## 🏃 Kullanım

### Model Eğitimi
```bash
python train.py
```

### Gerçek Zamanlı Tespit
```bash
python detect.py
```

## 📌 Veri Seti
- 7920 resim
- Kaynak: Roboflow Universe
- Format: YOLOv8