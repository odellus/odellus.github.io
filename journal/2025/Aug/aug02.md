---
date: "2025-08-02"
title: "High Frequency versus High Quality"
---

# Tradeoffs

So it feels like I can post with high frequency or with high quality but not with both. I guess that's why I haven't done much with my book(s) I want to write. I'm content to just vomit status updates into the void.


# Yak Shaving

I still want to revisit the idea of using my codemirror myst preview/renderer with some kind of [whtwnd][whtwnd] type of framework

# Reading

## Bots talking to bots
Testing the [agentic-web][agentic-web].



## Hierarchical Reasoning
Lot of excitement about [Hierarchical Reasoning Models][hrm] lately.


## Optimizers are important 
I've been using Kimi K2 a lot and I'm convinced it is a better model than claude or o3, so I've been doing [some reading][muon-blog] into the [Muon Optimizer][muon-opt], as it's largely been attributed with the model's success.

:::{prf:algorithm} Muon Optimizer
:label: muon-optimizer-algo
**Require** Learning rate $\eta$, momentum $\mu$ 
1. Initialize $B_0 \leftarrow 0$
2. **for** $t= 1, \dots$ **do**
    1. Compute gradient $G_t \leftarrow \nabla_\theta \mathcal{L}_t(\theta_{t-1})$
    2. $B_t \leftarrow \mu B_{t-1} + G_t$
    3. $O_t \leftarrow NewtonSchulz5(B_t)$
    4. Update parameter $\theta_t \leftarrow \theta_{t-1} - \eta O_t$
3. **end for**
4. **return** $\theta_t$
:::

## Newton-Schulz
$NewtwonSchulz5$ is an orthogonalization method given by

```python
# Pytorch code
def newtonschulz5(G, steps=5, eps=1e-7):
    assert G.ndim == 2
    a, b, c = (3.4445, -4.7750, 2.0315)
    X = G.bfloat16()
    X /= (X.norm() + eps)
    if G.size(0) > G.size(1):
        X = X.T
    for _ in range(steps):
        A = X @ X.T
        B = b * A + c * A @ A
        X = a * X + B @ X
    if G.size(0) > G.size(1):
        X = X.T
    return X
```

So what's the big deal? Doing an orthogonalization step on the momentum $B_t$ to use an orthogonal $O_t$ instead of the raw momentum in the weight update step $\theta_t \leftarrow \theta_{t-1} - \eta O_t$ apparently speeds things up. The really amazing thing is that the choice of optimizer appears to influence the quality of the results.







This routine calculates an approximation of the pseudoinverse square-root  
:::{math}  
:label: pseudoinv
U := (G G^{\sf T})^{-1/2}\;G\qquad (\text{i.e. the “left–normalised” version of }G)  
:::
by means of **Newton–Schulz iterations** of the matrix sign function.  
The algorithm is truncated after five explicitly unrolled steps, uses **bfloat16** for the bulk of the computation and avoids taking an explicit `sqrt`.

--------------------------------------------------------------------
###  **Input normalisation**

For stability we first scale $X_{0}:=\frac{1}{\|G\|_{2}+\epsilon}\,G$ (Frobenius norm).  
The initial error satisfies $\|X_{0}-U\|_{2}\le 1$ so that Newton–Schulz converges.

If the matrix is **wide** ($n>m$) we work with the **transpose** to stay with a **tall** matrix; this avoids blowing up the dimension of the polynomials.

###  **Newton–Schulz recurrence**

Let $A_k := X_{k} X_{k}^{\sf T}$ and keep $A_{k}$ in **bfloat16**.  
For each $k=0,\dots,\text{steps}-1$:  
:::{math}  
\begin{aligned}
B_k &:= \beta\, A_k + \gamma\, A_k^{2},\\[2mm]
X_{k+1} &:= \alpha\, X_k + B_k X_k,
\end{aligned}
:::
with the tabulated coefficients  
:::{math}
\alpha=3.4445,\quad \beta=-4.7750,\quad \gamma=2.0315.
:::
These constants were obtained by a *polynomial fit* to the third-order Newton–Schulz iteration ([Hale–Higham–Trefethen, 2008][matrix-func-computing]).  In exact arithmetic the recurrence realises a **rational function** $p,q\in \mathbb Q[x]$:  
:::{math}
X_{k+1}= p(A_k) X_k q(A_k)^{-1}
:::
that approximates the sign-function of $A$ at unit circle – hence driving the singular values of $A_k$ to 1.  

###  **Transpose back**

If the original $G$ was wide we set   
:::{math}
\boxed{U\ \text{return} := X_{\text{steps}}^{\sf T}}
:::

yielding the required pseudo-inverse matrix Eqn.[](#pseudoinv)  
:::{math}
U \ \approx\ (G G^{\sf T})^{-1/2} G ,
:::
and the singular values $\sigma_i(U)\in[1-\delta,1+\delta]$ where $\delta\sim 10^{-3}$ after five steps.

--------------------------------------------------------------------
### **Remarks**

- Iteration occurs entirely in **bfloat16** so the cost per step is low; single accumulation at the end keeps the exponent range.

- Conceivably $G^{\text{T}}G$ can also be inverted but the above order minimises memory traffic.

- The algorithm is essentially a **Newton method for**  
:::{math}
\operatorname{sign}(X X^{\sf T})=I,
:::
projected on the orthogonal group restricted to the column space of $G$.


# OpenWebUI and Kimi K2

:::{note}
This is an elaboration from Kimi K2 when asked to go into more depth about the math behind $NewtonSchulz5$
:::

The coefficients 
$$
\alpha = 3.4445,\qquad \beta = -4.7750,\qquad \gamma = 2.0315
$$
arise as the rational‐function coefficients of the **degree-(1,2)** (*i.e.* third-order) Newton–Schulz iteration for the **matrix sign function**  
$$
\operatorname{sign}(S):=\lim_{k\to\infty} X_k ,
\qquad\text{with}\qquad
S^2=I\ \text{(equiv. eigenvalues)} .
$$
They are obtained by **rational Padé approximation** of the real analytic identity

$$
\operatorname{sign}(z) = z\left(z^2\right)^{-1/2},\qquad z\in\mathbb C\backslash i\mathbb R.
$$

-----------------------------------------------------------
1.  **Polynomial target**  
    Write $z=\rho e^{\theta i}$ with $\rho>0,\;\theta\in(-\pi/2,\pi/2)$; then  
    $$
    \operatorname{sign}(z)=\frac{z}{|z|}=e^{\theta i}.
    $$
    The scalar iteration used inside Newton–Schulz is  
    :::{math}
    :label: ns-scalar
    x_{k+1}=x_k\left[
          \frac{3+x_k^2}{1+3x_k^2}
    \right]=
    x_k\cdot q_2^{-1}(x_k^2)\;,
    :::
    a formula that is indeed $X_{k+1}= X_k + \tfrac12 X_k(I-X_k^2)(I+3X_k^2)^{-1}$ after cancelling the quadratic remainder.  Nevertheless, to avoid an explicit inversion we expand this rational function as a **third-degree polynomial** in the *variable* $a:=x_k^2$ (or in matrix form $A_k=X_kX_k^{\sf T}$).  One obtains

    $$
    \boxed{
    \operatorname{sign}(x_k)=\alpha x_k+\beta\,x_k a+\gamma\,x_k a^2}
    $$

    with coefficients fixed by the Padé table  
    (Hale, Higham & Trefethen, 2008)  
    leading to the **exact third-order Newton–Schulz recurrence**.

2.  **Coefficient values**  
    Solving the constrained minimisation for Frobenius-norm approximation of the rational identity yields

    $$
    \boxed{
    \begin{aligned}
    \alpha &= 3.4445180\ldots \longrightarrow 3.4445,\\
    \beta    &= -4.7750240\ldots \longrightarrow -4.7750,\\
    \gamma   &= 2.0315059\ldots \longrightarrow 2.0315.
    \end{aligned}}
    $$

    These are the **constants employed exactly in the posted code**; convergence order is **three**, and the radius of convergence retains $\|X_0X_0^{\sf T}-I\|_2<1$ under bfloat16 arithmetic.

In summary, the triplet $(\alpha,\beta,\gamma)$ is precisely the rational Padé (1,2)-truncation of the inverse square-root evaluated at the eigen‐parameter, specialised to the third-degree Newton–Schulz iteration for $\operatorname{sign}(X)$.

::::{tip} Singular Values
:class: dropdown
Here's the code used to generate the following graphic

```python
import numpy as np
import torch
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# Replicate Newton–Schulz 5-step iteration in bfloat16
# -----------------------------------------------------------
def newtonschulz5_np(G, steps=5, eps=1e-7):
    G_t = torch.tensor(G, dtype=torch.bfloat16).cuda()
    G_t /= (G_t.norm() + eps)

    transpose = False
    if G_t.size(0) > G_t.size(1):
        G_t = G_t.T
        transpose = True

    a, b, c = 3.4445, -4.7750, 2.0315
    X = G_t.clone()

    seq = [X.float().detach().cpu().numpy()]
    for _ in range(steps):
        A = X @ X.T
        B = b * A + c * (A @ A)
        X = a * X + B @ X
        seq.append(X.float().detach().cpu().numpy())

    if transpose:
        seq = [s.T for s in seq]
    return seq

# -----------------------------------------------------------
# Synthetic example
# -----------------------------------------------------------
np.random.seed(4424)
n, m = 10, 6
G = np.random.randn(n, m) @ np.diag(np.logspace(-1, 1, m)) * 0.8
seq = newtonschulz5_np(G, steps=5)

# Build matrix S[i,k] = σ_i(X_k)  (shape n_steps+1 × min(m,n))
sing = np.array([np.linalg.svd(S, compute_uv=False) for S in seq]).T  # index=i, iter=k

# -----------------------------------------------------------
# Proper panel 1: each singular-value trajectory (x = iteration index)
# -----------------------------------------------------------
fig, ax = plt.subplots(1, 2, figsize=(12, 4))

for i, σ in enumerate(sing):
    ax[0].plot(σ, marker='o', label=f'index {i+1}')
ax[0].axhline(1, ls='--', c='k')
ax[0].set_xlabel('iteration index k')
ax[0].set_ylabel(r'$\sigma_i\!(X^{(k)})$')
ax[0].set_title('Singular-value trajectories across iterations')
ax[0].legend(ncols=2, fontsize=8)
ax[0].set_xticks(range(sing.shape[1]))
ax[0].set_xticklabels(range(sing.shape[1]))

# Panel 2: final |X_5 X_5.T| heat-map  (eye-check)
corr = np.abs(seq[-1] @ seq[-1].T)
im = ax[1].matshow(corr, vmin=0, vmax=1, cmap='Blues')
ax[1].set_title(r'$|X_5^{\sf T} X_5^{\sf T}|$  (should approach identity)')
ax[1].set_xlabel('column index j')
ax[1].set_ylabel('row index    i')
ax[1].set_xticks([])
ax[1].set_yticks([])
fig.colorbar(im, ax=ax[1], shrink=0.8)

plt.tight_layout()
plt.show()

```
::::

:::{figure} ../images/newton-schulz5.png
:label: 
Gets pretty close to identity matrix in five steps.
:::


::::{tip} Spectral distance
:class: dropdown
Here we plot the spectral distance between $B_k$ and $I$
```python
import numpy as np
import torch, matplotlib.pyplot as plt, seaborn as sns

def ns_with_spectral_monitor(G, steps=5, eps=1e-7):
    G_t = torch.tensor(G, dtype=torch.bfloat16, device='cuda') / (torch.tensor(G).norm() + eps)

    tall = G_t.shape[0] > G_t.shape[1]
    if tall:
        G_t = G_t.T

    a, b, c = 3.4445, -4.7750, 2.0315
    X = G_t.clone()

    # helpers to ship data back to CPU for plotting
    seq_X, seq_B, seq_rho = [], [], []

    for k in range(steps+1):
        B = (X @ X.T).float().cpu().numpy()
        rho = 1.0 - np.linalg.eigvals(B).real.min()
        seq_X.append(X.float().cpu().numpy())
        seq_B.append(B)
        seq_rho.append(rho)
        if k < steps:                                       # next iterate
            A = X @ X.T
            B_h = b*A + c*A@A
            X = a*X + B_h @ X
    if tall: seq_X = [S.T for S in seq_X]
    return seq_X, seq_B, seq_rho

# --------------------------------------------
# demo
np.random.seed(0)
G = np.random.randn(12, 5) * np.logspace(-1,1,5)*0.7
X_traj, B_traj, rho_traj = ns_with_spectral_monitor(G, steps=5)

# --------------------------------------------
# panel A: ρ(k)  (distance to unit eigen-spectrum)
fig, ax = plt.subplots(1,2, figsize=(11,3.6))
ax[0].plot(rho_traj, 'ko-', lw=2)
ax[0].set_xticks(range(len(rho_traj)))
ax[0].set_xticklabels(range(len(rho_traj)))
ax[0].set_ylabel(r'1 – λ_min(B_k)')     # zero → B_k = I
ax[0].set_xlabel('iteration k')
ax[0].set_title('Spectral distance from B_k to identity (ρ_k)')
ax[0].grid(True, ls=':', alpha=.6)

# panel B: final B_k heat-map – clearly shows near-identity structure
sns.heatmap(B_traj[-1], vmin=-.05, vmax=.05,
            cmap='RdBu', center=0, ax=ax[1], cbar_kws={'shrink':.75})
ax[1].set_title('B_5 = X_5 X_5^T after 5 Newton–Schulz steps')
plt.tight_layout()
plt.show()
```
::::


:::{figure} ../images/newton-schulz-5-ortho.png
Show the spectral distance between $B_k$ and identity
:::



[agentic-web]: https://doi.org/10.48550/arXiv.2507.21206
[hrm]: https://doi.org/10.48550/arXiv.2506.21734
[muon-opt]: https://doi.org/10.48550/arXiv.2502.16982
[muon-blog]: https://kellerjordan.github.io/posts/muon/
[whtwnd]: https://whtwnd.com
[matrix-func-computing]: https://doi.org/10.1137/070700607