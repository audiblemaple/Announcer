from selenium import webdriver
from datetime import datetime
from playsound import playsound
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def init_driver():
    EXTPATH = r'C:\3.12_0'
    chrome_options = Options()
    chrome_options.add_argument('load-extension=' + EXTPATH)

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = PATH)
    driver.get("https://www.youtube.com/watch?v=zJODMh2cULg")

    return driver


def init_bracelets():
    bracelets = [["green.wav", "12:21", "13:35", "16:05", "18:35"],
                 ["purple.wav", "11:35", "14:05", "16:35", "19:05"],
                 ["blue.wav", "12:05", "14:35", "17:05", "19:35"],
                 ["yellow.wav", "12:35", "15:05", "17:35", "20:05"],
                 ["orange.wav", "13:05", "16:35", "18:05", "20:35"]]
    return bracelets

def init_adv():
    adv = ["adv.wav", "10:20", "12:20", "14:20", "16:20", "18:20", "19:15"]


def announce(fname, now, driver):
    video = driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE)  # hits space
    time.sleep(1)
    print("announced:", fname[0:len(fname) - 4:], now.strftime("%H:%M:%S"))
    playsound(fname)
    time.sleep(1)
    video = driver.find_element_by_id('movie_player')
    video.send_keys(Keys.SPACE)  # hits space


def main():
    driver = init_driver()
    identifier = "watch"
    bracelets = init_bracelets()
    adv = init_adv()

    while True:
        flg = False
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("checked:", now.strftime("%H:%M:%S"))
        for i in range(0, len(bracelets)):
            for j in range(0, len(bracelets[i])):
                #
                # for k in range(1, len(adv)):
                #     if current_time == adv[i]:
                #         announce(adv[0], now, driver)
                #         time.sleep(59.8)
                #
                if current_time == bracelets[i][j]:
                    original_tab = driver.current_window_handle
                    tabs = driver.window_handles
                    for t in tabs:
                        if t != original_tab:
                            driver.switch_to.window(t)
                            continue
                        if driver.current_url.find(identifier) != -1:
                            announce(bracelets[i][0], now, driver)
                            flg = True
                            break
                    if flg:
                        break
                    time.sleep(1)
                    print("announced:", bracelets[i][0][0:len(bracelets[i][0]) - 4:], now.strftime("%H:%M:%S"))
                    playsound(bracelets[i][0])
                    time.sleep(1)
                if flg:
                    break
            if flg:
                break
        time.sleep(59.8)


main()



#                       ORIGINAL BRACELETS
# bracelets = [["green.wav", "11:00", "13:35", "16:05", "18:35"],
#               ["purple.wav", "11:35", "14:05", "16:35", "19:05"],
#               ["blue.wav", "12:05", "14:35", "17:05", "19:35"],
#               ["yellow.wav", "12:35", "15:05", "17:35", "20:05"],
#               ["orange.wav", "13:05", "15:35", "18:05", "20:35"]]



#     # CHROME PART
#     original_tab = driver.current_window_handle
#     tabs = driver.window_handles
#     for i in tabs:
#         if i != original_tab:
#             driver.switch_to.window(i);
#         if driver.current_url.find(identifier) != -1:
#             start_stop(driver)
#             print("stop\n")
#             time.sleep(5)
#             start_stop(driver)
#             print("start\n")
#             time.sleep(5)








# from selenium import webdriver
# from datetime import datetime
# from playsound import playsound
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import time
#
#
# def init_driver():
#     EXTPATH = r'C:\3.12_0'
#
#     chrome_options = Options()
#     chrome_options.add_argument('load-extension=' + EXTPATH)
#     PATH = "C:\Program Files (x86)\chromedriver.exe"
#     #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver = webdriver.Chrome(chrome_options = chrome_options, executable_path = PATH)
#
#     driver.get("https://www.youtube.com/watch?v=zJODMh2cULg")
#     return driver
#
#
# def start_stop(driver):
#     video = driver.find_element_by_id('movie_player')
#     video.send_keys(Keys.SPACE)  # hits space
#
#
# def init_bracelets():
#     bracelets = [["green.wav", "11:00", "13:35", "16:05", "18:35"],
#                  ["purple.wav", "11:35", "14:05", "16:35", "19:05"],
#                  ["blue.wav", "12:05", "14:35", "17:05", "19:35"],
#                  ["yellow.wav", "12:35", "15:05", "17:35", "20:05"],
#                  ["orange.wav", "13:05", "16:35", "18:05", "20:35"]]
#
#
#     #                       ORIGINAL
#     # bracelets = [["green.wav", "11:00", "13:35", "16:05", "18:35"],
#     #               ["purple.wav", "11:35", "14:05", "16:35", "19:05"],
#     #               ["blue.wav", "12:05", "14:35", "17:05", "19:35"],
#     #               ["yellow.wav", "12:35", "15:05", "17:35", "20:05"],
#     #               ["orange.wav", "13:05", "15:35", "18:05", "20:35"]]
#     return bracelets
#
#
# def announce(color, now):
#     time.sleep(1.5)
#     print("announced:", color[0:len(color) - 4:], now.strftime("%H:%M:%S"))
#     playsound(color)
#     time.sleep(1)
#
#
# def main():
#     driver = init_driver()
#     identifier = "watch"
#     bracelets = init_bracelets()
#
#     while True:
#         flg = False
#         now = datetime.now()
#         current_time = now.strftime("%H:%M")
#         print("checked:", now.strftime("%H:%M:%S"))
#         for i in range(0, len(bracelets)):
#             for j in range(0, len(bracelets[i])):
#                 if current_time == bracelets[i][j]:
#                     original_tab = driver.current_window_handle
#                     tabs = driver.window_handles
#                     for t in tabs:
#                         if t != original_tab:
#                             driver.switch_to.window(t)
#                             continue
#                         if driver.current_url.find(identifier) != -1:
#                             start_stop(driver)
#                             print("stop\n")
#
#                             announce(bracelets[i][0], now)
#                             flg = True
#
#                             start_stop(driver)
#                             print("start\n")
#                             break
#                     if flg:
#                         break
#                     announce(bracelets[i][0], now)
#                 if flg:
#                     break
#             if flg:
#                 break
#         time.sleep(59.8)
#
#
# main()