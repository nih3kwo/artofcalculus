# Замкнутые множества, точки замыкания (=точки прикосновения), замыкание множества.

:::{prf:definition}
**Замкнутое множество** в метрическом пространстве $E$ есть дополнение открытого множества. 
:::

Пустое множество замкнуто, замкнуто и всё пространство $E$.

:::{prf:example}
Пусть $E = \mathbb{R}$, $d(x,y):= |x-y|$. Тогда промежутки $[a, + \infty)$, $(- \infty,a]$ замкнуты, потому что 
$$
[a, + \infty) = \mathbb{R} \setminus \cup_{n \ge 1} (a-n, a)
$$
:::

:::{prf:definition}
:name: limit_point
Пусть $E$ — метрическое пространство, $d$ — расстояние в нём, и пусть $A \subseteq E$. **Точка замыкания** (=**точка прикосновения**) множества $A$ — такая точка $x \in E$, каждая окрестность которой имеет с $A$ непустое пересечение. Множество всех точек замыкания называется **замыканием** множества $A$ и обозначается символом $\overline{A}.$
:::

:::{prf:example}

1. $E= \mathbb{R}$ с обычной метрикой $d(x,y) = |x-y|$, $A = (0,1]$, тогда $0$ — точка замыкания, потому что любой шар $B(0,r) = (-r,r) \cap A \ne \varnothing$.
2. На расширенной прямой $\overline{\mathbb{R}}$ шары $B(+\infty, r) = (\frac{1-r}{r}, +\infty)$ есть просто луч. Ясно, что $B(+\infty, r)\cap \mathbb{R} \ne \varnothing$, т. е. это и означает, что замыкание множества $\mathbb{R}$ и даст расширенную прямую $\overline{\mathbb{R}}.$

:::

:::{prf:lemma}
:name: closure
Множество $F$ в метрическом пространстве замкнуто, если и только если все его точки это предельные точки, **т.е.,** $F = \overline{F}.$ 
:::
(1) Пусть $F$ — замкнуто, тогда найдётся какое-то открытое $\mathscr{U} \subseteq E$, такое, что $F = E \setminus \mathscr{U}$. Пусть $x \notin F$, тогда $x \in \mathscr{U}$, и тогда найдётся окрестность $\mathscr{W}(x)$ такая, что $\mathscr{W}(x) \subseteq \mathscr{U}$, потому что $\mathscr{U}$ — открыто, **т.е.,** $\mathscr{W}(x) \cap F = \varnothing.$ Таким образом, получили, что если $F$ — замкнуто, то никакая точка $x \notin F$ не может быть предельной для $F$, **т.е.,** $F = \overline{F}.$ 

(2) Пусть $F = \overline{F}$, тогда для любой точки $x \notin F$, можно всегда найти окрестность $\mathscr{W}(x)$ такую, что $\mathscr{W}(x) \cap F = \varnothing$. Пусть $\mathscr{U}:= \cup_{x E\setminus F} \mathscr{W}(x)$, тогда, $\mathscr{U}$ — открыто в $E$ и $F = E \setminus \mathscr{U}.$


:::{prf:lemma}
:name: preimage_of_closed
Отображение $f:E \to E'$ между метрическими пространствами непрерывно тогда и только тогда, когда прообраз любого замкнутого множества в $E'$ есть замкнутое множество в $E.$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $F'$ — замкнутое подмножество в $E'$, тогда $\mathscr{U}': = E'\setminus F'$ — открыто в $E'$ и $E' = F' \cup \mathscr{U}'$, $F' \cap \mathscr{U}' = \varnothing$. Далее, ясно что $f^{-1}(F') \cap f^{-1}(\mathscr{U}') = \varnothing$ и $E = f^{-1}(F') \cap f^{-1}(\mathscr{U}')$. Тогда согласно Теореме [](#preimage_of_open), $f$ — непрерывно если и только если $f^{-1}(\mathscr{U}')$ — открыто в $E$, но тогда $f^{-1}(F') = E \setminus \mathscr{U}'$ замкнуто тогда и только тогда, когда $f^{-1}(\mathscr{U}')$ — открыто. Это завершает доказательство.
:::

:::{prf:lemma}
:name: closed_ball=closed
Замкнутый шар — замкнут.
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $(E,d)$ — метрическое пространство, $\bar B(a,r)$ — замкнутый шар. Покажем, что $E\setminus B(a,r)$ — открыто. Пусть $x\notin \bar B(a,r)$, тогда $d(a,x) > r$, и положим $\varepsilon: = d(a,x) - r$, очевидно, что $\varepsilon >0$. Имеем $d(x,a) \le d(y,a) + d(y,x)$, тогда $d(y,a) \ge d(x,a) - d(y,x)$.

Пусть теперь $y\in B(x, \frac{\varepsilon}{2})$, тогда получаем
$$\begin{align*}
d(y,a) &\ge & d(x,a) - d(y,x) \\
&\ge & r + \varepsilon- \frac{\varepsilon}{2}\\
&=& r + \frac{\varepsilon}{2}\\
&>& r
\end{align*}$$
т.е. $y\notin \bar B(a,r)$. А это означает, что весь открытый шар $B(x, \frac{\varepsilon}{2})$ не лежит в $\bar B(a,r)$, что и требовалось доказать.
:::