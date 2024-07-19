import keyboard
import pyautogui
import time
import win32api
import win32con

start_button_code = win32con.VK_XBUTTON1
stop_key = ']'
pause_keys = {'space', 'w', 'a', 's', 'd', 'shift'}
pause_button_code = win32con.VK_XBUTTON2
click_delay = 0.1

terminate_program = False
pause_detection = False

def detect_mouse_button4():
    global pause_detection
    while True:
        if win32api.GetKeyState(start_button_code) < 0:
            pause_detection = False
            return
        if terminate_program:
            return
        time.sleep(0.01)

def detect_left_click():
    print("STart Double CPS")
    while True:
        if win32api.GetKeyState(win32con.VK_LBUTTON) < 0:
            pyautogui.click()
            pyautogui.click()
            print("1 More CPS")
            time.sleep(click_delay)

        if terminate_program:
            print("exit")
            exit(0)

        if pause_detection or win32api.GetKeyState(pause_button_code) < 0:
            print("Pause")
            detect_mouse_button4()
            print("Start Double Again")
            break

        time.sleep(0.01)

def on_key_event(event):
    global terminate_program, pause_detection
    if event.name == stop_key:
        terminate_program = True
    elif event.name not in pause_keys:
        pause_detection = True

def main():
    print("Programe Start")
    keyboard.hook(on_key_event)
    while not terminate_program:
        detect_mouse_button4()
        detect_left_click()
    print("Exit")

if __name__ == "__main__":
    main()
