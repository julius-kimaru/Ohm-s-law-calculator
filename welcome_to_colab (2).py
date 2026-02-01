
while True:
    try:
        voltage_input = input("Enter voltage (V) or 'exit' to quit: ")
        if voltage_input.lower() == 'exit':
            break
        voltage = float(voltage_input)

        resistance_input = input("Enter resistance (ohms) or 'exit' to quit: ")
        if resistance_input.lower() == 'exit':
            break
        resistance = float(resistance_input)

        if resistance == 0:
            print("Error: Resistance cannot be zero for current calculation.")
        else:
            current = voltage / resistance
            print(f"Current (A): {current:.2f}")

            # Calculate and display power
            power = voltage * current
            print(f"Power (W): {power:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for voltage and resistance.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("----------------------------------")

"""LAB 1 OHM'S LAW CALCULATOR"""
