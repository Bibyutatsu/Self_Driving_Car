# title: window.py
# v: 2021-05-23 AU


import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions


from environment import create_level_1
from utils import car_model_management, car_reset
from car import Car
from ai import GA


##################################################
# Environment Variables
HEIGHT = 720
WIDTH = 1280
THICKNESS = 100
STROKE = 1
MOUSE_pressed = False
BUTTON_pressed = []
# FPS = 60 # QC # 2021-05-23T1506 AU
FPS = 50 # QC # 2021-05-23T1506 AU


##################################################
# AI variables
POPULATION = 20


##################################################
# Pyglet
window = pyglet.window.Window(WIDTH, HEIGHT, "Tester", resizable=False)
options = DrawOptions()


##################################################
# Pymunk
space = pymunk.Space()
environment = create_level_1(space, HEIGHT, WIDTH, THICKNESS, STROKE)


##################################################
# AI
ai_handle = GA(POPULATION)


##################################################
# Cars
cars = [
    Car(
        space
        , THICKNESS + THICKNESS // 2
        , HEIGHT - 3 * THICKNESS // 2
        , i + 10
        , environment
    ) for i in range(POPULATION)
    ]
car_model_management(cars, ai_handle)
collided = []


##################################################
# Window Events
@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
    if epoch_to_show is not None:
        epoch_to_show.draw()
    if timestep_to_show is not None:
        timestep_to_show.draw()
    if counter_to_show is not None:
        counter_to_show.draw()


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


##################################################
# GLOBAL PARAMETERS
# V: 2021-05-23T1809 AU

epoch = 1
time_step = 20 # seconds; default: 5 # 2021-05-21T1810 AU
time_counter = 0
collided = []

# Show pyglet Text
text_font_name = 'Times New Roman' # QC # 2021-05-23T1511 AU
text_font_size = 20 # QC # 2021-05-23T1511 AU
text_x = WIDTH // 6 # QC # 2021-05-23T1511 AU
text_y = HEIGHT - 20 # QC # 2021-05-23T1511 AU
text_anchor='center' # QC # 2021-05-23T1511 AU

text_epoch = 'Epoch: {0}'.format(epoch) # QC # 2021-05-23T1516 AU
text_time_step = 'Time step: {0}'.format(time_step) # QC # 2021-05-23T1516 AU
text_time_counter = 'Time counter: {0}'.format(time_counter) # QC # 2021-05-23T1516 AU


def show_pyglet_text(my_text_epoch, my_text_font_name, my_text_font_size, my_text_x, my_text_y, my_text_anchor_x, my_text_anchor_y):
    return pyglet.text.Label(
        my_text_epoch,
        font_name=my_text_font_name, # QC # 2021-05-23T1511 AU
        font_size=my_text_font_size, # QC # 2021-05-23T1511 AU
        x=my_text_x, # QC # 2021-05-23T1511 AU
        y=my_text_y, # QC # 2021-05-23T1511 AU
        anchor_x=my_text_anchor_x, # QC # 2021-05-23T1511 AU
        anchor_y=my_text_anchor_y # QC # 2021-05-23T1511 AU
    )

epoch_to_show = show_pyglet_text(text_epoch, text_font_name, text_font_size,1 * text_x, text_y, text_anchor, text_anchor)
timestep_to_show = show_pyglet_text(text_time_step, text_font_name, text_font_size, 3 * text_x, text_y, text_anchor, text_anchor)
counter_to_show = show_pyglet_text(text_time_counter, text_font_name, text_font_size, 5 * text_x, text_y, text_anchor, text_anchor)


# Update Function
# v: 2021-05-23T1803 AU
def update(dt):
    global time_counter, collided, time_step, epoch, epoch_to_show
    time_counter += 1
    space.step(dt)

    for i in range(len(cars)):
        if cars[i].car_collided is False:
            cars[i].drive()
        else:
            if i not in collided:
                collided.append(i)

    if time_counter >= FPS * time_step or len(collided) == POPULATION:
#        if epoch % 5 == 0:
#            time_step += 5 # give more time for each new epoch
        # update: give less time for each tenth epoch
        if epoch % 10 == 0: # every 10th epoch # 2021-05-23T1500 AU
            time_step -= 1 # give less time # QC # 2021-05-23T1500 AU
            time_step = max(time_step, 5) # keep at least some time # QC # 2021-05-23T1800 AU
        print(
            "Epoch: ", epoch,
            " Reward stats: ",
            ai_handle.evolve_iter(
                cars,
                best_model_path=('./Model', epoch)
            )
        )
        car_model_management(cars, ai_handle)
        car_reset(cars)
        time_counter = 0
        collided = []
        epoch += 1
        epoch_to_show.text = 'Epoch: {0}'.format(epoch) # QC # 2021-05-23T1756 AU
        timestep_to_show.text = 'Time step: {0}'.format(time_step) # QC # 2021-05-23T1756 AU
    counter_to_show.text = str(time_counter // FPS + 1) # QC # 2021-05-23T1758 AU


##################################################
# Main function
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1.0 / FPS)
    pyglet.app.run()
