import streamlit as st
#스트림릿에서 제목을 사용할 때
#st.title("내 스트림릿 페이지에 온 것을 환영한다.")
#스트림릿에서 헤더를 사용할 때
#st.header("이것은 헤더이다.")
#스트림릿에서 서브헤더를 사용할 때
#st.subheader("이것은 서브헤더이다.")

#스트림릿에서 텍스트를 사용할 때 ==========================
# text -> 비교적 제한된 글쓰기. 단순한 문자, 포맷팅 없음, 일반 텍스트 형식 출력 가능
# write -> 다양한 데이터 유형 표현 가능, 마크다운, html, LaTeX, Json,  입력 데이터 유형에 따라
# 자동으로 형식을 지정, 포맷팅 f{}
#1. text
#2. write

"""html_page = 
<div style="background-color:blue;padding:50px">
	<p style="color:yellow;font-size:5'px">Enjoy Streamlit!</p>
</div>
"""
# 팝업 --> 시스템 메시지 띄우기

# 성공, 정보전달, 경고, 에러
st.success("성공!")
st.info("추가 정보는 여기에 있습니다.")
st.warning("뭔가 잘못되었음")
st.error("에러 발생하여 잘못되었음")

from PIL import Image
#Image.open("이미지 파일 경로")
# ./ = 현재 디렉토리
image = Image.open("/Users/son/Downloads/F107888F-A75F-4E50-8DA8-7C3D6D5D53FA.png")
st.image(image, width=300, caption="VGG19")


# 비디오 삽입

# 1. 가지고 있는 비디오 재생하기
# video_file = open("dir", "rb").read()
# st.video(video_file)

# 스트리밍 된 비디오 파일 재생
st.video("https://www.youtube.com/watch?v=D8VEhcPeSlc")

# 오디오 삽입
# audio_file = open("", "rb").read()
# st.audio(audio_file)

# 상호작용
if st.button("Happy Birthday!"):
    st.balloons()

# 체크박스
if st.checkbox("check"):
    st.write("Checked in")

# 라디오 버튼
radio_button = st.radio("What is your favorite color?", ["red", "yellow", "blue"])
if radio_button == "red":
    st.write("recommand red flower")
if radio_button == "yellow":
    st.write("recommand yellow flower")
if radio_button == "blue":
    st.write("recommand blue flower")

# 셀렉트 박스
city = st.selectbox("당신이 사는 도시는?", ["서울", "대전", "대구", "부산", "천안", "부천"])
job = st.multiselect("당신이 원하는 직업은?", ["개발자", "디자이너", "데이터분석가", "연주가"])

# 텍스트 인풋
name = st.text_input("당신의 이름은?", "input your name")
if st.button("제출"):
    result = name.title()
    st.success(result)

# 텍스트 에어리어
# 여러 줄의 텍스트 입력 받기 가능
# 플레이스 홀더 설정, 줄 수 지정 등이 가능
message = st.text_area("메시지를 입력하세요", "메시지를 입력하세요")
if st.button("제출하기"):
    result = message.title()
    st.success(result)

# 슬라이더
st.slider("당신의 나이는?", 1, 80, 1)

import datetime
import time
st.header("Date & Time")
today = st.date_input("오늘은 언제인가요?", datetime.datetime.now())
hours = st.time_input("지금 몇 시인가요?", datetime.time())

import pandas as pd

st.header("판다스 데이터프레임")
df = pd.read_csv("/Users/son/Downloads/auto.csv")
st.dataframe(df)

# 플롯 그리기
st.area_chart(df["mpg"])
st.bar_chart(df["mpg"])
st.line_chart(df["mpg"])

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
sns.heatmap(df[['mpg', 'cylinders']].corr(), annot=True, ax=ax)
st.pyplot(fig)

import time
my_bar = st.progress(0)
for v in range(100):
    my_bar.progress(v+1)
    time.sleep(0.1)

with st.spinner("잠시만 기다려 주세요"):
    time.sleep(5)
st.success("완료됐습니다")