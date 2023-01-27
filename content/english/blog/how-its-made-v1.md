---
date: "Sat, 28 Jan 2023 13:40:00 -0500"
title: "How it's Made, v1"
description: "A look at what goes into recording, producing, & publishing an episode of the Volunteer Technologist"
image: "images/how-its-made-v1.png"
categories:
  - Behind-the-Scenes
draft: true
---

I've been surprised at all that goes into making and sharing an episode of the Volunteer Technologist podcast. Even as a long time techie and consumer of podcasts about podcasting, it turns out there's more to it than I thought. Not only that, doing a quality production without also doing everything the long and/or hard way is notably more expensive than I expected (see my [contribute page]({{< ref "/contribute" >}}) for details). This post is a look behind the scenes at how I'm doing things. I've entitled it "How it's Made, v1" because I fully expect things to change as I learn more and as some of the tech involved matures, and I plan to post additional iterations in the future.

Before we get into how I am doing things (the _what_), let's take a step back and first look at _why_ I'm doing things the way I am. To do that, we need to start with talking about what Podcasting 2.0 is.

## Podcasting 2.0

I was introduced to this newish thing being called "Podcasting 2.0" while listening to several of the shows from [Jupiter Broadcasting](https://www.jupiterbroadcasting.com), and it really resonated with me. Basically, it's a set of initiatives to advance podcasting technology and to decentralize podcasting, taking control of the medium out of the hands of large technology companies like Apple and Spotify.

### New & Exciting Features

This initiative is bringing many new features to podcasts and the apps that play them, including:

* __PodcastIndex.org:__ an open alternative to Apple's podcast directory
* __Podping:__ this facilitates nearly instant notification about any change within a podcast's rss feed. These notifications can be utilized by apps and hosted services alike.
* __Transcripts:__ these are not only able to be displayed directly in a podcast player, but that can scroll along automatically as it plays ([Podverse](https://podverse.fm) has this feature). Transcripts make podcasts easier for people with difficulty hearing to consume and also make episodes searchable.
* __Chapters:__ these facilitate an image, even one other than the main artwork of the show or episode, being displayed during specific portions of an episode along with a relevant hyperlink. These help provide additional context to what a portion of an episode is talking about. They also make it easy to jump around within an episode.
* __Funding:__ this provides a link to somewhere like [buymeacoffee.com/genebean](https://www.buymeacoffee.com/genebean) or Patreon. Apps are already starting to include a button that makes it easy for listeners to support a show by jumping right to the specified funding link.
* __Boostagrams:__ these are donations with messages that you can send directly to creators. They are comparable to YouTube's "Super Chat" and Twitch's "Elevated Chat." [Fountain][f] takes boostagrams a step farther and uses them as the basis for higher quality comments on shows and episodes.

As if these features weren't enough, there's actually quite a bit more going on too. These two articles cover the topic in much more detail:

* [Podcasting 2.0 Introduction](https://blubrry.com/support/podcasting-2-0-introduction/) by [Todd Cochrane](https://podcastindex.social/@Todd_Blubrry)
* [An Introduction to Podcasting 2.0](https://medium.com/@everywheretrip/an-introduction-to-podcasting-2-0-3c4f61ea17f4) by Gary Arndt

## My Desire (the _why_)

As I said before, the Podcasting 2.0 features really resonated with me, so I set out with the intention of utilizing them as fully as I can. My workflow (the _what_) is, therefore, alittle more complicated than that of a show that doesn't implement some of this new functionality. The additional complexity is a byproduct of the fact that much of Podcasting 2.0 is still very new. I fully expect that the complexity will be reduced as thing mature, just as tends to happen with most new technology.

## My Workflow (the _what_)

With the foundation of where I am coming from laid, let's dive into what I am actually doing.

### An Episode's Journey

At a high level, each episode's creation goes something like this:

1. Find someone who's technically inclined AND who's volunteering that knowledge outside of work.
2. Pitch the idea of them coming on the show to them.
3. Schedule a time outside of normal working hours, or over lunch, to record.
4. Record an interview for roughly 25-35 minutes without us being in the same place.
5. Edit the audio.
6. Insert my intro music and outro audio.
7. Upload audio and wait for additional processing to complete.
8. Create a transcript based on the same file that is uploaded.
9. Figure out a title for the episode (sometimes this is harder than you'd think).
10. Write show notes.
11. Create chapters.
12. Send a link to the guest so they can review the episode before it goes live.
13. Schedule publishing of the episode.
14. Create a soundbite from the episode to use as a teaser in social media posts.
15. Publish the episode to this website once the podcast is published.
16. Promote the new episode on social media.

As you can see, there is a lot more to making an episode than doing a simple recording and throwing it out to the world and hoping people will hear it.

### Guests

Seeing as the basis of my podcast is doing interviews with technically inclined people who also volunteer their skills, the first part of any episode is finding such a person, seeing if they are willing to be on my podcast, and then finding a time that works for both of us to do the actual recording. I have been blessed to have some friends and coworkers who are doing some pretty awesome stuff so I have started off pulling from that pool of talent. I've also been lucky enough to get a couple of suggestions of people to interview who are friends of friends. I even got one volunteer out of the blue... that was more than a little exciting! I'm hoping that word of mouth continues to provide me people to chat with while I work to build up a body of work that I can show to people I reach out to cold-call style.

### Recording

All of the episodes I have recorded so far, and all the ones I hope to record in the near future, include me at my house and someone located in another city, state, or country... but I don't want the recording to _sound_ like we are in drastically different locations. Fortunately, a positive thing that came out of the lock downs of 2020 was a rapid improvement in tools that facilitate this kind of scenario.

One of the podcasts about podcasting that I listen to is [Buzzcast](https://buzzcast.buzzsprout.com). They both use and talk about [Riverside.fm](https://riverside.fm). After doing some research of my own, I quickly realized why they liked Riveride and decided to try it myself. I'm quite happy with it and, so far, have even been able to get by with the free version. When it is time to record, I open up [Vivaldi](https://vivaldi.com) since Riverside requires a chromium based browser (I don't use Google Chrome) and login into [riverside.fm](https://riverside.fm). From there I am able to send my guest a link to the "studio" used for this podcast. Once they join, we are able to see each other and chat just like you would in Zoom or any other video conferencing application. The big difference here is that we are able to record high quality audio that is perfectly synchronized. Riverside achieves this by recording the audio locally on each of our computers and uploading it in the background. It also has the ability to record video, but I am not using that right now.

Once we are finished recording, we just hang out chatting for a few minutes more while the uploads finish and then can go our separate ways. The chatting hasn't yet been any big deal since that's a good time to talk about the logistics around when what we just recorded will be published.

### Editing the Audio

When it is time to edit, I download each track from Riverside and then load them up in [Audacity](https://www.audacityteam.org/). Audacity allows me to fairly easily cut out pops and longer pauses in the conversation. If we have to backup and try again while talking during the interview, I am also able to cut out the not so great version so that you, the listener, only get the better version. Think of this as the same kind of cleanup you'd do while proof reading a term paper or a novella. This process tends to take about 3 times as long as the original recording, so a 30 minute recording will take about 90 minutes to edit. This is because there is a lot of stopping and starting and going back to listen again.

Once I have finished editing the original audio tracks I add in my intro music at the beginning and my outro at the end. This usually takes another 15 minutes or so. The last step in Audacity is to export a high quality WAV file. This file is what gets sent to my podcast host ([Buzzsprout][b]) and is what gets used when making the transcript later.

### Uploading to Buzzsprout

The next step is to take the exported WAV file and upload it to [Buzzsprout][b]. At this point, I have a complete episode, but the volume level is generally fluctuating all over the place between the four tracks (intro music, guest track, my track, and the outro). Yes, this could be fixed in Audacity or similar, but it takes more skill with the tools than I have and a lot more effort than I am willing to expend as effort correlates directly to time and I'd rather spend that time with my family. My solution: spend $6 a month and let Buzzsprout fix it for me. I do this by paying for their [Magic Mastering](https://www.buzzsprout.com/help/67-magic-mastering) service. Magic Mastering goes to work as soon as I upload the WAV file and notifies me by email when it is finished.

### Transcripts

In the last year, I have heard about several different ways to generate transcripts of a show in an automated manner... but what I didn't realize is that most of them are only partial solutions that are not much better than just doing it by hand. The challenge for me is that I only feel a transcript is worth while if it conforms to [the specifications defined](https://github.com/Podcastindex-org/podcast-namespace/blob/main/transcripts/transcripts.md#srt) as part of Podcasting 2.0. I did a bit of research and it seems that the SRT format is the most compatible one and also provides the information needed so that apps like [Podverse](https://podverse.fm) can have them scroll in sync with the audio that is being listened to. The kicker is that you can get a SRT file from the [Descript](https://www.descript.com/) application or for free via <https://riverside.fm/podcast-transcript> or generate one yourself using [Whisper](https://openai.com/blog/whisper/) like [Castopod describes](https://blog.castopod.org/transcribe-your-podcast-for-free-using-only-a-laptop-and-whisper/)... but none of those both conform to the 32 characters per line limit of the specification and include speaker names so that the reader knows who is saying each part. Fortunately, [Otter](https://otter.ai/) does do both. The downside of Otter is that it is far from cheap, but I feel pretty strongly that having a quality transcript is a something that's worth spending money on.

To actually get the transcript, I upload the same WAV file I uploaded to Buzzsprout to Otter and wait a little while for the magic to happen. Once it is complete I can easily use their interface to identify each speaker and then download the needed SRT file in the proper format.

Once it is downloaded, I head back over to the episode page in Buzzsprout and upload it. Buzzsprout then processes the file and generates an HTML version to go along with the SRT version. Both versions are then made available via their servers and appropriate references are added into the episode's entry in the podcast's rss feed so that apps will know where to find either version.

#### Title & Show Notes

After uploading I have to figure out how to title the episode so that it conveys the overall topic in as few words as possible. Since this podcast is centered around doing interviews with people about how they volunteer, I have decided to have my titles follow the format of "[what they do] with [who they are]." For example, my first full length episode was with a friend of mine named RJ Hill and talked about the awesome stuff he does with an an organization called [Engineered Reform](https://www.engineeredreform.com/). That episode is entitled "[Engineered Reform with RJ Hill]({{< relref "/blog/engineered-reform-with-rj-hill" >}})." Sometimes what the title should be is cut and dry, and sometimes it takes a lot of work to come up with... naming things is hard.

Once I figure out a tile, I need to write up what's called "show notes." Show notes are the text that shows up in a podcast player to describe an episode and is where you can provide links to things talked about during the show. I generally start this off with a brief overview of what the episode is about and then add in any extra info that is worth calling out. After that I provide a section that is a simple list of links to things we talked about that others might want to check out.

### Chapters

Chapters are a really cool feature of Podcasting 2.0. Like I mentioned earlier, I can use them as a means of showing images that relate to a give part of the episode. Since I generally start each episode by introducing the podcast and my guest, I have been setting the image for the first chapter to one showing my guest. This means that anyone listening in [Fountain][f] or another Podcast 2.0 app will see a picture of my guest from as soon as the episode start until we finish the intro section.

To crate these chapters, I go back to the WAV file on my computer and open it up in an audio play such as [VLC](https://www.videolan.org/vlc/) that makes it easy to pause and jump backwards in time. I also open up the chapter editor in Buzzsprout. I then start listening for when what we are talking about changes and record the timestamp in Buzzsprout. In addition to the timestamp, I also have to come up with a name for that section (chapter), add a link if there is a relevant one, and add an image if it makes sense. Once these bits have been added, I resume listening until the next place it makes sense to insert a chapter marker. Eventually I get to the end of the episode and am able to check off another part of the episode production todo list.

### Guest Preview Time

At this point, I am finished working on the episode. Fortunately, Buzzsprout provides a way to send a link to the unpublished version to someone so that they can check everything out ahead of time, and this is exactly what I do so that my guest can see the notes and hear the final audio before it is published to the world.

### Scheduled Publishing

One thing that you are supposed to do as a podcast host is pick a consistent time to publish, as opposed to just publishing when things are ready. For a podcast like mine that is published monthly, this means publishing on exactly the same day at exactly the same hour and minute each month. Though I originally published on the 30th at 8am eastern, I have since realized that a better time to post is on the 1st at 5am eastern. I decided to make this change for two reasons: 1) every month has a 1st whereas not all have a 30th (I'm looking at you February) and 2) 5am eastern gets the episode out early enough for it to have downloaded in time for morning consumption on release day.

### Visual Soundbites

Buzzsprout has taken the `<podcast:soudbite>` [tag from Podcasting 2.0](https://github.com/Podcastindex-org/podcast-namespace/blob/main/docs/1.0.md#soundbite) and added a visual component to it that facilitates sharing on social media. They call this [Visual Soundbites (Audiogram)](https://www.buzzsprout.com/help/57-setup-visual-soundbite). Basically, it's a clip from the episode with a visual soundwave of the clip's audio that is useful when promoting an episode. For example:

{{< video "/videos/engineered-reform-with-rj-hill_soundbite.mp4" "mp4" >}}

### Publishing Here

When each episode goes live, I also want a page created here that includes a way to listen to it, all the show notes, and the transcript. To simplify this process, I have a script that reads the podcast's rss feed and uses the info in it to generate each needed page. I'm going to save all the details of that script for a separate post, but I will go ahead and say that I plan to have that script run automatically whenever a podping event for my show happens. The idea is to automatically update this site if I change anything in any episode or publish a new episode.

### Promoting New Episodes

Last, but certainly not least, is to promote new episodes. This is done via the soundbites before an episode comes out and by linking to the episode after it comes out.

## Wrap up

This is kind of a lot... but it feels worth it and will only get easier as time goes on. I really love getting to help bring the awesome work people do behind the scenes out in the open so that others can see it. Sometimes it is really surprising just how much of our daily lives is directly impacted by volunteers.

[b]: https://www.buzzsprout.com/?referrer_id=1803680
[f]: https://fountain.fm/genebean?code=5cb3b5f06a
