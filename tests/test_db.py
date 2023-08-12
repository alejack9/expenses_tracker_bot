import unittest
import psycopg2
import os

class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.conn = psycopg2.connect(database=os.environ.get('POSTGRES_DB'),
                                host=os.environ.get('POSTGRES_HOST'),
                                user=os.environ.get('POSTGRES_USER'),
                                password=os.environ.get('POSTGRES_PASSWORD'))

    def test_expeneses_table_existence(self):
        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM expenses")

        res = cursor.fetchall()
        print(res)
        
        self.conn.close()
        
        self.assertTrue(self.conn.closed)

if __name__ == '__main__':
    unittest.main()
