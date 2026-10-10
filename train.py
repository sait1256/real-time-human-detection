from ultralytics import YOLO

def main():
    model = YOLO("yolo11n.pt")

    model.train(
        data="data.yaml",
        epochs=20,
        imgsz=640,
        batch=8,
        device="cuda",
        workers=0,
        name="human-detector"
    )

    print("Eğitim tamamlandı!")

if __name__ == "__main__":
    main()