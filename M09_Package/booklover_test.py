import unittest
from booklover import BookLover


class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        book_lover.add_book("The Great Gatsby", 5)
        self.assertTrue(
            "The Great Gatsby" in book_lover.book_list['book_name'].values)

    def test_2_add_book(self):
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        book_lover.add_book("The Great Gatsby", 5)
        book_lover.add_book("The Great Gatsby", 5)
        self.assertEqual(
            book_lover.book_list[book_lover.book_list['book_name'] == "The Great Gatsby"].shape[0], 1)

    def test_3_has_read(self):
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        book_lover.add_book("The Great Gatsby", 5)
        self.assertTrue(book_lover.has_read("The Great Gatsby"))

    def test_4_has_read(self):
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        self.assertFalse(book_lover.has_read("The Catcher in the Rye"))

    def test_5_num_books_read(self):
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        book_lover.add_book("The Great Gatsby", 5)
        book_lover.add_book("1984", 4)
        self.assertEqual(book_lover.num_books_read(), 2)

    def test_6_fav_books(self):
        book_lover = BookLover("John Doe", "johndoe@example.com", "fiction")
        book_lover.add_book("The Great Gatsby", 5)
        book_lover.add_book("1984", 4)
        book_lover.add_book("Moby Dick", 2)
        favorite_books = book_lover.fav_books()
        self.assertTrue(
            all(rating > 3 for rating in favorite_books['book_rating']))


if __name__ == '__main__':
    unittest.main()
