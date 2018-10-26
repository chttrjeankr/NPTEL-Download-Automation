import bs4
import re
import requests
import webbrowser

"""reference and ideas snatched from
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#beautiful-soup-documentation"""

subjectid = input("Enter the subjectID of the course to download from: ")  # 106105151
##  CHANGE THIS ACCORDINGLY ## THE SUBJECT ID OF THE COURSE

video_format = input("Enter video format required: (.mp4 or .flv or .3gp): ")  # ".mp4"
##  CHANGE THIS ACCORDINGLY ## THE VIDEO FORMAT

res = requests.get("https://nptel.ac.in/courses/nptel_download.php?subjectid={}".format(subjectid))
soup = bs4.BeautifulSoup(res.text, 'lxml')
linkList = soup.findAll("a", href=re.compile(video_format))

total_videos = len(linkList)

start_lecture_no = int(input("Enter the first lecture sl.no. (0 to {}) to download from: ".format(total_videos)))
##  CHANGE THIS ACCORDINGLY ## THE NUMBER OF LECTURE FROM WHERE TO START

end_lecture_no = int(input("Enter the last lecture sl.no. (0 to {}) to download to: ".format(total_videos)))
##  CHANGE THIS ACCORDINGLY ## THE NUMBER OF LECTURE TILL WHICH TO DOWNLOAD

#JUST CHECKING
# for link in linkList:
#     print(link)

## Sample Links of downloading videos
# https://nptel.ac.in/courses/download_mp4.php?subjectId=106106182&filename=mod01lec01.mp4&subjectName=Introduction%20to%20Programming
# https://nptel.ac.in/courses/download_mp4.php?subjectId=106105151&filename=mod01lec01.mp4&subjectName=Module%201:%20Recap%20of%20C%20(Lecture%2001)

for i in range(start_lecture_no - 1, end_lecture_no):
    webbrowser.open("https://nptel.ac.in/" + linkList[i].get("href"))

print("Hope you saved all files to the correct location")
print("*-*-*-*-END-*-*-*-*")