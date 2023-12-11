from sqlalchemy import create_engine, Column, Integer, String,VARCHAR,Date,ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

Base=declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id= Column(Integer, primary_key=True)
    first_name= Column(String())
    last_name=Column(String())
    profile_name=Column(VARCHAR)
    email=Column(VARCHAR)
    password=Column(VARCHAR)
    date_joined=Column(Date)
    post=relationship('Post',backref='user_post')
    like=relationship('Like',backref='user_like')
    groups = relationship('Group', secondary='users_groups', back_populates='users')
 
   
class Post(Base):
    __tablename__='posts'
    post_id=Column(Integer(),primary_key=True)
    user_id=Column(Integer(),ForeignKey('users.user_id'))
    post_content=Column(VARCHAR)
    likes_total=Column(Integer())
    date_created=Column(Date)
    comment=relationship('Comment',backref='post_comment')
    likes=relationship('Like', backref='like_post')



class Like(Base):
    __tablename__='likes'
    like_id=Column(Integer(),primary_key=True)
    user_id=Column(Integer(),ForeignKey('users.user_id'))
    post_id=Column(Integer(),ForeignKey('posts.post_id'))

class Group(Base):
    __tablename__='groups'
    group_id=Column(Integer(),primary_key=True)
    group_name=Column(VARCHAR)
    date_created=Column(Date())
    users = relationship('User', secondary='users_groups', back_populates='groups')

class Comment(Base):
    __tablename__='comments'
    comment_id=Column(Integer(),primary_key=True)
    user_id=Column(Integer(),ForeignKey('users.user_id'))
    post_id=Column(Integer(),ForeignKey('posts.post_id'))
    content=Column(VARCHAR)
    date_created=Column(Date())

user_group= Table(
    'users_groups',
    Base.metadata,
    Column('user_id', ForeignKey('users.user_id'), primary_key=True),
    Column('group_id', ForeignKey('groups.group_id'), primary_key=True),
    extend_existing=True,
)



engine=create_engine('sqlite:///social_app.db')
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()


