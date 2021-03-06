import unittest


class TestRevereString(unittest.TestCase):

    # Check that the return string is in the correct reverse order.
    def test_is_equal(self):
        self.assertEqual(reverse_string('abcdefg6'), '6gfedcba')

    # Check that the returned string is not in the correct reverse order.
    def test_is_not_equal(self):
        self.assertIsNot(reverse_string('abcdefg'), 'abcdefg')

    # Check that the return string ignores upper and lower case..
    def test_upper_case(self):
        self.assertEqual(reverse_string('abcDeFg'), 'gfedcba')
    
    # Check that numbers in strings are correctly treated as strings within the function.
    def test_numbers_as_strings(self):
        self.assertEqual(reverse_string('123456'), '654321')

    # Check that we raise the correct error if an empty string is passed.
    def test_raise(self):
        with self.assertRaises(ValueError): reverse_string('')

def reverse_string(string_a): 
    
    # Raise an error for an empty string.
    if (string_a == ''):
        raise ValueError('String cannot be empty.')

    # Ensure we are only comparing lowercase characters
    str_lower = string_a.lower()
    # Convert the string into a list of characters so that we can use an index.
    x = list(str_lower)
    # Create an index variable for the first character item.
    start = 0
    # Create an index variable for the last character item.
    end = len(x) - 1
    
    # Swap items at the start and end positions until we meet in the middle, meaning all character items have been swapped.
    while start < end: 
        # Create a temporary variable to store the start value which will eventually replace the end value. 
        temp = x[start]
        # Replace the start value with the end value.
        x[start] = x[end] 
        # Replace the end value with the item value previously at the start.
        x[end] = temp 
        # Move forward one character position in the list.
        start += 1
        # Move backward one character position in the list.
        end -= 1

    # Convert the list back into a string, now in reversed order.
    result = ''
    for i in x:
        result += i

    print(result)
    return result

# Test method
if __name__ == '__main__':
    unittest.main()
        
