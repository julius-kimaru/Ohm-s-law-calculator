# Ohm's law calculator
voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter resistance (Ohms): "))

if resistance != 0:
    current = voltage / resistance
    print("Current (A):", current)
else:
    print("Error: Resistance cannot be zero")
    while True:
    try:
        print("--- Ohm's Law Calculator ---")
        v_input = input("Enter Voltage (or type 'exit' to quit): ")
        
        if v_input.lower() == 'exit':
            break
            
        V = float(v_input)
        R = float(input("Enter Resistance: "))

        if R == 0:
            print("Error: You cannot divide by zero resistance.")
        else:
            I = V / R
            P = V * I

            print("Current (I) is: " + str(I) + " Amps")
            print("Power (P) is: " + str(P) + " Watts")
        print("") 
        
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        print("")
