from ultralytics import YOLO
import cv2

# Load model YOLOv8 dari file
model = YOLO("fishgen.pt")

# Load gambar
image_path = r"path/ke/folder/best.pt" # Gantilah "path/ke/folder/" dengan path lengkap tempat file best.pt berada.
image = cv2.imread(image_path)

# Deteksi
results = model(image)

# Visualisasi hasil
annotated_frame = results[0].plot()

# Tampilkan hasil
cv2.imshow("Deteksi", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
