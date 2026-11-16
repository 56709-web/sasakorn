import streamlit as st
st.title(" แอป พลิ เคชั่น แปลง ปี พ.ศ . เป็น ค.ศ . ")
bh_year=st.number_input(" กรอก ปี พ.ศ . ที่ ต้องการ แปลง " ,value=2569)
ce_year=bh_year-543
st.header(f" ปี ค.ศ . คือ : {ce_year}")
