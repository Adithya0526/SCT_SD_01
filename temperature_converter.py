import tkinter as tk
from tkinter import ttk

# Conversion Functions
def convert_temperature(*args):
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
        label_result.config(text="Enter a valid number!")

# Update Dropdown Options
def update_dropdowns(*args):
    from_unit = combo_from.get()
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    available_to_units = [unit for unit in units if unit != from_unit]
    combo_to["values"] = available_to_units
    if combo_to.get() == from_unit:  # Reset if the selected value matches the excluded one
        combo_to.set(available_to_units[0])
    convert_temperature()  # Trigger conversion after dropdown change

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x350")
root.configure(bg="#E6E6FA")  # Lavender background

# Input Field
label_temp = tk.Label(root, text="Enter Temperature:", bg="#E6E6FA", font=("Arial", 12))
label_temp.pack(pady=10)
entry_temp = tk.Entry(root, width=10, font=("Arial", 14))
entry_temp.pack()
entry_temp.bind("<KeyRelease>", convert_temperature)  # Trigger conversion on input change

# From Dropdown
label_from = tk.Label(root, text="From:", bg="#E6E6FA", font=("Arial", 12))
label_from.pack(pady=5)
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 12))
combo_from.set("Celsius")  # Default value
combo_from.pack()
combo_from.bind("<<ComboboxSelected>>", update_dropdowns)  # Trigger dropdown update

# To Dropdown
label_to = tk.Label(root, text="To:", bg="#E6E6FA", font=("Arial", 12))
label_to.pack(pady=5)
combo_to = ttk.Combobox(root, values=["Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 12))
combo_to.set("Fahrenheit")  # Default value
combo_to.pack()
combo_to.bind("<<ComboboxSelected>>", convert_temperature)  # Trigger conversion on selection change

# Result Label
label_result = tk.Label(root, text="Result: ", bg="#E6E6FA", font=("Arial", 16))
label_result.pack(pady=20)

# Run the application
root.mainloop()
