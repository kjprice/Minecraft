import unittest

from .MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunctionTest
from .common.tools import CommonToolsTest
from .common.images import CommonImageToolsTest

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(MinecraftFunctionTest))
suite.addTest(unittest.makeSuite(CommonToolsTest))
suite.addTest(unittest.makeSuite(CommonImageToolsTest))


runner = unittest.TextTestRunner()
runner.run(suite)
