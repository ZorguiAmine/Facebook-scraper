from fastapi import FastAPI
from src.fb_scraper import ScrapData
from typing import Optional,List
from sqlmodel import Field, SQLModel, create_engine, Session, select
import os



app = FastAPI()
class Post(SQLModel, table=True):
    post_id: Optional[str] = Field(default=None, primary_key=True)
    page_name : Optional[str]
    text: Optional[str]
    post_text: Optional[str]
    shared_text: Optional[str]
    time: Optional[str]
    timestamp: Optional[str]
    image: Optional[str]
    image_lowquality: Optional[int]
    images: Optional[str]
    images_description: Optional[str]
    images_lowquality: Optional[str]
    images_lowquality_description: Optional[str]
    video: Optional[str]
    video_duration_seconds: Optional[str]
    video_height: Optional[str]
    video_id: Optional[str]
    video_quality: Optional[str]
    video_size_MB: Optional[str]
    video_thumbnail: Optional[str]
    video_watches: Optional[str]
    video_width: Optional[str]
    likes: Optional[str]
    comments: Optional[str]
    shares: Optional[str]
    post_url: Optional[str]
    link: Optional[str]
    links: Optional[str]
    user_id: Optional[str]
    username: Optional[str]
    user_url: Optional[str]
    is_live: Optional[str]
    factcheck: Optional[str]
    shared_post_id: Optional[str]
    shared_time: Optional[str]
    shared_user_id: Optional[str]
    shared_username: Optional[str]
    shared_post_url: Optional[str]
    available: Optional[str]
    comments_full: Optional[str]
    reactors: Optional[str]
    w3_fb_url: Optional[str]
    reaction_count: Optional[str]
    withh: Optional[str]
    image_id: Optional[str]
    image_ids: Optional[str]
    was_live: Optional[str]
    
DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL, echo=True)  
SQLModel.metadata.create_all(engine)  




@app.get("/insert_posts/{page}")
async def insert_posts(page):
    fb_loader = ScrapData()
    List = fb_loader.get_data(page)
    for i in range(0, len(List)):
        with Session(engine) as session:
            if List:
                session.add(Post(**List[i], page_name=page))
                session.commit()
            else:
                return {"message": f"ERROR to load data"}
    
    
    return({"message": f"Posts added to the database Successfully"})
    
@app.get("/get_posts/{page}") #, response_model=List[Post]
async def get_posts(page):
    with Session(engine) as session:
        posts = session.exec(select(Post).where(Post.page_name == page)).all()
    #return posts
    L = []
    for post in posts:
            L.append(post)
    return L


