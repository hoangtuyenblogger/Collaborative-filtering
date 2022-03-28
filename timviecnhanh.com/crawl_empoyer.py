from bs4 import BeautifulSoup
import requests
import sqlite3

def get_ung_vien(conn,url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")
        # lay ten ung vien
        ung_vien_element = soup.findAll('p', class_="fw-400 mb-0 fs-14")
        # lay ten cong viec ung tuyen
        job_name_element = soup.findAll('span', class_='job-name')
        # lat kinh nghiem
        kinh_nghiem_element = soup.findAll('span', class_="new-2021-item-candidate-exp")
        # lay dia diem lam viec
        locations = soup.findAll('span', class_="mr-15")
        query = """
        INSERT INTO EMPLOYER(NAME,JOB_NAME,LOCATION,EX) VALUES(?,?,?,?) 
        """
        for i in range(len(ung_vien_element)):
            conn.execute(query,(str(ung_vien_element[i].text).replace("Đang tìm việc","").strip(),
                                str(job_name_element[i].text).strip(),
                                str(locations[i].text).replace("Địa điểm:", "").strip(),
                                str(kinh_nghiem_element[i].text).replace("Kinh nghiệm:","").strip()))
            conn.commit()
            print("Đã thêm ", " . . .",str(ung_vien_element[i].text).replace("Đang tìm việc","").strip())

    except Exception as ex:
        print("Erro: ", ex)
        pass
def get_ung_vien_theo_phan_trang(link):
    conn = sqlite3.connect("data/DBTimviec.db")
    #link = "https://timviec.com.vn/tim-ung-vien-it-phan-mem-tai-ho-chi-minh?page="
    a = int(input("Bắt đầu craw từ phân trang thứ: "))
    b= int(input("Đến phân trang thứ: "))
    for i in range(a,b+1):
        url = link + str(i)
        print(url)
        get_ung_vien(conn,url)

if __name__ == '__main__':
    url = str(input("url = "))
    get_ung_vien_theo_phan_trang(url)

