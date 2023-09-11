import streamlit as st
import time

st.title('Stramlit 超入門')

st.write('プログレスバーの表示')
'Start'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)



img='HNI_0008.JPG'
img2='aa.jpg'

left_Column, right_Column = st.columns(2)

button=left_Column.button('右カラムに文字を表示')
if button:
    right_Column.image('HNI_0008.JPG')

ex=st.expander('高村の写真')

ex.image(img)
ex.image(img2)


# text=st.text_input("あなたの趣味を教えてください")
# condition=st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味は',text
# 'あなたの調子は?',condition

# option=st.selectbox(
#     'あなたが好きな数字を選択してください',
#     list(range(1,10))
# )

# 'あなたの好きな数字は',option,'です'

# if st.checkbox('Show Image'):
#     img=Image.open('HNI_0008.JPG')

#     st.image(img,caption='takamura', use_column_width=True)
