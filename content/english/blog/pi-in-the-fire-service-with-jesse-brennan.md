---
aliases:
- /episode/4
author: Gene Liverman
categories:
- Podcast Episode
date: Wed, 01 Mar 2023 05:00:00 -0500
description: 'Listen as Jesse Brennan talks about how Raspberry Pi 3''s are making
  a significant impact in his fire department and others across the country. Also,
  did you now that more than 85% of all fire fighters in the US are volunteers, and
  that the percentage is significantly higher outside of large cities? Jesse talks
  about this and how technology is allowing departments to better respond to needs
  while still being staffed primarily by these volunteers.Links:'
guid: Buzzsprout-12216153
image: images/episode-header.png
title: Pi in the Fire Service with Jesse Brennan

---
{{< buzzsprout-episode episode_id_number="12216153" podcast_id_number="2053906" file_name="pi-in-the-fire-service-with-jesse-brennan" >}}
{{< listen-apple >}}{{< listen-overcast >}}{{< listen-google >}}{{< listen-rss >}}
{{< tabs >}}
{{< tab "Show Notes" >}}
{{< rawhtml >}}
<p>Listen as Jesse Brennan talks about how Raspberry Pi 3&apos;s are making a significant impact in his fire department and others across the country. Also, did you now that more than 85% of all fire fighters in the US are volunteers, and that the percentage is significantly higher outside of large cities? Jesse talks about this and how technology is allowing departments to better respond to needs while still being staffed primarily by these volunteers.<br/><b>Links:</b></p><ul><li><a href='https://github.com/CtrlAltJesse/IAmRespondingKiosk'>I Am Responding Kiosk</a></li><li>You can reach Jesse via email at <a href='mailto:me@jesse-brennan.com'>me@jesse-brennan.com</a></li></ul><p> </p><a rel="payment" href="https://www.buzzsprout.com/2053906/support">Support the show</a><p>You can find me on Mastodon at <a href='https://podcastindex.social/@volunteertechnologist'>podcastindex.social/@volunteertechnologist</a> You can also reach me via <a href='https://www.volunteertechnologist.com/contact/'>volunteertechnologist.com/contact/</a><br/>If you got value from today&apos;s show, then I hope you&apos;ll consider contributing to its ongoing production by sending a boost with a new podcast app such as <a href='https://fountain.fm/genebean?code=5cb3b5f06a'>Fountain</a>, or via the buy me a coffee link on <a href='https://www.volunteertechnologist.com/contribute/'>volunteertechnologist.com/contribute/</a><br/>Visit <a href='https://www.volunteertechnologist.com/'>volunteertechnologist.com</a> for show notes, transcripts, or more information.</p>
{{< /rawhtml >}}
{{< /tab >}}
{{< tab "Transcript" >}}
{{< rawhtml >}}
  <cite>Gene Liverman:</cite>
  <time>0:05</time>
  <p>Hello, everyone,and welcome to the Volunteer Technologist podcast. Here we take a look at the ways that people who are technically inclined volunteer outside of their primary job. Today I&#39;m joined by Jesse Brennan, and he is going to talk to us about his work with the local fire department. Hi, Jesse.</p>
  <cite>Jesse Brennan:</cite>
  <time>0:23</time>
  <p>Hey, how you doing Gene? How&#39;s everything?</p>
  <cite>Gene Liverman:</cite>
  <time>0:25</time>
  <p>Pretty good,pretty good. I wanted to give you a chance to introduce yourself to the audience.</p>
  <cite>Jesse Brennan:</cite>
  <time>0:30</time>
  <p>Yeah, awesome. So yeah, my name is Jesse Brennan.I&#39;m a lieutenant with the Penn Forest Volunteer Fire Company Number 2, and also have largely been in tech for the last maybe15 years or so in different engineering and project management roles.</p>
  <cite>Gene Liverman:</cite>
  <time>0:46</time>
  <p>Very cool. So I know you from us both working together previously. During that time, you had told me about some custom electronics that you had built for your local fire department, and that it facilitated getting the firefighters some information they needed before leaving the station while they were still on Wi Fi and before they got out into areas where they might not have such good service.</p>
  <cite>Jesse Brennan:</cite>
  <time>1:12</time>
  <p>Yeah.</p>
  <cite>Gene Liverman:</cite>
  <time>1:12</time>
  <p>And that&#39;s about all I remember about it. I knew it sounded really interesting,so I wanted to give you a chance to tell us about that, and anything else you want to talk about in the same general field.</p>
  <cite>Jesse Brennan:</cite>
  <time>1:21</time>
  <p>Yeah, absolutely.So So to put this in a bit of context, just so everybody&#39;s aware it firefighters in the US is largely volunteer dominated,right. So unless you&#39;re really in a big city, if you call 911,and you&#39;re looking for help from the fire department, it&#39;s very likely going to be volunteers that come out, right, and those those volunteers are sitting at home, they might be at work,they might be, you know, at a restaurant or something like that. But we all effectively get pagers, and we respond when we are around. So something like85% of all fire departments in the United States are either volunteer or mostly volunteer.And in states like mine in Pennsylvania, that number actually grows to 97%, you typically don&#39;t see a career firefighter until you get into Philly, or Pittsburgh, in the state of Pennsylvania. So that creates some unique challenges where 911 is a 24/7 operation,right, fires will always happen.And when they do, it&#39;s, it&#39;s really urgent. So we typically use a couple, a suite of apps that really will give our officers and our chiefs some additional information on who&#39;s responding where they&#39;re coming from. And we also have some apps that will connect to our computer aided dispatch center,whether that&#39;d be the county or the township that we&#39;re in to give us more information on that call. And what that does is that allows us to really start formulating a plan earlier. And we start having an idea of who&#39;s going to be arriving for a particular call, and the manpower that we&#39;re going to have to be working with, right,some calls, we have 40, guys,sorry, 40 people, some calls might be a weird time people are at work, we might have 10. And we need to make deal with 10.But knowing that sooner rather than later, helps us to really make that response appropriate.So within those apps, we all kind of will say whether or not we&#39;re responding if we&#39;re going right to the scene, if we&#39;re going to station if maybe we&#39;re picking up a certain apparatus or something. But then that starts having an issue with how do we start communicating that to everybody, right? Everybody&#39;s putting in information. But how do we pick up that information when I get to the firehouse? I want to know who&#39;s coming and how do we communicate that in the easiest way possible. And typically, fire departments will solve this by your typical firefighter isn&#39;t really a technical person, to be perfectly honest. Right? So typically, fire departments will solve this by go to Best Buy,they&#39;ll get an off the shelf computer, throw it up on the TV or monitor somewhere, and it&#39;s off the shelf windows, patches,whenever it patches that is usually on a login screen three quarters of the time, and not really showing the right data.So you know</p>
  <cite>Gene Liverman:</cite>
  <time>4:11</time>
  <p>that login screen</p>
  <cite>Jesse Brennan:</cite>
  <time>4:11</time>
  <p>working</p>
  <cite>Gene Liverman:</cite>
  <time>4:11</time>
  <p>isn&#39;t all that helpful whenever you&#39;re trying to get responding to a fire it&#39;s like &quot;Oh, gee, what&#39;s the password for that again?&quot; So yeah, to see why that&#39;s not exactly ideal.</p>
  <cite>Jesse Brennan:</cite>
  <time>4:21</time>
  <p>Yeah, and when you&#39;re running it to the firehouse, you want to know immediately who&#39;s coming, how far away are they? And, you know, what&#39;s the threshold for where I&#39;m keeping this apparatus still before I go in route,effectively, right. So if I can quickly see I have three people a quarter mile away, I know they&#39;re coming. I&#39;m gonna wait for them before that fire truck starts going somewhere. So I&#39;m not showing up to a scene with a potentially empty fire truck and a bunch of firefighters that are sitting at station. So in my mind, and you know, we&#39;re pretty solution oriented people, right,that&#39;s our day job. It&#39;s real hard to turn that off in the evenings sometimes.</p>
  <cite>Gene Liverman:</cite>
  <time>4:59</time>
  <p>Yes, yes it is.</p>
  <cite>Jesse Brennan:</cite>
  <time>5:00</time>
  <p>So. So you look at that and you go, Okay, well,how do I solve this problem,because what was happening is we were getting dispatched to some pretty serious calls, whether they be motor vehicle accidents,or structure fires or wildfires that we typically have in our area, we get the station and somebody&#39;s gotta log in and that takes up precious seconds, where maybe we&#39;re not giving the best response to the township and our</p>
  <cite>Gene Liverman:</cite>
  <time>5:24</time>
  <p>just to kind of pause right there for a second.responding area that we could be. So I took a look I know, fortunately, most of us haven&#39;t experienced a house</p>
  <cite>Jesse Brennan:</cite>
  <time>5:32</time>
  <p>Yes</p>
  <cite>Gene Liverman:</cite>
  <time>5:33</time>
  <p>I was whenever we still had pagers, which I think fire. But as a late teenager, I was a volunteer firefighter,also. And my first thing about hearing about what you&#39;re were almost identical to the ones that are being handed out talking about is it&#39;s amazing how even the standard baseline of tech has evolved in the last20 years.today. Back then. Yeah. Back in that time, virtually nobody had a cell phone. Yeah, flip phones weren&#39;t even a thing yet. They were brutal. There were almost a size of the pagers that the firefighters carried. And so we had no idea who was coming. It&#39;s like when you get enough people to operate the truck you left.And if nobody showed up, then sometimes you took the truck with one or two people on it.But the other thing I wanted to mention, just for context for people listening, is if you&#39;ve ever started any kind of fire,you know, it starts off a little slow, and then all of a sudden,it will just take off and go.And if you&#39;ve ever seen how fast a fire can grow, that&#39;s where the seconds that Jesse was just mentioning come in so critical.The difference in arriving one to two minutes difference can be the difference of whether or not a house is saveable or not.</p>
  <cite>Jesse Brennan:</cite>
  <time>6:54</time>
  <p>Yes, 100%</p>
  <cite>Gene Liverman:</cite>
  <time>6:55</time>
  <p>or in a motor vehicle accident, the difference whether somebody has bled out or not. And so this this time you&#39;re talking about isn&#39;t just as a geek, it&#39;s not just &quot;oh,cool, I shaved off 30 seconds.&quot;Like we&#39;re talking people&#39;s houses not burning all the way down. Somebody&#39;s surviving a car crash or a heart attack. So I just want to make sure we set the stage right for the people listening that were geeks, we talked about a lot of tech, but this stuff matters at whole lot deeper level. And that&#39;s part of why I&#39;m so interested in it.</p>
  <cite>Jesse Brennan:</cite>
  <time>7:26</time>
  <p>Yeah, yeah. And that that kind of goes to fire departments aren&#39;t really a tech first operation a lot of the times because by the time tech really gets into most fire departments, it needs to be proven, it needs to 100%absolutely be proven, which really dictates the type of tech that we&#39;re we&#39;re using. Because if we cannot 100% rely on it,then that could really cause some issues. Right.</p>
  <cite>Gene Liverman:</cite>
  <time>7:55</time>
  <p>And I think that&#39;s why the pagers haven&#39;t changed all that much because it is battle proven tech that works in some of the worst conditions and worst signal areas you can imagine, but it still gets that signal out to the people who need it.</p>
  <cite>Jesse Brennan:</cite>
  <time>8:08</time>
  <p>Oh, yeah. 100%.So, so the pagers themselves just to kind of give a little bit of insight into into that tech. Those are just simplex radio frequencies. Typically,they might be repeated on towers. But how a pager triggers for particular fire department is two tones is sent over RF, it opens up the pager and then the dispatcher gives the report and pretty much tells us where we&#39;re going. Just over standard RF most people can buy an off the shelf scanner and actually hear what&#39;s going on with their local fire department their local EMS.Because that technology is so so proven. And that is why we&#39;re going up to digital. Yeah,exactly. And not for nothing. We kind of break our radios a lot too. So when our radios cost$1,000 That&#39;s about firefighters</p>
  <cite>Gene Liverman:</cite>
  <time>8:59</time>
  <p>aren&#39;t the most technical people they&#39;re also not the easiest don&#39;t electronics, or Yeah, I don&#39;t know anything. I mean, stuffs got to be built to last around the fire department.</p>
  <cite>Jesse Brennan:</cite>
  <time>9:08</time>
  <p>Oh, yeah. And electronics as a whole doesn&#39;t like water and it doesn&#39;t like fire. And those are the two main things that we&#39;re really working with.</p>
  <cite>Gene Liverman:</cite>
  <time>9:17</time>
  <p>Ask your cell provider how much electronics like fire or like fire and water. I think they have those clauses about water equals no warranty. So yeah,</p>
  <cite>Jesse Brennan:</cite>
  <time>9:27</time>
  <p>yep. Yeah, yeah,there are no warranty claims in the fire department because we know we fried it by the time we&#39;re done using it. But that kind of goes to having that computer in the bay somewhere right presenting that information. Even if that computer in a bay presenting that information does work most of the time where we can tell who&#39;s who&#39;s coming, where where responders are coming from and how close they are to the department. Having a computer in a fire department bay is a pretty inherently hostile place.We do training there, things are getting kicked things are getting battered around I personally broken a lot of stuff in a bay drums without without having any intention to, to break anything. Right. So that that starts to. So looking at that, I kind of thought, how do we get around this problem? How do we communicate effectively,where, ideally our officers and our apparatus operators, because those are the people that initially need to know that information, First, know where people are, how far away they are, and can make the right decisions to make sure that we have the most effective response possible. And at least at our fire department, what we ended up doing was we started taking some LCD TVs, we suspended them about six feet up. So right away, it&#39;s a less hostile territory where things are getting kicked and ran into and possibly thrown, right? But how do we how do we solve for that that computer that&#39;s still laying on the floor too. And looking at it, a lot of these apps like I&#39;m responding and active 911 and the applications that we&#39;re using, they&#39;re ultimately just a web kiosk,right, we can, we can display all this information from a view perspective within a web page.And that&#39;s exactly what we did.So looking at it, I pretty much looked at it and said, I think I could solve this problem with a Raspberry Pi. So what we ended up doing was really just taking the Raspberry Pi stripping out the entire OS to the point where it&#39;s just a very basic Window Manager starts up chromium just enough to display the webpage auto logs in. So it&#39;s really just a mixture of scripts and settings and a couple of Chrome extensions to automate the moment you turn that Raspberry Pi on, it loads, and it auto login auto logs in and then tells you pretty much what the status of your fire department is who&#39;s responding. And they stay on 24/7. And that that really kind of solves a problem.So what that has now allowed us to do, instead of going to BestBuy. And spending $600 on a machine that&#39;s off the rack and doesn&#39;t really fit our use case to begin with. Now we can take I started with Raspberry Pi zeros,they work, they&#39;re a little laggy eventually went to Raspberry Pi threes for everything. But looking at the cost savings. Now we can spend some of that money on additional screens. So what we end up with is pretty much every bay now has a screen where the apparatus operator can hop in, start the engine, start the truck, start a rescue, get that idling, but also start making determinations of where&#39;s my crew? How far away are they? What&#39;s my plan, we can also give a live view of the map of the scene. So when I say that it&#39;s really just a quick like Google map, you know, here&#39;s where the scene is, here&#39;s your approach. Not not like a like a live satellite deal. But it kind of starts giving us some information because most towns have a couple of main roads and then you know, you get most addresses can be hit two or three turns from the main road.Right? So right away, we&#39;re looking where in the town this is rather than having to fuss around with Google Maps, see what&#39;s going on there? Like how do we pull up directions real quick, we could just look and go oh, it&#39;s a left on this and the right on that. And I&#39;m right there. That&#39;s that&#39;s really invaluable information for the apparatus operator and, and Gene to your point that you made when when you were a firefighter, I started in 2005 as well. And it was the same thing, volunteer departments, we&#39;d get a page,and then you just kind of made like hoped people were coming.There wasn&#39;t a whole lot more than that, to be perfectly honest, everybody, firefighters in departments, they&#39;re a close knit group, we all kind of know what each other doing where each other&#39;s ad if you know,somebody&#39;s going away for a weekend, we have an understanding that okay, so and so won&#39;t be here for the take any calls this weekend. But for the most part, you were just kind of making sure like, all right, I think I&#39;m gonna get eight people. Yeah. And if you got between six and 10. Great.</p>
  <cite>Gene Liverman:</cite>
  <time>14:01</time>
  <p>Yeah, no kidding.One thing that stood out to me from what you were just saying too, is by switching to the kind of setup that you described with the Raspberry Pi&#39;s for the same amount of money, you&#39;ve now got at least six times, or well,counting screens, maybe four and a half to five times as many or getting information displayed four and a half to five times as many places for the same amount of money. And so yeah, didn&#39;t love itself is huge. Plus, being that most I think you said 85%of departments are volunteer, or85% of firefighters are volunteer, you have to imagine that if the vast majority of firefighters are volunteers.That also means there&#39;s not a tremendous amount of extra funding, because if there was a ton of funding, you&#39;d probably have more professional fire fighters. Well, when you don&#39;t have a ton of funding being able to get this information up for one six the cost roughly 100bucks is stead of six to seven hundred bucks. That&#39;s a that&#39;s a pretty big deal, especially in a lot of departments that aren&#39;t in a city.</p>
  <cite>Jesse Brennan:</cite>
  <time>15:06</time>
  <p>Yeah, it absolutely is and I&#39;m a little rural, where I&#39;m at. And looking at our budgets, right we don&#39;t,we don&#39;t really get a whole lot from taxes. The nice part about living a little bit more rural is the taxes are cheaper. But at the end of the day, you kind of get what you pay for. Right?There&#39;s there&#39;s a lot less of that pie to go around. So in our volunteer department, we have to make up that funding shortfall in other ways, right. So that that might be something called boot drives, where you kind of stand in the road, and I&#39;m sure everybody&#39;s ran across it if you&#39;ve been outside of a city on Memorial Day weekend or July 4weekend, or something where the local fire departments pretty much standing in the road with a booth begging for donations, or some sort of pancake breakfast or some other way, we are pretty lucky, we are pretty well funded considering the area that we are in just due to some of the fundraising activities that we do. But it&#39;s absolutely a cost saving exercise, right? When you look at it, the off the shelf.And I see this in departments all the time, because this is a pretty common app that a lot of departments use, especially if you&#39;re volunteer because you you know where people are coming from, right? It&#39;s not really consideration if everybody&#39;s career because they&#39;re all there. But typically, that use case has been by a computer by a TV, hook it all up. And unfortunately, Windows updates takes over and three in the morning, you&#39;re typing in a password because it rebooted.Because nobody knows how to correctly configure Windows machine and kiosk mode. And when you do sometimes an update will revert some changes there. So looking at what we did, and rolling it out across our fire department, we definitely and the size of a fire department here, right. So we have a six Bay fire department to have one system that contains all that information to look at real quick before you hop on an apparatus isn&#39;t the most effective thing you&#39;re, you&#39;re not, you&#39;re kind of running around in the opposite direction that you need to be going at a certain point. So so to have it right on the bay doors.</p>
  <cite>Gene Liverman:</cite>
  <time>17:06</time>
  <p>You said you had sometimes have as many as 40people responding to a given fire. I can&#39;t imagine 40 people trying to stand around this way to figure out what the heck&#39;s going own. If you&#39;ve ever done that in a restaurant trying to always see the same menu sign or at an airport all trying to see the same flight board flight arrivals board, you know exactly how ineffective that is. So yeah, that totally makes sense.And not something I had thought about until you said that.</p>
  <cite>Jesse Brennan:</cite>
  <time>17:32</time>
  <p>Yeah, and having40 people in a volunteer fire department is a good problem to have. But it does cause some scaling issues sometimes. But yeah, that&#39;s that&#39;s exactly it because one of the benefits of these dashboards too, is they plug into our local dispatch centers. So we are now getting more context on the calls, we might have an initial dispatch of two carMVA two injuries, but reading the screens, especially while you&#39;re waiting apparatus kind of warm up, you know,they&#39;re really big diesel engines are most of our larger apparatus, I believe is between500 and 675 horsepower that we don&#39;t want to, you know, the nature is you start it up and you go, and that does a lot of damage to engines over time. So we can spend a couple minutes idling and waiting for people.That also helps us money wise to not put too too much wear and tear on our engines. So if we can sit there idle, have the apparatus operator be in the driver&#39;s seat, but also read a screen in front of him or her where it says, yeah, it&#39;s a two car MVA, but one person has head injuries, one person might have a sprained wrist, that changes the picture a little bit,because now we just have one really critical injury that we need to worry about. But that&#39;s not necessarily something that gets communicated over the radios.</p>
  <cite>Gene Liverman:</cite>
  <time>18:45</time>
  <p>Yeah, ya know, in the, in the area I live in, it&#39;s really common for there to be a single paid professional at each station, or in each general area. And then everybody else has a volunteer. And frequently that paid professional, they&#39;ve got a full time gas vehicle, as opposed to the big diesel trucks, but they&#39;ve got a full time gas vehicle, and they will respond initially and do some of that singing assessment. And then I&#39;m assuming let the people back at the station, have a little more information or let dispatch know what&#39;s going on.But it sounds like this would help make sure that gets down to the volunteers who aren&#39;t necessarily going to be on the radios, they just have their pagers, or at least for a while,will only have pagers so much.Yeah, it sounds like a much better way of communicating a lot of that info to the people who really need to know it</p>
  <cite>Jesse Brennan:</cite>
  <time>19:36</time>
  <p>it is right? And there&#39;s a lot of times that you know, the initial hustle of somebody calling 911 They&#39;re in a panic, they might be communicating the wrong things.And a lot of departments have it to where a senior officer will go right to the scene, at the very least to validate the call.Right They know responding units are coming in, but let me get there. First, let me start formulating a plan. If you have achieved that goes to this Scene, you know, while we&#39;re all at the fire department going you hop on this apparatus, we&#39;ll hop on this apparatus, this is what we need to bring to the scene for a response that senior officers looking at a potential structure that&#39;s on fire and going, Okay, what&#39;s my first attack path when things start getting here, and at that point,you&#39;re starting to put a plan together in in parallel, right that the last thing you want to do is show up to a scene and go,Okay, now what? Because that&#39;s also not, that&#39;s not great some of the times, but at the very least, are validating some of those dispatch notes that we might be seeing and starting to formulate a plan in the back of an engine on the way to a call that we might have seen on our screens. Yep. Yeah. And then on top of that, to some of these applications, we have iPads and our vehicles where we can actually put ourselves in route,and it will follow our GPS. So you know, if we do have a chief,or a senior officer at a scene,they now know how, like where the closest engine is? Are they five minutes away? Are they 10minutes away? Because that might dictate what the plan is going to be? Yeah, when they get there. So this? Yeah,</p>
  <cite>Gene Liverman:</cite>
  <time>21:05</time>
  <p>I imagine that could also bring into bear whether or not they need to maybe upgrade the call to like a mutual aid call or something like that. Okay, I don&#39;t people from my station coming, do I need to get another station in route also, because we just don&#39;t have enough people to deal with this thing I&#39;m looking at.</p>
  <cite>Jesse Brennan:</cite>
  <time>21:22</time>
  <p>Exactly. And, and that&#39;s what essentially these these apps really kind of afford us. And just the way that we&#39;re showing the information, both at the station and on scene as well, where we&#39;re communicating now, in a whole nother way to where there&#39;s a lot more telemetry and data on who&#39;s responding where they&#39;re responding from and what you&#39;re getting to be able to make those choices sooner. And what that Yeah, yeah. And that translates into</p>
  <cite>Gene Liverman:</cite>
  <time>21:50</time>
  <p>home. Yeah, I think you&#39;re about Yeah, but that that translates into how fast whatever the problem is,can be resolved, and how well resolved. And that&#39;s when you&#39;re talking about people&#39;s livelihoods, their homes, their lives? You know, that&#39;s huge.</p>
  <cite>Jesse Brennan:</cite>
  <time>22:07</time>
  <p>Yeah, exactly.Yeah, so So putting these screens together really helped us out. So what I ended up doing was I ended up throwing all my shell scripts and things on GitHub to see if there are other departments that could could make use of this code, right,this is now a solved problem. I know, maybe not the most, not every department has, you know,somebody who might be an engineering or might be an engineer in the technology space. But they know how to configure a Raspberry Pi, right.So I put a set of instructions together that pretty much was on the baseline of if you could figure out how to load an OS onto a Raspberry Pi, you could build your own system here. And what I started seeing is that departments across the country started kind of interacting with this GitHub, either just via questions, or stars and forks.Some really advanced people would actually fork the code,put their own departments logo on the boot screen, which I thought was really, really cool.And kind of make it their own.Yeah, that really by Yeah, but now now we have, you know, a solved problem that we can now start deploying at multiple departments, because I can&#39;t tell you how many departments I walk into, and there&#39;s a computer somewhere on the bay floor, usually at a Windows OS boot screen that needs to be logged in before you actually start getting any functional information from some of these apps that we use.</p>
  <cite>Gene Liverman:</cite>
  <time>23:30</time>
  <p>That&#39;s incredible. Yeah, and I think I&#39;m really glad to hear that you&#39;ve put it out there. And we&#39;ll be sure and put links to what you were just describing in the show notes for this episode.So that anybody listening can take a look at it and either share it around with people they know, or if they happen to also be in the fire service. Maybe they can take advantage of it too.</p>
  <cite>Jesse Brennan:</cite>
  <time>23:53</time>
  <p>Yeah, yeah,absolutely. It&#39;s a couple of Raspberry Pi&#39;s and a little bit of code and Raspbian. And you&#39;re off to the races.</p>
  <cite>Gene Liverman:</cite>
  <time>24:01</time>
  <p>That&#39;s really cool. One question I did have is, how did you get into all this?</p>
  <cite>Jesse Brennan:</cite>
  <time>24:06</time>
  <p>Yeah, so I grew up around this a little bit. My,my father worked for a township DPW in New Jersey, where they were right next to the local EMS department. So they were a volunteer EMS department, they pretty much ran, they did the same thing that we do in the fire service just with EMS calls, right emergency medical services, where it was a volunteer ambulance company that would go out and solve medical issues. So with growing up in New Jersey and living in New Jersey when I turned 18, knowing that world I pretty much just walked into my local fire department asked for an application just wandered in on a drill night and just asked for an application and from there the rest is history. Just they all kind of took me under their wing. It&#39;s it&#39;s you know Joining a fire department it&#39;s it&#39;s a really good group of people at every fire department. They&#39;re they&#39;re committed to community service. But also you end up making a lot of friends, right.So if this is something that if you see firefighters and go, I&#39;d be interested in doing that chances are you live in an area with a volunteer department. And you could totally get involved somehow, you know, not, not every volunteer fire department means you need to be walking into structures that are on fire, or sometimes they could use drivers, or sometimes they could use helpers. But it&#39;s a really good cohesive group of people. And you end up making friendships for life there,because you end up getting pretty close to one another,just based on the shared experience, and then also in Jersey ended up joining a EMS squad, same thing. So it was an EMT for a little while and did the same thing, just in another organization.</p>
  <cite>Gene Liverman:</cite>
  <time>25:53</time>
  <p>There&#39;s definitely a lot of jobs around the fire service that don&#39;t require going into the buildings. Yeah, everything from being on a hose outside to pulling the hoses to one of the more skilled jobs is being the pump operators and the engineers that are actually operating the trucks or the apparatus,outside, I mean, those, those jobs are actually in a lot of cases are a much more skilled job than holding the hose and going into the building and some of the other stuff, just as you&#39;ve got to know, a lot,including Oh, dynamics and pump operation. And yep. Because all of a sudden, the pumps not working right and like, but it&#39;s also a incredibly rewarding thing. Or at least it was whenever I was younger, and was both willing and able to do that. And from what you&#39;ve described, I have to imagine you feel that it&#39;s incredibly rewarding too</p>
  <cite>Jesse Brennan:</cite>
  <time>26:45</time>
  <p>it is and honestly being in tech, we we get a lot of exposure to the same type of problem solving aspects, right. So there&#39;s,there&#39;s a lot of shared kind of problem solving aspects of you got to do what you got to do.But it makes you more well rounded in terms of being mechanically aware of things,right, because everything in the Fire Services is pumps and water flow management, and different mechanical type things that you&#39;re doing. Yeah. And you know, as an engineer that who pretty much sits in front of a keyboard all day, it&#39;s it&#39;s a welcome contrast to be perfectly honest. But it also makes you better well rounded. And it starts opening up new perspectives into how not only are you solving problems in the fire service coming from the IT space, but on the other way of okay, now you&#39;re in a more mechanically aware, how do I solve this certain problem that maybe my colleagues haven&#39;t considered because they&#39;re not,they&#39;re not typically mechanical type people they might have,they might be locked in a certain thought process where now you have exposure to several different types of problem solving methodologies that aren&#39;t typically represented within your industry.</p>
  <cite>Gene Liverman:</cite>
  <time>27:57</time>
  <p>It&#39;s amazing how your professional life can make you better and your volunteer life and your volunteer life can actually make you better in your professional life. You know,it&#39;s a two way street of improvement.</p>
  <cite>Jesse Brennan:</cite>
  <time>28:07</time>
  <p>Yeah, exactly.And it also gives perspectives to urgent issues in your job too, right? Like, now I&#39;m that calming person on a SEV 1,because my thought process is if nobody&#39;s dying, then we&#39;re not we&#39;re doing okay. Let&#39;s figure this out. Nobody&#39;s</p>
  <cite>Gene Liverman:</cite>
  <time>28:31</time>
  <p>car hasn&#39;t run into something.</p>
  <cite>Jesse Brennan:</cite>
  <time>28:32</time>
  <p>Exactly. Okay, we have a service down, it&#39;s pretty important. I completely understand that. But let&#39;s let&#39;s calmly you know, start troubleshooting this rather than really just just, you know,potentially doing something where where you&#39;re taking shortcuts and potentially causing a bigger issue. Yeah,absolutely. And it kind of gives you that rapport on those bridges where where you are the common voice to say, Okay, let&#39;s let&#39;s figure this out. Because it definitely gives you that that level of perspective.</p>
  <cite>Gene Liverman:</cite>
  <time>29:04</time>
  <p>Thank you so much for sharing your experiences and for once again, for both your fire department and for putting it out there for other part departments. It&#39;s really awesome. Wanted to give you a moment if you wanted to tell people how they could reach out to you if they have any follow ups? Or if there&#39;s just anything else you wanted to share with the audience?</p>
  <cite>Jesse Brennan:</cite>
  <time>29:24</time>
  <p>Yeah, if there&#39;s any questions at all, please feel free to send me an email me me at jesse dash brennan dot com And I&#39;m sure my name is going to be in the in the show notes. And yeah, the only other parting words that I would probably say is, that fire departments in the US are very accessible buildings. If you&#39;re interested at all, even if you just want to take a tour,you know, one of the one of the pleasures of every firefighter and showing off all the equipment, so don&#39;t hesitate. If if you&#39;re interested at all,just reach out to your local firehouse and say, Hey, can Can I see what you know what tools you have? And then what trucks are running and they will,they&#39;ll gladly bring you through and show you everything. And that&#39;s that&#39;s one of the pleasures of being a firefighters is showing the community are cool toys really.</p>
  <cite>Gene Liverman:</cite>
  <time>30:11</time>
  <p>And I will I will tack on to that that from what I have gathered, I don&#39;t think there&#39;s a firehouse around. That is sad when the parent brings around a small kid who is</p>
  <cite>Jesse Brennan:</cite>
  <time>30:21</time>
  <p>Oh God no</p>
  <cite>Gene Liverman:</cite>
  <time>30:22</time>
  <p>facsinted by the fire vehicles because they see them on TV or they see him in the cartoons or even in the books. Yeah. And then to see him in person. The way a kid&#39;s face lights up, when they get to see a fire truck up close. It&#39;s just phenomenal. And I say that because I got to take my kids to see a fire truck that was at a event we went to it was an event with fireworks and stuff like that. So they had the local fire service on scene. But of course,they&#39;re just parked there killing time, you know, hoping they don&#39;t have a reason to do anything. And so they were perfectly happy to have kids come around and look. But I know station houses are generally that way too.</p>
  <cite>Jesse Brennan:</cite>
  <time>30:59</time>
  <p>Yep. 100%. As long as there&#39;s somebody there,they will, they will show you around. You might You might,especially with volunteer departments that are not typically staffed 24/7 Although we will take calls 24/7. So you might have to wait till a drill night or something. But I can&#39;t tell you how often we&#39;ve we&#39;ve had families come or or you know, a parent with a few kids come on a drill night where there&#39;s 20 of us there. And we&#39;re all fighting to show the apparatus off right now. No,I&#39;ll give them the tour. It&#39;s</p>
  <cite>Gene Liverman:</cite>
  <time>31:25</time>
  <p>That&#39;s really awesome. Thank you again for fine.your time and for sharing your story and I really do appreciate it.</p>
  <cite>Jesse Brennan:</cite>
  <time>31:35</time>
  <p>Same here.</p>
  <cite>Gene Liverman:</cite>
  <time>31:36</time>
  <p>Have a wonderful day.</p>
  <cite>Jesse Brennan:</cite>
  <time>31:38</time>
  <p>You as well.Thank you so much</p>
  <cite>Gene Liverman:</cite>
  <time>31:40</time>
  <p>Bye bye.You&#39;ve been listening to the volunteer technologist podcast.This is a value for value podcast, which means I will never charge you to listen. That said producing and hosting it does cost money. If you got value from today&#39;s show that I hope you&#39;ll consider contributing to its ongoing production by sending a boost with a new podcast app such as fountain or via the buy me a coffee link on volunteer technologist.com forward slash contribute. You can find shownotes transcripts and links to the things talked about in today&#39;s episode at volunteer technologist dot com Thanks for listening</p>

{{< /rawhtml >}}
{{< /tab >}}
{{< /tabs >}}
