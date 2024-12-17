import cv2
import numpy as np
import threading
from model_switcher import switch_eye_model

model_type = None

alpha = 0.1  # スムージング強度
movement_multiplier = 2  # 移動感度

smoothed_pupil_position = None
eye_closed = False

def change_eye_model():
    global model_type
    while True:
        model_choice = input("Select eye model (0: Robot Monocular, 1: Ellipse Eye, 2: Cute Eye, 3: LED Eye): ")
        if model_choice == "0":
            model_type = "Robot Monocular"
        elif model_choice == "1":
            model_type = "Ellipse Eye"
        elif model_choice == "2":
            model_type = "Cute Eye"
        elif model_choice == "3":
            model_type = "LED Eye"
        else:
            print("No model.")

thread = threading.Thread(target=change_eye_model)
thread.daemon = True
thread.start()

# 表示ウィンドウ
background_width = 1920
background_height = 1080

# カメラキャプチャ
cap = cv2.VideoCapture(0)
prev_pupil_position = [background_width // 2, background_height // 2]

# ループ
while model_type is None:
    pass

cv2.namedWindow("Gaze Detection", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Gaze Detection", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.namedWindow("Debug Window - Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Debug Window - Thresholded", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # デバッグ
    original_debug_frame = frame.copy()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold_frame = cv2.threshold(gray_frame, 50, 255, cv2.THRESH_BINARY_INV)

    black_background = cv2.resize(np.zeros_like(frame), (background_width, background_height))
    screen_center = (black_background.shape[1] // 2, black_background.shape[0] // 2)

    # 瞳孔の重心計算
    moments = cv2.moments(threshold_frame)
    if moments['m00'] != 0:
        cx = int(moments['m10'] / moments['m00'])  # X
        cy = int(moments['m01'] / moments['m00'])  # Y
        pupil_center = (cx, cy)
        eye_closed = False
    else:
        pupil_center = None
        eye_closed = True

    # スムージング処理
    if smoothed_pupil_position is None:
        smoothed_pupil_position = pupil_center
    elif pupil_center is not None:
        smoothed_pupil_position = (
            int(alpha * pupil_center[0] + (1 - alpha) * smoothed_pupil_position[0]),
            int(alpha * pupil_center[1] + (1 - alpha) * smoothed_pupil_position[1])
        )

    # デバッグ用 緑ポイント
    if pupil_center:
        cv2.circle(original_debug_frame, pupil_center, 5, (0, 255, 0), -1)

    resized_original_frame = cv2.resize(original_debug_frame, (320, 240))
    resized_threshold_frame = cv2.resize(cv2.cvtColor(threshold_frame, cv2.COLOR_GRAY2BGR), (320, 240))
    cv2.imshow("Debug Window - Original", resized_original_frame)
    cv2.imshow("Debug Window - Thresholded", resized_threshold_frame)

    eye_center = (frame.shape[1] // 2, frame.shape[0] // 2)
    frame_center = (frame.shape[1] // 2, frame.shape[0] // 2)
    switch_eye_model(
        model_type, black_background, eye_center,
        smoothed_pupil_position if not eye_closed else None,
        frame_center, screen_center, prev_pupil_position,
        movement_multiplier, offset_x_adjustment=100
    )

    # デジタル目の表示
    cv2.imshow("Gaze Detection", black_background)

    # キーボード入力
    key = cv2.waitKey(1)
    if key == ord('0'):
        model_type = "Robot Monocular"
    elif key == ord('1'):
        model_type = "Ellipse Eye"
    elif key == ord('2'):
        model_type = "Cute Eye"
    elif key == ord('3'):
        model_type = "LED Eye"
    elif key == 27:  # Esc
        break

cap.release()
cv2.destroyAllWindows()
