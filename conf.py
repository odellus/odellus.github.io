# -- Project information -----------------------------------------------------
import sys

sys.path.append("scripts")
sys.path.append(".")
from social_media import add_social_media_js, SocialPost

project = "Thomas Wood"
copyright = "We don't need no stinking copyright"
author = "Thomas Wood"

extensions = [
    "myst_nb",
    "ablog",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_examples",
    "sphinxext.opengraph",
    "sphinxext.rediraffe",
]

# templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "*import_posts*",
    "**/pandoc_ipynb/inputs/*",
    ".nox/*",
    "README.md",
    "**/.ipynb_checkpoints/*",
]

# -- HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "navbar_align": "left",
    "show_navbar_depth": 3,  # This will show journal/2025/Jun
    "show_toc_level": 3,     # This will show journal/2025/Jun
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "navbar_secondary": ["page-toc"],
    "navbar_primary": ["navbar-nav"],
    "navbar_sidebar": ["sidebar-nav"],
    "navbar_sidebar_collapse": True,
    "navbar_sidebar_collapse_icon": True,
    "navbar_sidebar_collapse_style": "overlay",
}

# html_theme_options = {
#     "search_bar_text": "Search this site...",
#     "analytics": {"google_analytics_id": "UA-88310237-1"},
#     "icon_links": [
#         {
#             "name": "GitHub",
#             "url": "https://github.com/choldgraf/",
#             "icon": "fa-brands fa-github",
#         },
#         {
#             "name": "Twitter",
#             "url": "https://twitter.com/choldgraf",
#             "icon": "fa-brands fa-twitter",
#         },
#         {
#             "name": "Mastodon",
#             "url": "https://hachyderm.io/@choldgraf",
#             "icon": "fa-brands fa-mastodon",
#             "attributes": {"rel": "me"},
#         },
#         {
#             "name": "Blog RSS feed",
#             "url": "https://chrisholdgraf.com/blog/atom.xml",
#             "icon": "fa-solid fa-rss",
#         },
#     ],
# }

html_favicon = "_static/profile-circle.png"
html_title = "Thomas Wood"
html_static_path = ["_static", "images"]
html_extra_path = ["feed.xml"]
html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    "publications": ["hello.html"],
    "projects": ["hello.html"],
    "talks": ["hello.html"],
    "journal": ["ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"],
    "journal/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}

# OpenGraph config
ogp_site_url = "https://odellus.github.io"
ogp_social_cards = {
    "line_color": "#4078c0",
    "image": "_static/social-banner.jpg",
}

ogp_image = "_static/social-banner.jpg"
ogp_use_first_image = False

rediraffe_redirects = {
    "rust-governance.md": "blog/2018/rust_governance.md",
}
# Update the posts/* section of the rediraffe redirects to find all files
redirect_folders = {
    "posts": "journal",
}
from pathlib import Path

for old, new in redirect_folders.items():
    for newpath in Path(new).rglob("**/*"):
        if newpath.suffix in [".ipynb", ".md"] and "ipynb_checkpoints" not in str(
            newpath
        ):
            oldpath = str(newpath).replace("journal/", "posts/", 1)
            # Skip pandoc because for some reason it's broken
            if "pandoc" not in str(newpath):
                rediraffe_redirects[oldpath] = str(newpath)

# -- ABlog ---------------------------------------------------

blog_baseurl = "https://odellus.github.io"
blog_title = "Thomas Wood"
blog_path = "journal"
blog_post_pattern = "journal/*/*/*"  # This matches our myst.yml pattern
blog_feed_fulltext = True
blog_feed_subtitle = "Come along and ride on a fantastic voyage"
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 0
post_auto_excerpt = 2

# Use case-sensitive paths for URLs
blog_post_url_format = "{path}"
blog_post_pattern_format = "{path}"
blog_post_date_format = "{path}"
blog_post_slug_format = "{path}"

# -- MyST and MyST-NB ---------------------------------------------------

# MyST
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",  # Add this for $...$ inline math
    "html_image",
]

# MyST-NB
# Don't execute anything by default because many old posts don't execute anymore
# and this slows down build times.
# Instead if I want something to execute, manually set it in the post's metadata.
nb_execution_mode = "off"


def setup(app):
    app.add_directive("socialpost", SocialPost)
    app.connect("html-page-context", add_social_media_js)
    app.add_css_file("custom.css")
