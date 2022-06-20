import os
from unittest.mock import patch, MagicMock

from ....common import unit_test
from ....common.config import get_behavior_pack_functions_dir, get_data_pack_functions_dir


class MinecraftFunction():
    filepath = None
    function_name = None
    output = None
    function_directory = None
    def __init__(self, function_name: str, behavior_pack = None, data_pack = None) -> None:
        self.output = []
        self.function_name = function_name
        filename = '{}.mcfunction'.format(function_name)
        if data_pack is not None:
            self.function_directory = get_data_pack_functions_dir(data_pack.folder_name)
        elif behavior_pack is not None:
            self.function_directory = get_behavior_pack_functions_dir(behavior_pack.behavior_pack_folder_name)
        else:
            self.function_directory = get_behavior_pack_functions_dir()
        self.filepath = os.path.join(self.function_directory, filename)
    def save_output(self, output ) -> None:
        directory = os.path.dirname(self.filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(self.filepath, 'w') as f:
            f.write(output)
    def build(self) -> None:
        raise Exception('This method should be overwritten')
    def run(self, output):
        self.output.append(output)
    def run_all(self) -> None:
        self.build()
        self.save_output('\n'.join(self.output))

class MinecraftFunctionTest(unit_test.TestCase):
    def test_all(self):
        self.assertTrue(True)
    def test_init_without_behavior_pack(self):
        fn = MinecraftFunction('test_name')

        self.assertPathEqual(fn.filepath, 'minecraft_behavior_packs/first_behavior_pack/functions/test_name.mcfunction')
        self.assertEqual(fn.function_name, 'test_name')
        self.assertListEqual(fn.output, [])
        self.assertPathEqual(fn.function_directory, 'minecraft_behavior_packs/first_behavior_pack/functions')

    def test_init_with_behavior_pack(self):
        mock_behavior_pack = MagicMock()
        mock_behavior_pack.configure_mock(behavior_pack_folder_name='behavior_test_path')
        fn = MinecraftFunction('test_name', mock_behavior_pack)

        self.assertPathEqual(fn.filepath, 'minecraft_behavior_packs/behavior_test_path/functions/test_name.mcfunction')
        self.assertPathEqual(fn.function_directory, 'minecraft_behavior_packs/behavior_test_path/functions')

    def test_run(self):
        fn = MinecraftFunction('test_name')

        fn.run('test')

        self.assertListEqual(fn.output, ['test'])

    def test_build_throws_error(self):
        fn = MinecraftFunction('test_name')
        with self.assertRaises(Exception) as cm:
            fn.build()
        self.assertEqual(str(cm.exception), 'This method should be overwritten')

    def test_build_with_overide_creates_output(self):
        class TestFunction(MinecraftFunction):
            def build(self):
                self.run('test1')
        fn = TestFunction('test_name')

        fn.build()

        self.assertListEqual(fn.output, ['test1'])

    @patch('builtins.open')
    @patch('os.path.exists')
    @patch('os.makedirs')
    def test_save_output(self, mock_makedirs, mock_exists, mock_open):
        dir_path = 'minecraft_behavior_packs\\first_behavior_pack\\functions'
        fle_path = 'minecraft_behavior_packs\\first_behavior_pack\\functions\\test_name.mcfunction'
        output_text = 'test1'
        mock_exists.return_value = False

        fn = MinecraftFunction('test_name')
        fn.save_output(output_text)

        mock_exists.assert_called_once_with(dir_path)
        mock_makedirs.assert_called_once_with(dir_path)
        mock_open.assert_called_once_with(fle_path, 'w')

        file_handler = mock_open.return_value.__enter__()
        file_handler.write.assert_called_once_with(output_text)
