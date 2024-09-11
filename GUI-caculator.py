import tkinter as tk

# สร้างคลาส Calculator
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("KentaZad Calculator")
        
        # สร้างตัวแสดงผล (display) เดียวที่ใช้แสดงทั้งโจทย์และคำตอบ
        self.display = tk.Text(root, font=('Arial', 20), bd=10, insertwidth=4, width=14, height=2, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew")

        # สร้างปุ่มเครื่องคิดเลข
        self.create_buttons()

        # ปรับขนาดของแถวและคอลัมน์ให้ยืดหยุ่น
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)

    def create_buttons(self):
        # สร้างปุ่มและวางบน grid layout
        button_texts = [
            '(',')' ,'=' ,'DEL'
            '7', '8', '9', '/' 
            '4', '5', '6', '*' 
            '1', '2', '3', '-' 
            '0', '.', 'C', '+'   
        ]
        
        row_val = 1  # ปรับเป็น row 1 เนื่องจาก row 0 ใช้สำหรับจอแสดงผล
        col_val = 0
        
        for text in button_texts:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 16))
            button.grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1

            if col_val > 4:
                col_val = 0
                row_val += 1

# สร้างหน้าต่างหลักของ tkinter
root = tk.Tk()

# สร้างวัตถุของคลาส Calculator
calc = Calculator(root)

# เริ่ม loop ของ tkinter
root.mainloop()
