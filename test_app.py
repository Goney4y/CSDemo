#!/usr/bin/env python3
"""
Tests for the Hello World web application.
"""

import unittest
from app import app


class TestHelloWorldApp(unittest.TestCase):
    """Test cases for the Hello World web application."""

    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world_route(self):
        """Test the main hello world route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World!')

    def test_health_check_route(self):
        """Test the health check route."""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        # Check that it returns JSON with expected structure
        json_data = response.get_json()
        self.assertIn('status', json_data)
        self.assertIn('message', json_data)
        self.assertEqual(json_data['status'], 'healthy')


if __name__ == '__main__':
    unittest.main()