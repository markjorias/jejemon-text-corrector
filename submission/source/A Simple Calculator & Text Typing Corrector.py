class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2 
        self.history.append(f'Added {num1} and {num2} = {result}')
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.history.append(f'Subtracted {num2} from {num1} = {result}')
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f'Multiplied {num1} and {num2} = {result}')
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            self.history.append('Error: Division by zero is not allowed.')
            return print("Error: Division by zero is not allowed.")
        result = num1 / num2
        self.history.append(f'Divided {num1} by {num2} = {result}')
        return result

    def save_history(self, filename):
        with open(filename, 'w') as f:
            for line in self.history:
                f.write(f'{line}\n')

    def load_history(self, filename):
        try:
            with open(filename, 'r') as f:
                self.history = f.readlines()
        except FileNotFoundError:
            print("History not found.")
            menu()

def menu():
    calc = Calculator()
    while True:
        print("\nCalculator Menu:")
        print("0. Exit")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Save Calculator History")
        print("6. Load Calculator History")
        print("\nMore Tools:")
        print ("7. Jejemon Typings Corrector")
        print ("\n")
        choice = input("Enter your choice: ")
        if choice == '1': 
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = calc.add(num1, num2)
                if result is not None:
                    print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = calc.subtract(num1, num2)
                if result is not None:
                    print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = calc.multiply(num1, num2)
                if result is not None:
                    print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = calc.divide(num1, num2)
                if result is not None:
                    print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            filename = input("Enter filename to save history: ")
            calc.save_history(filename)
            print("History saved successfully.")
        elif choice == '6':
            filename = input("Enter filename to load history: ")
            calc.load_history(filename)
            print("History loaded successfully.")
            for line in calc.history:
                print(line.strip())
        elif choice == '7':
            file_path = input("Enter the file path: ")
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
            except FileNotFoundError:
                print("File not found.")
                menu()
            content = content.replace("0", "o")
            content = content.replace("1", "i")
            content = content.replace("3", "e")
            content = content.replace("4", "a")
            content = content.replace("5", "s")
            content = content.replace("7", "t") 
            new_file_path = file_path.replace(".txt", "_corrected.txt")
            with open(new_file_path, 'w') as file:
                file.write(content)
            print("File corrected and saved as:", new_file_path)
        elif choice == '0':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")
            break

if __name__ == "__main__":
    menu()