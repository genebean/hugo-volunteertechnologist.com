from bs4 import BeautifulSoup
from bs4 import CData
from json import JSONDecodeError
import dateutil.parser as dparser

import os
import re
import requests
import yaml


class ReadFeed:
    def __init__(self, podcast_feed, headers):
        try:
            self.r = requests.get(podcast_feed, headers=headers)
            self.status_code = self.r.status_code
        except Exception as e:
            print('Error fetching the URL: ', podcast_feed)
            print(e)
        try:
            self.soup = BeautifulSoup(self.r.text, features='lxml-xml')
        except Exception as e:
            print('Could not parse the xml: ', self.url)
            print(e)
        self.host_image_url = self.soup.find('podcast:person', role='host')['img']
        self.guid = self.soup.find('podcast:guid').text
        self.items = self.soup.findAll('item')
        self.episodes = []
        for e in self.items:
            show_notes = CData(e.find('description').text)
            first_element = BeautifulSoup(show_notes, features="html.parser").find().name
            if first_element == 'p':
                beginning_text = BeautifulSoup(show_notes, features="html.parser").p
            elif first_element == 'div':
                beginning_text = BeautifulSoup(show_notes, features="html.parser").div
            br = beginning_text.find('br')
            if br:
                before_br = beginning_text.prettify( ).split('<br')[0].replace('\n', ' ') + '</' + first_element + '>'
                before_br = BeautifulSoup(before_br, features="html.parser").get_text().strip()
                description = re.sub("\s+"," ", before_br)
            else:
                description = beginning_text.get_text()
            transcript_url = e.find(
                'podcast:transcript', type='text/html')['url']
            try:
                t = requests.get(transcript_url, headers=headers)
            except Exception as e:
                print('Error fetching the transcript from: ', transcript_url)
                print(e)
            transcript_html = t.text
            episode_number = e.find('podcast:episode').text
            pubdate = e.find('pubDate').text
            formatted_pub_date = dparser.parse(pubdate).strftime("%a, %d %b %Y %X %z")
            episode = {
                'aliases': ['/episode/%s' % (episode_number)],
                'author': e.find('itunes:author').text,
                'categories': ['Podcast Episode'],
                'date': formatted_pub_date,
                'description': description,
                'summary': description,
                'guid': e.find('guid').text,
                'image': 'images/episode-header.png',
                'mp3': e.find('enclosure', type='audio/mpeg')['url'],
                'title': e.find('title').text,
                'episode_number': episode_number,
                'show_notes': show_notes,
                'transcript': transcript_html,
            }
            self.episodes.append(episode)


class GetPodhomeEpisodeIds:
    def __init__(self, podhome_player_api_url, headers):
        try:
            self.r = requests.get(podhome_player_api_url, headers=headers)
            self.status_code = self.r.status_code
        except Exception as e:
            print('Error fetching the URL: ', podhome_player_api_url)
            print(e)
        try:
            self.json = self.r.json()
        except JSONDecodeError:
            print('Response could not be serialized')
        except Exception as e:
            print('Could not parse the json: ', self.url)
            print(e)
        self.episode_ids = {}
        for episode in self.json['episodes']:
            episode_number = str(episode['episodeNr'])
            episode_id = str(episode['episodeId'])
            self.episode_ids[episode_number] = episode_id


if __name__ == '__main__':
    podcast_feed = 'https://serve.podhome.fm/rss/ffcba3f9-1fbf-538e-92eb-431d85d92059'
    headers = {'User-Agent': 'feed-to-blog-posts'}
    feed = ReadFeed(podcast_feed, headers)
    podcast_guid = feed.guid
    podhome_player_api_url = 'https://serve.podhome.fm/api/player/' + podcast_guid
    episode_ids = GetPodhomeEpisodeIds(podhome_player_api_url, headers).episode_ids
    for episode in feed.episodes:
        transcript = episode.pop('transcript')
        show_notes = episode.pop('show_notes').replace(
            '<br/><br/>', '<br />').replace(
            '<br /><br />', '<br />').replace(
            '<p><br/>', '<p>').replace(
            '<p><br />', '<p>').replace(
            '<br/></p>', '</p>').replace(
            '<br /></p>', '</p>')
        # mp3 = episode.pop('mp3')
        # mp3_parts = mp3.split('/')
        # podcast_id_number = int(mp3_parts[-2])
        # mp3_name_parts = mp3_parts[-1].split('-')
        # episode_id_number = int(mp3_name_parts.pop(0))
        # file_name = '-'.join(mp3_name_parts).split('.')[0]
        formatted_title = re.sub(r"[^a-zA-Z0-9 -]", "", episode['title']).lower().replace(' ','-')
        output_file = 'content/english/blog/%s.md' % (formatted_title)

        episode_number = str(episode.pop('episode_number'))
        podhome_episode_id = episode_ids[episode_number]

        with open(output_file, 'w') as blog_post:
            blog_post.write('---' + os.linesep)
            blog_post.write(yaml.dump(episode) + os.linesep)
            blog_post.write('---' + os.linesep)
            blog_post.write('{{< podhome-episode' +
                            ' podhome_episode_id="%s"' % (podhome_episode_id) +
                            ' >}}' + os.linesep)
            blog_post.write('{{< listen-apple >}}')
            blog_post.write('{{< listen-overcast >}}')
            blog_post.write('{{< listen-spotify >}}')
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
