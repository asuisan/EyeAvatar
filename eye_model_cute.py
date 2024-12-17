import cv2

def draw_cute_eye(img, eye_center, pupil_center, frame_center, screen_center, prev_pupil_position, movement_multiplier, offset_x_adjustment):
    # かわいい目のデザイン
    eye_radius_x = 150  # 白目の横幅
    eye_radius_y = 200  # 白目の縦幅
    pupil_radius = 70  # 黒目の大きさ
    highlight_radius = 20  # ハイライトの大きさ
    eye_color = (255, 255, 255)  # 白目の色
    pupil_color = (0, 0, 0)  # 黒目の色
    pupil_outer_color = (0, 0, 139)  # 黒目の外側の色
    highlight_color = (255, 255, 255)  # ハイライトの色

    left_eye_x = screen_center[0] - 250
    right_eye_x = screen_center[0] + 250
    y_pos = screen_center[1]

    if pupil_center:
        offset_x = screen_center[0] + (pupil_center[0] - eye_center[0]) * movement_multiplier + offset_x_adjustment

        # 黒目に合わせて目の位置も移動
        left_eye_x = offset_x - 250
        right_eye_x = offset_x + 250

        # 白目を描画
        cv2.ellipse(img, (int(left_eye_x), int(y_pos)), (eye_radius_x, eye_radius_y), 0, 0, 360, eye_color, -1)
        cv2.ellipse(img, (int(right_eye_x), int(y_pos)), (eye_radius_x, eye_radius_y), 0, 0, 360, eye_color, -1)

        # 黒目を描画
        cv2.circle(img, (int(left_eye_x), int(y_pos)), pupil_radius, pupil_outer_color, -1)
        cv2.circle(img, (int(left_eye_x), int(y_pos)), pupil_radius - 20, pupil_color, -1)
        cv2.circle(img, (int(right_eye_x), int(y_pos)), pupil_radius, pupil_outer_color, -1)
        cv2.circle(img, (int(right_eye_x), int(y_pos)), pupil_radius - 20, pupil_color, -1)

        # ハイライトを追加
        cv2.circle(img, (int(left_eye_x - 30), int(y_pos - 50)), highlight_radius, highlight_color, -1)
        cv2.circle(img, (int(right_eye_x - 30), int(y_pos - 50)), highlight_radius, highlight_color, -1)

        prev_pupil_position[0] = offset_x
        prev_pupil_position[1] = y_pos
    else:
        # 閉じた目の状態
        arc_thickness = 40
        arc_color = (255, 255, 255)

        # 左目の円弧を描画
        cv2.ellipse(img, (int(left_eye_x), int(y_pos)), (eye_radius_x, eye_radius_y // 2), 0, 0, 180, arc_color, arc_thickness)

        # 右目の円弧を描画
        cv2.ellipse(img, (int(right_eye_x), int(y_pos)), (eye_radius_x, eye_radius_y // 2), 0, 0, 180, arc_color, arc_thickness)
