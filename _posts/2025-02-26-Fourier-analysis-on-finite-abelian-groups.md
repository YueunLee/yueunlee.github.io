---
title: Fourier Analysis on Finite Abelian Groups
---

In Fourier analysis on $\mathbb{C}$, complex-valued functions can be approximated as sums of exponentials. A similar approach applies to finite abelian groups. Let $V$ be the vector space of all complex-valued functions defined on a finite abelian group $G$. When $G = \mathbb{Z}_N = \mathbb{Z}/N\mathbb{Z}$, the set $\{ f_n \mid f_n(k) = w^{nk}, \, n \in \mathbb{Z}_N \}$ forms an orthonormal basis of $V$, where $w = e^{2\pi i / N}$. Moreover, this basis is isomorphic to $\mathbb{Z}_N$, as the mapping between $n$ and $f_n$ defines an isomorphism.  

To extend this framework to general finite abelian groups, we first construct an orthonormal basis of $V$. A **character** is defined as a nonzero multiplicative function in $V$. For $\mathbb{Z}_N$, the characters are precisely the functions $f_n$ described earlier. These characters form a group under function composition, known as the **dual group** of $G$, denoted by $\hat{G}$. A straightforward verification shows that $\hat{G}$ is an orthonormal subset of $V$.  

Since any finite abelian group can be expressed as a direct product of cyclic groups $\mathbb{Z}_N$, the dual group $\hat{G}$ can be similarly decomposed as a direct product of $\widehat{\mathbb{Z}_N}$. Given that $\widehat{\mathbb{Z}_N} \cong \mathbb{Z}_N$, we obtain $\hat{G} \cong G$, which implies $\lvert \hat{G} \rvert = \lvert G \rvert = \dim(V)$. Consequently, the group of characters $\hat{G}$ forms an orthonormal basis of $V$.  

This guarantees that any function on $G$ can be expressed as  

$$
f = \sum_{e \in \hat{G}} \hat{f}(e) e, \quad \hat{f}(e) = (f, e) = \frac{1}{\lvert G \rvert} \sum_{a \in G} f(a) \overline{e(a)},
$$  

along with the Plancherel formula:  

$$
\lVert f \rVert^2 = \sum_{e \in \hat{G}} \lvert \hat{f}(e) \rvert^2.
$$  
