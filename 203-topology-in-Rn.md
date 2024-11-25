---
authors:
  - name: Alyona Zarodnyuk
    affiliations:
      - Higher School of Economics
numbering:
  enumerator: 3.%s
---

# Топология в ℝⁿ

> Лекция 3, 01.10.2024

$M\subset \R^n$

```{prf:definition}
:name: inner_point
$x_0\in M$ называется **внутренней точкой** $M$, если $\exists\varepsilon>0, B_\varepsilon(x_0)\subset M$.
```

```{prf:definition}
:name: outer_point
$x_0\not\in M$, $x_0\in\R^n\setminus M$ называется **внешней точкой** $M$, если $\exists\varepsilon >0, B_{\varepsilon}(x_0)\subset\R^n\setminus M$.
```

```{prf:definition}
:name: border_point
$x_0\in\R^n$ называется **граничной точкой** $M$, если $\forall\varepsilon >0$

$$\begin{cases}
    B_\varepsilon(x_0)\cap M\neq\varnothing\\
    B_\varepsilon(x_0)\cap (R^n\setminus M)\neq\varnothing
\end{cases}$$

$\partial M$ — множество всех граничных точек $M$.
```

```{prf:definition}
:name: isolated_point
$x_0\in M$ называется **изолированной точкой** $M$, если $\exists\epsilon >0,\overset{\circ}B_\varepsilon(x_0)\cap M=\varnothing$.
```

```{prf:example}
$M=[0, 1)\cup\{3\}$

* $(0, 1)$ — внутренние точки
* $(-\infty, 0) \cup (1, 3) \cup (3, +\infty)$ — внешние точки
* $0, 1, 3$ — граничные точки
* $3$ — изолированная точка
```

```{prf:definition}
:name: limit_point2
$x_0 \in \R^n$ называется **предельной точкой** $M$, если $\forall\varepsilon >0, \overset{\circ}B_\varepsilon(x_0)\cap M\neq\varnothing$.
```

```{prf:example}
$M=[0, 1)\cup\{3\}$
* внутренние точки — предельные
* $0, 1$ — предельные
* $3$ не предельная, но граничная
    * изолированные точки не являются предельными точками
```

```{prf:definition}
:name: tangent_point
$x_0\in\R^n$ называется **точкой прикосновения** для $M$, если $\forall\varepsilon>0,B_\varepsilon(x_0)\cap M\neq\varnothing$.

:::{note}
Точки прикосновения = предельные точки $\oplus$ изолированные точки
:::
```

```{prf:definition}
Множество всех точек прикосновения M образует **замыкание** $M$ и обозначается $\overline {M}$.
```

```{prf:example}
$$M=(0,1)\cup(1, 2]\implies \overline{M}=[0,2]$$
$$M=\{x\in[0,1] | x\in\QQ\}\implies\overline{M}=[0,1]$$
```

```{prf:definition}
:name: open_set
Множество $M\subset\R^n$ называется **открытым**, если все его точки внутренние.
```

```{prf:definition}
:name: closed_set
$M\subset R^n$ называется **замкнутым**, если $\R^n\setminus M$ — открыто
```

```{note} Замечание
$\varnothing$ — открыто и замкнуто.
```

```{prf:example}
* $(0, 1)$ — открыто.
* $[0, 1]$ — замкнуто, т. к. $(-\infty, 0)\cup (1,+\infty)$ открыто в $\RR$.
* $(0, 1]$ — не открыто и не замкнуто в $\RR$.
```

```{prf:definition}
:name: bounded_set
Множество $М\subset \RR^n$ называется **ограниченным**, если $\exists x_0\in\R^n$ и $\exists 0<r<\infty$, что $M\subset B_r(x_0)$
```

```{prf:definition}
:name: compact
Множество $K$ в $\R^n$ называется **компактом**, если из $\forall$ его покрытия открытыми множествами можно выделить конечное подпокрытие.
```

```{note} Замечание
Если хоть для какого-то покрытия не выполнено $\implies$ не компакт.
```

```{prf:example}
$M=(0,1)$

$\{A_k\}_{k=1}^\infty\colon A_k=(0, 1-\tfrac{1}{k})$

При $n\to\infty, M\subset \bigcup_{k=1}^\infty A_k$, но если выбираем конечное $N$, то $M\not\subset\bigcup_{k=1}^NA_k\implies M$ — не компакт.
```

```{prf:theorem} Критерий замкнутости множества в $\R^n$
:name: closure_criterion
$M$ — замкнуто $\iff M$ содержит **ВСЕ** свои предельные точки.
```

```{prf:proof}
:nonumber:
$(\Rightarrow)$ **Необходимость** (от противного)
1. Пусть $x_0$ — предел точки $M$, но $x_0\not\in M$, тогда $x_0\in \R^n$
2. По условию $M$ замкнуто, т. е. $\R^n\setminus M$ открыто, т. е. все его точки внутренние $\implies$ для $x_0$ из п. 1 $\exists r >0, B_r(x_0)\subset \R^n\setminus M$ и $\overset{\circ} B_r(x_0)\cap M=\varnothing$, но т. к. $x_0$ предельная $\forall r >0, \overset{\circ}B_r(x_0)\cap M\neq\varnothing$
3. Получили противоречие $\implies M$ содержит все предельные точки.

$(\Leftarrow)$ **Достаточность**

$M$ содержит все свои предельные точки. $M$ — замкнуто?

Пусть $y_0$ не является предельной для $M$, т. е. $y_0\in\RR^n\setminus M\implies$

$$\exists r>0, \quad\begin{cases}
    \overset{\circ}B_r(y_0)\cap M=\varnothing\\
    y_0\in\RR^n\setminus M
\end{cases}\implies B_r(y_0)\subset\RR^n\setminus M\implies$$

$\RR^n\setminus M$ — открытое и состоит из всех точек, не являющихся предельными $M\implies M$ замкнуто по определению. 
```