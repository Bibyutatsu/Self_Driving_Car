import math
from pyglet.window import mouse
import pymunk
from ai import uncompress_model


def get_rotated_point(x_1, y_1, x_2, y_2, radians, WIDTH, HEIGHT):
    # Rotate x_2, y_2 around x_1, y_1 by angle.
    x_change = (x_2 - x_1) * math.cos(radians) + \
        (y_2 - y_1) * math.sin(radians)
    y_change = (y_1 - y_2) * math.cos(radians) - \
        (x_1 - x_2) * math.sin(radians)
    new_x = x_change + x_1
    new_y = HEIGHT - (y_change + y_1)
    return int(new_x), int(new_y)


def mouse_action(car, MOUSE_pressed, BUTTON_pressed):
    if MOUSE_pressed is True:
        if mouse.LEFT in BUTTON_pressed:
            car.move(1)
        if mouse.RIGHT in BUTTON_pressed:
            car.rotate(0.02)
        if mouse.MIDDLE in BUTTON_pressed:
            car.rotate(-0.02)
    return


def add_debug_point(space, position, radius=3, color=(255, 0, 0)):
    point_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    point_body.position = position
    point_shape = pymunk.Circle(point_body, radius)
    point_shape.color = color
    space.add(point_body, point_shape)
    return


def car_model_management(car_list, GA):
    for i, (car, model) in enumerate(zip(car_list, GA.models)):
        unc_model = uncompress_model(model)
        car_list[i].update_driver(unc_model)


def car_reset(car_list):
    for i in range(len(car_list)):
        car_list[i].reset()
