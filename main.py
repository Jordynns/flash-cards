# ------------[Imports]------------ #
import tkinter, sv_ttk, configparser, time, random
from tkinter import ttk
import json

# ------------[Define Config/JSON File]------------ #
config = configparser.ConfigParser()
config.read("config/config.ini")
cfg = config.get("config", "test")
with open(f"config/{cfg}.json", "r") as file:
    data = json.load(file)
    
# ------------[Main Window]------------ #
root = tkinter.Tk()
root.title("Jordyn Flash Cards")
root.geometry("1280x720")
root.resizable(False,False)

# ------------[Fonts]------------ #
font_questions = ("Helvetica", 32)
font_regular = ("Helvetica", 22)
font_small = ("Helvetica", 9)

# ------------[Styles]------------ #
style = ttk.Style()
style.configure("TButton.font_regular.TButton", font=font_regular)
style.configure("TButton.font_small.TButton", font=font_small)

# ------------[Theme]------------ #
sv_ttk.set_theme("dark")

# ------------[Functions]------------ #
def main():
    global count, rand_id, answer
    count = 0
    rand_id = random.randint(1, 2)
    answer = (data[f"id{rand_id}a"])
    btn_coords = [(160,650),
                  (480,650),
                  (790,650),
                  (1115,650)]
    question = ttk.Label(root,font=font_questions)
    
    ttk.Button.destroy(start_btn)
    print("First Card!"),print(data[f"qid{rand_id}"])
    question.config(text=data[f"qid{rand_id}"]),
    question.place(x=1280/2,
                   y=200,
                   anchor=tkinter.CENTER)
    print(data[f"id{rand_id}a"])
    
    # Places Answer Buttons # 
    random.shuffle(btn_coords)
    bg_color = "grey"
    btn1 = ttk.Button(root,text=answer,command=lambda:[destroy_button(btn1,btn2,btn3,btn4,question),correct()],style="TButton.font_regular.TButton")
    btn1.place(x=btn_coords[0][0],
               y=btn_coords[0][1],
               anchor=tkinter.S,
               width=240,
               height=125)
    btn2 = ttk.Button(root,
                      text=(data[f"id{rand_id}wa1"]),
                      command=wrong,
                      style="TButton.font_regular.TButton")
    btn2.place(x=btn_coords[1][0],
               y=btn_coords[1][1],
               anchor=tkinter.S,
               width=240,
               height=125)
    btn3 = ttk.Button(root,
                      text=(data[f"id{rand_id}wa2"]),
                      command=wrong,
                      style="TButton.font_regular.TButton")
    btn3.place(x=btn_coords[2][0],
               y=btn_coords[2][1],
               anchor=tkinter.S,
               width=240,
               height=125)
    btn4 = ttk.Button(root,
                      text=(data[f"id{rand_id}wa3"]),
                      command=wrong,
                      style="TButton.font_regular.TButton")
    btn4.place(x=btn_coords[3][0],
               y=btn_coords[3][1],
               anchor=tkinter.S,
               width=240,
               height=125)
    
def correct():
    global count
    count += 1
    print(f"Correct! {count}")
    return

def wrong():
    print("Wrong!")
    return

# Destroy Buttons/Labeles # 
def destroy_button(btn1,btn2,btn3,btn4,question):
    ttk.Button.destroy(btn1),
    ttk.Button.destroy(btn2),
    ttk.Button.destroy(btn3),
    ttk.Button.destroy(btn4),
    ttk.Label.destroy(question) 
    return

def generate_wrong_right():
    
    return 
    
# ------------[Stuff]------------ #
cfg_loaded = ttk.Label(root,
                       text=(f"Config: {cfg} Loaded"),
                       font=font_small)

# ------------[Application Loop]------------ #
start_btn = ttk.Button(root,
                       text="Start",
                       command=main,
                       style="TButton.font_regular.TButton")
start_btn.place(x=1280/2,
                y=720/2,
                anchor=tkinter.CENTER,
                width=200,
                height=50)
if cfg == "aplus":
    print(f"Loaded: {cfg}")
    cfg_loaded.place(x=65,
                     y=15,
                     anchor=tkinter.CENTER)
root.mainloop()