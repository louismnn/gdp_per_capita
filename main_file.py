from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import pandas as pd


root = Tk()
root.title("Graph of GDP per capita in Europe")
root.geometry("1155x540")
root.configure(bg="white")


file = pd.read_csv("continents_sorted.csv", index_col=0)
data = pd.read_csv("world_gdp_capita.csv", index_col=0)
file.fillna("nan", inplace=True)
data.fillna(0, inplace=True)


fig = Figure()
ax = fig.add_subplot(111)

ax.set_ylim(0, 100000)
ax.set_ylabel("GDP in US dollars", fontweight="bold", fontsize=10)

ax.set_xlim(1960, 2023)
ax.set_xlabel("Years", fontweight="bold", fontsize=10)
ax.set_facecolor("white")

ax.figure.set_facecolor("whitesmoke")
ax.set_title("Graph of GDP per capita from 1960 to 2023", fontsize=14,
            fontweight="normal", color="black", ha="center")
ax.grid(True, linestyle="--", alpha=0.7, c="grey")


number_lines = 0

list_of_countrys = []
list_of_lines = []

country_font = ("Arial", 10)
color = ["red", "limegreen", "royalblue", "gold", "deeppink"]


def myclick(country):
    global list_of_countrys, number_lines

    if country in list_of_countrys:

        position = list_of_countrys.index(country)
        list_of_countrys.remove(country)
        number_lines -= 1

        if number_lines < 5:
            warning.grid_remove()

        try:
            ax.lines[position].remove()
            ax.autoscale(axis="y")
            canvas.draw()
        except:
            pass

    else:
        list_of_countrys.append(country)

        x_axis = [1960 + x for x in range(65)]
        y_axis = data.loc[country]

        if number_lines > 4:
            number_lines += 1
            warning.grid(column=1, row=42, columnspan=1)

        else:
            ax.plot(x_axis, y_axis, lw=1.5, c=color[number_lines],
                    linestyle="solid")
            ax.autoscale(axis="y")

            number_lines += 1
            canvas.draw()



n = 10
z = 3

frame = LabelFrame(root, padx= 10,
                pady=10, bg="grey97", relief=RIDGE)
frame.grid(column=0, row=0, padx=10, pady=10)

for j in file["Europe"]:

    if n < 27:
        if j != "nan":
            var = IntVar()
            check = Checkbutton(frame, text=j, justify="left",
                                font=country_font, bg="grey97",
                                selectcolor="white",
                                command=lambda j=j: myclick(j),
                                variable=var)
            
            check.grid(column=z, row=n, sticky="w")
            n += 1
    else:
        if j != "nan":
            var = IntVar()
            n = 10
            z += 1
            check = Checkbutton(frame, text=j, justify="left",
                                font=country_font, bg="grey97",
                                selectcolor="white",
                                command=lambda j=j: myclick(j),
                                variable=var)
            
            check.grid(column=z, row=n, sticky="w")
            n += 1



canvas = FigureCanvasTkAgg(fig, frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(column=0, columnspan=2, rowspan=35, row=7)


message1 = Label(frame, text="*If GDP equal to 0 = no datas",
                font=("Arial", 7), bg="grey97", justify="left", fg="#515151")
message1.grid(column=0, row=41, columnspan=2, sticky="w", padx=5)

message2 = Label(frame, text="**The maximum number of charts is 5",
                  font=("Arial", 7), bg="grey97", justify="left", fg="#515151")
message2.grid(column=0, row=42, columnspan=2, sticky="w", padx=5)

warning = Label(frame, text="***Too much charts on the graph (max 5 graphs)",
                bg="grey97", font=("Arial", 8), justify="left", fg="red")


root.mainloop()