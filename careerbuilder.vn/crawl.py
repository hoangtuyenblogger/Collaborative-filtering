from newspaper import Article
from bs4 import BeautifulSoup
import requests
import sqlite3


if __name__ == '__main__':
    url = "https://bettering-learning.000webhostapp.com/3.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


    title = []
    link = []
    salary = []

    a_ = soup.findAll('a', class_="job_link")
    for i in a_:
        title_ = " ".join(str(i.text).split())
        link_ = i.attrs['href']

        title.append(title_)
        link.append(link_)

    salary_ = soup.findAll('div', class_="salary")
    for i in salary_:
        salaryy = str(i.text).replace("Lương: ","").strip()
        salary.append(salaryy)

    conn = sqlite3.connect("data/DBTimviec.db")

    for i in range(len(title)):
        try:
            query = """
                INSERT INTO JOBS_DATA (
                                  TITLE,
                                  LINK,
                                  ADDRESS,
                                  SALARY,
                                  EXPERIENCE,
                                  LEVEL,
                                  LOCATION,
                                  JOB_NAME
                              )
                              VALUES (?,?,?,?,?,?,?,?)
                """

            conn.execute(query,
                         (title[i], link[i], "TP Hồ Chí Minh", salary[i], "Đang cập nhật", "Đang cập nhật", "TP Hồ Chí Minh", "Công nghệ thông tin"))  # thêm dữ liệu craw vào db
            conn.commit()
            print("Added ")
        except Exception as erro:
            print("Có lỗi: ", + erro)