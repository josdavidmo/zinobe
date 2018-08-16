import hashlib
import unittest

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from dbconfig import engine
from users.model import User


class UserTestCase(unittest.TestCase):
    """
    Represents an user test case.
    """
    def setUp(self):
        """
        Prepares test case.

        Create an user call 'david'.
        """
        password = hashlib.sha256('1t3st1t'.encode()).hexdigest()
        user = User(name='david', email='david@gmail.com',
                    country='CO', password=password)

        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        session.add(user)
        session.commit()

    def test_unique_email(self):
        """
        Verifies unique email.

        Tries to create user with email 'david@gmail.com'.
        """
        password = hashlib.sha256('1t3st1t'.encode()).hexdigest()
        user = User(name='jose', email='david@gmail.com',
                    country='CO', password=password)

        with self.assertRaises(IntegrityError):
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            session.add(user)
            session.commit()

    def test_unique_exist(self):
        """
        Verifies unique exits.

        Tries to verify the created register.
        """
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        password = hashlib.sha256('1t3st1t'.encode()).hexdigest()
        query = session.query(User).filter(
            User.email == 'david@gmail.com', User.password == password)
        self.assertEqual(query.count(), 1)

    def tearDown(self):
        """
        Destroy test case.

        Delete 'david' user test.
        """
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        password = hashlib.sha256('1t3st1t'.encode()).hexdigest()
        query = session.query(User).filter(
            User.email == 'david@gmail.com', User.password == password)
        user = query[0]

        session.delete(user)
        session.commit()
