import tkinter as tk
from tkinter import ttk, messagebox

# Conversion Functions
def convert_temperature():
    try:
        input_value = float(entry_temp.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        
        # Conversion logic
        if from_unit == to_unit:
            result = input_value
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                result = (input_value * 9/5) + 32
            elif to_unit == "Kelvin":
                result = input_value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (input_value - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (input_value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = input_value - 273.15
            elif to_unit == "Fahrenheit":
                result = (input_value - 273.15) * 9/5 + 32
        
        label_result.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")

# Input Field
label_temp = tk.Label(root, text="Enter Temperature:")
label_temp.pack(pady=10)
entry_temp = tk.Entry(root, width=10)
entry_temp.pack()

# From Dropdown
label_from = tk.Label(root, text="From:")
label_from.pack()
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_from.set("Celsius")  # Default value
combo_from.pack()

# To Dropdown
label_to = tk.Label(root, text="To:")
label_to.pack()
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_to.set("Fahrenheit")  # Default value
combo_to.pack()

# Convert Button
btn_convert = tk.Button(root, text="Convert", command=convert_temperature)
btn_convert.pack(pady=20)

# Result Label
label_result = tk.Label(root, text="Result: ", font=("Arial", 14))
label_result.pack(pady=10)

# Run the application
root.mainloop()
