# Основные понятия

## Открытые множества и окрестности

:::{prf:definition}
**Окрестностью** точки $a \in \mathbb{R}$ радиуса $\varepsilon>0$ называется множество
$$
\mathscr{B}_\varepsilon(a):=\{x\in \mathbb{R}\, :\, |x-a| < \varepsilon\} = (a-\varepsilon, a+\varepsilon).
$$
Мы также будем рассматривать так называемые **проколотые** окрестности точки $a$, 
$$
\mathring{\mathscr{B}}_\varepsilon(x): = \mathscr{B}_\varepsilon(a) \setminus \{a\} = (a-\varepsilon, a) \cup (a, a+\varepsilon).
$$
:::

Теперь мы введём следующее очень важное для дальнейшего определение.

:::{prf:definition}
**Открытым множеством** в $\mathbb{R}$ называется подмножество $\mathscr{U} \subseteq \mathbb{R}$, обладающее следующим свойством: для любой точки $a \in \mathscr{U}$ существует такое $\varepsilon >0$, что $\mathscr{B}_\varepsilon(a) \subseteq \mathscr{U}$.
:::

:::{prf:lemma}
:name: interval_is_open
Любой интервал $(a,b) \subseteq \mathbb{R}$ является открытым множеством, а тогда и всякая открытая окрестность — это открытое множество.
:::
:::{prf:proof}
:class: dropdown
:nonumber: 
Пусть $(a,b)$ — интервал конечной длины, тогда на него можно посмотреть как на окрестность точки $c = \frac{b-a}{2}$ (= середина отрезка) с радиусом $r = \frac{a+b}{2}$, итак
$$
(a,b) = \mathscr{B}_r(c), \qquad c : = \frac{b-a}{2}, \qquad r: = \frac{a+b}{2}.
$$

Рассмотрим произвольную точку $x \in \mathscr{B}_r(c)$, отличную от точки $c$, т.е. $x \ne c$ и рассмотрим её окрестность $\mathscr{B}_\delta(x)$, где $0 < \delta < r-|c-x|$. Покажем, что $\mathscr{B}_\delta(x) \subseteq (a,b)$, это и докажет требуемое.

Возьмём произвольную точку $y\in \mathscr{B}_\delta(x)$, тогда $|x-y|<\delta$, а в силу выбора $\delta$, мы также получаем, что $|x-y| < \delta < r-|c-x|.$

\begin{figure}[h!]
\centering
\includegraphics[scale=0.5]{images/open_is_open.jpg}
\caption{На зелёном интервале с центром в точке $c$ мы рассматриваем произвольную синюю точку $x$ и окружаем её синей окрестностью так, чтобы она целиком была в зелёном интервале.}
\label{fig:enter-label}
\end{figure}

Далее, используя неравенство треугольника\footnote{$|a+b|\le |a| + |b|.$}, получаем
$$\begin{align*}
|c-y| &=& |c+x-x-y| \\
&=& |(c-x) + (x-y)| \\
&\le& |c-x| + |x-y| \\
&<& |c-x| + \delta \\
&<& |c-x| + r- |c-x| \\
&=& r,
\end{align*}$$
т.е. $|c-y| < r$, а значит, $y \in \mathscr{B}_r(c)$, но это и показывает, что $\mathscr{B}_\delta(x) \subseteq (a,b)$ для любой точки $x \in (a,b)$, т.е. интервал $(a,b)$ — открыт. Это завершает доказательство.
:::




:::{prf:lemma}
Пустое множество открыто.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Будем рассуждать от противного. Пусть $\varnothing$ не является открытым. Тогда это значит, что найдётся хотя бы одна точка $x \in \varnothing$, что для любого $\delta >0$, $\mathscr{B}_\delta(x) \not\subseteq \varnothing$. Но в таком случае это значит, что $\varnothing$ не является пустым множеством, что даёт противоречие. 
:::

:::{warning}
То рассуждение, которое было проведено в англоязычной среде, называют **a vacuous proof**. 
:::


:::{prf:lemma}
:name: union_and_cap_of_open
Объединение любого семейства открытых множеств открыто, и пересечение конечного числа открытых множеств открыто. 
:::
:::{prf:proof}
:class: dropdown
:nonumber:\

(1) Пусть $\mathscr{U} = \cup_{\alpha \in A}\mathscr{U}_\alpha$ и пусть $x \in \mathscr{U}$, тогда для какого-то $\alpha \in A$, $x \in \mathscr{U}_a$. Так как $\mathscr{U}_\alpha$ открыто, то найдётся такой $\varepsilon >0$, что $\mathscr{B}_\varepsilon(x) \subseteq \mathscr{U}_\alpha \subseteq \cup_{\alpha \in A}\mathscr{U}_\alpha$, что и доказывает открытость множества $\mathscr{U}.$

(2) Достаточно доказать, что множество двух открытых множеств $\mathscr{U}_1, \mathscr{U}_2$ открыто, а затем провести индукцию.

Если $x \in \mathscr{U}_1 \cap \mathscr{U}_2$, то найдутся такие $\varepsilon_1, \varepsilon_2 >0$, что $B_{\varepsilon_1}(x) \subseteq \mathscr{U}_1$, $B_{\varepsilon_2}(x) \subseteq \mathscr{U}_2$. Тогда, если $\varepsilon: = \min(\varepsilon_1,\varepsilon_2)$, то $B_\varepsilon(x) \subseteq \mathscr{U}_1 \cap \mathscr{U}_2$, что и доказывает открытость пересечения.
:::


:::{prf:corollary}
Вся прямая $\mathbb{R}$ и лучи $(-\infty, a), (a, +\infty)$, $a\in \mathbb{R}$ — открытые множества.
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Действительно, имеем
$$\begin{align*}
\mathbb{R} &=& \bigcup_{n=1}^\infty (-n,n),\\
(-\infty, a) &=& \bigcup_{\alpha <a} (\alpha, a),\\
(a, + \infty) &=& \bigcup_{\beta >a} (a,\beta),
\end{align*}$$
и так как каждое из множеств, участвующее в объединениях, открыто, то по лемме [](#union_and_cap_of_open) мы получаем, что вся прямая $\mathbb{R}$ и лучи $(-\infty, a), (a, +\infty)$, $a\in \mathbb{R}$ открытые множества.
:::



## Замкнутые множества

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
Множество $F$ в метрическом пространстве замкнуто, если и только если все его точки это предельные точки, т.е. $F = \overline{F}.$ 
:::
(1) Пусть $F$ — замкнуто, тогда найдётся какое-то открытое $\mathscr{U} \subseteq E$, такое, что $F  = E \setminus \mathscr{U}$. Пусть $x \notin F$, тогда $x \in \mathscr{U}$, и тогда найдётся окрестность $\mathscr{W}(x)$ такая, что $\mathscr{W}(x) \subseteq \mathscr{U}$, потому что $\mathscr{U}$ — открыто, т.е. $\mathscr{W}(x) \cap F = \varnothing.$ Таким образом, получили, что если $F$ — замкнуто, то никакая точка $x \notin F$ не может быть предельной для $F$, т.е. $F = \overline{F}.$ 

(2) Пусть $F = \overline{F}$, тогда для любой точки $x \notin F$, можно всегда найти окрестность $\mathscr{W}(x)$ такую, что $\mathscr{W}(x) \cap F = \varnothing$. Пусть $\mathscr{U}:= \cup_{x E\setminus F} \mathscr{W}(x)$, тогда, $\mathscr{U}$ — открыто в $E$ и $F = E \setminus \mathscr{U}.$


