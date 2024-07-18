import keyboard
import pyautogui
import time
import win32api
import win32con

def detect_mouse_button4():
    while True:
        if win32api.GetKeyState(win32con.VK_XBUTTON1) < 0:
            return
        time.sleep(0.01)

def detect_left_click():
    while True:
        if win32api.GetKeyState(win32con.VK_XBUTTON1) < 0:
            print("两倍cps启动!")
            while True:
                if win32api.GetKeyState(win32con.VK_LBUTTON) < 0:
                    pyautogui.click()
                    # print("增加一个cps")
                    time.sleep(0.1)
                
                if keyboard.is_pressed(']'):
                    print("程序终止")
                    exit(0)
                
                time.sleep(0.01)

def on_key_event(event):
    if event.name not in ['space', 'w', 'a', 's', 'd', 'shift'] and event.event_type == 'down':
        print("暂停双倍左键")
        return True
    return False

if __name__ == "__main__":
    print("启动程序")
    while True:
        detect_mouse_button4()
        keyboard.hook(on_key_event)
        detect_left_click()
        keyboard.unhook_all()
