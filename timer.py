import time
class Timer:
    def CountDown(self):
        print("Take a breather, you're about to take the quiz in")
        time.sleep(1)
        for i in range(3, 0, -1):
            print(f"{i}\n")
            time.sleep(1)
        print("GOODLUCK!!")

