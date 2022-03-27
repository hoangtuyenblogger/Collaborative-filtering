import os
import pickle
MODEL_PATH = "D://Dai Hoc Thu Dau Mot//NCKH//he tu van viec lam//hetuvan_vieclam//web//collaborative_filtering_tuvanvieclam"
                # patch chứa model + ma trận

X = pickle.load(open(os.path.join(MODEL_PATH, "scores_matrix.pkl"), 'rb'))
correlation_matrix = pickle.load(open(os.path.join(MODEL_PATH, "collaborative_filtering_tuvanvieclam.pkl"), 'rb'))

def get_recommend_job(id_job, n_recommend= 4): # mặc định số công việc recomend = 4
  list_jobs_id = list(X.index) # lấy list jobs_id, X là ma trận chuyển vị

  id = list_jobs_id.index(id_job) # tìm ID trong list
  correlation_by_ID = correlation_matrix[id] # lấy ma trận tương quan của job có id_jobs ra

  # Đề xuất n jobs_id có mức độ tương quan cao theo thứ tự
  recommend = list(X.index[correlation_by_ID > 0.6])
  return recommend[:n_recommend]

if __name__ == '__main__':
    # test
    print(get_recommend_job(5,5))
    #print(type(get_recommend_job(5,5)))