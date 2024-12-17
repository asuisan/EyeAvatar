import cv2

def draw_ellipse_eye(img, eye_center, pupil_center, frame_center, screen_center, prev_pupil_position, movement_multiplier, offset_x_adjustment):
    # Ellipse Eyeのデザイン
    ellipse_radius_x = 100
    ellipse_radius_y = 300
    ellipse_color = (255, 255, 255)
    bar_color = (255, 255, 255)

    if pupil_center:
        offset_x = screen_center[0] + (pupil_center[0] - eye_center[0]) * movement_multiplier + offset_x_adjustment
        y_pos = screen_center[1]

        left_eye_x = offset_x - 250
        right_eye_x = offset_x + 250

        # 楕円を描画
        cv2.ellipse(img, (int(left_eye_x), int(y_pos)), (ellipse_radius_x, ellipse_radius_y), 0, 0, 360, ellipse_color, -1)
        cv2.ellipse(img, (int(right_eye_x), int(y_pos)), (ellipse_radius_x, ellipse_radius_y), 0, 0, 360, ellipse_color, -1)

        prev_pupil_position[0] = offset_x
        prev_pupil_position[1] = y_pos
    else:
        # 横棒を2本描画
        bar_length = 200
        left_eye_x = prev_pupil_position[0] - 250
        right_eye_x = prev_pupil_position[0] + 250
        cv2.line(img, (int(left_eye_x - bar_length // 2), int(screen_center[1])),
                 (int(left_eye_x + bar_length // 2), int(screen_center[1])), bar_color, 40)
        cv2.line(img, (int(right_eye_x - bar_length // 2), int(screen_center[1])),
                 (int(right_eye_x + bar_length // 2), int(screen_center[1])), bar_color, 40)
