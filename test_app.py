import pytest
from unittest.mock import Mock


def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("test_app.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2

def get_fibonacci_number(n):
    if n <= 0:
        return "Nieprawidłowy indeks"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_prev = 0
        fib_current = 1
        for _ in range(3, n + 1):
            fib_prev, fib_current = fib_current, fib_prev + fib_current
        return fib_current

# Przykładowe użycie funkcji
print(get_fibonacci_number(10))  # Wyświetli 34


@pytest.mark.parametrize('n, result', (
   (0, 0),
   (1, 1),
   (2, 1),
   (3, 2),
   (10, 55),
   (15, 610)
))
def test_fibonacci(n, result):
   assert get_fibonacci_number(n) == result
