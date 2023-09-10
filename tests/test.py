import unittest
from pagecraft import PageCraft


class TestPageCraft(unittest.TestCase):
    def setUp(self) -> None:
        list_pbjects = [1, 2, 3, 4, 5, 6 ]
        self.pagecraft = PageCraft(list_pbjects)
        self.page1 = self.pagecraft.page(1)
        self.page2 = self.pagecraft.page(2)
        self.page3 = self.pagecraft.page(3)

    def test_total_pages(self):
        self.assertEqual(self.pagecraft.total_pages, 2)

    def test_len_page_data(self):
        self.assertEqual(len(self.page1.data), 5)
        self.assertEqual(len(self.page2.data), 1)
        self.assertEqual(len(self.page3.data), 0)

    def test_page_number(self):
        self.assertEqual(self.page1.number, 1)
        self.assertEqual(self.page2.number, 2)
        self.assertEqual(self.page3.number, None)

    def test_has_next_page(self):
        self.assertTrue(self.page1.has_next_page)
        self.assertFalse(self.page2.has_next_page)

    def test_has_prev_page(self):
        self.assertFalse(self.page1.has_prev_page)
        self.assertTrue(self.page2.has_prev_page)

    def test_is_exist(self):
        self.assertTrue(self.page1.is_exist)
        self.assertTrue(self.page2.is_exist)
        self.assertFalse(self.page3.is_exist)

    def test_page_number(self):
        self.assertEqual(self.page1.next_page, 2)
        self.assertEqual(self.page1.prev_page, None)
        self.assertEqual(self.page2.next_page, None)
        self.assertEqual(self.page2.prev_page, 1)


if __name__ == "__main__":
    unittest.main()
