from zxcompiler.stim_loader import example_bell_circuit

circuit = example_bell_circuit()

print("First Stim circuit:")
print(circuit)
print("Number of instructions:", len(circuit))