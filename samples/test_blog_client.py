from blogspotapi.blog_client import BlogClient
import os
from oauth2client.tools import argparser

def show_lyrics(blog_id, post_id, language):
    blog_client = BlogClient(os.path.join(os.path.dirname(__file__), '..', 'client_secrets.json'))
    video_id = blog_client.extract_video(blog_id, post_id)
    lyrics = blog_client.retrieve_lyrics(blog_id, post_id)
    print(video_id)
    print(lyrics)
    blog_client.insert_amara_tags(blog_id, post_id, language)

if __name__ == "__main__":
    argparser.add_argument('--blogId')
    argparser.add_argument('--postId')
    argparser.add_argument('--language')
    args = argparser.parse_args()
    show_lyrics(args.blogId, args.postId, args.language)
