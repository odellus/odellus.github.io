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
$$  
:label: pseudoinv
U := (G G^{\sf T})^{-1/2}\;G\qquad (\text{i.e. the “left–normalised” version of }G)  
$$
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
$$  
\begin{aligned}
B_k &:= \beta\, A_k + \gamma\, A_k^{2},\\[2mm]
X_{k+1} &:= \alpha\, X_k + B_k X_k,
\end{aligned}
$$
with the tabulated coefficients  
$$
\alpha=3.4445,\quad \beta=-4.7750,\quad \gamma=2.0315.
$$
These constants were obtained by a *polynomial fit* to the third-order Newton–Schulz iteration ([Hale–Higham–Trefethen, 2008][matrix-func-computing]).  In exact arithmetic the recurrence realises a **rational function** $p,q\in \mathbb Q[x]$:  
$$
X_{k+1}= p(A_k) X_k q(A_k)^{-1}
$$
that approximates the sign-function of $A$ at unit circle – hence driving the singular values of $A_k$ to 1.  

###  **Transpose back**

If the original $G$ was wide we set   
$$
\boxed{U\ \text{return} := X_{\text{steps}}^{\sf T}}
$$ 

yielding the required pseudo-inverse matrix Eqn.[](#pseudoinv)  
$$
U \ \approx\ (G G^{\sf T})^{-1/2} G ,
$$
and the singular values $\sigma_i(U)\in[1-\delta,1+\delta]$ where $\delta\sim 10^{-3}$ after five steps.

--------------------------------------------------------------------
### **Remarks**

- Iteration occurs entirely in **bfloat16** so the cost per step is low; single accumulation at the end keeps the exponent range.

- Conceivably $G^{\text{T}}G$ can also be inverted but the above order minimises memory traffic.

- The algorithm is essentially a **Newton method for**  
$$
\operatorname{sign}(X X^{\sf T})=I,
$$
projected on the orthogonal group restricted to the column space of $G$.


[agentic-web]: https://doi.org/10.48550/arXiv.2507.21206
[hrm]: https://doi.org/10.48550/arXiv.2506.21734
[muon-opt]: https://doi.org/10.48550/arXiv.2502.16982
[muon-blog]: https://kellerjordan.github.io/posts/muon/
[whtwnd]: https://whtwnd.com
[matrix-func-computing]: https://doi.org/10.1137/070700607