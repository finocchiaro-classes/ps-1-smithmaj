
import pytest
from io import StringIO
import sys
import os

# Helper function to capture printed output from script execution
def capture_script_output(script_path):
    captured_output = StringIO()
    sys.stdout = captured_output
    sys.stdin = StringIO()  # Ensure no input is required
    with open(script_path) as script_file:
        exec(script_file.read())
    sys.stdout = sys.__stdout__
    return captured_output.getvalue().strip()



def test_script(monkeypatch):
    script_path = os.path.join(os.path.dirname(__file__), "../ps1-part3.py")
    # Simulate user input
    inputs = iter([40, "E"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    
    output = capture_script_output(script_path)
    

    # Check the output
    assert "Your maximum heart rate is: 180" in output
    assert "Your target heart rate is between 108.0 and 144.0" in output


    # Simulate user input
    inputs = iter([40, "S"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    output = capture_script_output(script_path)

    # Check the output
    assert "Your maximum heart rate is: 180" in output
    assert "Your target heart rate is between 144.0 and 180" in output