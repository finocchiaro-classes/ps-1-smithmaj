
import pytest
from io import StringIO
import sys
import os

# Helper function to capture printed output from script execution
def capture_script_output(script_path, simulated_input=""):
    captured_output = StringIO()
    sys.stdout = captured_output
    sys.stdin = StringIO(simulated_input)  # Ensure no input is required
    with open(script_path) as script_file:
        exec(script_file.read())
    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__
    return captured_output.getvalue().strip()



def test_script(monkeypatch):
    script_path = os.path.join(os.path.dirname(__file__), "../ps1-part4.py")
    inputs = iter([3, "Y", 23])


    # Correct monkeypatch to handle prompts and inputs properly
    def mock_input(prompt):
        value = next(inputs)  # Get the next value from the iterator
        print(f"{prompt}{value}")  # Print the prompt and the value
        return str(value)  # Return the value as a string

    monkeypatch.setattr("builtins.input", mock_input)

    output = capture_script_output(script_path)

    # Check the output
    assert "Prior arrests: 3" in output
    assert "Prior arrests for local ordinance (Y/N): Y" in output
    assert "Age at release: 23" in output
    assert "The recidivism risk score is 3" in output

    # # Simulate user input
    inputs = iter([1, "N", 41])
    
    monkeypatch.setattr("builtins.input", mock_input)

    output = capture_script_output(script_path)
    # Check the output
    assert "Prior arrests: 1" in output
    assert "Prior arrests for local ordinance (Y/N): N" in output
    assert "Age at release: 41" in output
    assert "The recidivism risk score is -1" in output