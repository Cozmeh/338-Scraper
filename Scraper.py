import urllib.request , re , json , csv

def scraper():
    url = "https://news.ycombinator.com/"
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')
    #print(html_content)

    CommentPattern = re.compile(r'(\d+)(?:&nbsp;)?comments')
    LinkTitlePattern = re.compile(r'<span class="titleline"><a href="(?P<link>.*?)">(?P<title>.*?)</a>')

    mainContent = LinkTitlePattern.findall(html_content)
    comments = CommentPattern.findall(html_content)

    final = list(zip(mainContent, comments))

    result = {
        "0-100": [],
        "101-200": [],
        "201-300": [],
        "301-n": []
    }

    for x in final:
        title = x[0][1]
        link = x[0][0]
        comments = int(x[1])

        entry = {"title": title, "link": link, "comments": comments}

        if comments <= 100:
            result["0-100"].append(entry)
        elif 101 <= comments <= 200:
            result["101-200"].append(entry)
        elif 201 <= comments <= 300:
            result["201-300"].append(entry)
        else:
            result["301-n"].append(entry)

    return result

def export():
    result = scraper()
    json.dump(result, open("Hacker News.json", 'w'), indent=2)

    
    with open("Hacker News.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Url", "Comment"])
        for x in result:
            for y in result[x]:
                writer.writerow([y["title"], y["link"], y["comments"]])


export()