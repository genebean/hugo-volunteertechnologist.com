from bs4 import BeautifulSoup
from bs4 import CData
import os
import requests
import yaml


class ReadFeed:
    def __init__(self, rss_url, headers):
        try:
            self.r = requests.get(rss_url, headers=headers)
            self.status_code = self.r.status_code
        except Exception as e:
            print('Error fetching the URL: ', rss_url)
            print(e)
        try:
            self.soup = BeautifulSoup(self.r.text, features='lxml-xml')
        except Exception as e:
            print('Could not parse the xml: ', self.url)
            print(e)
        self.items = self.soup.findAll('item')
        self.episodes = []
        for e in self.items:
            transcript_url = e.find(
                'podcast:transcript', type='text/html')['url']
            try:
                t = requests.get(transcript_url, headers=headers)
            except Exception as e:
                print('Error fetching the transcript from: ', transcript_url)
                print(e)
            transcript_html = t.text
            episode = {
                'aliases': ['/episode/%s' % (e.find('itunes:episode').text)],
                'author': e.find('itunes:author').text,
                'date': e.find('pubDate').text,
                'guid': e.find('guid').text,
                'image': 'images/episode-header.png',
                'mp3': e.find('enclosure', type='audio/mpeg')['url'],
                'title': e.find('title').text,
                'description': CData(e.find('content:encoded').text),
                'transcript': transcript_html,
            }
            self.episodes.append(episode)


if __name__ == '__main__':
    podcast_feed = 'https://feeds.buzzsprout.com/2053906.rss'
    headers = {'User-Agent': 'feed-to-blog-posts'}
    feed = ReadFeed('https://feeds.buzzsprout.com/2053906.rss', headers)
    for episode in feed.episodes:
        transcript = episode.pop('transcript')
        description = episode.pop('description').replace(
            '<br/><br/></p>', '</p>').replace('<br/><br/>', '<br/>')
        mp3 = episode.pop('mp3')
        mp3_parts = mp3.split('/')
        podcast_id_number = int(mp3_parts[-2])
        mp3_name_parts = mp3_parts[-1].split('-')
        episode_id_number = int(mp3_name_parts.pop(0))
        file_name = '-'.join(mp3_name_parts).split('.')[0]
        output_file = 'content/english/blog/%s.html' % (file_name)
        player_html = '<script src="https://www.buzzsprout.com/%d/%d-%s.js?container_id=buzzsprout-player-%d&player=small" type="text/javascript" charset="utf-8"></script>' % (
            podcast_id_number, episode_id_number, file_name, episode_id_number)

        with open(output_file, 'w') as blog_post:
            # blog_post.write('testing' + os.linesep)
            blog_post.write('---' + os.linesep)
            blog_post.write(yaml.dump(episode) + os.linesep)
            blog_post.write('---' + os.linesep)
            blog_post.write('<div id="buzzsprout-player-%d"></div>' %
                            (episode_id_number) + os.linesep)
            blog_post.write(BeautifulSoup(
                player_html, 'html.parser').prettify() + os.linesep)
            blog_post.write(BeautifulSoup(
                description, 'html.parser').prettify() + os.linesep)
            blog_post.write('<h2>Transcript</h2>' + os.linesep)
            blog_post.write(BeautifulSoup(
                transcript, 'html.parser').prettify() + os.linesep)
