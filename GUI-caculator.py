import tkinter as tk

# สร้างคลาส Calculator
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("KentaZad Calculator")
        
        # สร้างตัวแสดงผล (display) เดียวที่ใช้แสดงทั้งโจทย์และคำตอบ
        self.display = tk.Text(root, font=('Arial', 20), bd=10, insertwidth=4, width=14, height=2, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # สร้างปุ่มเครื่องคิดเลข
        self.create_buttons()

        # ปรับขนาดของแถวและคอลัมน์ให้ยืดหยุ่นเท่ากัน
        for i in range(4):  # ปรับขนาดคอลัมน์ 4 คอลัมน์ให้เท่ากัน
            self.root.grid_columnconfigure(i, weight=1, uniform="equal")
        for i in range(6):  # ปรับขนาดแถว 6 แถวให้เท่ากัน
            self.root.grid_rowconfigure(i, weight=1, uniform="equal")

    def create_buttons(self):
        # สร้างปุ่มและวางบน grid layout
        button_texts = [
            '(', ')', '=', 'C',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'DEL', '+'
        ]
        
        row_val = 1  # ปรับเป็น row 1 เนื่องจาก row 0 ใช้สำหรับจอแสดงผล
        col_val = 0
        
        for text in button_texts:
            button = tk.Button(self.root, text=text, font=('Arial', 16), padx=5, pady=5)
            button.grid(row=row_val, column=col_val, sticky="nsew")  # ปรับขนาดให้ขยายเท่ากัน
            col_val += 1

            if col_val > 3:  # ปรับเป็น 3 เพราะเรามี 4 คอลัมน์
                col_val = 0
                row_val += 1

# สร้างหน้าต่างหลักของ tkinter
root = tk.Tk()

# สร้างวัตถุของคลาส Calculator
calc = Calculator(root)

# เริ่ม loop ของ tkinter
root.mainloop()
