from ultralytics import YOLO

# Load a model
model = YOLO("/home/fzm/MA/darts_auto_aim/darts4.0/yolo11n.pt")  # load an official detection model
# model = YOLO("yolo11n-seg.pt")  # load an official segmentation model
# model = YOLO("path/to/best.pt")  # load a custom model

# Track with the model
results = model.track(source="0", show=True)
print("results : ",results)
# results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")