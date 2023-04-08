import unittest

from pytictri import GroupInfo, PAPP_DESCRIPTION, UNIT_VA


class TestGroupInfo(unittest.TestCase):

    def test_from_str(self):
        group_info = GroupInfo.from_str("PAPP")

        self.assertEqual(group_info, GroupInfo.PAPP)
        self.assertEqual(group_info.description, PAPP_DESCRIPTION)
        self.assertEqual(group_info.unit, UNIT_VA)
