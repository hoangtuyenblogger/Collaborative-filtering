from bs4 import BeautifulSoup
import requests
import csv
import sqlite3

f = open('link.csv', 'a+')
f_writer = csv.writer(f,lineterminator='\n')


def get_links_job(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    a = soup.findAll('a', class_="title-job")
    links = [link.attrs['href'] for link in a]
    #add database
    conn = sqlite3.connect("data/DBTimviec.db")
    query = """
    INSERT INTO LINKS_JOB(LINK) VALUES (?)
    """
    for i in links:
        link = "https://timviecnhanh.com" + str(i).replace("?svs=max_box","")
        conn.execute(query, (link,))
        conn.commit()
        print("added to database ", link)

def get_links_job_from_range_page():
    a = int(input("Lấy link bắt đầu từ phân trang thứ : "))
    b = int(input("Đến phân trang thứ :"))
    link = str(input("link = "))
    for i in range(a,b+1,1):
        url = link + str(i)
        get_links_job(url)

if __name__ == '__main__':
    get_links_job_from_range_page()

