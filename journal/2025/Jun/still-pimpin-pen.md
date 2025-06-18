---
title: Still pimpin' pen
date: "2025-06-15"
---

My daily journal has already grown to be too unwieldy after focusing on it for a day! I guess I finally have something to say.

It's sort of blowing my mind that I'm technically going to be publishing my book as I write it but that's sort of the whole point of having my own journal/book site.

Okay I commented out that part of my `myst.yml`.
```yaml
version: 1
project:
  id: 91143d4d-0120-4764-9c1d-b16de83a4b9c
  title: Welcome
  authors:
    - name: Thomas Wood
      website: https://odellus.github.io/
      id: thomas
      orcid: 0009-0001-6099-2115
      github: odellus
      affiliations:
        - name: Phytomech Industries
          url: https://phytomech.com
  github: https://github.com/odellus/odellus.github.io
  plugins:
    - type: executable
      path: src/blogpost.py
    - src/socialpost.mjs
  toc:
    - file: index.md
    - file: about.md
    - file: projects.md
    # - file: books.md
    #   children:
    #     - title: Scientific Computing with Python
    #       children:
    #         - pattern: books/Scientific-Computing-with-Python/**{.ipynb,.md}
    - file: journal.md
      children:
        - title: '2025'
          children:
            - title: June
              children:
                - pattern: journal/2025/Jun/**{.ipynb,.md}

  thumbnail: _static/social-banner.jpg
site:
  template: book-theme
  options:
    folders: true
    logo_text: Thomas Wood
    favicon: _static/profile-color-circle-small.png
    style: _static/custom.css
  domains:
    - odellus.github.io
  nav:
    - title: About
      url: /about
    - title: Projects
      url: /projects
    # - title: Books
    #   url: /books
    - title: Journal
      url: /journal
```

unlike with journal posts, I don't want to necessarily share this automatically.

I can also add the drafts in journal/drafts to this. I did but I don't know when I'll ever use it.

Kinda feel like I'm on big brother but whatever. I mean I'm a poster on deer.social ffs. I'm already living in the bright eye of the panopticon.

In other words I decided to start publishing my scientific computing with python book live. Fuck it. I'm still not entirely sure what the final structure will be but the very first thing was going to be here's numpy.

I guess I do need to introduce more practical stuff in there and not just punt and say "here's `dir()` and `help()` you're welcome. Yeah what am I talking about this is terrible. Oh well. Somewhere to start.

23:11
---

Okay what's up?

What did I accomplish this weekend?
- Ripped off [Chris Holdgraf's website](https://chrisholdgraf.com/) shamelessly and published to [my own personal site](https://odellus.github.io)
- Got lerobot and manikill and [lerobot-sim2real](https://github.com/StoneT2000/lerobot-sim2real) set up and ready for further configuration with `uv` in a high reproducible manner
- Printed 10 [grow towers](https://github.com/OSRLab/vertical_grow_tower)
- Stopped being a wimp about filling up the hydroponics tank over the course of the day by setting timers to remind me when to turn it on and off
- Put the [first chapter](/books/scientific-computing-with-python/chapter-01) of the scientific computing with python book together


I've been meaning to put the book together for fucking years now. Now I have my own website that's not just a place to keep notes on what I've done but a place to publish it, I mean no joke I can just make a book out of jupyter notebooks and markdown files and host it at odellus.github.io like a crazy person.

I'm going to be revisiting each chapter in succession as I build up the subject material and yeah honestly I definitely need to motivate the reader with some worked examples showing the power of numpy to solve real world problems in science and engineering.

I think we really should start by building up towards the methods in maniskill and lerobot. Screw the nonsense. We picked the simulation framework and the learning/hardware framework because we're going to teach people about applied mathematics and that means simulations and optimization.

That's what we do. That's our whole business, and business is good.

I don't know every last little thing about how maniskill works right now, I'm not going to lie. But I know Emo Todorov and took some classes from him and I studied scientific and numerical computing under J. Nathan Kutz, who has written several books about the subject. That's my background. Heavy on SVD. Heavy on `ode45` and all of that jazz. 

I might not get right into Partial Differential Equations, but yeah we're going to have to go pretty deep into math to talk about what lerobot and maniskill do.



