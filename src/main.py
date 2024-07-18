import keyboard
import pyautogui
import time
import win32api
import win32con

# 设置
start_button_code = win32con.VK_XBUTTON1
stop_key = ']'
pause_keys = {'space', 'w', 'a', 's', 'd', 'shift'}
click_delay = 0.1

# 全局标志
terminate_program = False
pause_detection = False

def detect_mouse_button4():
    while True:
        if win32api.GetKeyState(start_button_code) < 0:  # 检测鼠标按键4
            return
        if terminate_program:
            return
        time.sleep(0.01)

def detect_left_click():
    print("开始检测左键点击")
    while True:
        if win32api.GetKeyState(win32con.VK_LBUTTON) < 0:  # 检测左键点击
            pyautogui.click()  # 模拟左键点击
            pyautogui.click()  # 再次模拟左键点击
            print("增加一个cps")
            time.sleep(click_delay)  # 模拟点击延迟

        if terminate_program:
            print("程序终止")
            exit(0)

        if pause_detection:
            print("暂停检测")
            detect_mouse_button4()  # 等待鼠标按键再次启动检测
            print("重新开始检测")
            break

        time.sleep(0.01)

def on_key_event(event):
    global terminate_program, pause_detection
    if event.name == stop_key:
        terminate_program = True
    elif event.name not in pause_keys:
        pause_detection = True
    else:
        pause_detection = False

if __name__ == "__main__":
    print("启动程序")
    keyboard.hook(on_key_event)
    while not terminate_program:
        detect_mouse_button4()
        detect_left_click()
    print("程序已终止")
