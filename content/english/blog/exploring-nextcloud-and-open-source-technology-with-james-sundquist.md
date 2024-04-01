---
aliases:
- /episode/6
author: Gene Liverman
categories:
- Podcast Episode
date: Tue, 01 Aug 2023 09:00:00 +0000
description: In this episode, Terence Eden talks about his project OpenBenches , which
  aims to create a database of memorial benches around the world. He discusses how
  the project started, the challenges they faced, and the impact it has had. Terence
  also shares his thoughts on gamification and the future of mapping with OpenStreetMap
  and the Fediverse .
guid: Buzzsprout-13268521
image: images/episode-header.png
mp3: https://op3.dev/e/serve.podhome.fm/episode/d4f02a91-cead-4ab3-6c02-08dc1c0c24e3/638416094984372334c638311b-63fb-4a28-b2b2-d2c928290a97v1.mp3
podverse_podcast_id: Kd9Z2u-92d
summary: In this episode, Terence Eden talks about his project OpenBenches , which
  aims to create a database of memorial benches around the world. He discusses how
  the project started, the challenges they faced, and the impact it has had. Terence
  also shares his thoughts on gamification and the future of mapping with OpenStreetMap
  and the Fediverse .
title: Exploring Nextcloud and Open Source Technology with James Sundquist

---
{{< podverse-episode-single podverse_episode_id="T87IN2ktO" >}}
{{< listen-apple >}}{{< listen-overcast >}}{{< listen-spotify >}}{{< listen-google >}}{{< listen-rss >}}
{{< tabs >}}
{{< tab "Show Notes" >}}
{{< rawhtml >}}
Ever wondered how open source technology is revolutionizing the way we store and share data? Well, you are in for a treat! In my latest conversation with James Sundquist, a landscaper with a techie heart, we get down to the nuts and bolts of <a href="https://nextcloud.com/" target="_blank">Nextcloud</a>, an open source file sharing platform that is shaking up the data storage game. James gives us a peek into the <a href="https://docs.nextcloudpi.com/" target="_blank">Nextcloud Pi</a> project, a genius solution for self-hosting Nextcloud on devices like a <a href="https://www.raspberrypi.org/" target="_blank">Raspberry Pi</a> and the exciting challenges of generating and maintaining documentation with <a href="https://www.discourse.org/" target="_blank">Discourse</a>. <br />Our conversation takes an exciting turn as we explore the continuous evolution of Nextcloud Pi, moving beyond just documentation. Its integration with <a href="https://matrix.org/" target="_blank">Matrix</a> and <a href="https://telegram.org/" target="_blank">Telegram</a> is breaking down barriers making collaboration a breeze. We also get into the adrenaline rush of the <a href="https://nextcloud.com/conference" target="_blank">Nextcloud Conference</a> and how Nextcloud Pi is a crucial tool for Nextcloud employees. Then, we move on to James's personal journey with open source projects, where he masterfully crafts tools for his theatrical projects. Our episode concludes with a heartfelt shoutout to <a href="https://www.meremortalspodcast.com/" target="_blank">Kyrin from the Mirror Mortals podcast</a> for their unwavering support. Get ready to immerse yourself in the fascinating world of open source technology!<br /><strong>Links:</strong><br /><ul><li>Docs for Nextcloud: <a href="https://docs.nextcloudpi.com" target="_blank">docs.nextcloudpi.com</a></li><li>Nextcloud Pi: <a href="https://github.com/nextcloud/nextcloudpi" target="_blank">github.com/nextcloud/nextcloudpi</a></li><li>Roadmap of Nextcloud Pi development - <a href="https://github.com/orgs/nextcloud/projects/67" target="_blank">github.com/orgs/nextcloud/projects/67</a></li><li>Noisebridge hacker space: <a href="https://noisebridge.net" target="_blank">noisebridge.net</a></li><li>Meta site for Discourse: <a href="https://meta.discourse.org" target="_blank">meta.discourse.org</a></li><li>Q Light Controller+: <a href="https://www.qlcplus.org/" target="_blank">qlcplus.org</a></li><li>Jame's personal website for shows and events: <a href="https://james.network" target="_blank">james.network</a></li><li>Jupiter Broadcasting: <a href="https://www.jupiterbroadcasting.com/" target="_blank">jupiterbroadcasting.com</a></li><li>Inkscape: <a href="https://inkscape.org" target="_blank">inkscape.org</a></li><li>DaVinci Resolve: <a href="https://www.blackmagicdesign.com/products/davinciresolve" target="_blank">blackmagicdesign.com/products/davinciresolve</a></li><li>Kdenlive: <a href="https://kdenlive.org" target="_blank">https://kdenlive.org</a></li><li>Debian: <a href="https://www.debian.org" target="_blank">debian.org</a></li><li>Let's Encrypt: <a href="https://letsencrypt.org" target="_blank">letsencrypt.org</a></li></ul><strong>Correction:<br /></strong>I just wanted to note that <a href="https://nextcloud.com" target="_blank">Nextcloud</a> was forked from <a href="https://owncloud.com" target="_blank">ownCloud</a>, not Open Cloud.&nbsp;<br /> <p>Support the show via <a href="https://www.buymeacoffee.com/genebean" target="_blank">Buy Me a Coffee</a><br />Send a boost with a new podcast app such as <a href="https://fountain.fm/genebean?code=5cb3b5f06a" target="_blank">Fountain</a> or via <a href="https://conshax.app/support/volunteertechnologist" target="_blank">conshax.app/support/volunteertechnologist</a><br />See all the ways to contribute, and what producing this podcast costs, at <a href="https://www.volunteertechnologist.com/contribute/" target="_blank">volunteertechnologist.com/contribute/</a><br />You can find me on Mastodon at <a href="https://podcastindex.social/@volunteertechnologist" target="_blank">podcastindex.social/@volunteertechnologist</a> You can also reach me via <a href="https://www.volunteertechnologist.com/contact/" target="_blank">volunteertechnologist.com/contact/</a><br />Visit <a href="https://www.volunteertechnologist.com/" target="_blank">volunteertechnologist.com</a> for show notes, transcripts, or more information.</p>
{{< /rawhtml >}}
{{< /tab >}}
{{< tab "Transcript" >}}
{{< rawhtml >}}
  <cite>Gene Liverman:</cite>
  <time>0:05</time>
  <p>Hello everyone and welcome to the Volunteer Technologist podcast. Here we take a look at the different ways that people who are technically inclined volunteer outside of their primary job. Today I&#39;m joined by James Sundquist, who does landscaping as his day job but uses his tech skills in a variety of different ways. How are you doing, James? Hey, I&#39;m doing well. It&#39;s very good to meet you and be on the show. Nice to meet you as well, and thank you for taking the time and for reaching out and letting me know some of the things that you&#39;re doing. </p>
  <cite>James Sundquist:</cite>
  <time>0:35</time>
  <p>Yeah, absolutely. I heard about your show through the Jupiter Broadcasting plug. Oh, nice I was very excited about it. </p>
  <cite>Gene Liverman:</cite>
  <time>0:43</time>
  <p>Thank you very much. Yeah, I love their podcast and I was very thankful that they were willing to mention mine on there, so that&#39;s a very good thing. </p>
  <cite>James Sundquist:</cite>
  <time>0:52</time>
  <p>Yeah, absolutely. </p>
  <cite>Gene Liverman:</cite>
  <time>0:53</time>
  <p>So in the email that you sent me, you had mentioned doing a few different things, including working with the Nextc loud project and doing a variety of different things for them and doing some work in some hacker spaces and even some stuff related to theater, and so I thought maybe we would just kind of talk through a couple of those things. But since a lot of the audience may not be as aware of what Nextc loud is as much as they might know what theater is, I thought maybe you could start off by just giving a brief introduction to maybe what you do for Nextc loud and then what it actually is. </p>
  <cite>James Sundquist:</cite>
  <time>1:27</time>
  <p>Next c loud is a company and they develop the premier open source file sharing platform online. It&#39;s called Next c loud and it actually forked from a previous project called Open Cloud and offer that to the community, and where they make money is in paid commercial support for clients. Very cool, yeah. So there are a number of enthusiasts who want to use tools like Nextc loud. It&#39;s a self-hosted sort of Drop box or Google Drive, and the project has expanded and expanded to become more of a Google Suite alternative at this point for not just file sharing but associated things like video calls and calendars and tasks and beyond. That&#39;s very cool, yeah. And so the issue comes in. Well, what if you want to use Next cloud yourself and you&#39;re not a company? So you might want to self-host it at home on something like a Raspberry Pi, and for some people that process might become very daunting. So some of the people in the community decided to start working on a project specifically Ignacio, a gentleman who is developing Next c loud Pi which is sort of a platform for Next c loud which includes a Debian stack, and then on top of Debian you have a MariaDB and Apache web server and you basically have this simple to maintain variation of Nextcl oud that&#39;s all in one, an image you can just install on your machine, and now it&#39;s become also available as virtual machine, docker container and is all community maintained for people who want to run Next c loud at home. </p>
  <cite>Gene Liverman:</cite>
  <time>3:13</time>
  <p>I actually hadn&#39;t heard about Nextc loud Pi. I&#39;m actually in the process of taking a kind of I guess you&#39;d call it a trial installation of Next c loud that I had and moving it to something slightly more permanent, and I think I might check that one out. </p>
  <cite>James Sundquist:</cite>
  <time>3:30</time>
  <p>Yeah, it&#39;s a fantastic project. It&#39;s really great, and it&#39;s now switched lead developers to Tobias, who is in Germany and along with Next c loud themselves and still just a volunteer developer, but helms the project along with other volunteers that. You can find out more information at NextcloudPi. com. There&#39;s also docs. NextcloudPi. com and the Next c loud Pi GitHub. </p>
  <cite>Gene Liverman:</cite>
  <time>3:57</time>
  <p>Very cool. I gathered from our chat that you do something with the documentation for Next c loud. What do you do with them there? </p>
  <cite>James Sundquist:</cite>
  <time>4:04</time>
  <p>Oh, so Next c loud Pi was hosting all of their documentation on a WordPress website at docs. NextcloudPi. com, and the whole process of editing and maintaining the documentation was sort of writing on one person Ignacio at that time, who also was maintaining the website. And so, as time went on and trying to figure out a better solution for getting collaboration on documentation, I was looking into this forum platform called Discourse, which is fully open source and it happens to be the software that Nextc loud uses at help. Nextcloud. com. But also my hackerspace at the time, Noisebridge, was also using Discourse, so I became an admin for our Discourse instance at Noisebridge so I could understand how it worked. And I also joined the meta. discourse. org, which is sort of a dog food presentation of discourse, where everything developed in discourse is actually happening on the meta site and you can contact developers directly. So I started contacting them, giving feedback as I&#39;m trying to figure out how different features work, with the intention of trying to understand discourse, because maybe there was something there we could use for the Nextcloud Pi project in addition to the hacker space that we didn&#39;t already know about. It&#39;s an amazing platform. </p>
  <cite>Gene Liverman:</cite>
  <time>5:31</time>
  <p>That sounds pretty cool. </p>
  <cite>James Sundquist:</cite>
  <time>5:32</time>
  <p>Yeah, so what we ended up doing was, over a couple of years, communicating with the discourse team, sort of finding different features or bugs that weren&#39;t working as intended, but would allow us eventually to basically create a sub forum for Nextcloud Pi within help. nextcloud. com, and people within this group are privately writing draft documentation which is then being published for a static website, docs. nextcloudpi. com, instead of WordPress, and all of the pages you&#39;re reading are actually topics on a forum, but you&#39;re still seeing them in the way you saw them previously on WordPress, but now you don&#39;t have to be a part of the WordPress anymore. Our pool of contributors actually comes from the forum itself. </p>
  <cite>Gene Liverman:</cite>
  <time>6:25</time>
  <p>How are you getting the static content from discourse into whatever you use in to generate your static website? </p>
  <cite>James Sundquist:</cite>
  <time>6:32</time>
  <p>It&#39;s based on categories and tags. Discourse supports categories and tags. You can also tag by groups. You can have associated tags and we were able, thankfully, to have that tag grouping system match what Ignacio had already created for the WordPress documentation. So the basic layout is still the same, but now it all lives within discourse as tags and topics. </p>
  <cite>Gene Liverman:</cite>
  <time>7:00</time>
  <p>That&#39;s really cool. Are the docs pages actually showing discourse itself or is it pulling the data from discourse? It&#39;s showing discourse itself oh nice. </p>
  <cite>James Sundquist:</cite>
  <time>7:11</time>
  <p>Very nice. That&#39;s really cool. And then by joining the discourse, and especially if you join the Nextcloud Pi group, you get access to draft documentation, which might be new documentation or proposed rewrites, and it&#39;s a way that we&#39;re able to have conversations freely with any volunteer who wants to join but also keep that information away from people who just want to read the finalized documentation. </p>
  <cite>Gene Liverman:</cite>
  <time>7:34</time>
  <p>That&#39;s really cool. Yeah, that&#39;s a really neat adaptation of forum software to be able to actually turn it into a documentation site. That sounds like it would be quite useful. </p>
  <cite>James Sundquist:</cite>
  <time>7:45</time>
  <p>Yeah, it just took time. It took a couple of years of being involved in the Nextcloud forum and it took a few years of being involved with the meta Discourse forum and just basically testing things on your own instance of the software, and then you&#39;re reporting bugs or proposing ideas, along with this other group of people from all over the world who are engaged in these same conversations. </p>
  <cite>Gene Liverman:</cite>
  <time>8:14</time>
  <p>So what made you want to put in so much time and effort to work on the docs project for Nextcloud? </p>
  <cite>James Sundquist:</cite>
  <time>8:22</time>
  <p>I just get really excited about technology and I always am curious about what it can do, and sometimes I find projects that I just feel really amazed by the potential, and two of those projects would be Nextcloud and Discourse, and I would just amaze at how fantastic Discourse is like right now. Gradually, they&#39;ve been developing a chat platform which it&#39;s like hmm, I don&#39;t know what I think about that, but it&#39;s exciting because that chat platform is also developing Matrix support for Federation and it also now includes activity pub support for topics. This is all optional, but there&#39;s all these different things being developed optionally and it just takes time, but they&#39;re just truly amazing and the level of customization is incredible. </p>
  <cite>Gene Liverman:</cite>
  <time>9:16</time>
  <p>I&#39;m a big fan of Mastodon and I&#39;ve heard about the activity pub support that&#39;s being done in Discourse and I&#39;m really interested to see how that evolves every time to see where the real benefit comes in If it comes to being able to show or share information well through other activity pub like social media platforms, or if it&#39;s just more beneficial for maybe sharing between two Discourse instances. Or maybe it&#39;s all of the above and only time will tell on that. But it&#39;s been kind of intriguing to hear where that&#39;s going, because real time chat and social media type posting and a discussion forum aren&#39;t usually things you think about cramming together. </p>
  <cite>James Sundquist:</cite>
  <time>9:57</time>
  <p>Yeah, but so the great thing about doing this is it&#39;s making it easier for people to collaborate and to work together, but it&#39;s also proven to be tooling that bridges out beyond even just being documentation for Next c loud Pi and a help forum. We actually are also able to track with RSS discussion and support questions, documentation questions into our chat. The volunteer chat is Telegram and because people are in Telegram rather than forcing them to move, we bridged Telegram into Matrix because when Tobias took over, he was very interested in Matrix, so now anyone in Matrix can seamlessly communicate with anyone in Telegram and they&#39;re able to have discussions about topics coming from the forum, and that allows us to keep all of our support questions for Next c loud Pi in the forum itself. But you can still see all of that from the chats if you want. And it&#39;s really cool, and I think the other thing that&#39;s really great about this system is it&#39;s trying to find ways to alleviate the amount of dependence on a specific person or a specific platform. So you don&#39;t have to have the WordPress account, forum account and chat account. You could just have the forum. But people can kind of live where they&#39;re comfortable and I&#39;m really appreciative of that, because for me personally, I don&#39;t really want to be in the chat actually, and I&#39;m not. I just want to focus on the documentation with the time I have available. </p>
  <cite>Gene Liverman:</cite>
  <time>11:39</time>
  <p>Yeah, committing to some of those chat, especially a support chat room, can be daunting and it can be very, very time consuming. I&#39;m very thankful for the people who do it, but I can also see why that&#39;s nice to not have to get in on that but still be able to participate. </p>
  <cite>James Sundquist:</cite>
  <time>11:56</time>
  <p>Yeah, it&#39;s fantastic and it was really exciting this last year. So we got the opportunity to fly out to Berlin and present as part of the Next c loud conference and talk about the project of Next c loud Pi, and a little bit about that project is that at this point it&#39;s a very popular project that&#39;s used I can&#39;t remember how many downloads it is anymore, but it&#39;s incredibly robust projects that&#39;s used by also Nextcloud employees for just running Nextcloud instances at home for fun with friends or family. Getting to learn that the company members themselves were using our project and interested in our project was really exciting. I just want to say how grateful I am for the work of Nacho and Tobias to have made this platform, which makes it easy to do things like take snapshots of your system and to restore backups if anything goes wrong. This is using multiple tools like ButterFS, r-sync, and it&#39;s an ongoing process of refinement and basically, like a wizard, like hand-holding. It&#39;s something that brings a lot of magic to the Nextcloud platform. </p>
  <cite>Gene Liverman:</cite>
  <time>13:24</time>
  <p>Yeah, you&#39;ve gotten me pretty excited about it, especially touching on the backups part, because that&#39;s been the one Achilles heel with the way I had it set up the first time is I didn&#39;t have a way that I felt confident in backups of it. It&#39;s like if I&#39;m pulling all my stuff in from a decade on plus on Dropbox and Google Drive and other places to get off of those, I don&#39;t sure want to make sure I&#39;ve got my backups in order, because that&#39;s decades worth of information and I don&#39;t want to lose it because I was an idiot and didn&#39;t have battery backups or something got corrupted, because my single server decided to crap out, because I&#39;m not running in a data center. </p>
  <cite>James Sundquist:</cite>
  <time>14:09</time>
  <p>Yeah, it&#39;s interesting the way that the project works. If you&#39;re running Nextcloud Pi at home, you set it up and then, as part of installation, you have access to an additional web UI or command line interface. You can connect to your box over SSH or over web UI outside of Nextcloud. If, say, Nextcloud is not working, you can still go to the optional web UI or command line interface and use that to problem solve and share logs or to figure out what&#39;s not working. Yeah, you can do things like deploy Let&#39;s Encrypt certificates and try to take as many pain points as possible out of maintaining this box. One of the really great things about running this project, which is geared towards non-technical users, is that we maintain a very conservative release cycle in relation to Nextcloud. You can always update at any time, but you have the option to do auto updates. Auto updates include Nextcloud. It includes the system supporting Nextcloud, which is Debian, and MariaDB  and PHP. That way, if you don&#39;t touch anything, volunteers will test all these different aspects of the project. That&#39;s what we do with our time on GitHub. We test the new releases, we&#39;re looking for bugs, breaks, before the updates are given out and encouraged to general Nextcloud Pi users. </p>
  <cite>Gene Liverman:</cite>
  <time>15:44</time>
  <p>The volunteers are basically performing QA on the entire stack before it gets released out to us radio or home users. </p>
  <cite>James Sundquist:</cite>
  <time>15:52</time>
  <p>Nextcloud is doing as well, right. </p>
  <cite>Gene Liverman:</cite>
  <time>15:55</time>
  <p>Right, but I meant your QA in the stack as a whole, like the particular bundle that makes up Nextcloud Pi. </p>
  <cite>James Sundquist:</cite>
  <time>16:01</time>
  <p>Exactly, Nextcloud 27 was just released in the last two weeks, I believe, but we just released Nextcloud 26. Okay, anyone&#39;s welcome to move to any version of the software, but if they get too far ahead, all they have to do is go back to the auto update process and wait until we catch up to them. </p>
  <cite>Gene Liverman:</cite>
  <time>16:24</time>
  <p>That&#39;s cool. It&#39;s nice to have flexibility with guardrails or with with a safety net. I guess would be a better way of putting is. </p>
  <cite>James Sundquist:</cite>
  <time>16:30</time>
  <p>Flexibility with the safety net is really interesting things have cropped up, especially support for 32-bit devices, which was actually removed and then reinstated, and Also things like changes in PHP and these kinds of major pain point changes, or coming up now would be the move To the new version of Debian that just came out. Look warm. So things like this Getting gradually worked on and iterated so that you, the home user, don&#39;t have to worry about it. </p>
  <cite>Gene Liverman:</cite>
  <time>17:02</time>
  <p>That&#39;s very nice. So you mentioned also doing some work in a hacker space. I think you said you were doing some teaching there. What have? First off, what exactly is your hacker space kind of focused on, and then what kind of things were you doing? </p>
  <cite>James Sundquist:</cite>
  <time>17:16</time>
  <p>there. So my original intention with the Next cloud Pi would actually was to use it at this hacker space noise bridge and I did for three years and it was running quietly being used and Basically, people are using it to share files which if they weren&#39;t access over a period of, I think, 90 days they would just be deleted and the space would be freed up is like temporary storage people could use in the space Very cool, and then after three years no one wanted to help maintain it and Eventually someone wrote over it and I thought that&#39;s okay, three years is still good. And it comes back to the same idea that I always have, which is I never want a project to live and die on myself, and it&#39;s that&#39;s really difficult thing to Learn how to do. It&#39;s really hard to give a project to someone else that they can also maintain. So that&#39;s a big inspiration of for me and Wanting to help people make that process possible in technology. </p>
  <cite>Gene Liverman:</cite>
  <time>18:23</time>
  <p>That&#39;s very cool. Did you say you were doing some teaching at the hacker space? </p>
  <cite>James Sundquist:</cite>
  <time>18:26</time>
  <p>Yeah, I did so. I heard the space needed Fundraising support so when I first joined around ten years ago, I hosted a series of fundraisers on no budget and we set up recurring Donations for the first time to the space for like think to ten dollars a month. We called it the savior fund. It was a huge success and Got always people to like make vegan food and we got all these different artists to perform and have this big bonanza blowout and groups like laughing squid were really helpful and it was Fantastically fun. And my interest in open source just led me to want to work with others and talking about Linux Administration and so we did a kind of an ongoing working group is what we called it, or people would show up. I think it was once a week and then it became Twice a month and we would go over like bash scripting and all these different kinds of things together and At that time, yeah, there was assembly at that time also being taught. It&#39;s really fun, very cool. </p>
  <cite>Gene Liverman:</cite>
  <time>19:37</time>
  <p>I guess my last question for you is how does the theater company fit into your technical volunteering or your use of All the same products that your products and projects you were talking about, right well? </p>
  <cite>James Sundquist:</cite>
  <time>19:52</time>
  <p>I. I have a theater degree and creative writing degree from college and Coming out of college, I worked for the San Francisco Mime Troop as a sound designer and I&#39;ve been a touring drummer and things. But I&#39;ve never been totally sure of how to secure funding and put together projects with With others that fully follow my own vision. So by being involved in DIY spaces, hacker spaces, it let me learn how to use basically open hardware things like laser cutters. Using Inkscape, which is a free vector graphics tool, and having some work with like the Adobe Creative Suite, I was able to adapt that work to using free SVG tooling and to run things like laser cutters to make my own shadow puppets, to make my own props, and I created my own shows and then toured those shows yeah, expensively, until COVID locked everything down. And it&#39;s been yeah, it&#39;s been great to have those skills and the tooling is only improving with software and hardware. These days. You have yeah, you have tools like all these really excellent video editing tools now and KDN Plus, and then working with raw in DaVinci Resolve and on the lighting side of things, I do lighting design for shows and for performances and there&#39;s a free tool called QL Plus. It&#39;s lighting design software. It&#39;s totally open source and you can do crazy things like control your LED lighting from a MIDI joystick, and that&#39;s a really fun project that is used professionally by theaters. </p>
  <cite>Gene Liverman:</cite>
  <time>21:46</time>
  <p>Nice. I really appreciate you taking the time to walk through what you&#39;re doing, and I&#39;m truly fascinated by the Next c loud Pi Project. I was already interested in Nextc loud before we chatted, so this is both a timely conversation and one that&#39;s very interesting. </p>
  <cite>James Sundquist:</cite>
  <time>22:01</time>
  <p>Yeah, I just. I get really excited about open source projects and I think most people don&#39;t even know what we&#39;re talking about. But when I learn about something, I always wonder how it&#39;s applicable, Like if there&#39;s a tool, for example, to help us organize like maybe we&#39;re gonna organize events once a month and I always wonder if there&#39;s a open source version of that that&#39;s freely available or accessible to more people. And once I find things, I start testing them, digging into them, and really that&#39;s, in my opinion, that&#39;s how you get involved in volunteer work and you just put yourself out there and once you find something that you can sync your teeth into, you just keep exploring it and it&#39;s kind of this endless chasm, but it can be rewarding. And I never imagined, volunteering for Nextcloud, for example that I would be speaking at a conference in Europe this last year. I&#39;d never even left the country before, so it&#39;s just amazing. </p>
  <cite>Gene Liverman:</cite>
  <time>23:06</time>
  <p>That&#39;s a pretty amazing opportunity, yeah, and it&#39;s fun either way. It&#39;s a fun way to spend free time, especially if you feel bored otherwise and yeah, thank you very much, and I wanted to give you a minute to share anything additional that you wanted to and also maybe mention how people could reach out to you if they had questions or comments. </p>
  <cite>James Sundquist:</cite>
  <time>23:30</time>
  <p>My biggest recommendation, if you&#39;re interested in open source projects, is to start to involve yourself in them and I think one way to do that is definitely you&#39;re listening to this podcast, and that is a fantastic step and find communities of people who are also interested in that, which could be like a Matrix Chat or Discord Chat, and then you start looking into these projects Like do they have community chats? Do they have documentation? Do they need help with doing things? And maybe there&#39;s code you contribute or maybe you can help with things like translations or answering support questions and in doing that you might make mistakes everyone does but also, if you continue to learn and try to actually be helpful to the project or even to the developers like maybe you can help with testing things you&#39;ll grow and learn from there, and if anyone has questions, you&#39;re welcome to email me. It&#39;s S-U-N-J-A-M at james dot network. </p>
  <cite>Gene Liverman:</cite>
  <time>24:29</time>
  <p>Very cool and I&#39;ll be sharing and include links to the things we talked about and ways to reach out to you in the notes for this show also, so they should show up in the podcast apps and on my website and anywhere else you can find info about the podcast Great, thank you so much. Before we go, I&#39;d like to take a moment to thank Kyran from  the Mere Mortals podcast for boosting in support for several of my episodes via the Fountain podcast app. It is very much appreciated. This is a value for value podcast, which means I rely on listeners like yourself contributing back to fund it. As such, I&#39;ll never charge you to listen, but producing and hosting it does cost money. If, like Kyran, you got value from this episode, then I hope you&#39;ll consider supporting its ongoing production by sending a boost, like he did, or via the support the show link in the show notes. You can also find the show notes, transcripts, and links to things we talked about in today&#39;s episode at volunteertechnologist. com. If you would like to come on the show or know someone I should reach out to about being on the show, please send me a message via one of the links at the bottom of the show notes. Thanks for listening. </p>

{{< /rawhtml >}}
{{< /tab >}}
{{< /tabs >}}
