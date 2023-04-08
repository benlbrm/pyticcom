import unittest
from unittest import mock

from pytictri import Teleinfo, GroupInfo


class TestTeleinfo(unittest.TestCase):

    def test_teleinfo(self):
        with open("./ressources/serial.dat", "r") as serial:
            def readline():
                line = serial.readline()
                return line.replace('\r', '').replace('\n', '')
            teleinfo = Teleinfo()
            teleinfo.open = mock.MagicMock()
            teleinfo.close = mock.MagicMock()
            teleinfo._readline = mock.MagicMock()
            teleinfo._readline.side_effect = readline

            frame = teleinfo.read_frame()

            self.assertIsNotNone(frame, "Frame empty")
            self.assertEqual(len(frame.groups), 11)

    def test_frame(self):
        with open("./ressources/serial.dat", "r") as serial:
            def readline():
                line = serial.readline()
                return line.replace('\r', '').replace('\n', '')

            teleinfo = Teleinfo()
            teleinfo.open = mock.MagicMock()
            teleinfo.close = mock.MagicMock()
            teleinfo._readline = mock.MagicMock()
            teleinfo._readline.side_effect = readline

            frame = teleinfo.read_frame()

            group = frame.get(GroupInfo.PAPP)

            self.assertIsNotNone(group, "Group not found")
            self.assertEqual(group.value, "03580")

    def test_checksum(self):
        teleinfo = Teleinfo()
        valid = teleinfo.validate_checksum("ADCO 041961860507", 'F')
        self.assertTrue(valid, "Unable to validate checksum")
