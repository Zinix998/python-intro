import unittest
import app


class TestAppFunctions(unittest.TestCase):
    
    def test_validate_email_correct(self):
        self.assertTrue(app.validate_email("test@example.com"))
        self.assertTrue(app.validate_email("user.name@domain.co.uk"))
    
    def test_validate_email_incorrect(self):
        self.assertFalse(app.validate_email("invalid.email"))
        self.assertFalse(app.validate_email("user@"))
        self.assertFalse(app.validate_email("@domain.com"))
        self.assertFalse(app.validate_email(""))
    
    def test_validate_email_edge_cases(self):
        self.assertFalse(app.validate_email(None))
        self.assertFalse(app.validate_email("user@domain"))
    
    def test_calculate_circle_area_positive(self):
        self.assertAlmostEqual(app.calculate_circle_area(5), 78.53975, places=4)
        self.assertAlmostEqual(app.calculate_circle_area(1), 3.14159, places=4)
    
    def test_calculate_circle_area_zero(self):
        self.assertEqual(app.calculate_circle_area(0), 0)
    
    def test_calculate_circle_area_negative(self):
        with self.assertRaises(ValueError):
            app.calculate_circle_area(-5)
    
    def test_filter_even_numbers_normal(self):
        self.assertEqual(app.filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(app.filter_even_numbers([2, 4, 6]), [2, 4, 6])
        self.assertEqual(app.filter_even_numbers([1, 3, 5]), [])
    
    def test_filter_even_numbers_empty(self):
        self.assertEqual(app.filter_even_numbers([]), [])
    
    def test_filter_even_numbers_invalid_input(self):
        with self.assertRaises(TypeError):
            app.filter_even_numbers("not a list")
    
    def test_convert_date_format_correct(self):
        self.assertEqual(app.convert_date_format("2024-01-15"), "15.01.2024")
        self.assertEqual(app.convert_date_format("1999-12-31"), "31.12.1999")
    
    def test_convert_date_format_incorrect(self):
        with self.assertRaises(ValueError):
            app.convert_date_format("2024/01/15")
        with self.assertRaises(ValueError):
            app.convert_date_format("2024-1-15")
        with self.assertRaises(ValueError):
            app.convert_date_format("")
    
    def test_convert_date_format_invalid_type(self):
        with self.assertRaises(ValueError):
            app.convert_date_format(20240115)
    
    def test_is_palindrome_true(self):
        self.assertTrue(app.is_palindrome("kajak"))
        self.assertTrue(app.is_palindrome("A to kanapa pana kota"))
        self.assertTrue(app.is_palindrome("Madam"))
        self.assertTrue(app.is_palindrome("12321"))
    
    def test_is_palindrome_false(self):
        self.assertFalse(app.is_palindrome("python"))
        self.assertFalse(app.is_palindrome("hello world"))
    
    def test_is_palindrome_edge_cases(self):
        self.assertTrue(app.is_palindrome("a"))
        self.assertTrue(app.is_palindrome(""))
        self.assertFalse(app.is_palindrome(12321))
        self.assertFalse(app.is_palindrome(None))


if __name__ == '__main__':
    unittest.main()