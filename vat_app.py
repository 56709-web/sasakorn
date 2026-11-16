import streamlit as st
st.title("แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")

price = st.number_input("ป้อนราคาสินค้า (บาท)", min_value=0.0, step=100.0)

vat_rate = 0.07
vat = price * vat_rate
total_price = price + vat

st.write(f"ภาษีมูลค่าเพิ่ม 7%: {vat:,.2f} บาท")
st.write(f"ราคารวมสุทธิ: {total_price:,.2f} บาท")
