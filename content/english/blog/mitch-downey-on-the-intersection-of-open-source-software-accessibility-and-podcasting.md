---
aliases:
- /episode/9
author: Gene Liverman
categories:
- Podcast Episode
date: Sun, 01 Oct 2023 09:00:00 +0000
description: Ever wondered about the mechanics of making an app accessible to all
  users? Journey with us as we explore this important topic with Mitch Downey , the
  co-founder of the Podverse podcast app. He shares his commitment to enhancing the
  app's accessibility after consultation with an expert. We plunge into the world
  of open source platforms, underscoring its vital role in fostering inclusion, especially
  for the visually impaired, and discuss the significant role color contrast plays
  in designing an accessible app.
episode_artwork: https://assets.podhome.fm/d4f02a91-cead-4ab3-6c02-08dc1c0c24e3/6384160951973891665819ad.jpg
guid: Buzzsprout-13650585
image: images/episode-header.png
mp3: https://op3.dev/e/serve.podhome.fm/episode/d4f02a91-cead-4ab3-6c02-08dc1c0c24e3/6384160952126227817b4cc672-af63-455c-aa62-e92b7361ab7ev1.mp3
podverse_podcast_id: Kd9Z2u-92d
summary: Ever wondered about the mechanics of making an app accessible to all users?
  Journey with us as we explore this important topic with Mitch Downey , the co-founder
  of the Podverse podcast app. He shares his commitment to enhancing the app's accessibility
  after consultation with an expert. We plunge into the world of open source platforms,
  underscoring its vital role in fostering inclusion, especially for the visually
  impaired, and discuss the significant role color contrast plays in designing an
  accessible app.
title: Mitch Downey on the Intersection of Open Source Software, Accessibility, and
  Podcasting
transcript_vtt: ''

---
{{< episode-player >}}
{{< listen-apple >}}{{< listen-overcast >}}{{< listen-spotify >}}{{< listen-google >}}{{< listen-rss >}}
{{< tabs >}}
{{< tab "Show Notes" >}}
{{< rawhtml >}}
Ever wondered about the mechanics of making an app accessible to all users? Journey with us as we explore this important topic with <a href="https://podcastindex.social/@mitch" target="_blank">Mitch Downey</a>, the co-founder of the <a href="https://podverse.fm/" target="_blank">Podverse</a> podcast app. He shares his commitment to enhancing the app's accessibility after consultation with an expert. We plunge into the world of open source platforms, underscoring its vital role in fostering inclusion, especially for the visually impaired, and discuss the significant role color contrast plays in designing an accessible app.<br />Switching gears, we delve into the innovative 'value for value' model and the <a href="https://github.com/podverse/podverse-ops/tree/master/bounties" target="_blank">bounties program of Podverse</a>. Discover how their premium memberships keep the wheels turning and how they've managed to capture interest without extensive advertisement. Mitch expounds on their cost-effective approach that outshines traditional contractors and corporate environments. He acknowledges key figures like <a href="https://www.jupiterbroadcasting.com/hosts/chris/" target="_blank">Chris Fisher</a> and the <a href="https://www.jupiterbroadcasting.com" target="_blank">Jupiter Broadcasting Network</a> for their support. We also discuss the various ways dedicated listeners can bolster the show's growth and offer insights on how to actively participate in the project. Tune in and take a deep dive into the fascinating intersection of open source software, accessibility, and podcasting!<br /><strong>Links:</strong><br /><ul><li>Contact Mitch on mastodon: <a href="https://podcastindex.social/@mitch" target="_blank">podcastindex.social/@mitch</a></li><li>Contact the Podverse team: <a href="https://podverse.fm/contact" target="_blank">podverse.fm/contact</a></li><li>Podverse bounties: <a href="https://github.com/podverse/podverse-ops/tree/master/bounties" target="_blank">github.com/podverse/podverse-ops/tree/master/bounties</a></li><li>Podverse source code: <a href="https://github.com/podverse" target="_blank">github.com/podverse</a></li><li>Podverse free vs premium: <a href="https://podverse.fm/membership" target="_blank">podverse.fm/membership</a>&nbsp;</li><li><a href="https://podverse.fm/podcast/Kd9Z2u-92d" target="_blank">Volunteer Technologist on Podverse</a></li><li>Jupiter Broadcasting: <a href="https://www.jupiterbroadcasting.com/" target="_blank">jupiterbroadcasting.com</a></li></ul><br /> <p>Support the show via <a href="https://www.buymeacoffee.com/genebean" target="_blank">Buy Me a Coffee</a><br />Send a boost with a new podcast app such as <a href="https://fountain.fm/genebean?code=5cb3b5f06a" target="_blank">Fountain</a> or via <a href="https://conshax.app/support/volunteertechnologist" target="_blank">conshax.app/support/volunteertechnologist</a><br />See all the ways to contribute, and what producing this podcast costs, at <a href="https://www.volunteertechnologist.com/contribute/" target="_blank">volunteertechnologist.com/contribute/</a><br />You can find me on Mastodon at <a href="https://podcastindex.social/@volunteertechnologist" target="_blank">podcastindex.social/@volunteertechnologist</a> You can also reach me via <a href="https://www.volunteertechnologist.com/contact/" target="_blank">volunteertechnologist.com/contact/</a><br />Visit <a href="https://www.volunteertechnologist.com/" target="_blank">volunteertechnologist.com</a> for show notes, transcripts, or more information.</p>
{{< /rawhtml >}}
{{< /tab >}}
{{< tab "Transcript" >}}
{{< rawhtml >}}
  <cite>Gene Liverman:</cite>
  <time>0:05</time>
  <p>Hello everyone and welcome to the Volunteer Technologist podcast. Here we take a look at the different ways that people who are technically inclined volunteer outside of their primary job. Today I&#39;m joined by Mitch Downey, the co-founder of the Podverse Podcast app. How are you doing, Mitch? </p>
  <cite>Mitch Downey:</cite>
  <time>0:20</time>
  <p>I&#39;m doing great. How are? </p>
  <cite>Gene Liverman:</cite>
  <time>0:22</time>
  <p>you doing, doing wonderful. </p>
  <cite>Mitch Downey:</cite>
  <time>0:24</time>
  <p>Thanks for having me today. </p>
  <cite>Gene Liverman:</cite>
  <time>0:25</time>
  <p>You&#39;re very welcome. I appreciate you taking the time. We were chatting on Mastodon a little bit and I gathered that you&#39;ve done quite a bit of work around accessibility in the Podverse app. I was interested to maybe hear a little more about that and then just some of how you contribute to open source and spend your time outside of work in general. </p>
  <cite>Mitch Downey:</cite>
  <time>0:45</time>
  <p>Sure, sounds good. So for accessibility our apps didn&#39;t begin with accessibility, because I&#39;ve been working on Podverse for almost nine years now. When I began I didn&#39;t know how to program. This has been my primary exercise for learning how to code. Over time, as I&#39;ve wanted to offer a more complete product, it came to my attention. We had a couple people email us saying, hey, I was so excited to try Podverse I heard about it through Podcasting 2.0, and I love what you&#39;re doing with open source. But I opened the app and I couldn&#39;t do anything. It turned out the mobile app just wasn&#39;t compatible at all with accessibility. You couldn&#39;t focus on anything when the screen started. Oh, wow, yeah, I didn&#39;t really know that I hadn&#39;t done work in that respect. It was kind of heartbreaking because it&#39;s like well, there&#39;s these people who really want to use the app and it&#39;s simply not accessible because of my own incompetence in putting it together. Beyond that, it&#39;s important for me personally. Before I got into programming, I worked in special education with people of variety of disabilities and it just felt so wrong to me to be alienating so many users based on not offering a finished product that can it&#39;s truly accessible for everybody. </p>
  <cite>Gene Liverman:</cite>
  <time>2:12</time>
  <p>Which more people approached it that way. </p>
  <cite>Mitch Downey:</cite>
  <time>2:15</time>
  <p>Yeah Well, it is a lot of work. Now, if you&#39;re really smart and competent, you can create accessibility as you go and it&#39;s more manageable. But it is a lot to think about. With the mobile app in particular. It was last year especially. I basically dedicated three months to going through the mobile app. I did other things on top of this, but it was an ongoing project where I had to go through every single screen in the mobile app and turn on a screen reader and navigate from element to element. Not look at my phone. Just try to understand the experience from somebody who isn&#39;t able to see the phone. It was a very tedious process but I got the hang of it after a while. Now the app is. I&#39;ve been told it has good accessibility, but it doesn&#39;t have great accessibility. Some people have said it&#39;s great, but we recently had an audit done by a really good accessibility expert who just I don&#39;t know, maybe it was a post that you had on Mastodon, but somehow this guy reached out to us through Mastodon and said he loves that we&#39;re open source and he&#39;s been trying to use it and it&#39;s okay, but it&#39;s just not totally where he wants it to be. So he volunteered his time to. We talked for about an hour and a half and I have a list currently of about 30, mostly micro improvements, but they&#39;ll add up a lot as I go through and add them. So that is tentatively. I expect to have it done by the before the end of the year. It&#39;s one of my top priorities it&#39;s probably like in the top three priorities we have right now to go through that audit and really complete the picture for accessibility. </p>
  <cite>Gene Liverman:</cite>
  <time>4:13</time>
  <p>That&#39;s really amazing. That&#39;s a. It&#39;s one of the things that fascinates me with open source is how a random conversation can result in somebody else volunteering some time, and then you putting in some work as one of the primary code contributors, and then you know, in just a matter of months a entire segment of our population can have a much better experience using a podcasting app. That&#39;s just fascinating to me. </p>
  <cite>Mitch Downey:</cite>
  <time>4:38</time>
  <p>Yeah, absolutely, and podcasting in particular is a largely audio based medium. You know videos are also can be podcasts, but you know it makes sense that people it&#39;s a preferred medium for people who may have visual disabilities. </p>
  <cite>Gene Liverman:</cite>
  <time>4:53</time>
  <p>Yeah, totally makes sense. </p>
  <cite>Mitch Downey:</cite>
  <time>4:55</time>
  <p>Yeah, so for us to not have adequate support for that was unacceptable. And yeah, I spent a lot of time working on that and we&#39;ll be spending some more time on it. Like I said, it&#39;s a very. You have to be very diligent and make sure there are no loose ends, no way you can get lost in the UI. </p>
  <cite>Gene Liverman:</cite>
  <time>5:14</time>
  <p>I have to imagine that that work benefits more than just the people who need the accessibility features, though that it has ways of bringing to light things that you might not have noticed otherwise, that other people would benefit from too. </p>
  <cite>Mitch Downey:</cite>
  <time>5:27</time>
  <p>It does Well, at least from a programming perspective. It requires you to think in terms of how everything is grouped together in the UI. The screen readers tend to, on mobile, just go from one element to the next. Then there&#39;s some shortcuts you can skip to groupings of elements. Yeah, you definitely have to think more deeply about how you&#39;ve laid out your features, because some assumptions you can make visually don&#39;t necessarily hold up. Yeah, when you&#39;re using a screen reader, yeah, that totally makes sense. </p>
  <cite>Gene Liverman:</cite>
  <time>5:59</time>
  <p>Just out  curiosity, did that audit also cover things like the way colors are perceived by people who are color-blind and stuff like that. </p>
  <cite>Mitch Downey:</cite>
  <time>6:09</time>
  <p>It did. However, we haven&#39;t received many changes requested for color contrast. That is something I think I&#39;ve been pretty mindful of with color contrast and icon contrast, like a cardinal mistake that I was making early on was sometimes making an icon. That is, you have an active and an inactive state and the active state would have a different color than the inactive state. And okay, that can work for a lot of people, but some people won&#39;t be able to differentiate the color of it, and so you want to add an extra indicator, like a line through it or something, to show the different focus states. </p>
  <cite>Gene Liverman:</cite>
  <time>6:51</time>
  <p>Something so that they don&#39;t have to rely on the colors to know what&#39;s going on. </p>
  <cite>Mitch Downey:</cite>
  <time>6:56</time>
  <p>Yeah, exactly. </p>
  <cite>Gene Liverman:</cite>
  <time>6:57</time>
  <p>That totally makes sense. Does the accessibility work you&#39;re doing extend to the web version, or is it just primarily focused on the mobile apps, or how does that fit in? </p>
  <cite>Mitch Downey:</cite>
  <time>7:06</time>
  <p>Yes, we&#39;ve also done accessibility work on the website. It&#39;s similar process. It&#39;s more difficult with mobile apps because you have to explicitly put IDs on all of these elements and make them focusable, whereas HTML for websites has some kind of smart defaults. I guess that can kind of mask whether you&#39;re trying to make it screen reader accessible or not. You can kind of get away with a little bit more, but we have updated the website. There are all kinds of different HTML elements that are designed to help you navigate, say between the navigation menu or the footer, or into the content or dive into a list. If you&#39;re using the tags correctly, it can be a nice experience. That didn&#39;t take nearly as long as the mobile app and there&#39;s probably room for improvement there, but we have generally received good feedback on the web accessibility. That&#39;s awesome. </p>
  <cite>Gene Liverman:</cite>
  <time>8:11</time>
  <p>I&#39;m glad to hear that. That&#39;s really an exciting thing to hear. The one thing I gathered from the mastodon conversation that kicked all of this off was that the number of podcast apps that actually take the time to do the work that you&#39;ve been doing is in the single digits. There&#39;s the Apple Podcast app and one other app, and Podverse is pretty much it. I think that&#39;s what it said. </p>
  <cite>Mitch Downey:</cite>
  <time>8:39</time>
  <p>Yeah, it&#39;s pretty crazy to hear that, but I can believe it. I&#39;m sure there&#39;s more on the list that just weren&#39;t people weren&#39;t aware of, but typically accessibility is done more by large corporations which have legal obligations to provide accessibility. Since we&#39;re a free and open source project and our resources are very thin and we have day jobs, it&#39;s pretty typical for programmers to skip that step because it is a small percentage-wise of your audience. But everybody is equally important and if you can do it, I think you should try. I understand why people often cut that corner because, like I said, it took me a few months. I had to go through on iOS. I had to go through on Android, I had to navigate to every single screen. It is quite a process and if people are limited on time, limited on money resources, I can understand them skipping that step. </p>
  <cite>Gene Liverman:</cite>
  <time>9:43</time>
  <p>Yeah, absolutely so, beyond the accessibility work that you&#39;ve done in Podverse. As you mentioned, it&#39;s an open source app. What kind of time commitments does that require from you, being the co-founder of a podcast app that I&#39;ve gathered is pretty widely used? </p>
  <cite>Mitch Downey:</cite>
  <time>10:00</time>
  <p>Well, it has taken a lot of time. It&#39;s taken a lot of my 30s, to be honest, to bring it to where it is today. I have a day job that has paid the bills for the past nine years and I&#39;ve been working on Podverse along the way the whole time. It&#39;s a large time commitment but it brings so much satisfaction to me to work on open source in a way that my day job has been great to me, not a knock against it, just the potential of open source, the ability to basically create something of value and give it away for free and make it available to everyone across the world. It has fascinated me ever since I was a kid in the 90s. Downloading open source software. It&#39;s like free software Wow, this is incredible. And it&#39;s more than just free software. It&#39;s that it&#39;s transparent software and you know how it works and you can modify it to how you want. So, yeah, it has been a massive time commitment and it has honestly been a challenge to keep up with it. I&#39;ve been pretty relentless with my. You know I basically worked on it 40 hours a week for many years and, honestly, lately for the past few months I was a little burnt out from working on it so much. </p>
  <cite>Gene Liverman:</cite>
  <time>11:27</time>
  <p>I mean, you&#39;ve effectively been working two jobs for many years, so I can understand how that would happen. Yeah it happens with all kinds of volunteering that you just give more than you&#39;ve got to give and sometimes you have to step back a little bit. </p>
  <cite>Mitch Downey:</cite>
  <time>11:39</time>
  <p>Yeah, I always thought, you know, burn out, not me, I&#39;ll never get burnt out, and then it&#39;s like I can barely. Very so. That was as exciting as, as the app has been more downloaded, we have about 20,000 installs, I believe, across iOS and Android something like 7,000 active daily users. Oh, wow, and that&#39;s been exciting. As things get, you know, things are picking up and we get a lot of very positive feedback, people who like the UX we provide and the and and our principles. You know we have. We&#39;re all open source. We don&#39;t add advertisements. We&#39;re a value for value company. We&#39;ll give people free, premium subscriptions by request. But as it has gotten more popular, the demands put on us as a team have gone up, like in a linear way. We get a lot more emails. We get a lot of more people requesting features or submitting bug reports, and that&#39;s that&#39;s kind of where the I think the burnout started to set in. For me was Trying to figure out a way to manage this like for a long time I was just I could focus almost a hundred percent on the programming and and I had the bandwidth to do it. But as we also pride ourselves on being responsive to our users, we like we try to reply to everything one within one or two business days and you know, if they DM me on on Mastodon or Twitter, try even faster. But the good news is that you know we&#39;ve been putting effort into Strategizing and planning and figuring out how to make this, how to maintain this, better. So we have a bounties program, for example, where we are paying people to work on some of our most requested features. You know I have like nine different contact options across Macedon, twitter, discord matrix, like it&#39;s a lot to maintain. </p>
  <cite>Gene Liverman:</cite>
  <time>13:40</time>
  <p>Take a good bit of time just to get through all the different ways people can get in contact with you. It sounds like. </p>
  <cite>Mitch Downey:</cite>
  <time>13:45</time>
  <p>Yes, yes, and so I&#39;ve seen like people complain about other open source projects, like the maintainers seem cold or unresponsive, and the more I&#39;m in the weeds of it, the more I&#39;m sympathetic to like. Well, this is just an unmanageable burdin for a lot of people. Yeah who aren&#39;t. This isn&#39;t their primary job. </p>
  <cite>Gene Liverman:</cite>
  <time>14:08</time>
  <p>And, let&#39;s be honest, a lot of programmers are not people. People to start with. They&#39;re the leave me alone and let me do my coding, and Somebody else can handle the customer service side of things, and so sometimes they can be really good at writing whatever software it is, and not so great at interacting with the humans that use it. </p>
  <cite>Mitch Downey:</cite>
  <time>14:28</time>
  <p>Yeah, absolutely. Just because you maybe a great programmer doesn&#39;t necessarily mean you have all the people skills to right right. Yeah, and so much you have to. You have to do all of the different aspects of it. So many open source libraries are maintained by one person and Used by hundreds of apps you know and services that depend on it. It&#39;s kind of incredible how anything really gets done and anything works. </p>
  <cite>Gene Liverman:</cite>
  <time>14:55</time>
  <p>Yeah, no kidding. You mentioned your bounties program and obviously we&#39;ve been talking about all the volunteer aspects of this. How do those two intersect? How is it that, as something that you&#39;re doing and volunteer time, you&#39;re able to pay bounties to help with some of the development? </p>
  <cite>Mitch Downey:</cite>
  <time>15:14</time>
  <p>Yeah, good question. So we have more of a hybrid model of open source, like we. We have a premium option Through our website and mobile app that will allow you to use features that have to write to our servers in some way. So if you want to listen on web and mobile and you want it to sync your history between the two devices, well that has to write to our servers in order to make that connection happen. I and so, and also like sharing clips. Like a clip has to get saved to our server in some way, so that is a premium only feature. </p>
  <cite>Gene Liverman:</cite>
  <time>15:52</time>
  <p>And those things cost you money, I&#39;m assuming is why you have them as a premium feature. </p>
  <cite>Mitch Downey:</cite>
  <time>15:57</time>
  <p>Yes, the server costs definitely have to cost us a lot more money. So we charge for premium, but it&#39;s more of a suggestion than a requirement. We are a value for value company, so if somebody requests a premium membership, we will extend their membership no questions asked, at least for now. I don&#39;t know if abuse happens, but I don&#39;t foresee that happening. Yeah, we&#39;ll extend it for free and, you know, after it gets up to expiring will extend it again. We just need some sort of some sort of way to be able to prevent people from spamming our servers with, like free membership requests. So yeah so we do it by request. Only if people write us and say they want a free membership will give it to them. So that is a we&#39;re making, or about breaking even, I would say, on our expenses. Now the bounties program is probably pushing us over breaking even. I&#39;ve put quite a bit of personal money into the project, but it&#39;s what I love to do. But so that is how we are able to make a bounties program feasible. Is that we do ask for pay for premium memberships and hope it&#39;s been growing, hopefully continues to grow. Be wonderful if we can eventually hire a full time engineers to maintain it. Not totally might sense one of the coolest things about the bounties program now we barely advertise it at all, barely even posted about it, and people are still stumbling across it. We have in our GitHub. We have a page that lists all the bounties that are available and we&#39;ve had four people already work on or complete bounties for us awesome. And If we&#39;re being honest, the amount of money that it would cost to go through a traditional contractor and a corporate environment to get this work done will be far more expensive than what these bounties are. And you know, I feel bad that I want to pay people Absolutely the full rate that they can get in the corporate world. But we&#39;re finding that it is actually being a difference maker and it&#39;s encouraging people to own a feature and deliver it to completion. One of the biggest ones we have in progress right now is android auto, which we have a bounty for twelve hundred dollars to complete, because it&#39;s just one of the most requested and also a lot of work and, yeah, it looks like it&#39;s about ninety percent done awesome. And yeah, and I don&#39;t think if we didn&#39;t offer a bounty that somebody would pick that up for us. </p>
  <cite>Gene Liverman:</cite>
  <time>18:36</time>
  <p>Yeah, no doubt I imagine that at least a little bit of the stumbling across it is where some other people been helping spread the word about it. I actually heard about your bounties program through some of the podcast in the Jupiter Broadcasting Network, Chris Fisher, and that group has been real active in saying hey, hey, don&#39;t look at this bounty, saying you might have to know Android auto Go, help him out. </p>
  <cite>Mitch Downey:</cite>
  <time>18:59</time>
  <p>Chris has been amazing for us. He&#39;s been so supportive. The whole Jupiter Broadcasting team really we have. I See quite a few of their, their addresses in our, in our matrix room, because it says like at Jupiter broadcasting. So it&#39;s quite a few people in there. Yeah, I really love what they&#39;re doing and they they&#39;re really true open source supporters. </p>
  <cite>Gene Liverman:</cite>
  <time>19:20</time>
  <p>Oh, absolutely. </p>
  <cite>Mitch Downey:</cite>
  <time>19:21</time>
  <p>It&#39;s flattering that they are helping support us so much. </p>
  <cite>Gene Liverman:</cite>
  <time>19:25</time>
  <p>Yeah, that&#39;s a. You know, that&#39;s one of the cool things with the value for value model that you were talked about is it&#39;s not just money that people can give back. You know, taking the time to mention your app on their podcast and ask their audience to maybe come give you a hand is Another way of giving value back, and I think that&#39;s a really cool thing. </p>
  <cite>Mitch Downey:</cite>
  <time>19:44</time>
  <p>Yeah, absolutely, and it&#39;s hard for me to even list all the ways that people can contribute, because I mean we can use help in every capacity you can imagine, from just recommending it to friends or family or design suggestions or Project management, like helping organize, keeping things in line. You know, my, my strengths are in programming, and mobile app and web app specifically, not all forms of programming. So, yeah, that&#39;s. We wanted to try to foster as much Collaboration as possible and we appreciate all the help we can get. </p>
  <cite>Gene Liverman:</cite>
  <time>20:21</time>
  <p>That sounds pretty awesome. I really appreciate you taking the time to tell us about all the different things that you&#39;ve got going on. The accessibility work sounds pretty amazing and really looking forward to seeing how how things work out after you&#39;ve been able to work through that checklist and Imagine that if anybody wanted to help you with that checklist, you&#39;d be more than happy to take some help. What would be a good way for people to reach out to you if they wanted to just get in touch in general or if they wanted to maybe help out with some of this stuff? </p>
  <cite>Mitch Downey:</cite>
  <time>20:49</time>
  <p>Sure, we have quite a few different contact options, as I think I mentioned earlier. Maybe the best way to go is to go to podverse. fm/ contact. You can find some contact options there. Also, in the footer We&#39;ll see our discord, our matrix, twitter, mastodon, all kinds of things, and I&#39;m active across all of them. I have a daily checklist to make sure I keep up with them every day. </p>
  <cite>Gene Liverman:</cite>
  <time>21:17</time>
  <p>And I&#39;m assuming that you have somewhere central where you have all of your code. Is that on GitHub or do you have it somewhere else? </p>
  <cite>Mitch Downey:</cite>
  <time>21:24</time>
  <p>Yes, github. com, slash, podverse. All of the software that we create is free and open source with the AGPLv3 license and, yeah, we&#39;d love to get feedback. If anyone it would be interested in collaborating, please reach out. You can create an issue on there or email us. Another option is contact at podverse. fm. </p>
  <cite>Gene Liverman:</cite>
  <time>21:49</time>
  <p>Just for the, for the layperson who might not be familiar what is the AGPLv3? Just in layman&#39;s terms, not in the nice legal version. </p>
  <cite>Mitch Downey:</cite>
  <time>21:58</time>
  <p>Broadly in open source. There there is the type of open source software where you can download it, modify it and use it for any purpose you want, in any way. That is traditionally thought of as the MIT license, or that&#39;s like the one that stands out the most. And then there are share alike licenses, which stipulate that if you use this software, if you modify it, you also have to share it. Both of them are good in my opinion, but the spirit of what we do with podverse is we want to create the software, we want to release it for free and we want it to be stay free for everybody going forward. You know, am I nothing wrong with MIT license, but it just fits what we&#39;re trying to do here. </p>
  <cite>Gene Liverman:</cite>
  <time>22:42</time>
  <p>I totally make sense. Just want people to give back if they&#39;re utilizing what you and others have put their time into. </p>
  <cite>Mitch Downey:</cite>
  <time>22:49</time>
  <p>Yeah, exactly very cool. </p>
  <cite>Gene Liverman:</cite>
  <time>22:51</time>
  <p>Well, before we sign off, I want to take a moment to thank the people who have taken the time to boost in and provided some value back. To me, this is a value for value podcast, which means I&#39;ll never ask people to pay for it, but it does cost money to do all the production and hosting and all the other work that goes into it. And If people do get value from this, then I hope they&#39;ll take the time to consider sending a contribution in, either via boost using a podcasting app like podverse or some other modern podcasting out, or via the support the show link in the bottom of the show notes. You can also find the show notes, transcripts and links to the things that Mitch and I talked about today at volunteer technologist. com, and If you know anyone who would like to come on the show or you think I should reach out to about coming on the show, then please send me a message using the links at the bottom of the show notes. Mitch, thank you very much for your time and thanks everyone for listening. Thanks, gene, have a good day. </p>

{{< /rawhtml >}}
{{< /tab >}}
{{< /tabs >}}
