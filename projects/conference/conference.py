import re
import sys
import logging
import threading
import random
import itertools
import datetime

lightning = 5

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def parse_input(dir,file):
    lineList = list()
    with open(file) as f:
        lineList = [line.rstrip('\n') for line in f]

    first = [" ".join(a.split()[:-1]) for a in lineList]
    last = [a.split()[-1] for a in lineList]
    final_list = list(zip(first,last))
    return final_list

def worker():
    conf = Conference()
    conf.start_conference()
    return

class Presenter:
    def __init__(self):
        return

    def in_time(self,in_time):
        print("Presenter arrival time is : %s", in_time)


class Timer:
    def __init__(self):
        self.time = datetime.datetime.strptime('9:00', '%H:%M')
    
    def get_time(self):
        return self.time.time()
    
    def update_time(self, value):
        self.time = self.time + datetime.timedelta(minutes=value)

class Event:
    def __init__(self, event_type):
        self.event_type = event_type
        return

    def start_event(self, timer):
        print(str(timer.get_time()) + " Networking")

    def time_validator(self, start_time, end_time):
        if start_time > 4 and end_time < 5:
            return 
        else:
            raise ValueError("Time should be between 4 and 5")

class Track:
    id = 0
    def __init__(self, input=None):
        self.timer = Timer()
        self.input= input
        self.talk_list=[]
        Track.id += 1
        print("Track"+ str(self.id) + "")
        self._create_track_list()
    
        
    def start_session(self,session_type):
        if session_type == 'Morning':
            total_minutes = 180
        else:
            total_minutes = 240
        
        session  = Session(session_type)
        session.create_session(total_minutes)
        
    def start_lunch(self):
        time = datetime.datetime.strptime('12:00', '%H:%M').time()
        if self.timer.get_time() == time:
            print(str(self.timer.get_time()) + " Lunch" )
            self.timer.update_time(60)

    def start_event(self, event_type):
        event = Event(event_type)
        event.start_event(self.timer)

    def _create_track_list(self):
        for i in self.input:
            a,b = i            
            talk = Talk(a,b)
            self.talk_list.append(talk)
        return self.talk_list

class Session(Track):
    def __init__(self, session_type):
        super().__init__()
        self.session_type = session_type
    
    def create_session(self,total_minutes):
        track_list = self._create_talk_list(total_minutes)
        for t in track_list:
            start_time = datetime.datetime.strptime('9:00', '%H:%M').time()
            lunch_time = datetime.datetime.strptime('12:00', '%H:%M').time()
            end_track = datetime.datetime.strptime('17:00', '%H:%M').time()
            if (self.timer.get_time() == lunch_time or self.timer.get_time() >= end_track):
                return
            else:
                if (t.time == 'lightning'):
                    result = lightning
                else:
                    result = int(re.search(r"\d+(\.\d+)?", t.time).group(0))
                
                print(str(self.timer.get_time()) + " " + t.title + " " + t.time)
                self.timer.update_time(result)
    
    def update_track_list(self,track_list):
        for t in track_list:
            for x in self.talk_list:
                    if t.title == x.title:
                        self.talk_list.remove(x)
    
    def _create_talk_list(self, total_minutes):
        scenario = self._calculate_scenario(self.talk_list, total_minutes)
        self.update_track_list(scenario)
        return scenario
    
    def _calculate_scenario(self, session_list, total_minutes):
        talk_list = []
        time_list= []
        new_list = [(s.title,5) if (s.time == 'lightning') else (s.title, int(s.time.replace('min',''))) for s in session_list]
        for a,b in new_list:
            time_list.append(b)
        result = [seq for i in range(0,len(time_list)) for seq in itertools.combinations(time_list, i) if sum(seq) == total_minutes]
        random_choice = random.choice(result)
        final_list = []
        item_list = []
        for item in random_choice:
            for s in new_list:
                if item in s:
                    if item not in item_list:
                        item_list.append(s)
            
            elem = random.choice(item_list)
            final_list.append(elem)
            item_list=[]
        new_list = [(s, 'lightning') if (v == 5) else (s, str(v)+'min') for s,v in final_list]        
        for a in new_list:
            x,y = a 
            talk_list.append(Talk(x,y))
        return talk_list


class Talk:
    def __init__(self,title,time):
        self.title = title
        self.time = time
    
    @property
    def title(self):
        return self._title

    @property
    def time(self):
        return self._time
    
    @title.setter
    def title(self, title):
        pattern = '[0-9]'
        check = any(char.isdigit() for char in title)
        if check == True:
            raise Exception("Title should not contain numbers")
        self._title = title

    @time.setter   
    def time(self, time):
        if ('min' in time):
            self._time=time
        elif (time == 'lightning' or 5):
            self._time=time
        else:
            raise ValueError("Talk length should be lighting or in minutes")


class Conference:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
        self.timer = Timer()
        return
    
    def start_conference(self):
        lineList = list()
        input = parse_input('.','input.txt')
        track = Track(input)
        track.start_session("Morning")
        track.start_lunch()
        track.start_session("Evening")
        track.start_event("Networking")
        track = Track(input)
        track.start_session("Morning")
        track.start_lunch()
        track.start_session("Evening")
        track.start_event("Networking")
        
        
def main ():
    conf = Conference()
    conf.start_conference()


if __name__== "__main__":
  main()