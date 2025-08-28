import unittest
from dashboard_server import app

class DashboardApiTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client for Flask app."""
        self.client = app.test_client()

    def test_status_endpoint(self):
        """Test /api/status returns 200 and dict."""
        resp = self.client.get('/api/status')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.get_json(), dict)

    def test_voltage_endpoint(self):
        """Test /api/voltage returns 200 and dict."""
        resp = self.client.get('/api/voltage')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.get_json(), dict)

    def test_logs_endpoint(self):
        """Test /api/logs returns 200 and contains logs or error."""
        resp = self.client.get('/api/logs')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue('logs' in data or 'error' in data)

    def test_invalid_endpoint(self):
        """Test invalid endpoint returns 404."""
        resp = self.client.get('/api/invalid')
        self.assertEqual(resp.status_code, 404)

if __name__ == '__main__':
    unittest.main()
