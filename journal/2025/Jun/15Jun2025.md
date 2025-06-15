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

### Surface Concentration

Let's first derive the closed-form formulas for an $n$-ball:

:::{math}
:label: ball-formulas
\begin{align}
V_n(R) &= \frac{\pi^{n/2}}{\Gamma\!\bigl(\tfrac{n}{2}+1\bigr)}\,R^{\,n} \\
S_{n-1}(R) &= \frac{2\,\pi^{n/2}}{\Gamma\!\bigl(\tfrac{n}{2}\bigr)}\,R^{\,n-1}
\end{align}
:::

::::{note}
:class: collapsible
### Deriving the closed-form formulas for an $n$-ball

#### 1. Start with the $n$-dimensional Gaussian integral
Cartesian factorisation gives:

:::{math}
:label: gaussian
\begin{align}
I_n = \int_{\mathbb R^{n}}e^{-\lVert x\rVert^{2}}d^{\,n}x
    = \Bigl(\int_{-\infty}^{\infty}e^{-t^{2}}dt\Bigr)^{\!n}
    = \pi^{\,n/2}
\end{align}
:::

#### 2. Rewrite in spherical coordinates
Using $d^{\,n}x=r^{\,n-1}dr\,d\Omega$ and letting $S_{n-1}(1):=\displaystyle\int_{S^{n-1}}d\Omega$:

:::{math}
:label: spherical
\begin{align}
I_n = S_{n-1}(1)\int_{0}^{\infty}r^{\,n-1}e^{-r^{2}}dr
\end{align}
:::

#### 3. Evaluate the radial integral
Set $u=r^{2}\;(du=2r\,dr)$:

:::{math}
:label: gamma
\begin{align}
\int_{0}^{\infty}r^{\,n-1}e^{-r^{2}}dr
   = \frac12\int_{0}^{\infty}u^{\tfrac{n}{2}-1}e^{-u}du
   = \frac12\,\Gamma\!\Bigl(\frac{n}{2}\Bigr)
\end{align}
:::

#### 4. Solve for surface area
:::{math}
:label: surface
\begin{align}
\pi^{n/2} = S_{n-1}(1)\;\frac12\,\Gamma\!\Bigl(\frac{n}{2}\Bigr)
\;\;\Longrightarrow\;\;
S_{n-1}(1) = \frac{2\,\pi^{n/2}}{\Gamma\!\bigl(\tfrac{n}{2}\bigr)}
\end{align}
:::

#### 5. Integrate shells for volume
:::{math}
:label: volume
\begin{align}
V_n(1) = \int_{0}^{1}S_{n-1}(r)\,dr
       = \int_{0}^{1}S_{n-1}(1)\,r^{\,n-1}dr
       = \frac{S_{n-1}(1)}{n}
       = \frac{\pi^{n/2}}{\Gamma\!\bigl(\tfrac{n}{2}+1\bigr)}
\end{align}
:::

#### 6. Scale to general radius $R$
:::{math}
:label: scaling
\begin{align}
V_n(R) = V_n(1)\,R^{\,n},\qquad
S_{n-1}(R) = S_{n-1}(1)\,R^{\,n-1}
\end{align}
:::

Combining (4), (5), and (6) yields the desired closed forms.

### Quick Gamma-function checkpoints
- **Recurrence:** $\Gamma(z+1)=z\,\Gamma(z)$, giving $\Gamma(n)=(n-1)!$
- **Half-integer base:** $\Gamma\!\bigl(\tfrac12\bigr)=\sqrt{\pi}$

The Gamma function appears naturally because the radial Gaussian integral in (3) is exactly its defining integral at $z=n/2$.
::::

### Distance Concentration

The pairwise distance convergence to $\sqrt{2}$ follows from three key insights:

1. By the Central Limit Theorem, the random sum $S_n$ grows like $\sqrt{n}$
2. By the Law of Large Numbers, each vector's length grows like $\sqrt{n}$; the product of two such lengths therefore grows like $n$
3. Dividing the $\sqrt{n}$-sized numerator by the $n$-sized denominator forces the dot product toward 0 at speed $1/\sqrt{n}$

Once $\langle X,Y \rangle$ goes to 0, the equation:

:::{math}
:label: distance
\begin{align}
|X-Y|^2 = 2(1 - \langle X,Y \rangle)
\end{align}
:::

immediately gives the distance concentration at $\sqrt{2}$.

This is why high-dimensional spaces behave so differently from our 3D intuition - the points are all effectively on the surface of a hollow shell (as shown in Eqn. [](#ball-formulas)), and they're all roughly the same distance apart (as shown in Eqn. [](#distance)).

```{admonition} Why This Matters
:class: tip
This is exactly why I wanted to get MyST and LaTeX working - being able to write math like this, with proper equations and proofs, is crucial for sharing these ideas. I do math all the time, but it's usually on a notepad. Now I can actually publish my mathematical journey, with all the rigor and beauty intact.
```

## What I'm Actually Working On

I'm knee deep in robotics! I spent a good hour or so working on getting maniskill hooked up to lerobot. Didn't end up connecting it to my robot and move the configuration over into the newly cloned repo because it's saturday night and fuck I've just been crunching on my own projects.

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

So here's where we are: I'm knee-deep in robotics with maniskill and lerobot, but that's just one piece of the puzzle. The real work is building a system that helps people explore and share their ideas - whether that's robotics, math, or anything else.

The journal extension we're working on is the first step. It helps organize thoughts into a structure that makes sense, but it's not just about organization. It's about creating a space where people can write in their own voice, explore complex ideas, and share their knowledge while maintaining their authentic style.

The whtwnd clone is the next piece - a proper editor that helps people write and explore technical content. It's not just about making things look pretty. It's about creating a tool that helps people write more effectively, explore complex ideas, and share their knowledge while maintaining their authentic voice.

And the MyST/Jupyter Book integration ties it all together. It's not just about making things look pretty. It's about creating a system that helps people write more effectively, explore complex ideas, and share their knowledge while maintaining their authentic voice.

The goal isn't to replace human writing - it's to help people be more intentional about how they organize and present their thoughts, whether that's a tweet, a blog post, or a full-blown book. Most of us are more eloquent than we seem - we just need help getting our thoughts together.