from newspaper import Article
from bs4 import BeautifulSoup
import requests
import sqlite3

def get_data(conn,url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find("span", class_="title").text
    address = soup.find("span", class_="jsx-1425348829 d-none d-md-block").text.replace("Địa chỉ: ", "").strip()

    ul = soup.find("ul", class_="jsx-1425348829 no-style p-0")
    li = ul.findAll('li')

    salary = str(li[0].text).replace("- Mức lương:", "").strip()
    ex = str(li[1].text).replace("- Kinh nghiệm:", "").strip()
    level = str(li[2].text).replace("- Trình độ:", "").strip()
    location = str(li[3].text).replace("- Tỉnh/Thành phố:", "").strip()
    job_name = str(li[4].text).replace("- Ngành nghề:", "").strip()

    try:
        query = """
            INSERT INTO JOBS_DATA (TITLE,LINK,ADDRESS,SALARY,EXPERIENCE,LEVEL,LOCATION,JOB_NAME)
                          VALUES (?,?,?,?,?,?,?,?)
            """
        conn.execute(query, (title, url, address, salary, ex, level, location, job_name))  # thêm dữ liệu craw vào db
        conn.commit()
        print("Added {} to database".format(title))
    except Exception as erro:
        print("Có lỗi: ", + erro)

def craw_from_links():
    conn = sqlite3.connect("data/DBTimviec.db")
    a = int(input("Bắt đầu từ : "))
    b = int(input("Đến : "))
    data = conn.execute("select * from LINKS_JOB WHERE ID BETWEEN ? AND ?", (a, b))

    for row in data:
        get_data(conn, row[1])
if __name__ == '__main__':
    conn = sqlite3.connect("data/DBTimviec.db")
    try:
        #a = int(input("Bắt đầu từ : "))
        #b = int(input("Đến : "))
        data = conn.execute("select * from LINKS_JOB ")


        #get_data(conn,"https://timviecnhanh.com/tuyen-nhan-vien-chot-don-hang-qua-dien-thoai-quan-12-tp-hcm-100171796.html")

        for row in data:
            get_data(conn,row[1])
    except Exception as erro:
        print(erro)

