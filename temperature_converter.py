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

# Update layout dynamically
def update_layout(event):
    # Get the window dimensions
    width = root.winfo_width()
    height = root.winfo_height()
    
    # Scale font sizes and widget dimensions dynamically
    font_size = max(10, int(min(width, height) / 30))  # Dynamic font size
    label_temp.config(font=("Arial", font_size))
    label_from.config(font=("Arial", font_size))
    label_to.config(font=("Arial", font_size))
    label_result.config(font=("Arial", font_size + 2))  # Slightly larger font for result
    entry_temp.config(font=("Arial", font_size))
    combo_from.config(font=("Arial", font_size))
    combo_to.config(font=("Arial", font_size))
    
    # Adjust padding and widget sizes dynamically
    container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")  # Custom window title
root.geometry("400x350")
root.configure(bg="#E6E6FA")  # Lavender background
root.bind("<Configure>", update_layout)  # Bind resize event

# Create a style for the dropdowns
style = ttk.Style()
style.theme_use("default")  # Use the default theme
style.configure("TCombobox", font=("Arial", 12))  # Font for combobox entry
style.map("TCombobox", fieldbackground=[("readonly", "white")])

# Customize the dropdown options font size
root.option_add('*TCombobox*Listbox.font', ("Arial", 14))  # Dropdown options font

# Create a container for centering the layout
container = tk.Frame(root, bg="#E6E6FA")
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Input Field
label_temp = tk.Label(container, text="Enter Temperature:", bg="#E6E6FA", font=("Arial", 12))
label_temp.pack(pady=10)
entry_temp = tk.Entry(container, width=10, font=("Arial", 14))
entry_temp.pack()
entry_temp.bind("<KeyRelease>", convert_temperature)  # Trigger conversion on input change

# From Dropdown
label_from = tk.Label(container, text="From:", bg="#E6E6FA", font=("Arial", 12))
label_from.pack(pady=5)
combo_from = ttk.Combobox(container, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 12))
combo_from.set("Celsius")  # Default value
combo_from.pack()
combo_from.bind("<<ComboboxSelected>>", update_dropdowns)  # Trigger dropdown update

# To Dropdown
label_to = tk.Label(container, text="To:", bg="#E6E6FA", font=("Arial", 12))
label_to.pack(pady=5)
combo_to = ttk.Combobox(container, values=["Fahrenheit", "Kelvin"], state="readonly", font=("Arial", 12))
combo_to.set("Fahrenheit")  # Default value
combo_to.pack()
combo_to.bind("<<ComboboxSelected>>", convert_temperature)  # Trigger conversion on selection change

# Result Label
label_result = tk.Label(container, text="Result: ", bg="#E6E6FA", font=("Arial", 16))
label_result.pack(pady=20)

# Run the application
root.mainloop()
