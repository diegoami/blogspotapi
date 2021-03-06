from blogspotapi import BlogClient

import argparse
import os
from blogspotapi.blog_repository import BlogRepository
from amara.amara_env import amara_headers
import time
import logging

logging.basicConfig(level=logging.DEBUG )

def update_blog_collection(blog_repository, blog_client, blog_id):
    for blog_post in blog_client.iterate_blog_posts(blog_id):

        blog_repository.update_blog_post(blog_post)
        time.sleep(0.2)

def update_subtitles_collection(blog_repository, blog_client, blog_id, languages_str, amara_headers):
    languages_list = languages_str.split(',')
    for blog_post in blog_client.iterate_blog_posts(blog_id):
        blog_repository.update_sub_titles(blog_post, languages_list, amara_headers)
        time.sleep(0.2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--blogId', type=str)
    parser.add_argument('--languages', type=str)
    parser.add_argument('--mongo_connection', type=str, default='mongodb://localhost:27017/musicblogs')

    parser.set_defaults(update_subtitles=True)
    args = parser.parse_args()

    blog_repository = BlogRepository(args.mongo_connection, args.blogId)
    blog_client = BlogClient(os.path.join(os.path.dirname(__file__), '..', 'client_secrets.json'))
    update_blog_collection(blog_repository, blog_client, args.blogId)
    if args.update_subtitles:
        update_subtitles_collection(blog_repository, blog_client, args.blogId, args.languages, amara_headers)
