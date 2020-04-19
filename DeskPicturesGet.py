#This is a simple pictureGettingProgram
#Programmer: FANGJIANSI
import requests
import re
import os
import traceback
import time

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getUrlList(list, html):
    try:
        findJpg = re.findall(r'data-wallpaper-id=\"[a-zA-Z0-9]+\"', html)
        for i in range(len(findJpg)):
            number = eval(findJpg[i].split("=")[1])
            list.append(number)
    except:
        traceback.print_exc()
        print("")


def storagePictures(list, path, count):
    count1 = 0
    for i in list:
        try:
            count = count+1
            filename = (path+"//{}.jpg".format(count))
            if not os.path.exists(path):
                os.mkdir(path)
            if not os.path.exists(filename):
                r = requests.get("https://w.wallhaven.cc/full/{}{}/wallhaven-{}.jpg".format(i[0], i[1], i))
                time.sleep(3)
                with open(filename, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    count1 = count1 + 1
                    print("\rCurrent progress: {:.2f}%".format(count1 * 100 / len(list)), end="")
            else:
                print("====                   The number you input at first is wrong!                    ====")
        except:
            traceback.print_exc()
            count1 = count1 + 1
            print("\rCurrent progress: {:.2f}%".format(count1 * 100 / len(list)), end="")
            continue


def main():
    count = 0
    theme = "tree"
    print("             Please input the number of the pictures in folder \n        （if it is the first time you use this program, please input 0）Then hit the Enter key！ ")
    count = int(input("->:"))
    print("              Please input the type of the deskpictures you want in English!\n       (example: tree）Then hit the Enter key！ ")
    theme = input("->:")
    url = "https://wallhaven.cc/search?q="+theme
    jpglist = []
    folderName = 'D://DeskPicturesGet'
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            #"cookie": "__cfduid=ddc150ac31d74334e0d6f76d929ca119f1586215694; XSRF-TOKEN=eyJpdiI6ImtkWU13UGJ2QTNXeG42Y1hFckVNVVE9PSIsInZhbHVlIjoiajhFaE4rc0Jtd1J5WExJaktlRDEwem12c0M1YnRxXC9LQlBZYUo5MFJpRGJNRDNBOUdHcUFpK1dHcHRaOUpwRDkiLCJtYWMiOiJiOTQ4MzBhZmNkNjY3MGJkNzIyYjBhM2NkMTBhOGFjNzQzNTliZDg3N2NiNzJhZjhmZjQ4ZjdjZTc0MTAyMjc3In0%3D; wallhaven_session=eyJpdiI6Ikw2RmN0UUN3TU1DVzBSYzdlbEJBRXc9PSIsInZhbHVlIjoiamtuUWFrVnJjN0N1eTUyeUxuRU5TdUdRQjI2Qko5c0NXRmZYVVlOMUZqaVwvbWUzTGp6ZTcyYkN3a2RMalBENDYiLCJtYWMiOiI4NDhjZjM3ODk1Nzc0ZjlkNTcyMzY4NmE4NGQ5MThmYTM3YmJmMThkOTU5MzM5Y2M4ZTFlOTlhMWZkN2U5ZjM0In0%3D; _pk_id.1.01b8=0a7a2092dbf0bfbb.1586215716.3.1586248645.1586248645.; _pk_ses.1.01b8=1"
        }
        html = requests.get(url, headers=headers)
        getUrlList(jpglist, html.text)
        storagePictures(jpglist, folderName, count)
        print("==================               Mission accomplished!           ===========================")
        print("=====              Now you can find your pictures in drive D DeskPicturesGet folder           ========")
        a = input()
    except:
        print("====================                Mission failed!               =======================")


main()


