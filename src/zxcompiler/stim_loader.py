from pathlib import Path
import stim


def load_stim_circuit(path: str | Path) -> stim.Circuit:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Stim file not found: {path}")
    return stim.Circuit(path.read_text())


def example_bell_circuit() -> stim.Circuit:
    return stim.Circuit("""
H 0
CX 0 1
M 0 1
""")