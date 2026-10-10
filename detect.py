import cv2
from ultralytics import YOLO

# Eğittiğimiz modeli yükle
model = YOLO(r"C:\Users\MEHMET SAIT\runs\detect\human-detector-4\weights\best.pt")

cap = cv2.VideoCapture(0)

print("Kamera açıldı! Çıkmak için 'q' tuşuna bas.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()
    cv2.imshow("İnsan Tespiti", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()