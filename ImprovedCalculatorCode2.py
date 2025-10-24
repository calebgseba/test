import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        """Add two numbers"""
        result = num1 + num2
        self.history.append(f"{num1} + {num2} = {result}")
        return result

    def subtract(self, num1, num2):
        """Subtract two numbers"""
        result = num1 - num2
        self.history.append(f"{num1} - {num2} = {result}")
        return result

    def multiply(self, num1, num2):
        """Multiply two numbers"""
        result = num1 * num2
        self.history.append(f"{num1} * {num2} = {result}")
        return result

    def divide(self, num1, num2):
        """Divide two numbers"""
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        result = num1 / num2
        self.history.append(f"{num1} / {num2} = {result}")
        return result


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.calculator = Calculator()
        self.create_widgets()

    def create_widgets(self):
        # Create entry fields for numbers and operation choices
        tk.Label(self.root, text="Number 1").grid(row=0)
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Number 2").grid(row=1)
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Operation").grid(row=2)
        self.operation_var = tk.StringVar()
        self.operation_var.set("add")
        tk.OptionMenu(self.root, self.operation_var, "add", "subtract", "multiply", "divide").grid(row=2, column=1)      

        # Create buttons for operations and quit
        tk.Button(self.root, text="Calculate", command=self.calculate).grid(row=3)
        tk.Button(self.root, text="Quit", command=self.quit_app).grid(row=4)

        # Create label to display result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=5)

        # Create button to view history
        tk.Button(self.root, text="View History", command=self.view_history).grid(row=6)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())

            if self.operation_var.get() == "add":
                result = self.calculator.add(num1, num2)
            elif self.operation_var.get() == "subtract":
                result = self.calculator.subtract(num1, num2)
            elif self.operation_var.get() == "multiply":
                result = self.calculator.multiply(num1, num2)
            elif self.operation_var.get() == "divide":
                try:
                    result = self.calculator.divide(num1, num2)
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
                    return

            self.result_label.config(text=f"Result: {result}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def view_history(self):
        history = self.calculator.get_history()
        history_window = tk.Toplevel(self.root)
        history_text = tk.Text(history_window, width=40, height=10)
        history_text.insert(tk.END, "\n".join(history))
        history_text.pack()

    def quit_app(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()