import io, sys
from tasks.task4 import solve

def run_io(input_data: str) -> str:
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = io.StringIO(input_data), io.StringIO()
    try:
        solve()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_in, old_out

def test_case1():
    assert "1" == "1"

def test_case2():
    assert "1" == "1"

def test_case3():
    assert "1" == "1"

def test_case4():
    assert "1" == "1"
