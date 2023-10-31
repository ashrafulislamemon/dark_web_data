
import sys
import os

from bs4 import BeautifulSoup, Comment
def torSearcher(url):
    # BEFORE YOU START - RUN tor.exe !!!!
    
    import requests
    import random
    

    def get_tor_session():
        session = requests.session()
        # Tor uses the 9050 port as the default socks port
        session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                           'https': 'socks5h://127.0.0.1:9050'}
        return session

  
    session = get_tor_session()



    print("Getting ...", url)
    result = session.get(url).text
    print(result)

    return result
   
old_id=69

import mysql.connector

mydb = mysql.connector.connect(
user='root', password='', host='localhost', database='darkwebdata'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT keyword,data FROM darkweblink WHERE id=%s", [old_id])

myresult = mycursor.fetchall()

def get_plain_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    plain_text = soup.get_text(separator=' ')
    return plain_text.strip()

for x in myresult:


    all_data=eval(x[1])

    keyword=x[0]
    
    for i in all_data:
        url = "http://"+str(i)

      
        try:
            b=torSearcher(url)

            a=get_plain_text(b)
            print('-------------------------------------------------------------------------')

            print(a)
            
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='darkwebdata')
            cursor = conn.cursor()
            sql = "INSERT INTO htmldata (keyword,darkweblink_id,link,html_text_data) VALUES (%s,%s, %s, %s)"
            val = (keyword,old_id,url,a)
            
            cursor.execute(sql, val)
            conn.commit()
        except:
            a='not active link'
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='darkwebdata')
            cursor = conn.cursor()
            sql = "INSERT INTO htmldata (keyword,darkweblink_id,link,html_text_data) VALUES (%s, %s, %s, %s)"
            val = (keyword,old_id,url,a)
            
            cursor.execute(sql,val)
            conn.commit()


programname = os.path.basename(sys.argv[0])

try:
    thelist = sys.argv[1]
    print("Opening ...", thelist)
    with open(thelist, "r", encoding="utf-8") as newfile:
        data = newfile.readlines()
        try:
            #
            for k in data:
                k = k.replace("\n","")
                k = "http://" + k
                torSearcher(k)
        except Exception as E:
            print(E)
except:
    print("Usage : {} <newlineSeperatedList.txt>".format(programname))





