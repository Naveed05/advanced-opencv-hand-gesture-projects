import cv2
import numpy as np

# ===============================
# 1. Load the video safely
# ===============================
video_path = r"C:\NareshIT All\Advanced openCV projects\video frame\los_angeles.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Error: Could not open video. Check the file path.")
    exit()

# ===============================
# 2. Show ONLY the first frame
# ===============================
ret, frame = cap.read()

if ret:
    cv2.imshow("First Frame", frame)
    print("Showing first frame... Press any key.")
    cv2.waitKey(0)
else:
    print("❌ Error: Could not read first frame.")

# ===============================
# 3. Show video frame-by-frame (Press key for next)
# ===============================
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video

while True:
    ret, frame = cap.read()
    if not ret:
        print("Reached end of video.")
        break

    cv2.imshow("Frame by Frame (Press any key)", frame)

    key = cv2.waitKey(0)
    if key == 27:  # ESC to exit
        break

# ===============================
# 4. Play video continuously
# ===============================
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video
print("Playing video in real-time... Press ESC to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Reached end of video.")
        break

    cv2.imshow("Real-Time Video", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

# ===============================
# Cleanup                              
# ===============================
cap.release()
cv2.destroyAllWindows()
