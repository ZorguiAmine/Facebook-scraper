import facebook_scraper
from facebook_scraper import get_posts as get_posts
import pandas as pd 


class ScrapData:


    #def __init__(self):
        #self._db = db
        #self.page = page
        
    #getting data from the facebook page
    def get_data(self,page):
        List = []
        for post in get_posts(page, pages=3):
            List.append(post)
        return List
    # Adding collected data to the database
    #def posts_to_db(self):
        #if self.get_data() is not None:
            #for i in len(List):
                
            #df = pd.DataFrame(self.get_data())
            #df.to_sql('FB_POSTS', con=self._db, if_exists='append')

        


    
