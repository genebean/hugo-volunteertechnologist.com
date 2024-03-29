from bs4 import BeautifulSoup
from bs4 import CData
from json import JSONDecodeError
import dateutil.parser as dparser

import os
import re
import requests
import yaml


class ReadFeed:
    def __init__(self, podcast_feed, headers) -> list:
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
            self.episodes.append(ParseEpisode(e).__dict__['episode'])


class ParseEpisode:
    def __init__(self, e) -> dict:
        self.show_notes = CData(e.find('description').text)
        self.first_element = BeautifulSoup(self.show_notes, features="html.parser").find().name
        if self.show_notes.startswith('<'):
            if self.first_element == 'p':
                self.beginning_text = BeautifulSoup(self.show_notes, features="html.parser").p
            elif self.first_element == 'div':
                self.beginning_text = BeautifulSoup(self.show_notes, features="html.parser").div
        else:
            self.beginning_text = BeautifulSoup(self.show_notes, features="html.parser")
        self.br = self.beginning_text.find('br')
        if self.br:
            self.before_br = self.beginning_text.prettify( ).split('<br')[0].replace('\n', ' ') + '</' + self.first_element + '>'
            self.before_br = BeautifulSoup(self.before_br, features="html.parser").get_text().strip()
            self.description = re.sub("\s+"," ", self.before_br)
        else:
            self.description = self.beginning_text.get_text()
        self.transcript_html_url = e.find(
            'podcast:transcript', type='text/html')['url']
        try:
            self.t = requests.get(self.transcript_html_url, headers=headers)
        except Exception as ex:
            print('Error fetching the transcript from: ', self.transcript_html_url)
            print(ex)
        self.transcript_html = self.t.text
        self.transcript_vtt = e.find('podcast:transcript', type='text/vtt')
        if self.transcript_vtt:
            self.transcript_vtt = self.transcript_vtt['url']
        else:
            self.transcript_vtt = ''
        self.episode_number = e.find('podcast:episode').text
        self.pubdate = e.find('pubDate').text
        self.formatted_pub_date = dparser.parse(self.pubdate).strftime("%a, %d %b %Y %X %z")
        self.episode = {
            'aliases': ['/episode/%s' % (self.episode_number)],
            'author': e.find('itunes:author').text,
            'categories': ['Podcast Episode'],
            'date': self.formatted_pub_date,
            'description': self.description,
            'summary': self.description,
            'guid': e.find('guid').text,
            'image': 'images/episode-header.png',
            'mp3': e.find('enclosure', type='audio/mpeg')['url'],
            'episode_artwork': e.find('itunes:image')['href'],
            'transcript_vtt': self.transcript_vtt,
            'title': e.find('title').text,
            'episode_number': self.episode_number,
            'show_notes': self.show_notes,
            'transcript_html': self.transcript_html,
            'podverse_podcast_id': 'Kd9Z2u-92d',
        }
        self.episode




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


class GetPodverseEpisodeIds:
    def __init__(self, podverse_episode_api_url, headers):
        try:
            self.r = requests.get(podverse_episode_api_url, headers=headers)
            self.status_code = self.r.status_code
        except Exception as e:
            print('Error fetching the URL: ', podverse_episode_api_url)
            print(e)
        try:
            self.json = self.r.json()
        except JSONDecodeError:
            print('Response could not be serialized')
        except Exception as e:
            print('Could not parse the json: ', self.url)
            print(e)
        self.episode_ids = {}
        for episode in self.json[0]:
            episode_number = str(episode['itunesEpisode'])
            episode_id = str(episode['id'])
            self.episode_ids[episode_number] = episode_id


if __name__ == '__main__':
    podcast_feed = 'https://serve.podhome.fm/rss/ffcba3f9-1fbf-538e-92eb-431d85d92059'
    headers = {'User-Agent': 'feed-to-blog-posts'}
    feed = ReadFeed(podcast_feed, headers)
    for episode in feed.episodes:
        transcript_html = episode.pop('transcript_html')
        show_notes = episode.pop('show_notes').replace(
            '<br/><br/>', '<br />').replace(
            '<br /><br />', '<br />').replace(
            '<p><br/>', '<p>').replace(
            '<p><br />', '<p>').replace(
            '<br/></p>', '</p>').replace(
            '<br /></p>', '</p>')

        formatted_title = re.sub(r"[^a-zA-Z0-9 -]", "", episode['title']).lower().replace(' ','-')
        output_file = 'content/english/blog/%s.md' % (formatted_title)

        episode_number = str(episode.pop('episode_number'))

        with open(output_file, 'w') as blog_post:
            blog_post.write('---' + os.linesep)
            blog_post.write(yaml.dump(episode) + os.linesep)
            blog_post.write('---' + os.linesep)
            blog_post.write('{{< episode-player >}}' + os.linesep)
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
            blog_post.write(transcript_html + os.linesep)
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
                'podverse_podcast_id': 'Kd9Z2u-92d',
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


class GetPodverseEpisodeIds:
    def __init__(self, podverse_episode_api_url, headers):
        try:
            self.r = requests.get(podverse_episode_api_url, headers=headers)
            self.status_code = self.r.status_code
        except Exception as e:
            print('Error fetching the URL: ', podverse_episode_api_url)
            print(e)
        try:
            self.json = self.r.json()
        except JSONDecodeError:
            print('Response could not be serialized')
        except Exception as e:
            print('Could not parse the json: ', self.url)
            print(e)
        self.episode_ids = {}
        for episode in self.json[0]:
            episode_number = str(episode['itunesEpisode'])
            episode_id = str(episode['id'])
            self.episode_ids[episode_number] = episode_id


if __name__ == '__main__':
    podcast_feed = 'https://serve.podhome.fm/rss/ffcba3f9-1fbf-538e-92eb-431d85d92059'
    headers = {'User-Agent': 'feed-to-blog-posts'}
    feed = ReadFeed(podcast_feed, headers)
    podverse_episode_api_url = 'https://api.podverse.fm/api/v1/episode?podcastId=Kd9Z2u-92d'
    episode_ids = GetPodverseEpisodeIds(podverse_episode_api_url, headers).episode_ids
    for episode in feed.episodes:
        transcript = episode.pop('transcript')
        show_notes = episode.pop('show_notes').replace(
            '<br/><br/>', '<br />').replace(
            '<br /><br />', '<br />').replace(
            '<p><br/>', '<p>').replace(
            '<p><br />', '<p>').replace(
            '<br/></p>', '</p>').replace(
            '<br /></p>', '</p>')

        formatted_title = re.sub(r"[^a-zA-Z0-9 -]", "", episode['title']).lower().replace(' ','-')
        output_file = 'content/english/blog/%s.md' % (formatted_title)

        episode_number = str(episode.pop('episode_number'))
        podverse_episode_id = episode_ids[episode_number]

        with open(output_file, 'w') as blog_post:
            blog_post.write('---' + os.linesep)
            blog_post.write(yaml.dump(episode) + os.linesep)
            blog_post.write('---' + os.linesep)
            blog_post.write('{{< podverse-episode-single' +
                            ' podverse_episode_id="%s"' % (podverse_episode_id) +
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
