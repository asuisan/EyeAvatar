import cv2

def draw_robot_eye(img, eye_center, pupil_center, frame_center, screen_center, prev_pupil_position, movement_multiplier, offset_x_adjustment):
    # Robot Monocularの目のデザイン
    outer_circle_radius = 450
    inner_circle_radius = 200
    line_thickness = 40
    outer_circle_color = (255, 255, 255)
    inner_circle_color = (0, 255, 255)
    bar_color = (0, 255, 255)

    fixed_x = screen_center[0]
    fixed_y = screen_center[1]

    # 白い弧を描画
    cv2.ellipse(img, (int(fixed_x), int(fixed_y)), (outer_circle_radius, outer_circle_radius), 0, 30, 150, outer_circle_color, line_thickness)
    cv2.ellipse(img, (int(fixed_x), int(fixed_y)), (outer_circle_radius, outer_circle_radius), 0, 210, 330, outer_circle_color, line_thickness)

    if pupil_center:
        # 黒目の動きに応じた描画
        offset_x = screen_center[0] + (pupil_center[0] - eye_center[0]) * movement_multiplier + offset_x_adjustment
        y_pos = screen_center[1]
        cv2.circle(img, (int(offset_x), int(y_pos)), inner_circle_radius, inner_circle_color, -1)
        prev_pupil_position[0] = offset_x
        prev_pupil_position[1] = y_pos
    else:
        # 黒目が検出されなかった場合、最後の位置に横棒を描画
        bar_length = 300
        cv2.line(img, (int(prev_pupil_position[0] - bar_length // 2), int(prev_pupil_position[1])),
                 (int(prev_pupil_position[0] + bar_length // 2), int(prev_pupil_position[1])), bar_color, line_thickness)

