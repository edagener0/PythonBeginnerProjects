import time

def countDownTimer(t):
    while t:
        mins, secs = divmod(t, 60)
        print(f'{mins:02d}:{secs:02d}')
        time.sleep(1)
        t -= 1
    
    print("BEEEP BEEEEP BEEEEP BEEEEEPPPPPPPPP")


def main():
    seconds = int(input("How many seconds do you wanna countdown from?\n"))
    countDownTimer(seconds)


if __name__ == '__main__':
    main()
