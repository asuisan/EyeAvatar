import cv2

def draw_led_eye(img, eye_center, pupil_center, frame_center, screen_center, prev_pupil_position, movement_multiplier, offset_x_adjustment):
    # LED Eyeのデザイン
    led_size = 20  # LED 1つのサイズ
    led_color = (0, 255, 0)  # LEDの色
    black_color = (0, 0, 0)  # 背景色

    left_eye_x = screen_center[0] - 250 + 200
    right_eye_x = screen_center[0] + 250 + 200
    y_pos = screen_center[1] - 100

    num_leds_x = 10
    num_leds_y = 5

    # LEDマトリクスの描画
    def draw_led_matrix(eye_x, y_pos):
        for i in range(num_leds_x):
            for j in range(num_leds_y):
                x = int(eye_x + (i - num_leds_x // 2) * led_size)
                y = int(y_pos + (j - num_leds_y // 2) * led_size)
                cv2.rectangle(img, (x, y), (x + led_size, y + led_size), black_color, -1)

    if pupil_center:
        offset_x = screen_center[0] + (pupil_center[0] - eye_center[0]) * movement_multiplier + offset_x_adjustment + 200
        left_eye_x = offset_x - 250
        right_eye_x = offset_x + 250

        draw_led_matrix(left_eye_x, y_pos)
        draw_led_matrix(right_eye_x, y_pos)

        led_pupil_offset_x = led_size * 2
        cv2.rectangle(img, (int(left_eye_x - led_pupil_offset_x), int(y_pos - led_size)),
                      (int(left_eye_x + led_pupil_offset_x), int(y_pos + led_size)), led_color, -1)
        cv2.rectangle(img, (int(right_eye_x - led_pupil_offset_x), int(y_pos - led_size)),
                      (int(right_eye_x + led_pupil_offset_x), int(y_pos + led_size)), led_color, -1)

        prev_pupil_position[0] = offset_x
        prev_pupil_position[1] = y_pos
    else:
        draw_led_matrix(left_eye_x, y_pos)
        draw_led_matrix(right_eye_x, y_pos)

    # 鼻を固定位置に描写
    draw_nose(img, screen_center)

# 鼻を固定位置に描写する関数
def draw_nose(img, screen_center):
    nose_color = (255, 255, 255)  # 白色の鼻

    # 鼻を三角形で描画
    nose_top = (screen_center[0], screen_center[1] + 100)
    nose_left = (screen_center[0] - 40, screen_center[1] + 160)
    nose_right = (screen_center[0] + 40, screen_center[1] + 160)
    cv2.line(img, nose_top, nose_left, nose_color, 10)
    cv2.line(img, nose_left, nose_right, nose_color, 10)
    cv2.line(img, nose_right, nose_top, nose_color, 10)
