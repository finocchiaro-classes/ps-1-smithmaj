
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
    script_path = os.path.join(os.path.dirname(__file__), "../ps1-part1.py")
    # Simulate user input
    inputs = iter(["50", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    
    output = capture_script_output(script_path)
    

    # Check the output
    assert "You entered 50 and 2" in output
    assert "50 + 2 = 52" in output
    assert "50 * 2 = 100" in output
    assert "50 ** 2 = 2500" in output
    assert "50 % 2 = 0" in output

    # Simulate user input
    inputs = iter(["31", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    
    output = capture_script_output(script_path)


    # Check the output
    assert "You entered 31 and 3" in output
    assert "31 + 3 = 34" in output
    assert "31 * 3 = 93" in output
    assert "31 ** 3 = 29791" in output
    assert "31 % 3 = 1" in output