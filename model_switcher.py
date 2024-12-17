from eye_model_robot import draw_robot_eye
from eye_model_ellipse import draw_ellipse_eye
from eye_model_cute import draw_cute_eye
from eye_model_LED import draw_led_eye

def switch_eye_model(model_type, img, eye_center, pupil_center, frame_center, screen_center, prev_pupil_position, movement_multiplier, offset_x_adjustment):
    if model_type == "Robot Monocular":
        draw_robot_eye(img, eye_center, pupil_center, frame_center, screen_center, prev_pupil_position, movement_multiplier, offset_x_adjustment)
    elif model_type == "Ellipse Eye":
        draw_ellipse_eye(img, eye_center, pupil_center, frame_center, screen_center, prev_pupil_position, movement_multiplier, offset_x_adjustment)
    elif model_type == "Cute Eye":
        draw_cute_eye(img, eye_center, pupil_center, frame_center, screen_center, prev_pupil_position, movement_multiplier, offset_x_adjustment)
    elif model_type == "LED Eye":
        draw_led_eye(img, eye_center, pupil_center, frame_center, screen_center, prev_pupil_position, movement_multiplier, offset_x_adjustment)
