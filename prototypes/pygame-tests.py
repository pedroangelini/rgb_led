import pygame
import time

FPS = 120
FRAME_ns = 1_000_000_000 // FPS
NUM_LEDS = 50


pygame.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 20
RADIUS = WINDOW_WIDTH / NUM_LEDS / 2


leds = []

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


colors = [
    (255, 0, 0),  # red
    (255, 127, 0),  # orange
    (255, 255, 0),  # yellow
    (0, 255, 0),  # green
    (0, 255, 255),  # cyan
    (0, 0, 255),  # blue
    (127, 0, 255),  # violet
    (255, 0, 255),  # magenta
    (255, 0, 127),  # rose
    (0, 0, 0),  # black
]
num_colors = len(colors)
frame_count: int = 0
elapsed_time = 0
frame_start = 0


def show() -> None:
    # global leds
    # print(chr(27) + "[2J", end="", flush=True)
    # print("".join(str(x) for x in leds), flush=True)
    for l in range(NUM_LEDS):
        pygame.draw.circle(
            surface,
            leds[l],
            (2 * RADIUS * (1 + l) - RADIUS / 2, WINDOW_HEIGHT / 2),
            RADIUS,
        )
    pygame.display.flip()


def setup() -> None:
    global leds
    global running
    global start_time, frame_start

    leds = [0] * NUM_LEDS
    start_time = time.perf_counter_ns()
    frame_start = elapsed_time
    running = True


led_i = 0
color_i = 0
count_loops_frame = 0

LED_MOVE_RATE = 5  # times per second


def loop() -> bool:
    global start_time, frame_start, frame_count
    global leds
    global led_i, color_i
    global count_loops_frame

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    # handle end of frame
    current_time = time.perf_counter_ns()
    if current_time - frame_start >= FRAME_ns:
        show()
        print(f"frame {frame_count:>5} | loops frame {count_loops_frame}")
        frame_start = current_time
        frame_count += 1
        count_loops_frame = 0

        return True

    # We have time, let's do work
    elapsed_time_s = (current_time - start_time) // 1_000_000_000
    led_i += 1
    if led_i >= NUM_LEDS:
        led_i = 0

    leds[led_i] = colors[color_i]

    color_i = (elapsed_time_s + led_i) % num_colors
    count_loops_frame += 1

    return True


if __name__ == "__main__":
    setup()

    global running
    while running:

        running = loop()

    exit(0)
