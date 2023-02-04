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
        self.host_image_url = self.soup.find('podcast:person', role='host')['img']
        self.items = self.soup.findAll('item')
        self.episodes = []
        for e in self.items:
            show_notes = CData(e.find('content:encoded').text)
            description = BeautifulSoup(show_notes, features="html.parser").p.get_text()
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
                'categories': ['Podcast Episode'],
                'date': e.find('pubDate').text,
                'description': description,
                'guid': e.find('guid').text,
                'image': 'images/episode-header.png',
                'mp3': e.find('enclosure', type='audio/mpeg')['url'],
                'title': e.find('title').text,
                'show_notes': show_notes,
                'transcript': transcript_html,
            }
            self.episodes.append(episode)


if __name__ == '__main__':
    podcast_feed = 'https://feeds.buzzsprout.com/2053906.rss'
    headers = {'User-Agent': 'feed-to-blog-posts'}
    feed = ReadFeed('https://feeds.buzzsprout.com/2053906.rss', headers)
    for episode in feed.episodes:
        transcript = episode.pop('transcript')
        show_notes = episode.pop('show_notes').replace(
            '<br/><br/>', '<br/>').replace(
            '<br/></p>', '</p>')
        mp3 = episode.pop('mp3')
        mp3_parts = mp3.split('/')
        podcast_id_number = int(mp3_parts[-2])
        mp3_name_parts = mp3_parts[-1].split('-')
        episode_id_number = int(mp3_name_parts.pop(0))
        file_name = '-'.join(mp3_name_parts).split('.')[0]
        output_file = 'content/english/blog/%s.md' % (file_name)

        with open(output_file, 'w') as blog_post:
            blog_post.write('---' + os.linesep)
            blog_post.write(yaml.dump(episode) + os.linesep)
            blog_post.write('---' + os.linesep)
            blog_post.write('{{< buzzsprout-episode' +
                            ' episode_id_number="%d"' % (episode_id_number) +
                            ' podcast_id_number="%d"' % (podcast_id_number) +
                            ' file_name="%s"' % (file_name) +
                            ' >}}' + os.linesep)
            blog_post.write('{{< listen-apple >}}')
            blog_post.write('{{< listen-overcast >}}')
            blog_post.write('{{< listen-google >}}')
            blog_post.write('{{< listen-rss >}}')
            blog_post.write(os.linesep)
            blog_post.write('{{< tabs >}}' + os.linesep)
            blog_post.write('{{< tab "Show Notes" >}}' + os.linesep)
            blog_post.write('{{< rawhtml >}}' + os.linesep)
            blog_post.write(show_notes + os.linesep)
            blog_post.write('{{< /rawhtml >}}' + os.linesep)
            blog_post.write('{{< /tab >}}' + os.linesep)
            blog_post.write('{{< tab "Transcript" >}}' + os.linesep)
            blog_post.write('{{< rawhtml >}}' + os.linesep)
            blog_post.write(transcript + os.linesep)
            blog_post.write('{{< /rawhtml >}}' + os.linesep)
            blog_post.write('{{< /tab >}}' + os.linesep)
            blog_post.write('{{< /tabs >}}' + os.linesep)
    with open('content/english/about.md', 'r', encoding='utf-8') as file:
        about_lines = file.readlines()
    for i in range(len(about_lines)):
        if about_lines[i].startswith('image: '):
            about_lines[i] = 'image: "%s"%s' % (feed.host_image_url, os.linesep)
    with open('content/english/about.md', 'w', encoding='utf-8') as file:
        file.writelines(about_lines)
