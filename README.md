# Temperature Converter Application

## Overview
This application is a **Temperature Converter** built using Python and Tkinter. It allows users to convert temperature values between Celsius, Fahrenheit, and Kelvin with a responsive and user-friendly interface. The design features a lavender theme and dynamically updates the UI when the window is resized or maximized.

## Features
- **Real-time Conversion**: Automatically updates the result when the input or dropdown selection changes.
- **Dynamic Dropdowns**: The "To" dropdown excludes the currently selected value in the "From" dropdown.
- **Responsive Design**:
  - Adapts to window resizing and keeps all elements centered.
  - Adjusts font size dynamically for better readability.
- **Customizable Dropdown Options**: Larger font size for better visibility of dropdown options.
- **Lavender-Themed Interface**: Provides an aesthetically pleasing design.
- **Custom Window Title**: The application window is named "Temperature Converter."

## Requirements
- **Python 3.6+**
- **Tkinter** (usually included with Python)

## Installation
To ensure you have the required dependencies, run the following command to install Tkinter (if not already installed):
```bash
pip install tk
```

## How to Run the Application
1. Save the Python script provided in this repository as `temperature_converter.py`.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:
   ```bash
   python temperature_converter.py
   ```

## Usage
1. Enter the temperature value in the input field.
2. Select the unit from the "From" dropdown menu.
3. Select the desired unit in the "To" dropdown menu (the options will exclude the unit selected in the "From" dropdown).
4. The converted temperature will be displayed automatically below the dropdowns.
5. Resize or maximize the window to see the responsive layout in action.

## Code Highlights
1. **Dynamic Dropdown Logic**:
   - Automatically excludes the unit selected in the "From" dropdown from appearing in the "To" dropdown.
2. **Real-time Updates**:
   - Results are updated instantly without requiring a "Submit" button.
3. **Responsive Layout**:
   - Adjusts font size and element placement dynamically based on window size.
4. **Custom Styles**:
   - Lavender background theme.
   - Larger fonts for dropdown options using Tkinter style configuration.

## Notes
- If you encounter issues with scaling or font sizes, ensure that your Python and Tkinter versions are up-to-date.
- The application is designed to provide a smooth user experience and is optimized for both small and large screens.

## Future Enhancements
- Add support for additional temperature units (e.g., Rankine).
- Include an option for light/dark mode themes.
- Enhance error handling for invalid inputs.

## Author
Developed by Adithya S. 

