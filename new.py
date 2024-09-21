import time


WORK_TIME = 25
SHORT_REST_TIME = 5
LONG_REST_TIME = 15
completed = 0
isWork = True
running = True
workTime = WORK_TIME
restTime = SHORT_REST_TIME

while True:
    if running:
        if isWork:
            workTime -= 1
            if workTime == -1:
                completed += 1
                isWork = False
                restTime = SHORT_REST_TIME if completed % 4 == 0 else LONG_REST_TIME

                print("Time to Rest!")
        else:
            restTime -= 1
            if restTime == -1:
                isWork = True
                print("Time to Work!")
                workTime = WORK_TIME

        minutes, seconds = divmod(workTime if isWork else restTime, 60)

        print("{:02d}:{:02d}".format(minutes, seconds))
        time.sleep(0.7)
