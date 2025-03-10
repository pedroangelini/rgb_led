import time

FPS = 30
FRAME_ns = 1_000_000_000 // FPS
NUM_LEDS = 50

leds = []

colors = ["⚫", "🔴", "🟠", "🟡", "🟢", "🔵", "🟣"]
frame_count: int = 0
elapsed_time = 0
frame_start = 0


def show() -> None:
    global leds
    print(chr(27) + "[2J", end="", flush=True)
    print("".join(str(x) for x in leds), flush=True)


def setup() -> None:
    global leds
    leds = [0] * NUM_LEDS
    global elapsed_time, frame_start
    elapsed_time = time.perf_counter_ns()
    frame_start = elapsed_time


led_i = 0
color_i = 0


def loop() -> None:
    global elapsed_time, frame_start, frame_count
    global leds
    global led_i, color_i

    # Frame is over, show what we have
    current_time = time.perf_counter_ns()
    if current_time - frame_start >= FRAME_ns:
        show()
        frame_start = current_time
        frame_count += 1

        return

    # We have time, let's do work
    led_i += 1
    if led_i >= NUM_LEDS:
        led_i = 0
    leds[led_i] = colors[color_i]

    color_i = (frame_count + led_i) % len(colors)


if __name__ == "__main__":
    setup()
    while True:
        loop()
