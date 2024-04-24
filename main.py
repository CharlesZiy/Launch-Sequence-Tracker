# coding=utf8
import time
import datetime
from dateutil import parser
import os

T0_stamp = 0
term = []

event_list = []
term_list = []

class event:
    def __init__(self, t, name):
        self.t = t
        self.name = name

class term:
    def __init__(self, strt, end, name):
        self.strt = strt
        self.end = end
        self.name = name

def file_read():
    with open('CZ-2F/event.txt', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        for i in range(0, len(lines)-1, 2):
            line1 = lines[i].strip()
            line2 = lines[i + 1].strip()
            tmp = event(int(line1) + T0_stamp, line2)
            event_list.append(tmp)

    with open('CZ-2f/term.txt', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            line1 = lines[i].strip()
            line2 = lines[i + 1].strip()
            line3 = lines[i + 2].strip()
            tmp = term(int(line1) + T0_stamp, int(line2) + T0_stamp, line3)
            term_list.append(tmp)

def seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    Str = str(int(hours)).zfill(2) + ":" + str(int(minutes)).zfill(2) + ":" + str(int(seconds)).zfill(2)
    return Str

cur_time = 0
Tp = 0

def update():
    term_iter = 0
    event_iter = 0
    while(1):
        cur_time = int(time.time())
        
        # update event:
        if (cur_time >= event_list[event_iter].t):
            event_iter = event_iter + 1
        
        # update term:
        if (cur_time >= term_list[term_iter].end):
            term_iter = term_iter + 1
        
        cur_term = term_list[term_iter].name
        nxt_event = event_list[event_iter].name
        
        display(cur_term, nxt_event, term_iter, event_iter)
        
        time.sleep(0.25)

def display(cur_term, nxt_event, term_iter, event_iter):
    os.system('cls')
    cur_time_form = time.strftime("%H:%M:%S", time.localtime())
    print(cur_time_form)
    T = int(time.time()) - T0_stamp
    T_str = ""
    if T >= 0:
        T_str = "T+ " + seconds_to_hms(T)
    else:
        T_str = "T- " + seconds_to_hms(-T)
    print(T_str + "UTC+8")
    print()

    print("Current Flight Term: %-20s" % cur_term)
    print("Next Event: %-20s" % nxt_event)

    dis = event_list[event_iter].t - int(time.time())
    dis_str = seconds_to_hms(dis)
    print("Next Event In: %-20s" % dis_str)
    

        
if __name__ == "__main__":
    # NOGUI Version:
    os.system('cls')
    print("星海学社神舟十八号追箭任务")
    T0 = input("请输入预计T0：")
    T0_obj = parser.parse(T0)
    T0_stamp = T0_obj.timestamp()
    os.system('cls')
    file_read()

    update()