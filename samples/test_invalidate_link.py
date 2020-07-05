from blogspotapi import BlogClient
import os
import logging
import argparse
import os
from blogspotapi.blog_repository import BlogRepository
from amara.amara_env import amara_headers
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--blogId', type=str)
    parser.add_argument('--postId', type=str)
    parser.add_argument('--videoUrl', type=str)

    parser.add_argument('--mongo_connection', type=str, default='mongodb://localhost:27017/musicblogs')

    parser.set_defaults(update_subtitles=True)
    args = parser.parse_args()

    blog_client = BlogClient(os.path.join(os.path.dirname(__file__), '..', 'client_secrets.json'))
    blog_repository = BlogRepository(args.mongo_connection, args.blogId)
    blog_repository.invalidate_link(args.postId, args.videoUrl)
    blog_client.invalidate_post(args.blogId, args.postId)