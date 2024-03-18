# numpy를 이용한 배열 연산
import numpy as np

# 중간고사 성적 배열로 나열
mid_scores = np.array([10, 20, 30])
# 기말고사 성적 배열로 나열 
final_scores = np.array([60, 70, 80])

# 연산
total = mid_scores + final_scores
print('성적의 합계: ', total)
print('성적의 평균: ', total/2)