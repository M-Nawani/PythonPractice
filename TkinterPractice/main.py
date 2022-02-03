import tkinter

window = tkinter.Tk()
window.title("Miles to Km Converter")
# window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


input_miles = tkinter.Entry(width=10)
input_miles.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)


def convert_miles_to_km():
    miles = float(input_miles.get())
    kms = round(miles * 1.609, 2)
    km_value_label.config(text=kms)
    km_value_label.grid(row=1, column=1)


km_label = tkinter.Label(text="Kms")
km_label.grid(row=1, column=2)

km_value_label = tkinter.Label(text=0)
km_value_label.grid(row=1, column=1)

calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()