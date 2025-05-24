---

numbering:
  enumerator: 3.1.%s

---

# 3.1 Открытость и замкнутость

## Открытые множества и окрестности

:::{prf:definition}
**Окрестностью** точки $a \in \mathbb{R}$ радиуса $\varepsilon>0$ (=$\varepsilon$-окрестностью) называется множество
$$
\mathscr{B}_\varepsilon(a):=\{x\in \mathbb{R}\, :\, |x-a| < \varepsilon\} = (a-\varepsilon, a+\varepsilon).
$$
:::

:::{warning}
С одной стороны, любая $\varepsilon$-окрестность любой точки это непустое множество, так как сама точка там находится, а с другой стороны, так как $\varepsilon>0$, то не может быть такого, чтобы $\varepsilon$-окрестность состояла всего из одной точки.
:::


Теперь мы введём следующее, очень важное для дальнейшего, определение.

:::{prf:definition}
:name: open_in_R
**Открытым множеством** в $\mathbb{R}$ называется подмножество $\mathscr{U} \subseteq \mathbb{R}$, обладающее следующим свойством: для любой точки $a \in \mathscr{U}$ существует такое $\varepsilon >0$, что $\mathscr{B}_\varepsilon(a) \subseteq \mathscr{U}$.
:::

:::{prf:lemma}
:name: point_is_not_open
Множество $\{a\}$ состоящее из одной точки не является открытым в $\mathbb{R}$. 
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Если бы множество $\{a\}$ было бы открыто, то для любого $x\in \{a\}$ можно было найти такую $\varepsilon$-окрестность $\mathscr{B}_\varepsilon(x)=(x-\varepsilon, x+\varepsilon)$, что $\mathscr{B}_\varepsilon(x) \subseteq \{a\}$, но множество $\{a\}$ состоит всего из одной точки, а любая $\varepsilon$-окрестность точки $a$ состоит более чем из одной точки. Поэтому включение $\mathscr{B}_\varepsilon(a) \subseteq \{a\}$ невозможно, поэтому множество $\{a\}$ не открыто.
:::

:::{prf:lemma}
:name: interval_is_open
Любой интервал $(a,b) \subseteq \mathbb{R}$ является открытым множеством, а тогда и всякая открытая окрестность — это открытое множество.
:::
:::{prf:proof}
:class: dropdown
:nonumber: 
Пусть $(a,b)$ — интервал конечной длины, тогда на него можно посмотреть как на окрестность точки $c = \frac{a+b}{2}$ (= середина отрезка) с радиусом $r = \frac{b-a}{2}$, итак
$$
(a,b) = \mathscr{B}_r(c), \qquad c : = \frac{a+b}{2}, \qquad r: = \frac{b-a}{2}.
$$

Рассмотрим произвольную точку $x \in \mathscr{B}_r(c)$, отличную от точки $c$, т.е. $x \ne c$ и рассмотрим её окрестность $\mathscr{B}_\delta(x)$, где $0 < \delta < r-|c-x|$. Покажем, что $\mathscr{B}_\delta(x) \subseteq (a,b)$, это и докажет требуемое.

Возьмём произвольную точку $y\in \mathscr{B}_\delta(x)$, тогда $|x-y|<\delta$, а в силу выбора $\delta$, мы также получаем, что $|x-y| < \delta < r-|c-x|.$

```{figure} ./images/open_is_open.jpg
На зелёном интервале с центром в точке $c$ мы рассматриваем произвольную синюю точку $x$ и окружаем её синей окрестностью так, чтобы она целиком была в зелёном интервале.
```

Далее, используя неравенство треугольника[^ref47-1], получаем
$$\begin{align*}
|c-y| &= |c+x-x-y| \\
&= |(c-x) + (x-y)| \\
&\le |c-x| + |x-y| \\
&< |c-x| + \delta \\
&< |c-x| + r- |c-x| \\
&= r,
\end{align*}$$
т.е. $|c-y| < r$, а значит, $y \in \mathscr{B}_r(c)$, но это и показывает, что $\mathscr{B}_\delta(x) \subseteq (a,b)$ для любой точки $x \in (a,b)$, т.е. интервал $(a,b)$ — открыт. Это завершает доказательство.
:::

:::{prf:lemma}
:name: empty_is_open
Пустое множество открыто.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Будем рассуждать от противного. Пусть $\varnothing$ не является открытым. Тогда это значит, что найдётся хотя бы одна точка $x \in \varnothing$, что для любого $\delta >0$, $\mathscr{B}_\delta(x) \not\subseteq \varnothing$. Но в таком случае это значит, что $\varnothing$ не является пустым множеством, что даёт противоречие. Это доказывает лемму.
:::

:::{warning}
То рассуждение, которое было проведено, в англоязычной среде называют **a vacuous proof**. 
:::


:::{prf:lemma}
:name: union_and_cap_of_open
Объединение любого семейства открытых множеств открыто, и пересечение конечного числа открытых множеств открыто. 
:::
:::{prf:proof}
:class: dropdown
:nonumber:\

(1) Пусть $\mathscr{U} = \cup_{\alpha \in A}\mathscr{U}_\alpha$ и пусть $x \in \mathscr{U}$, тогда для какого-то $\alpha \in A$, $x \in \mathscr{U}_a$. Так как $\mathscr{U}_\alpha$ открыто, то найдётся такой $\varepsilon >0$, что $\mathscr{B}_\varepsilon(x) \subseteq \mathscr{U}_\alpha \subseteq \cup_{\alpha \in A}\mathscr{U}_\alpha$, что и доказывает открытость множества $\mathscr{U}.$

(2) Достаточно доказать, что пересечение двух открытых множеств $\mathscr{U}_1, \mathscr{U}_2$ открыто, а затем провести индукцию.

Если $x \in \mathscr{U}_1 \cap \mathscr{U}_2$, то найдутся такие $\varepsilon_1, \varepsilon_2 >0$, что $B_{\varepsilon_1}(x) \subseteq \mathscr{U}_1$, $B_{\varepsilon_2}(x) \subseteq \mathscr{U}_2$. Тогда, если $\varepsilon: = \min(\varepsilon_1,\varepsilon_2)$, то $B_\varepsilon(x) \subseteq \mathscr{U}_1 \cap \mathscr{U}_2$, что и доказывает открытость пересечения.
:::

:::{warning}
Пересечение бесконечного числа открытых множеств, вообще говоря, **не будет** открытым.
:::

:::{prf:example}
Рассмотрим бесконечное семейство $\{\mathscr{U}_n\}_{n \in \mathbb{N}}$ открытых интервалов 
$$
\mathscr{U}_n:= \left( -\frac{1}{n}, \frac{1}{n}\right)
$$
нетрудно видеть, что $\cap_{n=1}^\infty \mathscr{U}_n = \{0\}$, а в силу [](#point_is_not_open), множество $\{0\}$ не открыто.  
:::


:::{prf:corollary}
:name: R_is_open
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
и так как каждое из множеств, участвующее в объединениях, открыто, то по [](#union_and_cap_of_open) мы получаем, что вся прямая $\mathbb{R}$ и лучи $(-\infty, a), (a, +\infty)$, $a\in \mathbb{R}$ открытые множества.
:::


:::{prf:definition}
:name: neigh_of_point
**Окрестностью точки** $x\in \mathbb{R}$ называется **любое** открытое множество, содержащее эту точку.
:::

Таким образом, окрестность радиуса $\varepsilon$ — это частный случай окрестности.  

:::{prf:proposition}
:name: open_via_open
Множество $\mathscr{U} \subseteq \mathbb{R}$ открыто тогда и только тогда, когда для любой точки $x$ существует такое открытое $\mathscr{V}$, что $x\in \mathscr{V} \subseteq \mathscr{U}.$
:::

:::{prf:proof}
:class: dropdown
:nonumber:

(1) Пусть $\mathscr{U}$ — открыто, тогда, согласно [](#open_in_R), для любой точки $x\in \mathscr{U}$ существует такая $\varepsilon$-окрестность $\mathscr{B}_\varepsilon(x)$, что $x \in \mathscr{B}_\varepsilon(x) \subseteq \mathscr{U}$, т.е. полагая $\mathscr{V}: = \mathscr{B}_\varepsilon(x)$, что и доказывает необходимость.

(2) Пусть $\mathscr{U}$ обладает тем свойством, что для любой точки $x$ существует такое открытое $\mathscr{V}_x$, что $x\in \mathscr{V}_x \subseteq \mathscr{U}.$ Рассмотрим множество
$$
\widetilde{\mathscr{U}}:=\bigcup_{x\in \mathscr{U}}\mathscr{V}_x,
$$
и покажем, что $\widetilde{\mathscr{U}} = \mathscr{U}$. Пусть $y\in \widetilde{\mathscr{U}}$, тогда существует хотя бы один $\mathscr{V}_x$, что $y \in \mathscr{V}_x$, но так как $\mathscr{V}_x \subseteq \mathscr{U}$, то $y \in \mathscr{U}$, поэтому $\widetilde{\mathscr{U}} \subseteq \mathscr{U}.$ Пусть теперь $x \in \mathscr{U}$, но тогда, согласно условию, существует такой $\mathscr{V}_x$, что $x \in \mathscr{V}_x \subseteq \mathscr{U}$, но тогда $x \in \widetilde{\mathscr{U}}$, потому что $\widetilde{\mathscr{U}} = \cup_{x \in \mathscr{U}}\mathscr{V}_x$, т.е. $\mathscr{U} \subseteq \widetilde{\mathscr{U}}$, а значит, $\mathscr{U} = \widetilde{\mathscr{U}}.$

Так как, согласно условию, каждый $\mathscr{V}_x$ — открытое множество, то согласно [](#union_and_cap_of_open), $\mathscr{U}$ — открытое множество, что и требовалось доказать.
:::


## Внутренние и внешние точки множества

:::{prf:definition}
:name: interior_point
Точка $x$ называется **внутренней точкой** множества $A \subseteq \mathbb{R}$, если существует такая окрестность $\mathscr{U}(x)$ (см. [](#neigh_of_point)) точки $x$, что $\mathscr{U}(x) \subseteq A.$ Множество всех внутренних точек множества $A$ называется **внутренностью** множества $A$ и обозначается $\mathrm{Int}(A).$
:::

:::{warning}
Если $A \ne \varnothing$, то может быть, что $\mathrm{Int}(A) = \varnothing$. Например, если $A =\{a\}$.
:::


:::{prf:proposition}
:name: int(A)_is_open
Для любого множества $A \subseteq \mathbb{R}$ множество $\mathrm{Int}(A)$ открыто.
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $x \in \mathrm{Int}(A)$, тогда существует такая окрестность $\mathscr{U}(x)$, что $x\in \mathscr{U}(x) \subseteq A$, но согласно [](#neigh_of_point), $\mathscr{U}(x)$ — открыто. Далее, для любой точки $y\in \mathscr{U}(x)$, мы получаем, что это же открытое множество $\mathscr{U}(x)$ есть её окрестность. Тогда для любой точки $y\in \mathscr{U}(x)$ положим $\mathscr{U}(y): = \mathscr{U}(x)$. Таким образом, все точки множества $\mathscr{U}(x)$ — внутренние, но это значит, что $\mathscr{U}(x) \subseteq \mathrm{Int}(A)$. Теперь, [](#open_via_open), мы завершаем доказательство.
:::



:::{prf:proposition}
:name: U_is_openUIntU
Множество $\mathscr{U} \subseteq \mathbb{R}$ открыто тогда и только тогда, когда $\mathscr{U} = \mathrm{Int}(\mathscr{U}).$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Действительно, согласно [](#int(A)_is_open), множество $\mathrm{Int}(\mathscr{U})$ — открыто. Далее, если $\mathscr{U}$ — открыто, то в силу [](#open_in_R), каждая его точка — внутренняя, что и означает $\mathscr{U} = \mathrm{Int}(\mathscr{U})$. Если же $\mathscr{U} = \mathrm{Int}(\mathscr{U})$, то каждая точка множества $\mathscr{U}$ является внутренней, но тогда, согласно [](#interior_point), это означает, что существует $\varepsilon$-окрестность этой точки которая целиком будет лежать в $\mathscr{U}$, т.е. согласно [](#open_in_R) означает открытость $\mathscr{U}$.
:::

:::{prf:example}
:name: (a,b)c(open
Согласно определению, имеем
$$\begin{align*}
\mathrm{Int}([a,b]) &=& (a,b),\\
\mathrm{Int}([a,b)) &=& (a,b),\\
\mathrm{Int}((a,b]) &=& (a,b),\\
\mathrm{Int}((a,b)) &=& (a,b),
\end{align*}$$
потому что ни $a$, ни $b$ не могут быть внутренними точками этих множеств; любая их $\varepsilon$-окрестность не может содержаться в этих множествах.

Таким образом, согласно [](#U_is_openUIntU), множества

$$
[a,b], \qquad [a,b), \qquad (a,b]
$$
не являются открытыми, а множество $(a,b)$ — открыто.
:::

:::{prf:example}
:name: (a,8)c(open)
Рассмотрим теперь множества $(a, +\infty)$, $[a,\infty)$, $(-\infty, b)$,  $(-\infty,b]$. Так как для точек $a,b$ любая их $\varepsilon$-окрестность не может содержаться в этих множествах, то получаем
$$\begin{align*}
\mathrm{Int}((a, +\infty)) &=& (a, +\infty), \\
\mathrm{Int}([a, +\infty)) &=& (a, +\infty), \\
\mathrm{Int}((-\infty, b)) &=& (-\infty, b), \\
\mathrm{Int}((-\infty, b]) &=& (-\infty, b),
\end{align*}$$
тогда, согласно [](#U_is_openUIntU), множества
$$
[a, +\infty), \qquad (-\infty, b]
$$
не являются открытыми, а множества  $(a, +\infty)$, $(-\infty, b)$ — открыты.
:::


:::{prf:definition}
Внутренняя точка множества $\mathbb{R}\setminus A$ называется **внешней точкой** множества $A$, а внутренность множества $\mathbb{R}\setminus A$ называется **множеством внешних точек** множества $A$.
:::



## Замкнутые множества

:::{prf:definition}
:name: def_of_closed
**Замкнутое множество** в $\mathbb{R}$ есть дополнение открытого множества. 
:::

:::{prf:lemma}
Пустое множество $\varnothing$ и вся прямая $\mathbb{R}$ — замкнутые множества.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Действительно, согласно [](#empty_is_open), множество $\varnothing$ — открыто в $\mathbb{R}$, а так как $\mathbb{R} = \mathbb{R}\setminus \varnothing$, то значит, $\mathbb{R}$ — замкнуто. Далее, согласно [](#R_is_open), множество $\mathbb{R}$ — открыто, а так как $\varnothing = \mathbb{R} \setminus \mathbb{R}$, то значит, множество $\varnothing$ — замкнуто.
:::

:::{warning}
Таким образом, множества $\mathbb{R}$, $\varnothing$ одновременно и открыты, и замкнуты; и вообще, не следует считать, что замкнутость — это отрицание открытости.
:::

:::{prf:example}
:name: abis_closed
Рассмотрим множества $[a,b]$, $[a,+\infty)$ и $(-\infty, b]$.

Имеем
$$\begin{align*}
[a,b] &=& \mathbb{R}\setminus ((-\infty, a) \cup (b, +\infty)),\\
{[a,+\infty)} &=& \mathbb{R} \setminus (-\infty, a),\\
{(-\infty, a]} &=& \mathbb{R} \setminus (a, +\infty),
\end{align*}$$
а так как согласно [](#(a,b)c(open)) [](#(a,8)c(open)), множества $(-\infty, a),$ $(b, +\infty)$ открыты, то множества $[a,b]$, $[a,+\infty)$ и $(-\infty, a]$ — замкнуты.
:::

:::{prf:lemma}
Пересечение любого семейства замкнутых множеств замкнуто, а объединение конечного числа замкнутых замкнуто.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $\{F_\alpha\}_{\alpha \in A}$ — какое-то семейство замкнутых множеств, тогда, согласно [](#def_of_closed), имеется семейство открытых множеств $\{\mathscr{U}_\alpha\}_{\alpha \in A}$, что $F_\alpha = \mathbb{R}\setminus \mathscr{U}_\alpha$ для любого $\alpha \in A.$

Согласно ([](#dM1)), ([](#dM1)) получаем
$$\begin{align*}
\bigcup_{i=1}^n F_i &=& \bigcup_{i=1}^n \mathbb{R} \setminus \mathscr{U}_i =  \mathbb{R} \setminus \bigcap_{i=1}^n\mathscr{U}_i, \\
\bigcap_{\alpha \in A} F_\alpha &=& \bigcap_{\alpha \in A} \mathbb{R} \setminus \mathscr{U}_\alpha = \mathbb{R} \setminus \bigcup_{\alpha \in A} \mathscr{U}_\alpha,   
\end{align*}$$
но согласно [](#union_and_cap_of_open), множества $\cap_{i=1}^n\mathscr{U}_i$, $\cup_{\alpha \in A} \mathscr{U}_\alpha$ — открыты, что и завершает доказательство.
:::

:::{warning}
Объединение бесконечного числа замкнутых, вообще говоря, не замкнуто. Более того, такое объединение может быть открытым множеством. Например, $\cup_{n=1}^\infty \left[\frac{1}{n},1-\frac{1}{n} \right] = (0,1).$
:::

:::{prf:lemma}
Множество $\{a\}$ является замкнутым множеством в $\mathbb{R}$.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Действительно, имеем
$$
\{a\} = \mathbb{R}\setminus \left( (-\infty, a) \cup (a, +\infty) \right),
$$
согласно [](#R_is_open), множества $(-\infty, a),$ $(a, +\infty)$ — открыты, а по [](#union_and_cap_of_open), множество $(-\infty, a) \cup (a, +\infty)$ — открыто, что и доказывает лемму.
:::

:::{warning}
Таким образом, любое множество $A$ в $\mathbb{R}$ можно представить как объедение замкнутых множеств, так как $A = \cup_{a \in A}\{a\}.$
:::

:::{prf:definition}
:name: limit_point
**Точка прикосновения** множества $A$ — это такая точка $x \in \mathbb{R}$, каждая окрестность которой имеет с $A$ непустое пересечение. Множество всех точек прикосновения называется **замыканием** множества $A$ и обозначается символом $\overline{A}.$
:::

:::{warning}
Таким образом, любая точка $a\in A$ есть точка прикосновения, а обратное, конечно же, неверно.
:::

:::{prf:remark}
Сказать, что **$x$ не является** точкой прикосновения множества $A$, значит сказать, что $x$ является внутренней точкой множества $\mathbb{R}\setminus A.$ 
:::

:::{prf:proposition}
:name: closure(A)=R-(R-A)
Для любого множества $A \subseteq \mathbb{R}$, $\overline{A} = \mathbb{R}\setminus \mathrm{Int}(\mathbb{R}\setminus A).$    
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Мы воспользуемся следующим фактом: $X = Y$ тогда и только тогда, когда $E\setminus X = E \setminus Y$, где $X,Y \subseteq E$.

Поэтому нам достаточно показать, что $\mathbb{R} \setminus \overline{A} = \mathrm{Int}( \mathbb{R}\setminus A).$

Если $x \in \mathbb{R} \setminus \overline{A}$, то $x \notin \overline{A}$, а это значит, что существует такая окрестность $\mathscr{U}(x)$, что $\mathscr{U}(x) \cap A = \varnothing$, т.е. $\mathscr{U}(x) \subseteq \mathbb{R}\setminus A$, а тогда это значит, что $x \in \mathrm{Int}(\mathbb{R} \setminus A)$, поэтому $\mathbb{R} \setminus \overline{ A} \subseteq \mathrm{Int}(\mathbb{R} \setminus A).$

Если $x \in \mathrm{Int}(\mathbb{R} \setminus A)$, то найдётся такая её окрестность $\mathscr{U}(x)$, что $\mathscr{U}(x) \subseteq \mathbb{R}\setminus A$, **т.е. ** $\mathscr{U}(x) \cap A = \varnothing $, а это значит, что $x$ не может быть точкой прикосновения, т.е. $x \in \mathbb{R}\setminus \overline{A}$, поэтому $\mathbb{R} \setminus \overline{ A} \supseteq \mathrm{Int}(\mathbb{R} \setminus A)$, что и доказывает утверждение.
:::

:::{prf:corollary}
Для любого $A\subseteq \mathbb{R}$, множество $\overline{A}$ — замкнуто. 
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Согласно [](#closure(A)=R-(R-A)), $\overline{A} = \mathbb{R}\setminus \mathrm{Int}(\mathbb{R}\setminus A)$, а согласно [](#int(A)_is_open), множество $ \mathrm{Int}(\mathbb{R}\setminus A)$ открыто, поэтому $\overline{A}$ — замкнуто.
:::

:::{prf:example}
Рассмотрим множества $(a,b), (a,b], [a,b), [a,b]$, точки $a,b$ являются точками прикосновения для обоих этих множеств, так как любая $\varepsilon$-окрестность (а значит, и любая вообще) этих точек имеет непустое пересечение, например,
$$
(a-\varepsilon, a+\varepsilon)\cap (a,b] = \begin{cases}
(a,a+\varepsilon], & a+\varepsilon \le b \\
(a,b], & a+\varepsilon > b, 
\end{cases}
$$
поэтому $\overline{(a,b)} = \overline{(a,b]} = \overline{[a,b)} = \overline{[a,b]} = [a,b].$
:::

:::{prf:definition}
Операция $A \mapsto \overline{A}$ называется замыканием множества $A\subseteq \mathbb{R}.$
:::


:::{prf:lemma}
:name: closure
Множество $F$ замкнуто, если и только если все его точки — это точки прикосновения, т.е. $F = \overline{F}.$ 
:::
:::{prf:proof}
:class: dropdown
:nonumber:
(1) Пусть $F$ — замкнуто, тогда найдётся какое-то открытое $\mathscr{U} \subseteq \mathbb{R}$ такое, что $F  = \mathbb{R} \setminus \mathscr{U}$. Пусть $x \notin F$, тогда $x \in \mathscr{U}$, и тогда найдётся окрестность $\mathscr{U}(x)$ такая, что $\mathscr{U}(x) \subseteq \mathscr{U}$, потому что $\mathscr{U}$ — открыто, т.е. $\mathscr{U}(x) \cap F = \varnothing.$ Таким образом, получили, что если $F$ — замкнуто, то никакая точка $x \notin F$ не может быть точкой прикосновения для $F$, т.е. $F = \overline{F}.$ 

(2) Пусть $F = \overline{F}$, тогда если $x \notin F$, то $x$ не может быть точкой прикосновения для $F$, а это значит, что можно найти окрестность $\mathscr{U}(x)$ такую, что $\mathscr{U}(x) \cap F = \varnothing$, иначе $x$ было бы точкой прикосновения. Итак, для любого $x \notin F$, мы имеем окрестность $\mathscr{U}(x)$ такую, что $\mathscr{U}(x) \cap F = \varnothing$. Рассмотрим теперь объединения всех таких окрестностей,
$$
\mathscr{U}:= \bigcup_{x \in \mathbb{R}\setminus F} \mathscr{U}(x),
$$
так как каждое $\mathscr{U}(x)$ открыто, то согласно [](#union_and_cap_of_open), $\mathscr{U}$ — открыто. 

Покажем, что $F = \mathbb{R} \setminus \mathscr{U}$, согласно ([](#dM1))
$$
\mathbb{R} \setminus \mathscr{U} = \mathbb{R} \setminus \bigcup_{x \in \mathbb{R}\setminus F} \mathscr{U}(x) = \bigcap_{x \in \mathbb{R} \setminus F} \mathbb{R} \setminus \mathscr{U}(x).
$$

Пусть $y \in F$, тогда $y \notin \mathscr{U}$, а тогда $y \in \mathbb{R}\setminus \mathscr{U}$, поэтому $F \subseteq \mathbb{R} \setminus \mathscr{U}$. Если $y \in \mathbb{R}\setminus \mathscr{U}$, то $y \in \cap_{x \in \mathbb{R} \setminus F} \mathbb{R} \setminus \mathscr{U}(x)$, т.е. для любого $x \notin F$, $y \in \mathbb{R}\setminus \mathscr{U}(x)$, т.е. $y \notin \mathscr{U}(x)$, но это значит, что $y \ne x$ для любого $x \notin F$, а тогда $y \in F$. Таким образом, $F \supseteq \mathbb{R} \setminus \mathscr{U}$, поэтому $F = \mathbb{R}\setminus \mathscr{U}.$ Это завершает доказательство леммы.
:::

:::{warning}
Множества $(a,b]$, $[a,b)$ и не открыты, и не замкнуты в $\mathbb{R}$, а множества $\varnothing,$ $\mathbb{R}$ и открыты, и замкнуты одновременно.
:::

[^ref47-1]: $|a+b|\le |a| + |b|.$