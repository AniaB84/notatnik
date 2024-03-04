from unittest.mock import Mock


def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("test_app.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2