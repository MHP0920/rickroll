from tkinter import *
import webbrowser
import os
import sys
from tkinter.ttk import *
import random
from tkinter import messagebox

app = Tk()
app.title("Security System")
app.geometry("400x400")

label = Label(app, text="Security System", font=20)
label.pack()
logtext = Text(app, height=10, width=50)
logtext.pack()
progress = Progressbar(app, orient=HORIZONTAL, length=200, mode='determinate')
progress.pack()
progress_label = Label(app, text="Progress: 0%", font=10)
progress_label.pack()
max_num = random.randint(1000, 9999)
def auto_log(text):
    logtext.insert(END, text + "\n")
    logtext.see(END)

def download_pay1(percent):
    percent += random.randint(1, 4)
    
    if percent < 100:
        auto_log("[+] Downloading system updates... " + str(percent) + "%")
        app.after(random.randrange(100, 200), download_pay1, percent)
    else:
        auto_log("[+] Downloading system updates... 100%")
        install_pay1(0)
def install_pay1(percent):
    percent += random.randint(1, 4)
    
    if percent < 100:
        auto_log("[+] Installing system updates... " + str(percent) + "%")
        app.after(random.randrange(100, 200), install_pay1, percent)
    else:
        auto_log("[+] Installing system updates... 100%")
        progress['value'] = 20
        progress_label['text'] = "Progress: 20%"
        payload_2()
def payload_2():
    auto_log("[+] Start scanning system...")
    auto_log("[+] Total file(s) scanned: 0 files")
    scan_pay2(0)
def scan_pay2(nums):
    nums += random.randint(10, 50)
    auto_log("[+] Total file(s) scanned: " + str(nums) + " files")
    if nums < max_num:
        app.after(random.randrange(50,100), scan_pay2, nums)
    else:
        auto_log("[+] Total file(s) scanned: " + str(max_num) + " files")
        progress['value'] = 40
        progress_label['text'] = "Progress: 40%"
        auto_log("[+] Scanning complete!")
        auto_log("[+] Starting system update...")
        auto_log("[+] Updating system... 0%")
        update_pay3(0)
def update_pay3(percent):
    percent += random.randint(1, 4)
    
    if percent < 100:
        auto_log("[+] Updating system... " + str(percent) + "%")
        app.after(random.randrange(100, 400), update_pay3, percent)
    else:
        auto_log("[+] Updating system... 100%")
        auto_log("[+] System updated!")
        progress['value'] = 100
        progress_label['text'] = "Progress: 100%"
        open_rickroll()
def open_rickroll():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    messagebox_payload(0)
def messagebox_payload(times):
    times += 1
    messagebox.showinfo("Security System", "Bạn đã bị Rickroll =))")
def payload_1():
    auto_log("[+] Downloading system updates...")
    percent = 0
    auto_log("[+] Downloading system updates... 0%")
    download_pay1(percent)
payload_1()
app.update()
app.mainloop()