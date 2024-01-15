import urllib.request
import re
import json
import csv

def scraper():
    url = "https://news.ycombinator.com/"
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')
    #print(html_content)

    CommentP = re.compile(r'(\d+)(?:&nbsp;)?comments')
    LinkTitleP = re.compile(r'<span class="titleline"><a href="(?P<link>.*?)">(?P<title>.*?)</a>')

    mainContent = LinkTitleP.findall(html_content)
    comments = CommentP.findall(html_content)

    # for content,comment in zip(mainContent, comments): 
    #     print("Link : " + content[0] + "\nTitle : " + content[1] + "\nNo of Comments : " + comment + "\n")

    zipped = zip(mainContent, comments)
    l = list(zipped)

    # print(l[0][0][0]) = link
    # print(l[0][0][1]) = title
    # print(l[0][1]) = comments

    # for comment in comments:
    #     print("No of Comments : " + comment)


scraper()