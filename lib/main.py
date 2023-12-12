#!/usr/bin/env python3
import click
from models import User, Post, Comment, Like, Group, session,user_group
from datetime import datetime
from sqlalchemy import VARCHAR

@click.command()
def user_input():
    click.echo('Creating a new user account...')
    first_name = click.prompt('Enter first name:', type=str)
    last_name = click.prompt('Enter last name:', type=str)
    user_name = click.prompt('Enter preferred user name:', type=str)
    email = click.prompt('Enter email address:', type=str)
    password = click.prompt('Enter password:', type=str)
    current_date = datetime.now()

    click.echo(f'{first_name} {last_name} {user_name} {email} {password} {current_date.strftime("%Y-%m-%d")}')

    new_user = User(first_name=first_name, last_name=last_name, profile_name=user_name, email=email, password=password, date_joined=current_date)
    session.add(new_user) 
    session.commit()

@click.command()
def create_group():
     click.echo('Creating a new group ...')
     group_name=click.prompt('Enter group name:',type=str)
     current_date = datetime.now()
     click.echo(f'{group_name},{current_date.strftime("%Y-%m-%d")}')
     new_group=Group(group_name=group_name,date_created=current_date)
     session.add(new_group)
     session.commit()
     
@click.command()
def join_group():
    click.echo('...Join a group ...')
    user_name = click.prompt("Enter your user_name", type=str)
    user = session.query(User).filter_by(profile_name=user_name).first()

    if user:
        group_to_join = click.prompt("Enter group you would like to join", type=str)
        group = session.query(Group).filter_by(group_name=group_to_join).first()

        if group:
            ins = user_group.insert().values(user_id=user.user_id, group_id=group.group_id)
            session.execute(ins)
            session.commit()

            click.echo(f"User '{user_name}' successfully joined group '{group_to_join}'")
        else:
            click.echo("Group does not exist")
    else:
        click.echo("User_name does not exist")

       
@click.command()
def view_group_members():
    group_name = click.prompt("Enter the group you'd like to view its members", type=str)
    if group_name:
        group = session.query(Group).filter_by(group_name=group_name).first()
        if group:
            users_in_group = [user.profile_name for user in group.users]
            click.echo(f" Group members for {group_name} are {', '.join(users_in_group)}")
        else:
            click.echo("Group does not exist")

@click.command()
def create_post():
    user_name = click.prompt("Enter user_name")
    user = session.query(User).filter_by(profile_name=user_name).first()

    if user:
        post_content = click.prompt("Enter new post:", type=str)
        current_date = datetime.now()

        click.echo(f'{user_name} has posted {post_content} on {current_date.strftime("%Y-%m-%d")}')

        new_post = Post(user_id=user.user_id, post_content=post_content, date_created=current_date)
        session.add(new_post)
        session.commit()
    else:
        click.echo("User_name does not exist")

@click.command()
def view_posts():
    user_name = click.prompt("Enter user_name of posts you want to view")
    user = session.query(User).filter_by(profile_name=user_name).first()

    if user:
        all_posts = session.query(Post).filter_by(user_id=user.user_id).all()

        if not all_posts:
            click.echo(f"No posts found for {user_name}")
            return

        click.echo(f'All posts by {user_name}:')

        for post in all_posts:
            click.echo(f'{post.post_content} - No of likes: {post.likes_total}')

    else:
        click.echo("User_name does not exist")


@click.command()
def update_posts():
    user_name = click.prompt("Enter your user_name")
    user = session.query(User).filter_by(profile_name=user_name).first()

    if user:
        all_posts = session.query(Post).filter_by(user_id=user.user_id).all()

        if not all_posts:
            click.echo(f"No posts found for {user_name}")
            return

        click.echo("Existing posts:")
        for i, post in enumerate(all_posts, start=1):
            click.echo(f"{i}. {post.post_content}")

        post_index = click.prompt("Select the post to update ", type=int)
        if 1 <= post_index <= len(all_posts):
            selected_post = all_posts[post_index - 1]
            updated_content = click.prompt("Update Post")           
            selected_post.post_content = updated_content
            session.commit()

            click.echo("Post updated successfully")
        else:
            click.echo("Invalid number")
    else:
        click.echo("User_name does not exist")


@click.command()
def like_post():
    user_name = click.prompt("Enter your user_name ")
    user = session.query(User).filter_by(profile_name=user_name).first()
    
    if user:
        all_posts = session.query(Post).all()
        
        click.echo("Existing posts:")
        for i, post in enumerate(all_posts, start=1):
            click.echo(f"{i}. {post.post_content} : No of likes: {post.likes_total}")

        post_index = click.prompt("Select the post to like ", type=int)

        if 1 <= post_index <= len(all_posts):
            selected_post = all_posts[post_index - 1]
            if selected_post.likes_total is None:
                selected_post.likes_total = 0
            selected_post.likes_total += 1
            click.echo(f'Post after new like: {selected_post.post_content} - No of likes: {selected_post.likes_total}')
            
            session.commit()
        else:
            click.echo("Invalid post index. Please select a valid post.")
    else:
        click.echo("User not found.")

@click.command
def delete_post():
    user_name = click.prompt("Enter your user_name")
    user = session.query(User).filter_by(profile_name=user_name).first()

    if user:
        all_posts = session.query(Post).filter_by(user_id=user.user_id).all()

        if not all_posts:
            click.echo(f"No posts found for {user_name}")
            return

        click.echo("Existing posts:")
        for i, post in enumerate(all_posts, start=1):
            click.echo(f"{i}. {post.post_content}")

        post_index = click.prompt("Select the post to delete ", type=int)
        if 1 <= post_index <= len(all_posts):
            selected_post = all_posts[post_index - 1]
            session.delete(selected_post)
            session.commit()

            click.echo("Post deleted successfully")
        else:
            click.echo("Invalid number")
    else:
        click.echo("User_name does not exist")

@click.command
def add_comment():
    user_name = click.prompt("Enter user_name")
    user = session.query(User).filter_by(profile_name=user_name).first()
    if user:
        all_posts = session.query(Post).all()
        click.echo("Existing posts:")
        for i, post in enumerate(all_posts, start=1):
            click.echo(f"{i}. {post.post_content} : No of likes: {post.likes_total}")
            post_index = click.prompt("Select the post to comment on ", type=int)
            if 1 <= post_index <= len(all_posts):
                    selected_post = all_posts[post_index - 1]
                    if selected_post.post_id=

    else:
        click.echo("User does not exist")
 


             

    


   
   


if __name__ == '__main__':
    click.secho("............Social App.....................")
    click.secho("What would you like to do?",fg='green')
    click.secho(".................................")
    click.secho("1: Create a new user account",fg='green')
    click.secho("2: Create a group",fg='green')
    click.secho("3: Join a group",fg='green')
    click.secho("4: View group members",fg='green')
    click.secho("5: Create a post",fg='green')
    click.secho("6: View posts",fg='green')
    click.secho("7: Update a post",fg='green')
    click.secho("8: Like a post",fg='green')
    click.secho("9: Delete a post",fg='green')
    click.secho("10: Add a comment",fg='green')
    click.secho("11:Update a comment",fg='green')
    click.secho("12:Delete a comment",fg='green')
    click.secho("13:View a user profile",fg='green')

    option=click.prompt("",type=int)
    if option==1:
        user_input()
    elif option==2:
        create_group()
    elif option==3:
        join_group()
    elif option==4:
        view_group_members()
    elif option==5:
        create_post()
    elif option==6:
        view_posts()
    elif option==7:
        update_posts()
    elif option==8:
        like_post()
    elif option==9:
        delete_post()

    else:
        click.echo("Exiting.......")




   
