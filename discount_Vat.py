import streamlit as st
print("================================")
print("  โปรแกรมคำนวณส่วนลดสินค้า")
print("================================")

# รับข้อมูลจากผู้ใช้
price = float(input("กรอกราคาสินค้า (บาท): "))
discountPercent = float(input("กรอกส่วนลด (%): "))

# ตรวจสอบข้อมูล
if price <= 0 or discountPercent < 0 or discountPercent > 100:
    print("กรุณากรอกข้อมูลให้ถูกต้อง")

else:
    # คำนวณส่วนลด
    discount = price * discountPercent / 100

    # คำนวณราคาหลังหักส่วนลด
    afterDiscount = price - discount

    # คำนวณ VAT 7%
    vat = afterDiscount * 0.07

    # คำนวณราคาสุทธิ
    total = afterDiscount + vat

    # แสดงผลลัพธ์
    print("\n========== ผลการคำนวณ ==========")
    print("ราคาสินค้า:", format(price, ".2f"), "บาท")
    print("ส่วนลด:", format(discount, ".2f"), "บาท")
    print("ราคาหลังหักส่วนลด:", format(afterDiscount, ".2f"), "บาท")
    print("VAT 7%:", format(vat, ".2f"), "บาท")
    print("--------------------------------")
    print("ราคาสุทธิที่ต้องจ่าย:", format(total, ".2f"), "บาท")
    print("================================")
