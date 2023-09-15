import streamlit as st
import csv as csv

st.title("健太郎＆華奈結婚式二次会")
st.image("kp.jpg")

ex=st.expander("開催場所")

ex.write("男爵")
ex.image("dansyaku.jpg")
ex.write("住所：〒403-0005山梨県富士吉田市上吉田5539")

ex2=st.expander("システム")

ex2.write("19時開始予定")
ex2.write("コース料理＆飲み放題🍺")
ex2.write("""
        料金\n
        女性＆後輩：4000円\n
        男性：4500円\n
""")

ex3=st.expander("参加回答")
name=ex3.text_input("名前")
sanka=ex3.radio("出欠",["出席","欠席"])
ex3.write("当日はハイランドから会場までバスが出ます。お手数ですがバスに登場するか否かの回答もお願いします")
bass=ex3.radio("バス",["乗る","乗らない"])

if ex3.button("回答送信"):
    ex3.write("回答送信中...")
    with open('二次会.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([name, sanka, bass])   
    ex3.write("回答を送信しました！")
