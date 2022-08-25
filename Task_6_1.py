from time import sleep
class TrafficLight:
    __tl_color = "Off"

    def tl_running(self):
        while True:
            print("\033[31m Red")
            sleep(7)
            print("\033[33m Yellow")
            sleep(2)
            print("\033[32m Green")
            sleep(7)


tl = TrafficLight()
tl.tl_running()
