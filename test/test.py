import unittest

from src.fb_scraper import ScrapData
import sqlite3 as sl
from typing import Optional,List
from sqlmodel import Field, SQLModel, create_engine, Session, select


DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL, echo=True)  
SQLModel.metadata.create_all(engine)  


class TestWriteDataBRToOS(unittest.TestCase):
    def test_getData(self, page):
        fb_loader = ScrapData()
        data = fb_loader.get_data(page)
        self.assertNotEqual(data, None)


if __name__ == '__main__':
    unittest.main()