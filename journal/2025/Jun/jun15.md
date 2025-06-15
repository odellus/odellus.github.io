---
date: "2025-06-15"
title: "Daily Journal - 15 Jun 2025"
---

```{note}
This is me thinking out loud, building in public, and showing the sausage being made. No editing, no polish - just raw thoughts and code.
```

## The Real Problem

The problem isn't that we lack ideas or eloquence - it's that our thoughts are fragmented across platforms and protocols. I can write extensively about software development in conversations with AI, but translating that into long-form content feels like an insurmountable task. This isn't about creating another AI writing tool to automate college essay slop generation. It's about building a system that helps organize our scattered knowledge into coherent structures, whether that's a tweet, a blog post, or a book. The goal is to help people maintain consistency, identify patterns in their thinking, and build on their ideas without losing the human element. Because the truth is, most of us are more capable than we realize - we just need help organizing our thoughts into something meaningful.

```{admonition} The Vision
:class: important
I launched a new site this weekend. I really liked the old one, but this is more than just a sexy CV site. Though tbh part of what I want to do when I do get the wntwnd clone working is put together better myst themes for sites than just book and article. MyST and jupyter book 2 are more tailored towards PDFs because it's mostly academic fucks who are using it so they can write markdown everywhere they don't need latex because that makes a hell of a lot of sense.
```

## Today's Mathematical Journey

I've been thinking a lot about high-dimensional spaces lately. It's one of those topics that keeps coming up in different contexts - from machine learning to quantum mechanics. The weird thing about high dimensions is how they completely break our 3D intuition. Let me walk through a proof that blew my mind when I first saw it.

### The N-Ball Properties

Let's prove two fascinating properties of high-dimensional spaces:

1. Points cluster near the surface of the N-ball
2. Any two points are approximately $\sqrt{2}$ units apart

# Radial Distance Distribution

What does the phrase "points cluster near the surface" really mean?  
Let $R\in[0,1]$ be the distance from the origin to a point picked 
*uniformly at random* inside the $n$–dimensional **unit** ball $B^n_1$.  
The probability that $R$ falls in $(r, r+dr)$ equals the fraction of the
ball's volume occupied by the thin spherical shell at that radius.  In
symbols,

:::{math}
:label: radial-pdf
f_n(r)\,dr\;=\;\frac{\text{vol of shell thickness }dr}{\text{vol}(B^n_1)}
            \;=\;\frac{S_{n-1}(r)\,dr}{V_n(1)},
:::

where $S_{n-1}(r)$ is the surface area of the $(n{-}1)$-sphere of radius
$r$ and $V_n(1)$ is the volume of the unit $n$-ball.
Because $V_n(r)=V_n(1)\,r^{n}$, differentiating with respect to $r$
shows that $S_{n-1}(r)=\tfrac{d}{dr}V_n(r)=n\,V_n(1)\,r^{n-1}$.  Plugging
this into the fraction above immediately gives the **probability-density
function**

:::{math}
:label: radial-pdf-closed
f_n(r)\;=\;n\,r^{n-1},\qquad 0\le r\le 1.
:::

## Meaning of $f_n(r)$

```{note}
$f_n(r)$ is the **probability-density function (PDF) of the distance $R$** from the centre of the $n$-dimensional unit ball to a uniformly chosen random point.  
Equivalently, $f_n(r)\,dr$ is the fraction of all points whose radius lies in the tiny interval $[r,r+dr]$.
```

---

## Why $f_n(r)=n\,r^{n-1}$

```{math}
\text{(thin shell volume)} 
    \;=\; \bigl[\text{surface area at radius }r\bigr]\,dr
    \;=\; S_n\,r^{\,n-1}\,dr,
```
where $S_n$ is the surface area of the unit $(n-1)$-sphere.

Because the point is chosen **uniformly**, its probability of landing in that shell is  
```{math}
\frac{S_n\,r^{\,n-1}\,dr}{V_n},
```
with $V_n$ the total volume of the unit $n$-ball.

The ratio $S_n/V_n$ equals $n$ for the unit ball, so  
```{math}
f_n(r)\,dr = n\,r^{\,n-1}\,dr
\quad\Longrightarrow\quad
f_n(r)=n\,r^{\,n-1}, \; 0\le r\le1.
```

The factor $r^{n-1}$ captures how the "room to place points" grows with radius, while the leading $n$ ensures the PDF integrates to 1.


:::{math}
\text{Because }V(r)=V_n r^{n}\text{ for an $n$-ball, } \frac{dV}{dr}=S_n(r)=\frac{d}{dr}\!\bigl(V_n r^{n}\bigr)=nV_n r^{\,n-1};\ \text{evaluating at }r=1\text{ gives }S_n=nV_n,\ \text{so } \dfrac{S_n}{V_n}=n.
:::


That single formula encapsulates the "surface concentration'' effect:
for large $n$ the density is negligible until $r$ is very close to $1$.
Indeed, $\mathbb E[R]=\tfrac{n}{n+1}\to 1$ and
$\operatorname{Var}(R)=\tfrac{1}{(n+1)(n+2)}\to 0$, so almost every point
lies within an $O\!\bigl(1/\sqrt n\bigr)$ shell of the boundary.

--- 

# Distance Between Two Random Points Concentrates at $\sqrt2$

Goal For independent, uniformly-random points  
$X,Y\in S^{\,n-1}\subset\mathbb R^{n}$ show  

```{math}
:label: goal
\lVert X-Y\rVert \;\xrightarrow{P}\; \sqrt2
```

as $n\to\infty$.



## Rewrite the distance via a dot product

Because $\lVert X\rVert=\lVert Y\rVert=1$,

```{math}
:label: dist-sq
\lVert X-Y\rVert^{2}=2\bigl(1-X\!\cdot\!Y\bigr).
```

Thus it suffices to prove $X\!\cdot\!Y\;\xrightarrow{P}\;0$.



## Model the sphere points with Gaussians

Represent each uniform point as a normalised Gaussian vector:

```{math}
:label: gaussian-model
X=\frac{Z}{\lVert Z\rVert},\qquad 
Y=\frac{W}{\lVert W\rVert},
```

where $Z_i,\,W_i\stackrel{\text{iid}}{\sim}\mathcal N(0,1)$ and
$Z\perp W$.

Then

```{math}
:label: dot-gamma
X\!\cdot\!Y=\frac{\sum_{i=1}^n Z_i W_i}{\lVert Z\rVert\,\lVert W\rVert}.
```



## Asymptotics of the numerator and denominators

* **Numerator**  
  Set $S_n=\sum_{i=1}^n Z_iW_i$.  Since
  $\mathbb E[Z_iW_i]=0$ and $\mathrm{Var}(Z_iW_i)=1$,

  ```{math}
  \frac{S_n}{\sqrt n}\;\Longrightarrow\;\mathcal N(0,1)
  ```
  (central-limit theorem).

* **Denominator**  
  By the law of large numbers  

  ```{math}
  \lVert Z\rVert^{2}=n\bigl(1+o(1)\bigr),
  \qquad
  \lVert W\rVert^{2}=n\bigl(1+o(1)\bigr),
  ```

  hence
  $\lVert Z\rVert\,\lVert W\rVert = n\bigl(1+o(1)\bigr)$.

Combine with [](#dot-gamma):

```{math}
X\!\cdot\!Y=\frac{1}{\sqrt n}\,\mathcal N(0,1)\bigl(1+o(1)\bigr)
           \;\xrightarrow{P}\;0.
```



## 4 Distance convergence

Insert $X\!\cdot\!Y\to 0$ into [](#dist-sq):

```{math}
\lVert X-Y\rVert^{2}\;\xrightarrow{P}\;2,
\qquad
\text{hence}\qquad
\lVert X-Y\rVert\;\xrightarrow{P}\;\sqrt2,
```

which establishes the claim in [](#goal).

:::{note}
A variance estimate shows
$\lvert \lVert X-Y\rVert-\sqrt2\rvert = O_p\!\bigl(n^{-1/2}\bigr)$, i.e.
concentration tightens like $1/\sqrt n$.
:::






```{admonition} Why This Matters
:class: tip
This is exactly why I wanted to get MyST and $\LaTeX$ working - being able to write math like this, with proper equations and proofs, is crucial for sharing these ideas. I do math all the time, but it's usually on a notepad. Now I can actually publish my mathematical journey, with all the rigor and beauty intact.
```

---

## From Geometry to Robots

All right, brain back in *applied* mode.  The same tooling that renders
those crisp equations is powering my day-to-day robotics stack, so the
next section pivots from hollow $n$-balls back to slow and boring coding.

## What I'm Actually Working On

I'm knee deep in robotics! I spent a good hour or so working on getting maniskill hooked up to lerobot. Didn't end up connecting it to my robot and move the configuration over into the newly cloned repo because it's saturday night and I've just been crunching on my website and typesetting projects.

```{mermaid}
graph TD
    subgraph "Local Development"
        A[Editor] --> B[MyST/Jupyter Book]
        B --> C[Local Code Execution]
        B --> D[Math Rendering]
        B --> E[Interactive Elements]
    end

    subgraph "DO Droplet"
        F[Jumpbox] --> G[Authentication]
        F --> H[File Sync]
        F --> I[Basic Hosting]
    end

    subgraph "Home Infrastructure"
        J[Self-hosted Services] --> K[Heavy Computations]
        J --> L[Data Storage]
        J --> M[Access Control]
    end

    A --> F
    F --> J
    J --> A

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#bbf,stroke:#333,stroke-width:2px
    style J fill:#bfb,stroke:#333,stroke-width:2px
```

```{admonition} The Architecture
:class: tip
This is the architecture I'm building - local development with the power of executable books, a DO droplet as a jumpbox, and self-hosted services at home. No unnecessary cloud dependencies, just pure control over your infrastructure.
```

## The Big Picture

I already live in the power-user endgame—VS Code, GitHub Pages, and an AI co-pilot wired straight into my editor. Spinning up a static site or a $\LaTeX$-heavy blog post is *possible* today; the real pain is in the dozen tiny steps that sit between inspiration and a shareable link. Those paper-cuts don't just slow me down—they keep everyone else from even trying.

So the goal isn't to invent new powers, it's to *compress* the ones we have into a single, low-friction loop that anyone who can type Markdown can ride.

1. **Capture → Journal extension.**  Works right inside whatever editor you love. Jot an idea, tag it, and it's instantly part of the knowledge graph—no copy-pasting, no context switching.
2. **Refine → *whtwnd* editor.**  One click promotes a note into a full-blown article lab. Live code blocks, $\LaTeX$ rendering, and a design system that makes even dense proofs look readable.
3. **Publish → Zero-touch deploy.**  The build spins up locally, ships through a DO jump-box, and lands in GitHub Pages (or your own server) without you touching a terminal. Good-looking, citation-ready pages, every time.

If we can make *that* cycle feel as effortless as pressing ⌘-S, then the subject matter—robotics tutorials, category-theory deep dives, garden-variety blog posts—becomes almost incidental. And when the tooling handles my edge-case chaos, chances are it will feel like magic for everyone else.



# Okay one bad thing

Now I feel like I have to make every damn post all sparkly and sexy and cool like I give a single solitary fuck. Yeah that's a definite reason to work hard to get whtwnd up and running. You can have posts that aren't visible to the public, though I don't know if that means people can't go see if they're on your PDS lol.

So I am going to use the designs for the base but I think I'm going to modify both the bottom part of the camera post but also the top. Try to get them pointing at the same basic work area for a nice degree of separation and difference in POV. I'm going to turn them like 30 degrees inward even though that might not be enough. It will create more overlapping field of vision in the cameras than having them both stare straight down.

They just seem like a collision obstacle right now, so I'm going to kick them out by extending the STL file somehow. I wish people shared the actual parametric models instead of just the STL meshes. Oh well. I can probably reinvent the part I need just looking at it, which I've already started doing.

---

# Multiple posts in a day, or one big ass journal entry?

I don't know! Certainly seems like I'm doing on big post-a-day, but they can be themed of course. Posts can and definitely should be longer thought out and revisited.

I've got the framework for writing my book on robotics now. I need to do that.