---
title: Dirichlet's theorem
mathjax: true
---

## 1. Fourier Analysis on Finite Abelian Groups

In Fourier analysis on $\mathbb{C}$, complex-valued functions can be approximated as sums of exponentials. A similar approach applies to finite abelian groups. Let $V$ be the vector space of all complex-valued functions defined on a finite abelian group $G$. When $G = \mathbb{Z}_N = \mathbb{Z}/N\mathbb{Z}$, the set $\\{ f_n \mid f_n(k) = w^{nk}, \, n \in \mathbb{Z}_N \\}$ forms an orthonormal basis of $V$, where $w = e^{2\pi i / N}$. Moreover, this basis is isomorphic to $\mathbb{Z}_N$, as the mapping between $n$ and $f_n$ defines an isomorphism.

To extend this framework to general finite abelian groups, we first construct an orthonormal basis of $V$. A character is defined as a homomorphism from $V$ to $\mathbb{C}^*$. For $\mathbb{Z}_N$, the characters are precisely the functions $f_n$ described earlier. These characters form a group under function composition, known as the dual group of $G$, denoted by $\hat{G}$. A straightforward verification shows that $\hat{G}$ is an orthonormal subset of $V$.  

Since any finite abelian group can be expressed as a direct product of cyclic groups $\mathbb{Z}_N$, the dual group $\hat{G}$ can be similarly decomposed as a direct product of $\widehat{\mathbb{Z}_N}$. Given that $\widehat{\mathbb{Z}_N} \cong \mathbb{Z}_N$, we obtain $\hat{G} \cong G$, which implies $\lvert \hat{G} \rvert = \lvert G \rvert = \dim(V)$. Consequently, the group of characters $\hat{G}$ forms an orthonormal basis of $V$.  

This guarantees that any function on $G$ can be expressed as  

$$
f = \sum_{\chi \in \hat{G}} \hat{f}(\chi) \chi, \quad \hat{f}(\chi) = (f, \chi) = \frac{1}{\lvert G \rvert} \sum_{a \in G} f(a) \overline{\chi(a)}.
$$  

## 2. Dirichlet's theorem

We now proceed to the proof of Dirichlet's theorem, which states that there are infinitely many primes satisfying $p\equiv a(\mathrm{mod}\ m)$ when $a$ and $m$ are coprime. Let $V = \mathbb{Z}_m^\*$ and extend characters on $\mathbb{Z}_m^\*$ to $\mathbb{Z}_m$ by setting them to zero outside the original domain. Noting that

$$
\delta_a(n)=\sum_{\chi}\hat{\delta}_a(\chi)\chi(n)=\sum_{\chi}\chi(n)\cdot\frac{1}{\varphi(m)}\sum_{l\in\mathbb{Z}_m^*}\delta_a(l)\overline{\chi(l)}=\frac{1}{\varphi(m)}\sum_{\chi}{\chi(n)\overline{\chi(a)}},
$$

we obtain

$$
\sum_{p\equiv a(\mathrm{mod}\ m)}\frac{1}{p^s}=\sum_{p}\frac{1}{p^s}\cdot\frac{1}{\varphi(m)}\sum_{\chi}{\chi(p)\overline{\chi(a)}}=\frac{1}{\varphi(m)}\sum_{\chi}{\overline{\chi(a)}\sum_{p}{\frac{\chi(p)}{p^s}}} \\
= \frac{1}{\varphi(m)}{(\sum_{p}{\frac{\chi_0(p)}{p^s}}+\sum_{\chi\not ={\chi_0}}{\overline{\chi(a)}}\sum_{p}{\frac{\chi(p)}{p^s}})},
$$

where $\chi_0$ is the principal character, taking the value 1 on all elements of $\mathbb{Z}_m^*$ and 0 elsewhere. Since these series converge uniformly for $s>1$, they are continuous in this region. Taking the limit as $s\rightarrow1^+$, the first term on the right-hand side diverges to infinity. If we establish that

$$
\sum_{p}{\frac{\chi(p)}{p}} \text{ is finite for }\chi\not =\chi_0,
$$

then the right-hand side also diverges, implying

$$
\sum_{p\equiv a(\mathrm{mod}\ m)}\frac{1}{p}=\infty,
$$

which confirms the infinitude of primes satisfying $p\equiv a(\mathrm{mod}\ m)$. Thus, it remains to prove this finiteness on the non-principal characters, leading to the definition of the Dirichlet L-function:

$$
L(s,\chi)=\sum_{n}{\frac{\chi(n)}{n^s}}.
$$

Observing that

$$
\lvert\sum_{n}{\frac{\chi(n)}{n^s}}-\prod_{p\le N}{\frac{1}{1-\frac{\chi(p)}{p^s}}}\rvert\le\sum_{n>N}\lvert\frac{\chi(n)}{n^s}\rvert,
$$

taking the limit as $N\rightarrow\infty$, we obtain 

$$
L(s,\chi)=\prod_{p}{\frac{1}{1-\frac{\chi(p)}{p^s}}}.
$$

for $\Re(s)>1$, because $L$ absolutely converges on this range. Moreover, for sufficiently large $p$, we can assume that $1-\frac{\chi(p)}{p^s}$ lies in $\mathbb{C}\setminus(-\infty,0]$, the principal branch of complex logarithms, allowing us to write

$$
L(s,\chi)=\exp\Big({\sum_{p}{-\log\big(1-\frac{\chi(p)}{p^s}\big)}}\Big)=\exp\Big({\sum_{p}{\frac{\chi(p)}{p^s}+O(\frac{\chi(p^2)}{p^{2s}})}}\Big)=\exp\Big({\sum_{p}{\frac{\chi(p)}{p^s}+O(1)}}\Big).
$$

Thus, it's enough to show that $L(1,\chi)$ is nonzero and finite for all $\chi\not =\chi_0$. Before addressing this, we explore some useful properties of $L(s,\chi)$, particularly for $\Re(s)>0$, in connection with Dirichlet series.

## 3. Dirichlet series

A Dirichlet series is defined as

$$
D(s)=\sum_{n}{\frac{a_n}{n^s}}.
$$

### Theorem 1 <!-- omit in toc -->
If the series defining $D(s)$ converges for some $s=s_0$, then it converges uniformly on each compact subset of $\Re(s)>\Re(s_0)$. Hence, $D$ is holomorphic on this half-plane.

### Proof <!-- omit in toc -->
Assume, without loss of generality, that $s_0=0$. Define $S_n=a_1+\cdots+a_n$, and there exists a constant $C$ such that $\lvert S_n \rvert\le C$. For $\Re(s)>0$, since $\frac{S_n}{n^s}\rightarrow0$ as $n\rightarrow\infty$, applying Abel's summation lemma gives

$$
\Big\lvert \sum_{n}{\frac{a_n}{n^s}}\Big\rvert=\Big\lvert\sum_{n}{S_n(\frac{1}{n^s}-\frac{1}{(n+1)^s})}\Big\rvert\le C\sum_{n}{\Big\lvert\frac{1}{n^s}-\frac{1}{(n+1)^s}\Big\rvert}.
$$

Furthermore,

$$
\Big\lvert\frac{1}{n^s}-\frac{1}{(n+1)^s}\Big\rvert\le\sup_{n\le x\le n+1}{\Big\lvert\frac{s}{x^{s+1}}\Big\rvert}\le\frac{\lvert s\rvert}{n^{\Re(s)+1}}.
$$

Thus,

$$
\lvert D(s)\rvert \le C\lvert s\rvert\sum_{n}\frac{1}{n^{\Re(s)+1}},
$$

which converges uniformly on any compact subset of $\Re(s)>0$, as they lie in some region $\Re(s)>\varepsilon>0$.

<div style="text-align: right"> $\square$ </div>

A similar application of Abel's summation lemma shows that $L(s,\chi)$ converges for a positive real $s$ when $\chi\not =\chi_0$, making it holomorphic on $\Re(s)>0$. Consequently, $L(1,\chi)$ is finite for $\chi\not =\chi_0$. 

For $\Re(s)>1$, we also have 

$$
L(s,\chi_0)=\prod_{p\nmid m}{\frac{1}{1-p^{-s}}}=\zeta(s)\prod_{p\mid m}{(1-p^{-s})}.
$$

Rewriting $\zeta(s)$,

$$
\zeta(s)=\frac{1}{s-1}+\sum_{n}{\frac{1}{n^s}}-\int_{1}^{\infty}{\frac{1}{t^s}dt}=\frac{1}{s-1}+\sum_{n}{\Big(\frac{1}{n^s}-\int_{n}^{n+1}{\frac{1}{t^s}dt}\Big)}=\frac{1}{s-1}+\sum_{n}{\int_{n}^{n+1}{\Big(\frac{1}{n^s}-\frac{1}{t^s}\Big)dt}}.
$$

Using

$$
\Big\lvert\int_{n}^{n+1}{\Big(\frac{1}{n^s}-\frac{1}{t^s}\Big)dt}\Big\rvert\le\sup_{n\le x\le n+1}\Big\lvert\frac{1}{n^s}-\frac{1}{t^s}\Big\rvert=\Big\lvert\frac{1}{n^s}-\frac{1}{(n+1)^s}\Big\rvert\le\frac{\lvert s\rvert}{n^{\Re(s)+1}},
$$

we conclude that the series of integrals converges on $\Re(s)>0$. Since each integral is holomorphic on $\Re(s)>0$, the series is also holomorphic on this region. Therefore, $\zeta(s)$ extends to a meromorphic function with a single simple pole at $s=1$ for $\Re(s)>0$, and $L(s,\chi_0)$ extends similarly. In other words, $L(s,\chi_0)$ is holomorphic on $\Re(s)>0$, except for a simple pole at $s=1$.

### Theorem 2 <!-- omit in toc -->
Suppose that all $a_n$ are non-negative real numbers. If the series defining $D(s)$ converges on $\Re(s)>s_0$ for some real $s_0$, and $D(s)$ extends to a holomorphic function on $\Re(s)>s_0-\varepsilon$ for some $\varepsilon>0$, then the series converges on $\Re(s)>s_0-\varepsilon$.

### Proof <!-- omit in toc -->
Without loss of generality, assume $s_0=0$. By Theorem 1, it suffices to show that the series converges for all real $s>-\varepsilon$. Since $D(s)$ is holomorphic on $\Re(s)>-\varepsilon$, we can write $D$ as

$$
D(s)=\sum_{m}{\frac{D^{(m)}(1)}{m!}(s-1)^m},
$$

with the $m$-th derivative 

$$
D^{(m)}(s)=\sum_{n}{\frac{a_n(-\log{n})^m}{n^s}}.
$$

Since $a_n\ge 0$, each $(-1)^mD^{(m)}(1)$ is a convergent series with positive terms. Thus, we can rewrite $D$ as

$$
D(s)=\sum_{n}{\frac{a_n}{n}\sum_{m}{\frac{((1-s)\log{n})^m}{m!}}}=\sum_{n}{\frac{a_n}{n}e^{(1-s)\log{n}}}=\sum_{n}{\frac{a_n}{n^s}},
$$

implying that this series also converges for $s>-\varepsilon$. 

<div style="text-align: right"> $\square$ </div>

This theorem is crucial for the final step of the proof in the next section.

## 4. Showing $L(s,\chi)\not = 0$ for $\chi\not =\chi_0$

Define
$$
f(s)=\prod_{\chi}{L(s,\chi)}.
$$

If some $\chi \neq \chi_0$ satisfies $L(s,\chi) = 0$, then from the previous results, $f(s)$ extends holomorphically to $\Re(s) > 0$. For $\Re(s) > 1$,

$$
f(s)=\prod_{\chi}\prod_{p}\Big(\frac{1}{1-\frac{\chi(p)}{p^s}}\Big)=\prod_{p\nmid m}\prod_{\chi}\Big(\frac{1}{1-\frac{\chi(p)}{p^s}}\Big).
$$

For $p\nmid m$, since $\chi(p)^{\text{ord}(p)}=1$, we obtain that $\chi(p)$ can only take the value of $\text{ord(p)}$-th root of unity. These roots form a subgroup $H\le\mathbb{Z}_m^\*$ of order $\lvert H\rvert=\text{ord}(p)$. Each characters on $H$ extend to a character on $\mathbb{Z}_m^\*$ in exactly $\lvert \widehat{\mathbb{Z}_m^\*/H}\rvert=\lvert \mathbb{Z}_m^\*/H\rvert=\frac{\varphi(m)}{\text{ord}(p)}$ ways, implying that each root of unity appears with multiplicity $\frac{\varphi(m)}{\text{ord}(p)}$ in $\chi(p)$. Consequently, for $p \nmid m$,

$$
\prod_{\chi}\Big(1-\frac{\chi(p)}{p^s}\Big)=\Big(\prod_{\omega\in H}(1-\frac{\omega}{p^{s}})\Big)^{\frac{\varphi(m)}{\text{ord}(p)}}=\Big(1-\frac{1}{p^{s\cdot\text{ord}(p)}}\Big)^{\frac{\varphi(m)}{\text{ord}(p)}}.
$$

Thus, for $\Re(s)>1$,

$$
f(s)=\prod_{p\nmid m}{\Big(\frac{1}{1-\frac{1}{p^{s\cdot\text{ord}(p)}}}\Big)^{\frac{\varphi(m)}{\text{ord}(p)}}}.
$$

The right-hand side is a Dirichlet series with nonnegative real coefficients $a_n$ and converges on $\Re(s) > 1$ since $f(s)$ is finite on this region. As $f(s)$ is holomorphic on $\Re(s) > 0$, Theorem 2 implies that this series also converges on $\Re(s) > 0$. However, for real $s$,

$$
\prod_{p\nmid m}\Big(\frac{1}{1-\frac{1}{p^{s\cdot\text{ord}(p)}}}\Big)^{\frac{\varphi(m)}{\text{ord}(p)}}\ge \prod_{p\nmid m}{\Big(1+\frac{1}{p^{s\cdot\varphi(m)}}+\frac{1}{p^{2s\cdot\varphi(m)}}+\cdots\Big)}=\sum_{(n,m)=1}{\frac{1}{n^{s\cdot\varphi(m)}}}.
$$

The series on the right diverges for $s = \frac{1}{\varphi(m)} > 0$, contradicting the assumption that $f(s)$ converges on $\Re(s)>0$. Thus, no character $\chi \neq \chi_0$ satisfies $L(s, \chi) = 0$, completing the proof of Dirichlet's theorem.

***