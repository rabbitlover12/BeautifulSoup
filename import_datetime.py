import tkinter as tk
import datetime
from PIL import ImageTk, Image

# 윈도우 생성
root = tk.Tk()
root.title("시험까지 남은 시간")

# 윈도우 크기 설정
root.geometry("800x600")

# Canvas 위젯 생성
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack(fill="both", expand=True)

# 이미지 로드
img = Image.open("popo.jpg")
img = img.resize((2000, 2000))  # 이미지 크기 조절
photo = ImageTk.PhotoImage(img)

# 이미지 삽입
canvas.create_image(0, 0, anchor="nw", image=photo)

# 라벨 생성
label = tk.Label(root, font=("Helvetica", 30), fg="black", bg="white")

# 라벨 배치
label.pack(side="bottom", fill="both")

def update_label(exam_date):
    remaining_time = exam_date - datetime.datetime.now()  # 남은 시간 계산

    # 라벨 업데이트
    label.config(text=f"정보처리산업기사 시험까지 {remaining_time.days}일 {remaining_time.seconds // 3600}시간 {remaining_time.seconds // 60 % 60}분 {remaining_time.seconds % 60}초 남았습니다.")

    # 1초 후 다시 업데이트
    label.after(1000, update_label, exam_date)

def set_exam_date():
    try:
        year = int(year_input.get())  # year_input에서 입력받은 값을 정수형으로 변환하여 year 변수에 저장
    except ValueError:
        year = None

    month = int(month_input.get())  # month_input에서 입력받은 값을 정수형으로 변환하여 month 변수에 저장
    day = int(day_input.get())  # day_input에서 입력받은 값을 정수형으로 변환하여 day 변수에 저장
    hour = int(hour_input.get())  # hour_input에서 입력받은 값을 정수형으로 변환하여 hour 변수에 저장
    minute = int(minute_input.get())  # minute_input에서 입력받은 값을 정수형으로 변환하여 minute 변수에 저장
    second = int(second_input.get())  # second_input에서 입력받은 값을 정수형으로 변환하여 second 변수에 저장

    exam_date = datetime.datetime(year, month, day, hour, minute, second)  # 입력받은 year, month, day, hour, minute, second 값을 이용하여 datetime 객체 생성 후 exam_date 변수에 저장
    update_label(exam_date)  # exam_date 값을 인자로 update_label 함수 호출

def clear_input():
    year_input.delete(0, tk.END)
    month_input.delete(0, tk.END)
    day_input.delete(0, tk.END)
    hour_input.delete(0, tk.END)
    minute_input.delete(0, tk.END)
    second_input.delete(0, tk.END)

# 라벨 생성
year_label = tk.Label(root, text="년")
year_input = tk.Entry(root, width=4)
month_label = tk.Label(root, text="월")
month_input = tk.Entry(root, width=2)
day_label = tk.Label(root, text="일")
day_input = tk.Entry(root, width=2)
hour_label = tk.Label(root, text="시")
hour_input = tk.Entry(root, width=2)
minute_label = tk.Label(root, text="분")
minute_input = tk.Entry(root, width=2)
second_label = tk.Label(root, text="초")
second_input = tk.Entry(root, width=2)

# 라벨 배치
year_label.pack(side=tk.LEFT)
year_input.pack(side=tk.LEFT)
month_label.pack(side=tk.LEFT)
month_input.pack(side=tk.LEFT)
day_label.pack(side=tk.LEFT)
day_input.pack(side=tk.LEFT)
hour_label.pack(side=tk.LEFT)
hour_input.pack(side=tk.LEFT)
minute_label.pack(side=tk.LEFT)
minute_input.pack(side=tk.LEFT)
second_label.pack(side=tk.LEFT)
second_input.pack(side=tk.LEFT)


# 버튼 생성
button = tk.Button(root, text="입력", command=set_exam_date)

# 버튼 배치
button.pack()

# 윈도우 실행
root.mainloop()