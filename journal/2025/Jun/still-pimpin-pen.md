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

  thumbnail: _static/social-banner.png
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

I can also add the drafts in journal/drafts to this 