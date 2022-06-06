import unittest
from .tools import format_to_unix_path

class TestCase(unittest.TestCase):
    """Extend the built-in unittest module with specific tests.
    """
    def assertPathEqual(self, path1: str, path2: str):
        unix_path1 = format_to_unix_path(path1)
        unix_path2 = format_to_unix_path(path2)
        
        self.assertEqual(unix_path1, unix_path2)
