# Sorting Algorithms Visualization

## Overview
This project showcases the implementation of five popular sorting algorithms in Python and visualizes their behavior step-by-step using `matplotlib`. The aim is to provide an educational tool for understanding how these sorting techniques operate.

## Algorithms Implemented
- **Selection Sort**
- **Heap Sort**
- **Bubble Sort**
- **Quick Sort**
- **Insertion Sort**

## Features
- Visualizes sorting in real-time with animated bar charts.
- Each algorithm yields intermediate steps to show how the array changes throughout the process.
- A plotting function handles the visualization of each algorithm's progress.

## Dependencies
Ensure you have the following Python packages installed:
- `matplotlib`
- `numpy`

You can install them via pip:
```bash
pip install matplotlib numpy
```

## How to Run
1. Clone this repository:
```bash
git clone <repository-url>
```
2. Navigate to the project directory:
```bash
cd sorting-algorithms-visualization
```
3. Run the Python file:
```bash
python Sorting\ Algorithms.py
```

## Usage
The script initializes an array of 70 random integers and visualizes each sorting algorithm's process in separate windows. The bar heights represent the array elements, and their changes during sorting are shown in real-time.

## Preview
The program visualizes sorting like this:
![Example visualization](example.png) *(Replace with an actual screenshot if available)*

## Customization
- Modify the `arr` initialization to change the input size or value range.
```python
arr = np.random.randint(1, 100, 100)  # Change size or range as needed
```

Feel free to explore and modify the code to learn more about sorting algorithms and their visual representation!
