from blogspotapi import BlogClient
import os

import argparse
import os
from blogspotapi.blog_repository import BlogRepository
from amara.amara_env import amara_headers

def update_blog_collection(blog_repository, blog_client, blog_id):
    for blog_post in blog_client.iterate_blog_posts(blog_id):
        blog_repository.update_blog_post(blog_post)
    blog_repository.delete_old_posts()

def update_subtitles_collection(blog_repository, blog_client, blog_id, languages_str, amara_headers):
    languages_list = languages_str.split(',')
    for blog_post in blog_client.iterate_blog_posts(blog_id):
        blog_repository.update_sub_titles(blog_post, languages_list, amara_headers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--blogId', type=str)
    parser.add_argument('--languages', type=str)
    parser.add_argument('--mongo_connection', type=str, default='mongodb://localhost:27017/musicblogs')

    parser.set_defaults(update_subtitles=True)
    args = parser.parse_args()

    blog_repository = BlogRepository(args.mongo_connection, args.blogId)
    blog_repository.delete_old_posts()
    blog_repository.delete_old_subtitles()

