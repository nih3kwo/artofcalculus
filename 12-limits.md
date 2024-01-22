# Пределы

Пусть $E$ — метрическое пространство, $d$ — расстояние в нём, пусть $A \subseteq E$ — некоторое его подмножество, пусть $a$ — точка замыкания для $A$, т. е. $a \in \overline{A}$, и пусть $f:A \to E'$ некоторое отображение в метрическое пространство $E'.$

:::{prf:definition}
:name: the_main_def_of_limit
Пусть $a \notin A$. Мы будем говорить, что $f(x)$ **имеет предел $a' \in E'$ при $x \in A$, стремящемся к $a$ (или $a'$ есть предел отображения $f$ в точке $a\in \overline{A}$ по множеству $A$)**, если отображение $\overline{f}:A \cup \{a\} \to E$, определённое условиями
$$
\overline{f}(x) = \begin{cases}
f(x), & x \in A, \\
a', & x = a,
\end{cases}
$$
непрерывно в точке $a$.
:::

В этом случае, мы пишем
$$
a' := \lim_{x\to a, x \in A} f(x).
$$

:::{warning}
Если $a \in A$, то мы пользуемся той же терминологией и теми же обозначениями как и в случае, когда отображение $f$ непрерывно в точке $a$, причём $a':=f(a).$
:::

:::{prf:example}


1. Пусть $E = E'=\mathbb{R}$, $d(x,y) = d'(x,y): |x-y|$, $A = \mathbb{R}\setminus \{0\}$, и отображение $f: A \to \mathbb{R}$ задаётся с помощью $f(x) = x$. 

Ясно, что $0$ есть точка замыкания для $A$, так как шар $B(0,r)$ с такой метрикой $d$ — это просто интервал $(-r,r)$, тогда очевидно, что $(-r, r) \cap A = (-r, r)\setminus \{0\} \ne \varnothing$, что и доказывает, что точка $0$ — точка замыкания для множества $A$.

Пусть
$$
\overline{f}(x): = \begin{cases}
x, & x \in A \\
\alpha, & x =0.
\end{cases}
$$

Если мы поймём, при каком $\alpha$ это отображение $\overline{f}$ непрерывно в точке $0$, то мы и найдём предел, который и будет равен этому $\alpha.$

Итак, пусть $\overline{f}$ непрерывна в точке $0$, тогда для любого шара $B(\alpha, r) \subseteq E' = \mathbb{R}$ должен найтись шар $B(0,\delta) \subseteq E = \mathbb{R}$ такой, что $f(B(0,\delta)) \subseteq B(\alpha, r)$.

Ясно, что $B(0,\delta) = (-\delta, \delta)$, $B(\alpha, r) = (\alpha - r,\alpha + r)$, и 
$$
\overline{f}(B(0,\delta)) = \overline{f}((-\delta, \delta)) = (-\delta, \delta) \setminus \{0\} \cup \{\alpha\},
$$
следовательно, если $\overline{f}$ будет непрерывной в точке $0$, то для любого $r >0$ можно найти $\delta >0$ такое, что
$$
\overline{f}(B(0,\delta)) = (-\delta, \delta) \setminus \{0\} \cup \{\alpha\} \subseteq (\alpha - r, \alpha + r),
$$
тогда $-\delta, \delta \in (\alpha - r, \alpha + r)$. Это значит, что $\alpha -r < 0$, $\alpha + r >0$. Таким образом, если $\alpha \ne 0$, **то только для шаров вида (т. е. не для всех!) $B(\alpha, r)$, где $\alpha -r < 0$, $\alpha + r >0$,** всегда найдётся шар $B(0,\delta)$ такой, что $f(B(0,\delta)) \subseteq B(\alpha, r)$, т. е. при $\alpha \ne 0$ отображение $\overline{f}$ не будет непрерывным в $0$. С другой стороны, если же $\alpha =0$, то мы получаем неравенства $-r <0$, $r>0$, которые выполняются всегда, так как мы требуем чтобы $r>0$.

Таким образом, $\lim_{x\in 0, x \in A}f(x) = 0.$

2. Пусть $E = E' = \mathbb{R}$ с расстоянием $d(x,y) = |x-y|$, $A = \mathbb{R}\setminus \{0\}$, $f(x): = x^2 \sin \frac{1}{x}.$ Тогда, как мы уже видели в примере [](#x^2sin(1x)), отображение  
$$
\overline{f}(x) = \begin{cases}
x^2 \sin \frac{1}{x}, & x \ne 0, \\
0, & x =0
\end{cases}
$$
непрерывно в точке $x = 0$, тогда $\lim_{x \to 0, x \in A}f(x) = 0.$


:::

Вспомнив определение непрерывности и точки замыкания, определение предела можно переформулировать следующими двумя эквивалентными способами:

:::{prf:definition}
$\lim_{x \to a, x \in A}f(x) = a'$ эквивалентно тому, что для любого шара $B(a',r) \subseteq E'$ найдётся такой шар $B(a,\delta) \subseteq A$, что $f(B(a,\delta)\cap A) \subseteq B(a',r)$.
:::
:::{warning}
Так как $a$ — точка замыкания, то множество $A \cap B(a,\delta)$ никогда не пусто для любого $\delta >0$.
:::




































:::{prf:definition}
:name: def_for_cont_via_d-e
$\lim_{x \to a, x \in A}f(x) = a'$ эквивалентно тому, что для каждого $\varepsilon>0$ можно найти такое $\delta >0$, что из $x \in A$ и $d(x,a)<\delta$ следует $d'(a',f(x))<\varepsilon.$
:::

:::{prf:proposition}
Отображение может иметь лишь один предел по множеству $A$ в данной точке $a \in \overline{A}.$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть  $\lim_{x \to a, x \in A}f(x) = a'$ и  $\lim_{x \to a, x \in A}f(x) = b'$, при этом $a' \ne b'$. Тогда, согласно Определению [](#def_for_cont_via_d-e), 

1.  $\lim_{x \to a, x \in A}f(x) = a'$ означает, что для любого $\varepsilon >0$ можно найти такое $\delta_1 >0$, что из $x \in A$ и $d(x,a)<\delta_1$ следует $d'(a',f(x))<\varepsilon$
2. $\lim_{x \to a, x \in A}f(x) = b'$ означает, что для того же $\varepsilon >0$ можно найти такое $\delta_2 >0$, что из $x \in A$ и $d(x,a)<\delta_2$ следует $d'(b',f(x))<\varepsilon$.

Тогда по неравенству треугольника
$$
d'(a',b') \le d'(a', f(x)) + d'(f(x), b') < 2\varepsilon,
$$
т. е. расстояние между фиксированными точками $a',b' \in E'$ может быть любым, что невозможно если $a' \ne b'.$
:::

Из определения предела вытекает:
:::{prf:theorem} Критерий непрерывности
Пусть $f$  — отображение метрических пространств $f:E \to E'$. Для того чтобы $f$ было непрерывно в точке $x_0 \in E$, являющейся точкой замыкания множества $E\setminus\{x_0\}$, необходимо и достаточно, чтобы $f(x_0) = \lim_{x \to x_0, x\in E \setminus \{x_0\}}f(x).$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Это лишь пересказ определения.
:::

:::{prf:theorem}
:name: limit_for_any_subset
Пусть $a' = \lim_{x \to a, x \in A} f(x)$. Тогда для каждого подмножества $B \subseteq A$, для которого $a \in \overline{B}$, $a' = \lim_{x \to a, x \in B}f(x)$.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Это сразу следует из определения предела и следствия [](#restriction).
:::

:::{prf:theorem}
:name: lim_of_composition
Пусть $E,E',E''$ — метрические пространства, $A \subseteq E$, и $f:A \to E'$, $g:E' \to E''$ — отображения. Если $\lim_{x \to a, x \in A}f(x) = a'$ и $g$ непрерывно в точке $a'$, то $g(a') = \lim_{x \to a, x \in A}g(f(x))$. 
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Это сразу следует из определения предела и теоремы [](#comp_of_continous).
:::

:::{warning}
В случае, когда $A = E$, мы будем вместо $\lim_{x \to a, x \in A}f(x)$  писать $\lim_{x \to a}f(x).$
:::

:::{prf:remark}
Пусть $E = \overline{\mathbb{R}}$ — расширенная прямая, рассмотрим выражение $\lim_{x \to +\infty, x \in \mathbb{{R}}}f(x) = a'$, где $f:\mathbb{R} \to E' $ - некоторое отображение. Мы знаем, что $B(+\infty, \delta) = (\frac{1-\delta}{\delta}, \infty]$. Тогда непрерывность в точке $+\infty$ означает, что для любого $r >0$ найдётся такой $\delta>0$, что $f((\frac{1-\delta}{\delta}, \infty]) \subseteq B(a',r)$. Другими словами, если $\lim_{x \to + \infty} f(x) = a'$, то для любого шара $B(a',r)$ найдётся такое число $\alpha \in \mathbb{R}$ что $f(\beta) \in B(a',r)$ для всех $\beta > \alpha.$ **Именно так мы и будем понимать запись $\lim_{x \to +\infty}f(x) = a'$**;
$$
\boxed{ 
\boxed{
\lim_{x \to +\infty}f(x) = a' \Longleftrightarrow \forall r > 0\, \exists \alpha \in \mathbb{R}:\, f(\beta) \in B(a',r) \,\forall \beta >\alpha.
}
}
$$
:::

:::{warning}
В частности, если $E' = \mathbb{R}$ с обычной метрикой и $\mathbb{N} \subseteq \overline{\mathbb{R}}$, то $\lim_{x \to +\infty, x \in \mathbb{{N}}}f(x) =a'$ есть знакомое нам определение предела последовательности.
:::

:::{prf:lemma}
:name: choice_of_seqeunce
Для любой точки $a \in \overline{A}$ существует такая последовательность $\{x_n\}$ точек из $A$, что $a = \lim_{n \to \infty} x_n$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Так как $a$ — точка замыкания, то любой шар $B(a, r)$ содержит хотя бы одну точку из $A$, т. е. $B(a, r) \cap A \ne \varnothing$. В частности, для любого $n\ge 1$, $B(a, \frac{1}{n}) \cap A \ne \varnothing$. Тогда по Аксиоме Выбора, для каждого $n\ge 1$ мы можем выбрать $x_n \in B(a, \frac{1}{n})$. Покажем, что $\lim_{n \to \infty} x_n = a$. Действительно, пусть $n<m$, и мы имеем тогда $x_n \in B(a, \frac{1}{n})$, $x_m \in B(a, \frac{1}{m})$. 

Тогда имеем
$$
d(x_n, x_m) \le d(a,x_n) + d(a,x_m) <\frac{1}{n} + \frac{1}{m} < \frac{2}{n}.
$$

Это означает, что все $x_n, x_{n+1}, \ldots \in B(a, \frac{2}{n})$, что и доказывает требуемое.
:::

:::{prf:corollary}
:name: Weirstrass_mega
Подмножество $F$ в метрическом пространстве $E$ замкнуто, тогда и только тогда, когда из любой последовательности $(x_n)$ в $F$, можно выбрать сходящуюся подпоследовательность $(x_{n_k})$, такую, что $\lim_{n\to \infty} x_{n_k} \in F$. 
:::

:::{prf:proof}
:class: dropdown
:nonumber:
По Предложению [](#closure), $F$ замкнуто, если и только если $F = \overline{F}$. Тогда используя лемму [](#choice_of_seqeunce}, мы завершаем доказательство. 
:::



:::{prf:theorem}
:name: lim=>for_any_sequence
Пусть $f: A \to E'$ — отображение множества $A \subseteq E$ в метрическое пространство $E'$ и $a \in \overline{A}.$ Для того, чтобы $f$ имело предел $a' \in E'$ в точке $a$ по $A$, необходимо и достаточно, чтобы для каждой последовательности $\{s_n\}$ точек из $A$, сходящейся к $a$, последовательность $f(s  _n)$ сходилась к $a'.$
:::

:::{prf:proof}
:class: dropdown
:nonumber:~

(1) Необходимость. 

Пусть $\lim_{x \to a, x \in A}f(x) = a'$, и пусть $s:\mathbb{N} \to {A}\cup \{a\}$ — последовательность $\{s_n\}$. По условию, $\lim_{n \to \infty }s_n = a$ и так как $\lim_{x \to a, x \in A}f(x) = a'$, то по определению предела [](#the_main_def_of_limit), $\overline{f}$ непрерывна в точке $a$. Тогда по Теореме [](#lim_of_composition}, последовательность $s':=\overline{f} \circ s: \mathbb{N} \to E'$, в которой $s'_n = f(s_n)$, имеет предел $\overline{f}(a) = a'$, что и доказывает необходимость.

(2) Достаточность.

Будем доказывать от противного. Пусть для любой последовательности $\{s_n\}$ точек из $A$, $\lim_{n \to \infty} s_n = a$ имеем $\lim_{n \to \infty}f(s_n) = a'$, но $a' \ne \lim_{x \to a, x\in A}f(x).$ Тогда  $\lim_{n \to \infty} s_n = a$ влечёт, что, начиная с какого-то номера $N$, $d(a,s_n) < \varepsilon$ для всех $n > N$.

С другой стороны, $a' \ne \lim_{x \to a, x\in A}f(x)$ означает, что $f(x)$ не является непрерывным в точке $a$. Тогда, существует такое $\varepsilon >0$, что для любого номера $n$ найдётся такая точка $x_n \in A$, удовлетворяющая двум условиям: $d(a,x_n) < \frac{1}{n}$ и $d'(a',f(x_n))\ge \varepsilon$. Но тогда последовательность $\{f(s_n)\}$ не сходится к $f(s)$, что противоречит условию.
:::


:::{prf:theorem}
:name: f<g=>lim
Пусть $E$ — метрическое пространство с метрикой $d$, и $\mathbb{R}$ — рассматривается с обычной метрикой $d'(x,y): = |x-y|$.  Пусть $f,g:A \to \mathbb{R}$ — функции такие что $f(x) \le g(x)$ для всех $x \in A$, тогда $\lim_{x\in A, x \to a}f(x) \le \lim_{x \in A, x \to a}g(x)$.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $\lim_{x\in A, x \to a}f(x) = \alpha$, $\lim_{x\in A, x \to a}g(x) = \beta$.

Тогда, по арифметике предела $\lim_{x\in A, x \to a}(g(x) - f(x)) = \beta - \alpha.$

Пусть $\alpha > \beta$. Пусть $\varepsilon : = \alpha - \beta$, тогда $\varepsilon >0$.

Из определения предела следует, что для выбранного $\varepsilon$, можно найти такое $\delta>0$, что из $d(x,a)<\delta$ будет следовать $|g(x) - f(x) - (\beta - \alpha)| < \varepsilon$, но тогда получаем, что
$$
g(x) - f(x) < \varepsilon + (\beta - \alpha) = 0,
$$
что даёт противоречие. Это и доказывает утверждение.
:::