import streamlit as st
import random

st.title("数字猜谜游戏 🎮")
st.write("猜一个0到10之间的数字！")

if 'num' not in st.session_state:
    st.session_state.num = random.randint(0, 10)

guess = st.number_input("输入你的猜测：", min_value=0, max_value=10, step=1)

if st.button("检查猜测"):
    if guess > st.session_state.num:
        st.error("猜大了！📈")
    elif guess < st.session_state.num:
        st.error("猜小了！📉")
    else:
        st.success("恭喜！猜对了！🎉")
        st.balloons()
        if st.button("再玩一次"):
            st.session_state.num = random.randint(0, 10)
            st.rerun()
