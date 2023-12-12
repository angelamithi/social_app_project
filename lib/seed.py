from models import User,Post,Like,Group,Comment,session,user_group,user_comment
from datetime import datetime

session.query(User).delete()
session.query(Post).delete()
session.query(Comment).delete()
session.query(Group).delete()
session.query(Like).delete()
session.query(user_group).delete()
session.query(user_comment).delete()

session.commit()

user_info = [
    {
        "user_id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "profile_name": "john_doe",
        "email": "john.doe@email.com",
        "password": "password123",
        "date_joined": datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
    },
    {
        "user_id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "profile_name": "jane_smith",
        "email": "jane.smith@email.com",
        "password": "pass456",
        "date_joined": datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
    },
    {
        "user_id": 3,
        "first_name": "Bob",
        "last_name": "Johnson",
        "profile_name": "bob_j",
        "email": "bob.johnson@email.com",
        "password": "securepass",
        "date_joined": datetime.strptime("2023-01-03", "%Y-%m-%d").date(),
    },
    {
        "user_id": 4,
        "first_name": "Alice",
        "last_name": "Williams",
        "profile_name": "alice_w",
        "email": "alice@email.com",
        "password": "password123",
        "date_joined": datetime.strptime("2023-01-04", "%Y-%m-%d").date(),
    },
    {
        "user_id": 5,
        "first_name": "David",
        "last_name": "Miller",
        "profile_name": "david_m",
        "email": "david.miller@email.com",
        "password": "pass789",
        "date_joined": datetime.strptime("2023-01-05", "%Y-%m-%d").date(),
    },
    {
        "user_id": 6,
        "first_name": "Eva",
        "last_name": "Jones",
        "profile_name": "eva_j",
        "email": "eva.jones@email.com",
        "password": "evapass",
        "date_joined": datetime.strptime("2023-01-06", "%Y-%m-%d").date(),
    },
    {
        "user_id": 7,
        "first_name": "Chris",
        "last_name": "Brown",
        "profile_name": "chris_b",
        "email": "chris.brown@email.com",
        "password": "chrispass",
        "date_joined": datetime.strptime("2023-01-07", "%Y-%m-%d").date(),
    },
    {
        "user_id": 8,
        "first_name": "Linda",
        "last_name": "Taylor",
        "profile_name": "linda_t",
        "email": "linda@email.com",
        "password": "lindapass",
        "date_joined": datetime.strptime("2023-01-08", "%Y-%m-%d").date(),
    },
    {
        "user_id": 9,
        "first_name": "Mark",
        "last_name": "Anderson",
        "profile_name": "mark_a",
        "email": "mark.anderson@email.com",
        "password": "markpass",
        "date_joined": datetime.strptime("2023-01-09", "%Y-%m-%d").date(),
    },
    {
        "user_id": 10,
        "first_name": "Olivia",
        "last_name": "Clark",
        "profile_name": "olivia_c",
        "email": "olivia.clark@email.com",
        "password": "oliviapass",
        "date_joined": datetime.strptime("2023-01-10", "%Y-%m-%d").date(),
    }
]

session.add_all([User(**user) for user in user_info])
session.commit()


post_info=[
    {
      "post_id": 1,
      "user_id": 1,
      "post_content": "Exploring the wonders of machine learning today! #AI #MachineLearning",
      "likes_total": 20,
      "date_created": datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
    },
    {
      "post_id": 2,
      "user_id": 2,
      "post_content": "Enjoying a peaceful weekend getaway. Nature is so refreshing! 🌳🌞",
      "likes_total": 15,
      "date_created": datetime.strptime("2023-01-02", "%Y-%m-%d").date(),
    },
    {
      "post_id": 3,
      "user_id": 3,
      "post_content": "Coding into the night. The best ideas come when the world is asleep. 💻🌙",
      "likes_total": 30,
      "date_created": datetime.strptime("2023-01-03", "%Y-%m-%d").date(),
    },
    {
      "post_id": 4,
      "user_id": 4,
      "post_content": "Delicious homemade dinner tonight! 🍝 #CookingAdventures",
      "likes_total": 25,
      "date_created": datetime.strptime("2023-01-04", "%Y-%m-%d").date(),
    },
    {
      "post_id": 5,
      "user_id": 5,
      "post_content": "Just finished a great book. Highly recommend it! 📚 #BookRecommendation",
      "likes_total": 18,
      "date_created": datetime.strptime("2023-01-05", "%Y-%m-%d").date(),
    },
    {
      "post_id": 6,
      "user_id": 6,
      "post_content": "Attended an inspiring tech conference today. Feeling motivated! 💪🚀",
      "likes_total": 22,
      "date_created": datetime.strptime("2023-01-06", "%Y-%m-%d").date(),
    },
    {
      "post_id": 7,
      "user_id": 7,
      "post_content": "Challenged myself with a new workout routine. Sweating it out! 💦💪",
      "likes_total": 27,
      "date_created": datetime.strptime("2023-01-07", "%Y-%m-%d").date(),
    },
    {
      "post_id": 8,
      "user_id": 8,
      "post_content": "Beautiful sunset view from my balcony. Grateful for simple moments. 🌅",
      "likes_total": 32,
      "date_created": datetime.strptime("2023-01-08", "%Y-%m-%d").date(),
    },
    {
      "post_id": 9,
      "user_id": 9,
      "post_content": "Exploring a new hobby—painting! 🎨 #ArtisticJourney",
      "likes_total": 23,
      "date_created": datetime.strptime("2023-01-09", "%Y-%m-%d").date(),
    },
    {
      "post_id": 10,
      "user_id": 10,
      "post_content": "Reflecting on the past year's accomplishments. Excited for what's ahead! 🎉 #NewBeginnings",
      "likes_total": 35,
      "date_created": datetime.strptime("2023-01-10", "%Y-%m-%d").date(),
    }
  ]



session.add_all([Post(**post) for post in post_info])
session.commit()

comments_info=[
    {
        "comment_id": 1,
        "user_id": 3,
        "post_id": 8,
        "content": "Great post!",
        "date_created": datetime.strptime("2023-01-10", "%Y-%m-%d").date(),
    },
    {
        "comment_id": 2,
        "user_id": 7,
        "post_id": 2,
        "content": "Interesting discussion!",
        "date_created": datetime.strptime("2023-01-15", "%Y-%m-%d").date(),
    },
    {
        "comment_id": 3,
        "user_id": 5,
        "post_id": 4,
        "content": "I totally agree.",
        "date_created": datetime.strptime("2023-01-11", "%Y-%m-%d").date(),
    },
    {
        "comment_id": 4,
        "user_id": 2,
        "post_id": 9,
        "content": "Nice one!",
        "date_created": datetime.strptime("2023-01-16", "%Y-%m-%d").date(),
    },
    {
        "comment_id": 5,
        "user_id": 9,
        "post_id": 6,
        "content": "Keep it up!",
        "date_created": datetime.strptime("2023-05-30", "%Y-%m-%d").date(),
    },
    {
        "comment_id": 6,
        "user_id": 1,
        "post_id": 5,
        "content": "Well said!",
        "date_created": datetime.strptime("2023-06-05", "%Y-%m-%d").date(),
    },
    {
        "comment_id": 7,
        "user_id": 8,
        "post_id": 3,
        "content": "I have a different perspective.",
        "date_created": datetime.strptime("2023-07-12", "%Y-%m-%d").date(),
    },
    {
        "comment_id": 8,
        "user_id": 6,
        "post_id": 7,
        "content": "Thanks for sharing!",
        "date_created": datetime.strptime("2023-08-18", "%Y-%m-%d").date(),
    },
    {
        "comment_id": 9,
        "user_id": 4,
        "post_id": 1,
        "content": "Looking forward to more posts!",
        "date_created": datetime.strptime("2023-09-22", "%Y-%m-%d").date(),
    },
    {
        "comment_id": 10,
        "user_id": 10,
        "post_id": 10,
        "content": "This is inspiring!",
        "date_created": datetime.strptime("2023-10-30", "%Y-%m-%d").date(),
    }
]
session.add_all([Comment(**comment) for comment in comments_info])
session.commit()

groups_info=[
  {
    "group_id": 1,
    "group_name": "Tech Enthusiasts",
    "date_created": datetime.strptime("2023-10-01", "%Y-%m-%d").date(),
  },
  {
    "group_id": 2,
    "group_name": "Travel Lovers",
    "date_created": datetime.strptime("2023-10-02", "%Y-%m-%d").date(),
  },
  {
    "group_id": 3,
    "group_name": "Fitness Buddies",
    "date_created": datetime.strptime("2023-10-03", "%Y-%m-%d").date(),
  },
  {
    "group_id": 4,
    "group_name": "Foodies Club",
    "date_created": datetime.strptime("2023-10-04", "%Y-%m-%d").date(),
  },
  {
    "group_id": 5,
    "group_name": "Bookworms Society",
    "date_created": datetime.strptime("2023-10-05", "%Y-%m-%d").date(),
  },
  {
    "group_id": 6,
    "group_name": "Gaming Guild",
    "date_created": datetime.strptime("2023-10-06", "%Y-%m-%d").date(),
  },
  {
    "group_id": 7,
    "group_name": "Music Aficionados",
    "date_created": datetime.strptime("2023-10-07", "%Y-%m-%d").date(),
  },
  {
    "group_id": 8,
    "group_name": "Artistic Minds",
    "date_created": datetime.strptime("2023-10-08", "%Y-%m-%d").date(),
  },
  {
    "group_id": 9,
    "group_name": "Movie Buffs",
    "date_created": datetime.strptime("2023-10-09", "%Y-%m-%d").date(),
  },
  {
    "group_id": 10,
    "group_name": "Outdoor Explorers",
    "date_created": datetime.strptime("2023-10-10", "%Y-%m-%d").date(),
  }
]
session.add_all([Group(**group) for group in groups_info])
session.commit()

likes_info=[
    {"like_id": 1, "user_id": 3, "post_id": 7},
    {"like_id": 2, "user_id": 8, "post_id": 4},
    {"like_id": 3, "user_id": 5, "post_id": 2},
    {"like_id": 4, "user_id": 2, "post_id": 9},
    {"like_id": 5, "user_id": 1, "post_id": 6},
    {"like_id": 6, "user_id": 10, "post_id": 3},
    {"like_id": 7, "user_id": 9, "post_id": 1},
    {"like_id": 8, "user_id": 4, "post_id": 8},
    {"like_id": 9, "user_id": 7, "post_id": 5},
    {"like_id": 10, "user_id": 6, "post_id": 10}
]
session.add_all([Like(**like) for like in likes_info])
session.commit()


data = [
  {"id": 1, "user_id": 5, "group_id": 3},
  {"id": 2, "user_id": 8, "group_id": 7},
  {"id": 3, "user_id": 2, "group_id": 1},
  {"id": 4, "user_id": 6, "group_id": 9},
  {"id": 5, "user_id": 3, "group_id": 2},
  {"id": 6, "user_id": 9, "group_id": 8},
  {"id": 7, "user_id": 1, "group_id": 4},
  {"id": 8, "user_id": 7, "group_id": 6},
  {"id": 9, "user_id": 4, "group_id": 10},
  {"id": 10, "user_id": 10, "group_id": 5}
]


for entry in data:
    user = session.query(User).filter_by(user_id=entry["user_id"]).first()
    group = session.query(Group).filter_by(group_id=entry["group_id"]).first()
    user.groups.append(group)
session.commit()

comment_data = [
  {"id": 1, "user_id": 5, "comment_id": 3},
  {"id": 2, "user_id": 8, "comment_id": 7},
  {"id": 3, "user_id": 2, "comment_id": 1},
  {"id": 4, "user_id": 6, "comment_id": 9},
  {"id": 5, "user_id": 3, "comment_id": 2},
  {"id": 6, "user_id": 9, "comment_id": 8},
  {"id": 7, "user_id": 1, "comment_id": 4},
  {"id": 8, "user_id": 7, "comment_id": 6},
  {"id": 9, "user_id": 4, "comment_id": 10},
  {"id": 10, "user_id": 10, "comment_id": 5}
]


for entry in comment_data:
    user = session.query(User).filter_by(user_id=entry["user_id"]).first()
    comment = session.query(Comment).filter_by(comment_id=entry["comment_id"]).first()
    user.comments.append(comment)
session.commit()