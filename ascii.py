#! /usr/bin/env python3
import sys
try:
    import requests
    import user_agent
    import bs4
    from rgbprint import gradient_print
except Exception as e:
    print(str(e)+"\n!")
    sys.exit('use "pip3 install -r requirements.txt')
def Session():
    url="https://ascii-generator.site/a/text_to_ascii_generator/"
    agent=user_agent.generate_user_agent()
    headers={
        "User-Agent":agent
    }
    req=requests.get(url,headers=headers)
    soup=bs4.BeautifulSoup(req.text,"html.parser").find("input",{"name":"csrfmiddlewaretoken"}).get("value")
    return req.headers["Set-Cookie"],soup,agent
def banner():
    banner="""
   _____      _________ _________   .___  .___
  /  _  \    /   _____/ \_   ___ \  |   | |   |             /  /_\  \   \_____  \  /    \  \/  |   | |   |
/    |    \  /        \ \     \____ |   | |   |            \____|__  / /_______  /  \______  / |___| |___|
        \/          \/          \/
              Code By issam iso 
    """
    gradient_print(banner,start_color="blue",end_color="red")
def ascii(word,fsaveasic):
    try:
        token,csrf,agent=Session()
    except Exception as e:
        sys.exit(str(e))
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': agent,
        'sec-ch-ua-platform': '"Android"',
        'Origin': 'https://ascii-generator.site',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ascii-generator.site/t/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-CA,en;q=0.9,ar-TN;q=0.8,ar;q=0.7,en-US;q=0.6',
        'Cookie': token
    }
    data={
        "csrfmiddlewaretoken": csrf,
        "txt":word,
        "txt_multi":""
    }
    url="https://ascii-generator.site/a/text_to_ascii_generator/"
    req=requests.post(url,headers=headers,data=data).json()
    for i in req["results"]:
        for z in i:
            file=open(fsaveasic,"a")
            file.write("\n"+z+"\n\n\n")
            file.close()
def Supper():
    banner()
    try:
        ascii_text=sys.argv[1]
        fsaveasic=ascii_text.replace(" ","").strip()+".txt"
        try:
            ascii(ascii_text,fsaveasic)
            gradient_print("[+] saved ascii text in ({})".format(fsaveasic),start_color="blue",end_color="yellow")
        except Exception as e:
            sys.exit(str(e))
    except:
        
        texf="[+] text to ascii generator: "
        gradient_print(texf,start_color="red",end_color="green",end="")
        ascii_text=input()
        if ascii_text =="" or ascii_text.strip() =="":
            sys.exit()
        fsaveasic=ascii_text.replace(" ","").strip()+".txt"
        try:
            ascii(ascii_text,fsaveasic)
            gradient_print("[+] saved ascii text in ({})".format(fsaveasic),start_color="blue",end_color="yellow")
        except Exception as e:
            sys.exit(str(e))
try:
    Supper()
except KeyboardInterrupt:
    sys.exit()
except Exception as e:
    sys.exit(str(e))