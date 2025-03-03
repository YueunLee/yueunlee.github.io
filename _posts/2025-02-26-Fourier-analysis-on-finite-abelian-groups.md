---
title: Fourier Analysis on Finite Abelian Groups
---

In Fourier analysis on $\mathbb{C}$, complex-valued functions can be approximated as sums of exponentials. A similar approach applies to finite abelian groups. Let $V$ be the vector space of all complex-valued functions defined on a finite abelian group $G$. When $G = \mathbb{Z}_N = \mathbb{Z}/N\mathbb{Z}$, the set $\\{ f_n \mid f_n(k) = w^{nk}, \, n \in \mathbb{Z}_N \\}$ forms an orthonormal basis of $V$, where $w = e^{2\pi i / N}$. Moreover, this basis is isomorphic to $\mathbb{Z}_N$, as the mapping between $n$ and $f_n$ defines an isomorphism.

To extend this framework to general finite abelian groups, we first construct an orthonormal basis of $V$. A character is defined as a homomorphism from $V$ to $\mathbb{C}^\*$. For $\mathbb{Z}_N$, the characters are precisely the functions $f_n$ described earlier. These characters form a group under function composition, known as the dual group of $G$, denoted by $\hat{G}$. A straightforward verification shows that $\hat{G}$ is an orthonormal subset of $V$.  

Since any finite abelian group can be expressed as a direct product of cyclic groups $\mathbb{Z}_N$, the dual group $\hat{G}$ can be similarly decomposed as a direct product of $\widehat{\mathbb{Z}_N}$. Given that $\widehat{\mathbb{Z}_N} \cong \mathbb{Z}_N$, we obtain $\hat{G} \cong G$, which implies $\lvert \hat{G} \rvert = \lvert G \rvert = \dim(V)$. Consequently, the group of characters $\hat{G}$ forms an orthonormal basis of $V$.  

This guarantees that any function on $G$ can be expressed as  

$$
f = \sum_{\chi \in \hat{G}} \hat{f}(\chi) \chi, \quad \hat{f}(\chi) = (f, \chi) = \frac{1}{\lvert G \rvert} \sum_{a \in G} f(a) \overline{\chi(a)}.
$$  

At this stage, we are ready to prove Dirichlet's theorem, which states that there are infinitely many primes satisfying $p\equiv a(\mathrm{mod}\ m)$ when $a$ and $m$ are coprime. Let $V = \mathbb{Z}_m^\*$ and extend characters on $\mathbb{Z}_m^\*$ to $\mathbb{Z}_m$ by setting them to zero outside the original domain. Noting that
$$
\delta_a(n)=\sum_{\chi}\hat{\delta}_a(\chi)\chi(n)=\sum_{\chi}\chi(n)\cdot\frac{1}{\varphi(m)}\sum_{l\in\mathbb{Z}_m^\*}\delta_a(l)\overline{\chi(l)}=\frac{1}{\varphi(m)}\sum_{\chi}{\chi(n)\overline{\chi(a)}},
$$
we obtain
$$
\sum_{p\equiv a(\mathrm{mod}\ m)}\frac{1}{p^s}=\sum_{p}\frac{1}{p^s}\cdot\frac{1}{\varphi(m)}\sum_{\chi}{\chi(p)\overline{\chi(a)}}=\frac{1}{\varphi(m)}\sum_{\chi}{\overline{\chi(a)}\sum_{p}{\frac{\chi(p)}{p^s}}} \\
= \frac{1}{\varphi(m)}{(\sum_{p}{\frac{\chi_0(p)}{p^s}}+\sum_{\chi\not ={\chi_0}}{\overline{\chi(a)}}\sum_{p}{\frac{\chi(p)}{p^s}})},
$$
where $\chi_0$ is the principal character that takes the value 1 on all elements of $\mathbb{Z}_m^\*$ and 0 elsewhere. Since these series converge uniformly for $s>1$, they are continuous in this region. Taking the limit as $s\rightarrow1^+$, the first term on the right-hand side diverges to infinity. If we can establish that
$$
\sum_{p}{\frac{\chi(p)}{p}} \text{ is finite for }\chi\not =\chi_0,
$$
then the right-hand side also diverges, implying
$$
\sum_{p\equiv a(\mathrm{mod}\ m)}\frac{1}{p}=\infin,
$$
which confirms the infinitude of primes satisfying $p\equiv a(\mathrm{mod}\ m)$. Thus, it remains to prove this finiteness on the non-principal characters, which leads us to define L-function as follows:
$$
L(s,\chi)=\sum_{n}{\frac{\chi(n)}{n^s}}.
$$



