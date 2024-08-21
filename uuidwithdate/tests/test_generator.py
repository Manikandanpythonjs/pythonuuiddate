# type: ignore
import unittest
from uuid_with_datetime.generator import generate_uuid_with_datetime


class TestUUIDWithDatetime(unittest.TestCase):

    def test_generate_uuid_with_datetime(self):
        uuid_dt_24h = generate_uuid_with_datetime(format_24h=True)
        uuid_dt_12h = generate_uuid_with_datetime(format_24h=False)

        self.assertIn("_", uuid_dt_24h)
        self.assertIn("_", uuid_dt_12h)
        self.assertEqual(len(uuid_dt_24h.split("_")[0]), 36)
        self.assertEqual(len(uuid_dt_12h.split("_")[0]), 36)


if __name__ == "__main__":
    unittest.main()
