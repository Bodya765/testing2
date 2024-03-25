import tkinter as tk
from tkinter import ttk

def submit_answer(question_num):
    selected_answer = selected_answers[question_num].get()
    correct_answer = questions[question_num]["correct_answer"]
    if selected_answer == correct_answer:
        result_labels[question_num].config(text="Правильно!", foreground="green")
        results[question_num] = {"question": questions[question_num]["question"], "user_answer": selected_answer, "result": "Правильно"}
    else:
        result_labels[question_num].config(text="Неправильно. Правильна відповідь: " + correct_answer, foreground="red")
        results[question_num] = {"question": questions[question_num]["question"], "user_answer": selected_answer, "result": "Неправильно"}
root = tk.Tk()
root.title("Вікно з питаннями")
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

questions = {
        1: {
            "question": "Яка столиця Франції?",
            "answers": ["Париж", "Лондон", "Рим"],
            "correct_answer": "Париж"
        },
        2: {
            "question": "Як називається найвища гора у світі?",
            "answers": ["Еверест", "Кіліманджаро", "Монт-Бланк"],
            "correct_answer": "Еверест"
        },
        3: {
            "question": "Яке число Пі - протягом багатьох років число цифр після коми?",
            "answers": ["3.14159", "3.1415926535", "Нескінченно"],
            "correct_answer": "3.1415926535"
        },
        4: {
            "question": "Яка країна виграла найбільше золотих медалей на Олімпійських іграх 2020 року?",
            "answers": ["Китай", "Велика Британія", "Сполучені Штати Америки"],
            "correct_answer": "Китай"
        },
        5: {
            "question": "Як називається головний елемент у програмуванні?",
            "answers": ["Функція", "Змінна", "Аргумент"],
            "correct_answer": "Функція"
        },
        6: {
            "question": "Скільки букв у латинському алфавіті?",
            "answers": ["23", "26", "30"],
            "correct_answer": "26"
        },
        7: {
            "question": "Яке море розташоване між Європою та Азією?",
            "answers": ["Адара", "Червоне море", "Середземне"],
            "correct_answer": "Середземне"
        },
        8: {
            "question": "Хто написав роман 'Майстер і Маргарита'?",
            "answers": ["Лев Толстой", "Михайло Булгаков", "Артур Конан Дойл"],
            "correct_answer": "Михайло Булгаков"
        },
        9: {
            "question": "Скільки планет в Сонячній системі?",
            "answers": ["7", "8", "9"],
            "correct_answer": "8"
        },
        10: {
            "question": "Яка найбільша пустеля в світі?",
            "answers": ["Атакама", "Сахара", "Каламінас"],
            "correct_answer": "Сахара"
        }
    }

selected_answers = {}
result_labels = {}
results = {}

for q_num, question_data in questions.items():
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=f"Питання {q_num}")
    question_label = ttk.Label(frame, text=question_data["question"], font=("Helvetica", 12, "bold"))
    question_label.pack()
    selected_answers[q_num] = tk.StringVar()
    for answer in question_data["answers"]:
        option = ttk.Radiobutton(frame, text=answer, variable=selected_answers[q_num], value=answer)
        option.pack()
    submit_button = ttk.Button(frame, text="Підтвердити",
                               command=lambda q=q_num: submit_answer(q))
    submit_button.pack()
    result_labels[q_num] = ttk.Label(frame, text="")
    result_labels[q_num].pack()
root.mainloop()
