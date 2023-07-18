import pandas as pd
import numpy as np


data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}
df = pd.DataFrame(data)

# 단순피벗
#행(row)에는 도시, 열(column)에는 연도, 행과 열이 교차하는 칸에는 인구가 위치
df.pivot( index='도시', column='연도', values='인구')


data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천","서울"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010",'2005'],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203,1000],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권","수도권"]
}
df = pd.DataFrame(data)


data = {
    "도시": ["서울", "서울","수원", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010","2005", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, np.nan,9762100, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권","수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}

df = pd.DataFrame(data)


#고객 테이블
df_left = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']
})
#주문테이블
df_right = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]
})
