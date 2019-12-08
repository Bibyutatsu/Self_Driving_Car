import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions

from environment import create_level_1
from utils import car_model_management, car_reset
from car import Car
from ai import GA

# Environment Variables
HEIGHT = 720
WIDTH = 1280
THICKNESS = 100
STROKE = 1
MOUSE_pressed = False
BUTTON_pressed = []
POPULATION = 15
FPS = 60

# Pyglet
window = pyglet.window.Window(WIDTH, HEIGHT, "Tester", resizable=False)
options = DrawOptions()

# Pymunk
space = pymunk.Space()
environment = create_level_1(space, HEIGHT, WIDTH, THICKNESS, STROKE)

ai_handle = GA(POPULATION)
cars = [Car(
    space,
    THICKNESS + THICKNESS // 2,
    HEIGHT - 3 * THICKNESS // 2,
    i + 10,
    environment) for i in range(POPULATION)]
car_model_management(cars, ai_handle)
collided = []


# Window Events
@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)


@window.event
def on_mouse_press(x, y, button, modifiers):
    global MOUSE_pressed, BUTTON_pressed
    MOUSE_pressed = True
    if button not in BUTTON_pressed:
        BUTTON_pressed.append(button)


@window.event
def on_mouse_release(x, y, button, modifiers):
    global MOUSE_pressed, BUTTON_pressed
    MOUSE_pressed = False
    if button in BUTTON_pressed:
        BUTTON_pressed.remove(button)


time_counter = 0
collided = []
time_step = 5  # In seconds
epoch = 1


# Update Function
def update(dt):
    global time_counter, collided, time_step, epoch
    time_counter += 1
    space.step(dt)

    for i in range(len(cars)):
        if cars[i].car_collided is False:
            cars[i].drive()
        else:
            if i not in collided:
                collided.append(i)

    if time_counter >= FPS * time_step or len(collided) == POPULATION:
        if epoch % 5 == 0:
            time_step += 5
        print("Epoch: ", epoch, " Reward stats: ", ai_handle.evolve_iter(cars))
        car_model_management(cars, ai_handle)
        car_reset(cars)
        time_counter = 0
        collided = []
        epoch += 1


# Main function
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1.0 / FPS)
    pyglet.app.run()
