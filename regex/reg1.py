#EPAM GOOGLE EXTRACT SSID using REGEX FROM LOGS

import re
import requests
import logging
import gzip
import json

URL = "http://74.208.16.97/interview/mynet.log.gz"
PATTERN = "SSID="

def main():
    response = requests.get(URL, stream=True)

    with open('mynet.log.gz', 'wb') as f:
        f.write(response.content)


    pattern = re.compile(r'\[(.*?)\](.*?)(?=\[|$)')

    info_list = []

    with gzip.open('mynet.log.gz', 'rt') as fin:
        for line in fin:
            if PATTERN in line:
                matches = re.findall(pattern , line)
                if len(matches) == 3:
                    info_list.append(matches[2])
    return info_list


def extract_ssid_freq(info):
    dict = {}
    for i in info:
        if i[1] != '':
            dict[i[0]] = i[1].split(",")[4]

    return dict


def extract_ssid_bssid(info):
    dict = {}
    for i in info:
        if i[1] != '':
            dict[i[0]] = i[1].split(",")[1]

    return dict



if __name__ == '__main__':
    info = main()
    freq = extract_ssid_freq(info)
    bssid= extract_ssid_bssid(info)
    print(freq)
