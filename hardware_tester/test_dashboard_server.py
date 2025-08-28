import unittest
from dashboard_server import app

class DashboardApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_status_endpoint(self):
        resp = self.client.get('/api/status')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.get_json(), dict)

    def test_voltage_endpoint(self):
        resp = self.client.get('/api/voltage')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.get_json(), dict)

    def test_logs_endpoint(self):
        resp = self.client.get('/api/logs')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue('logs' in data or 'error' in data)

if __name__ == '__main__':
    unittest.main()
