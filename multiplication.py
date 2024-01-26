def multiplication_table(n):
    for i in range(1, 13):
        result = n * i
        print(f"{n} x {i} = {result}")

# รับค่าจำนวนเต็มจากผู้ใช้
while True:
    try:
        n = int(input("ป้อนตัวเลขจำนวนเต็ม n: "))
        break  # ถ้าป้อนเลขที่ถูกต้องจะออกจากลูป
    except ValueError:
        print("กรุณาป้อนเฉพาะจำนวนเต็มเท่านั้น!")

# แสดงตารางแม่สูตรคูณ
multiplication_table(n)
