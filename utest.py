import sqlite3
import unittest

class db_exists_test(unittest.TestCase):
    def test1(self):
        self.assertTrue(True)

class db_unit_test(unittest.TestCase):
    def test2(self):
        try:
            db = sqlite3.connect("ApplianceBusiness.db")
            db_cursor = db.cursor()

            db_cursor.execute("DELETE FROM Address")
            db_cursor.execute("DELETE FROM Customer")
            db_cursor.execute("DELETE FROM Employee")
            db_cursor.execute("DELETE FROM Product")
            db_cursor.execute("DELETE FROM Stock")
            db_cursor.execute("DELETE FROM Supplier")
            db_cursor.execute("DELETE FROM Supplying")
            db_cursor.execute("DELETE FROM Event")
            db_cursor.execute("DELETE FROM Event_Ticket")
            db_cursor.execute("DELETE FROM Invoice")

            db_cursor.execute("INSERT INTO Address VALUES (1, '123 Main Street', 'San Jose', 'CA', 95192, 'test@sjsu.edu', 4085551234)")
            db_cursor.execute("SELECT * FROM Address")
            self.assertEqual((1, '123 Main Street', 'San Jose', 'CA', 95192, 'test@sjsu.edu', 4085551234),(db_cursor.fetchone()))

            db_cursor.execute("INSERT INTO Customer VALUES (1, 'Emily', 'Smith', 1)")
            db_cursor.execute("SELECT * FROM Customer")
            self.assertEqual((1, 'Emily', 'Smith', 1) ,(db_cursor.fetchone()))

            db_cursor.execute("INSERT INTO Employee VALUES (111, 'Jones', 'Anna', 'Cashier', 52000, 14)")
            db_cursor.execute("SELECT * FROM Employee")
            self.assertEqual((111, 'Jones', 'Anna', 'Cashier', 52000, 14) ,(db_cursor.fetchone()))

            db_cursor.execute("INSERT INTO Product VALUES (1, 'TV', 'Samsung', 2021, 1000, '')")
            db_cursor.execute("SELECT * FROM Product")
            self.assertEqual((1, 'TV', 'Samsung', 2021, 1000, '') ,(db_cursor.fetchone()))

            db_cursor.execute("INSERT INTO Stock VALUES (1, 1, 5, 1)")
            db_cursor.execute("SELECT * FROM Stock")
            self.assertEqual((1, 1, 5, 1) ,(db_cursor.fetchone()))

            db_cursor.execute("INSERT INTO Supplier VALUES (1, 'Friendly Supplier')")
            db_cursor.execute("SELECT * FROM Supplier")
            self.assertEqual((1, 'Friendly Supplier') ,(db_cursor.fetchone()))

            db_cursor.execute("INSERT INTO Supplying VALUES (1, 1, 1, '10')")
            db_cursor.execute("SELECT * FROM Supplying")
            self.assertEqual((1, 1, 1, '10') ,(db_cursor.fetchone()))

            db_cursor.execute("INSERT INTO Event VALUES (1, '2021 Holiday Event', '11/20/21', '01/05/22', 'Lottery for 80 Inch TV')")
            db_cursor.execute("SELECT * FROM Event")
            self.assertEqual((1, '2021 Holiday Event', '11/20/21', '01/05/22', 'Lottery for 80 Inch TV') ,(db_cursor.fetchone()))

            db_cursor.execute("INSERT INTO Event_Ticket VALUES (1, 1)")
            db_cursor.execute("SELECT * FROM Event_Ticket")
            self.assertEqual((1, 1) ,(db_cursor.fetchone()))

            db_cursor.execute("INSERT INTO Invoice VALUES (1, 1, 1, 1, 111, 1)")
            db_cursor.execute("SELECT * FROM Invoice")
            self.assertEqual((1, 1, 1, 1, 111, 1) ,(db_cursor.fetchone()))

            db_cursor.close()
            db.close()

        except Exception as e:
            print("Exception: ")
            print(e)

unittest.main()
