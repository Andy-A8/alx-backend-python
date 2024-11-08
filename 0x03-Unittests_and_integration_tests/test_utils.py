#!/usr/bin/env python3
"""
    Familiarize yourself with the utils.access_nested_map function and
    understand its purpose. Play with it in the Python console to
    make sure you understand

    In this task you will write the first unit test for
    utils.access_nested_map.

    Create a TestAccessNestedMap class that inherits from unittest.TestCase.

    Implement the TestAccessNestedMap.test_access_nested_map method to test
    that the method returns what it is supposed to.

    Decorate the method with @parameterized.expand to test the function
    for following inputs:

    nested_map={"a": 1}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a", "b")
    For each of these inputs, test with assertEqual that the function
    returns the expected result.

    The body of the test method should not be longer than 2 lines
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ class for testing access_nested_map function """
    @parameterized.expand(
            [
                ({"a": 1}, ("a",), 1),
                ({"a": {"b": 2}}, ("a",), {"b": 2}),
                ({"a": {"b": 2}}, ("a", "b"), 2)
            ]
    )
    def test_access_nested_map(self, nested_map, path, expected_output):
        """ Test that the method returns what it is supposed to """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand(
            [
                ({}, ("a",), KeyError),
                ({"a": 1}, ("a", "b"), KeyError)
            ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """ Test that the method returns the expected exception """
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ class for testing access_nested_map function """
    @parameterized.expand(
            [
               ('http://example.com', {"payload": True}),
               ('http://holberton.io', {"payload": True})
            ]
    )
    def test_get_json(self, url, expected_output):
        """ The method to test that function returns the expected result """
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)

            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """ class for testing acess_nested_map function """
    def test_memoize(self):
        """ Inside test_memoize, define TestClass class """
        class TestClass:

            def a_method(self):
                return 4

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
