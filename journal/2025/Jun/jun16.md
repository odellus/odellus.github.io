---
date: "2025-06-16"
title: "Damn I'm going to need projects aren't I?"
numbering:
  enumerator: A1.%s
---


Well I guess it's Monday already. Dang. Time flies when you're having fun typesetting. One thing I'd like to do is give my journal entries titles and change their names to the title after I'm done editing. But starting off with yeah Daily Journal - DD Mon YYYY works fine.




:::::::{div}
:class: col-body-inset-left

:::::{tip}🤖  ManiSkill and SO-100
:icon: false
LeRobot and Sim2Real, together at last! I'm going to end up writing a book about articulated photogrammetry as I work in the field, aren't I?
:::::

:::::::


:::::::{div}
:class: col-body-inset-right

:::::{tip}📰  Typesetting with MyST
:icon: false
I decided to use a way too fancy
:::::

:::::::

They've got theorems!!!!
::::{prf:theorem} Some theorem
:label: some-theorem
Yada yada $\forall x \in \R$
:::{math}
\begin{align}
A + B &= C \\
A &= C - B
\end{align}
:::
::::


Via [](#some-theorem)



```{exercise} A very good exercise
:label: my-exercise

Recall that $n!$ is read as "$n$ factorial" and defined as
$n! = n \times (n - 1) \times \cdots \times 2 \times 1$.

There are functions to compute this in various modules, but let's
write our own version as an exercise.

In particular, write a function `factorial` such that `factorial(n)` returns $n!$
for any positive integer $n$.
```

Thus via [](#my-exercise)


These are just examples I'm taking from the [MyST guide](https://mystmd.org/guide/). I spent freaking _hours_ pouring over the code of the website to understand how their parser works to fit it into my CodeMirror fork of the site. Now I'm going through the content (which isn't actually a part of the site necessarily as they do all kinds of redirecting between their parser machine and the static content).

Just added a customer enumerator to the numbering because it makes it look better when it's N.1 something versus raw ass numbering like 1, 2, 3, thank you Count Dracula.

Anyway as I was saying via Eqn. [](#gauss-law) of [my work on electroscalar waves](/journal/2025/jun/scalar-waves)

[gauss-law]: /journal/2025/jun/scalar-waves#gauss-law


Hell yeah that's the fucking good shit right there. I can reference any labeled equation I write here. Oh man oh man oh man. This is nice! This is the whole reason I started fooling with MyST was I found I could do crossrefs without pandoc after hearing about jupyter book. So yeah now I am cross-linking to my journal posts. I can reference them in my books. I will probably create another folder for articles that's not as focused on extremely long form content like a book but deserves a better home than inside my journal directory. Something a little less automatic.

Still not thrilled about having to create a github deployment every time I want to update the site tbh. That's my least favorite thing honestly and what's most likely to light a fire under my butt to get me working towards hosting this sucker on advanced-eschatonics.com.

I mean for one thing I'm running it with myst start under the hood of `uv run nox` so it's a static site that can be deployed there by the same steps I see in the `deploy.yml`. I've just got to figure out how to make sure I don't fuck up the /xrpc or whatever endpoints it's using for authorization since advanced-eschatonics.com is my PDS right now.

Yes eventually I want to host my own whtwnd app with all the capabilities I have here over there, but I **really** needed to start just hosting my content in a way I'm happy with, and I was not happy with mathjax inside of jekyll.


I'm tired of typing all day into a damn chat window with a fucking LLM. I want to write and have it interact with me when I'm writing in new and low friction ways. I want deer-flow to be running in the background on everything I'm typing trying to analyze my interests and predict things that will be interesting to me. I mean google does this to a large extent already tbh.

I'm even more tired of posting on deer.social than I am of my new hobby of sitting with the LLM hours a day solving programming problems. I don't like social media brain. I despise the way people act on the internet. I should limit my activity more to posting in my journal and writing articles.


Yeah the more I think about it projects shouldn't just be a landing page. It needs to be a folder where the projects have their own site. Fuck what am I saying. They're going to have whole ass folders. Yeah this is how I should be keeping notes on my projects, not just chronologically. 


:::{danger}🌍 Taking over the world ⚔️
:icon: false
Oh and by the way, we're taking over the world.
:::


So thinking about this as a writing assistant when I'm using my code assistant right there makes me want to just fucking fork VS Code and sit on top of the now open source copilot extension and come up with a project manager/worker. You don't have to just sit there and yack at the thing and all of your content goes through a damn slop filter, you can write your notes and have the responses that are worth a shit tagged in your running documentation.

Yeah it probably needs lot of help but I mean we're talking about managing tasks and it's already git and science is reproducibility so it has me thinking it might make a lot of sense to think about this less as a website with fancy rendering (which it totally is), but something more like the new AI assistant in overleaf on steroids from a person with the vision to make this a reality. We need knowledge graphs of domains inside domains, specifically starting with math and CS and branching into chemistry, physics, and biology/medicine. Oh look who already works in medicine and is the fucking Head of AI R&D at a clinical assistant startup? Me. That's who. So I've got a lot of domain expertise in this whole "let's build agents" thing.

Generalize what I work with (code agents) on top of what I use them to build (digital clinical assistants) and I'm remarkably well positioned for even a very lofty goal such as the one I'm laying out here. Build a better digital researcher. That's Humberto.


I'm also working on the whole BC thing and struggling with dataset creation and generalization to different poses due to changes in my environment (bumping the fucking table because I live in my lab) and now the damn dataset is crap. So I haven't started printing out the new camera stand yet because I want to make some modifications and all they have shared are STL files which are a pain to translate into shapes in FreeCAD.

Honestly what I should be fucking doing is working on an AI agent to fucking learn to make parametric models from STL files because that's a huge part of what I want to write about. That's really the idea. Instead of collecting a bunch of posts that don't index worth shit on deer (I don't use bsky - I find butterfly semiotics noxious), put them somewhere that an agent that's going through my interests with a fine tooth comb, creating prs when I sleep and testing them, assembling a knowledge base of working research and code to go along with it as it slowly but surely extends into the real of digital twins. I mean we're here already.

:::{danger}🤖 **lerobot-sim2real**
:icon: false
[we're already there](https://github.com/StoneT2000/lerobot-sim2real)
:::

03:36 EDT
---
Dropped the tower I put together out of the parts twice and broke a part each time. So now I have 13 tower parts instead of 15. The 5 v1 parts I have actually fit inside the v2s so I have 18 parts now. I decided to unwrap the next spool of filament and get to printing out the next tower.

Just looked and I can get around 10 of these from a single spool and a spool costs ~$30 (give or take) so they're like \$3 a pop. I just broke \$6 worth of equipment. I'm going to be okay.

Hardware is expensive! Both times what I was doing was stupid, the second time less so. If I didn't already have a lesson that these things don't mind falling to pieces, the second go around definitely conviced me.

I've been trying to think of any other way to put these together than my original idea of using a cap and a base that are connected with rope. I need some way of tightening them up with a couple of eye bolts. They're cheap so needing four per tower is so no biggee.

Yep. Eye bolts and washers to tighten the ropes. I looked and the paracord rope is so cheap there's no reason not to use it. Tensegrity grow towers lmao.

The alternative is to do something similar where they're basically strapped to boards and they're still held together from some form of $z$-axis tension. I have a feeling I will end up strapping them to some kind of board because they've got no torsional resistance otherwise. Any torque on the tower ends and it falls to pieces. Makes me wonder about the dual tower. Can't back that up against a board. Maybe thin strips of plywood on the sides and just pull them tight to it with zip ties? Yeah something like that. It needs some structural stability it currently doesn't have.

Should probably try the rope approach first. Plywood sheeting isn't that pricey. I kind of figured I'd be building this out of wood. Don't have a grow tent, so I have to build some scaffolding for the towers. I've got one right now. I'm printing out another roll. Going to buy another few rolls and keep the momentum going.

04:38 EDT
---
I can REALLY tell I've been writing math and thinking about knowledge graphs and computer science and all of that fun stuff. Mind is racing a mile a minute.


I need a better bibliography, which I'm sure MyST offers.

And again, I really really really need to fork the book/article theme.

Almost as much as I needed to just publish a fucking jupyter book / MyST site already.

:::{figure} ../images/grow_tower_jun16.jpg
:label: grow-tower-jpg
We've got a grow tower.
:::

So extremely chuffed.