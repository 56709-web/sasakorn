
import streamlit as st

st.title("โปรแกรมคำนวณส่วนลดสินค้าและ VAT")
st.write("คำนวณราคาสินค้าหลังหักส่วนลด พร้อมภาษี VAT 7%")

st.divider()

# รับข้อมูลสินค้า
price = st.number_input(
    "ราคาสินค้า (บาท)",
    min_value=0.0,
    value=1000.0
)

discountPercent = st.number_input(
    "เปอร์เซ็นต์ส่วนลด (%)",
    min_value=0.0,
    max_value=100.0,
    value=20.0
)

# ปุ่มคำนวณ
if st.button("คำนวณราคา"):

    # คำนวณส่วนลด
    discount = price * discountPercent / 100

    # ราคาหลังหักส่วนลด
    afterDiscount = price - discount

    # คำนวณ VAT 7%
    vat = afterDiscount * 0.07

    # ราคาสุทธิ
    total = afterDiscount + vat

    st.divider()
    st.subheader("ผลการคำนวณ")

    st.write(f"ราคาสินค้า: {price:,.2f} บาท")
    st.write(f"ส่วนลด: {discount:,.2f} บาท")
    st.write(f"ราคาหลังหักส่วนลด: {afterDiscount:,.2f} บาท")
    st.write(f"VAT 7%: {vat:,.2f} บาท")

    st.success(f"ราคาสุทธิที่ต้องจ่าย: {total:,.2f} บาท")
