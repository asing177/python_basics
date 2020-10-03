import pytest
import time
import sys
import tempfile
import shutil
from os import path
import unittest

from conference import *

class TestConference(unittest.TestCase):
    def parse_error(self):
        raise ValueError("Unable to parse the file")

    def test_raises_exception_on_non_string_arguments(self):
        try:
            f = open(('test.txt'), 'w')
            f.write('The owls 99889889 what they seem')
            parse_input('.','test.txt')
        except: 
            self.assertRaises(ValueError, self.parse_error())
    
    def test_talk(self):
        title = "Python hello world"
        time = "45min"
        t = Talk(title,time)
        print(t.time)
    
    def test_talk_title_with_number(self):
        title = "Python9 hello world"
        time = "45"
        t = Talk(title,time)
        print(t.time)
    
    def test_talk_time_without_minutes(self):
        title = "Python hello world"
        time = "45"
        t = Talk(title,time)
        print(t.time)

    # def test_track_morning_session(self):
    #     track = Track(input)
    #     track.start_session("Morning")


                   