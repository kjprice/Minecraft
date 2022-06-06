import unittest

def format_to_unix_path(path: str):
    return path.replace('\\', '/')

class CommonToolsTest(unittest.TestCase):
    def test_format_to_unix_path_empty(self):
        self.assertEqual(format_to_unix_path(''), '')
    def test_format_to_unix_path_from_windows(self):
        windows_path = 'b\c\d'
        unix_path = 'b/c/d'
        self.assertEqual(format_to_unix_path(windows_path), unix_path)
    def test_format_to_unix_path_from_unix(self):
        windows_path = 'b/c/d'
        unix_path = 'b/c/d'
        self.assertEqual(format_to_unix_path(windows_path), unix_path)
