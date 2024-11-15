---

numbering:
  enumerator: 3.2.%s

---

# 3.2. Компактность на прямой

Прежде всего, мы разберём топологию подмножеств на вещественной прямой. 

## Открытость и замкнутость в подмножествах

:::{prf:definition}
:name: e-neigh_in_A
Пусть $A \subseteq \mathbb{R}$ — непустое подмножество в $\mathbb{R}$, **$\varepsilon$-окрестностью точки $a \in A$ в множестве $A$** называется множество вида $(a-\varepsilon, a+\varepsilon) \cap A$. Чтобы подчеркнуть, что рассматривается $\varepsilon$-окрестность в $A$, мы будем писать $\mathscr{B}_\varepsilon(a)|_A$. Таким образом, согласно определению,
$$
\mathscr{B}_\varepsilon(a)|_A: = \mathscr{B}_\varepsilon(a) \cap A.
$$

Далее, множество $\mathscr{U} \subseteq A$ называется **открытым в $A$**, если для любой точки $x \in \mathscr{U}$ найдётся такая $\varepsilon$-окрестность $\mathscr{B}_\varepsilon(x)|_A$, что $\mathscr{B}_\varepsilon(x)|_A \subseteq \mathscr{U}$.
:::

:::{warning}
Обратим внимание, что если $A = \mathbb{R}_{\ge 0} \subseteq \mathbb{R}$, то, например, $[0,1)$ — открытый шар в $A = \mathbb{R}_{\ge 0}$, так как $[0,1) = (-1,1) \cap \mathbb{R}_{\ge 0}$. Hо! В $\mathbb{R}$, $[0,1)$ и не открыт, и не замкнут!
:::

:::{prf:theorem}
:name: open_in_K
Для того, чтобы множество $\mathscr{U} \subseteq A$ было открыто в $A$, необходимо и достаточно, чтобы существовало такое открытое в $\mathbb{R}$ множество $\widetilde{\mathscr{U}} \subseteq \mathbb{R}$, что $\mathscr{U} = \widetilde{\mathscr{U}}\cap \mathbb{R}.$
:::

:::{prf:proof}
:class: dropdown
:nonumber:

(1) Пусть $\mathscr{U}$ открыто в $A$, это значит, что для любой точки $x \in \mathscr{U}$ можно найти $\varepsilon$-окрестность $\mathscr{B}_\varepsilon(x)|_A$ такую, что $\mathscr{B}_\varepsilon(x)|_A \subseteq \mathscr{U}$, **т.е.,** $\mathscr{B}_\varepsilon(x) \cap A \subseteq \mathscr{U}$.

Так как $\mathscr{U} = \cup_{x \in \mathscr{U}} \mathscr{B}_\varepsilon(x) \cap A$, то получаем следующее:

$$
\mathscr{U} = \bigcup_{x \in \mathscr{U}} \mathscr{B}_\varepsilon(x) \cap A = A \cap \left( \bigcup_{x \in \mathscr{U}} \mathscr{B}_\varepsilon(x) \right) =  A \cap \widetilde{\mathscr{U}},
$$
где $\widetilde{\mathscr{U}}: = \cup_{x\in \mathscr{U}} \mathscr{B}_\varepsilon(x) \subseteq \mathbb{R}$. Согласно [](#interval_is_open), [](#union_and_cap_of_open), множество $\widetilde{\mathscr{U}}$ — открыто в $\mathbb{R}$, что и доказывает необходимость.


(2) Пусть $\widetilde{\mathscr{U}}$ — открытое множество в $\mathbb{R}$, и пусть $x \in \mathscr{U} \cap A$. Так как $\widetilde{\mathscr{U}}$ — открыто в $\mathbb{R}$, то найдётся $\varepsilon$-окрестность $\mathscr{B}_\varepsilon(x) \subseteq \mathbb{R}$ такая, что $\mathscr{B}_\varepsilon(x) \subseteq \widetilde{\mathscr{U}}$. Тогда $A \cap \mathscr{B}_\varepsilon(x) \subseteq A \cup \widetilde{\mathscr{U}}$. Но согласно [](#e-neigh_in_A), $\mathscr{B}_\varepsilon(x)\cap A = : \mathscr{B}_\varepsilon(x)|_A$. Тогда включение $A \cap \mathscr{B}_\varepsilon(x) \subseteq A \cup \widetilde{\mathscr{U}}$ и означает, что $\widetilde{\mathscr{U}} \cap A$ открыто в $A$, ибо $x$ — произвольная точка в $\widetilde{\mathscr{U}} \cap A.$
:::

:::{prf:definition}
:name: closed_in_A
Пусть $A \subseteq \mathbb{R}$ — непустое множество, множество $F \subseteq A$ называется **замкнутым в $A$**, если существует такое открытое множество $\mathscr{U}$ в $A$, что $F = A \setminus \mathscr{U}$. 
:::

:::{prf:remark}
Иногда также говорят об относительной открытости или относительной замкнутости какого-то множества относительно выделенного подмножества.
:::

:::{prf:proposition}
:name: closed_in_A_if
Множество $F$ замкнуто в $A$ тогда и только тогда, когда существует такое замкнутое $\widetilde{F}$ в $\mathbb{R}$ множество, что $F  = A \cap \widetilde{F}.$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Нам понадобится равенство 
\begin{equation}\label{good_for_us}
B \cap (\mathbb{R} \setminus C) = B \setminus (B \cap C),
\end{equation}
которое верно для любых подмножеств $B,C \subseteq \mathbb{R}$.
Действительно, если $x \in B \cap (\mathbb{R} \setminus C)$, то $x \in B$ и $x \in \mathbb{R} \setminus C$, т.е. $x \notin C$, а это значит, что $x \in B \setminus (B \cap C)$. Наоборот, если $x \in B \setminus (B \cap C)$, то $x \in B$, но $x \notin B \cap C$, т.е. $x \notin C$, а это значи, что $x \in \mathbb{R} \setminus C$.

(1) Пусть $F$ — замкнуто в $A$, тогда (см. [](#closed_in_A)), $A\setminus F$ — открыто в $A$, а тогда, согласно [](#open_in_K), существует такое открытое в $\mathbb{R}$ множество $\mathscr{U}$, что $A \setminus F = A \cap \mathscr{U}$. Пусть $\widetilde{F}: = \mathbb{R} \setminus\mathscr{U}$, тогда, согласно [](#def_of_closed), $\widetilde{F}$ — замкнуто в $\mathbb{R}$, а согласно [](#good_for_us), имеем
$$
A \cap \widetilde{F} = A \cap (\mathbb{R}\setminus \mathscr{U}) = A \setminus (A \cap \mathscr{U}) = A\setminus(A \setminus F) = F, 
$$
что и требовалось доказать.

(2) Пусть теперь $\widetilde{F}$ — замкнутое множество в $\mathbb{R}$, покажем, что $\widetilde{F} \cap A$ — замкнуто в $A.$ Согласно [](#def_of_closed), найдётся такое открытое в $\mathbb{R}$ множество $\mathscr{U}$, что $\widetilde{F} = \mathbb{R}\setminus \mathscr{U}$, тогда, воспользовавшись равенством [](#good_for_us), имеем
$$
A \cap \widetilde{F} = A \cap (\mathbb{R}\setminus \mathscr{U}) = A \setminus (A \cap \mathscr{U}),
$$
но согласно [](#open_in_K), множество $A \cap \mathscr{U}$ — открыто в $A$, а тогда, согласно [](#closed_in_A), множество $A \setminus (A \cap \mathscr{U})$ — замкнуто в $A$. Тем самым предложение полностью доказано.
:::


## Понятие компактности

:::{prf:definition}

Пусть $X$ — произвольное непустое множество. Множество $(\mathscr{U}_\lambda)_{\lambda \in \Lambda}$ подмножеств множества $X$ называется его **покрытием**, если $X = \bigcup_{\lambda \in \Lambda} \mathscr{U}_\lambda$.    

Если $X \subseteq Y$, то множество $(\mathscr{U}_\lambda)_{\lambda \in \Lambda}$ подмножеств множества $Y$ называется **покрытием** множества $X\subseteq Y$, если $X \subseteq \bigcup_{\lambda \in \Lambda} U_\lambda$.

Если $(\mathscr{U}_\lambda)_{\lambda \in \Lambda}$ — покрытие для $X$, то подпокрытием называют какие-то части этого покрытия, т.е. если существует такое $\Lambda' \subseteq \Lambda$, что $X = \bigcup_{\lambda \in \Lambda '}\mathscr{U}_{\lambda}$.
:::


:::{prf:example}
Пусть $X = \mathbb{R}$, и $\mathscr{U}_\alpha: = (-\alpha, \alpha)$, где $\alpha$ — любое ненулевое положительное вещественное число, тогда ясно что $\mathbb{R}  = \cup_{\alpha \in \mathbb{R}} (-\alpha, \alpha)$. Таким образом, мы получили покрытие $\{(-\alpha ,\alpha)\}_{\alpha \in \mathbb{R}_+}$. Если теперь мы ограничимся рассмотрением только рациональных чисел, т.е. рассмотрением интервалов $(-r, r)$, где $r \in \mathbb{Q}_+$, то мы получаем подпокрытие $\{(-r, r)\}_{r\in \mathbb{Q}_+}$ для $\mathbb{R}$, ведь $\mathbb{R} = \cup_{r\in \mathbb{Q}_+}(-r,r)$. В этом случае $\Lambda = \mathbb{R}_+$, $\Lambda'= \mathbb{Q}_+$. Можно рассмотреть только целые положительные числа, и тогда получаем ещё одно подпокрытие $\{(-n,n)\}_{n \in \mathbb{N}}$ для $\mathbb{R}$.
:::


:::{prf:example}
Пусть $X = [0,1)$, $Y = \mathbb{R}$, ясно, что $X \subseteq Y$. Тогда, например, множества
$$
\{(-1,2), (0,5)\},\qquad  \{(-n,n)\}_{n \in \mathbb{N}}, \qquad \left\{\left[0,1-\frac{2}{n}\right)\right\}_{n \in \mathbb{N}},  
$$ 
являются покрытиями для $X$ множествами из $Y$, так как
$$
[0,1) \subseteq (-1,2) \cup (0,5), \qquad [0,1) \subseteq \bigcup_{n \in \mathbb{N}} (-n,n), \qquad [0,1) \subseteq \bigcup_{n \in \mathbb{N}}\left[0,1-\frac{2}{n}\right),
$$
а так как 
$$
[0,1) = \bigcup_{n \in \mathbb{N}}\left[0,1-\frac{2}{n}\right),
$$
то последнее множество — это есть просто покрытие для $X$, так как все $\left[0,1-\frac{2}{n}\right)$ находятся в $X$.
:::


:::{prf:definition}
Непустое множество $K \subseteq \mathbb{R}$ называется **компактным**, если в любом его открытом покрытии всегда можно найти подпокрытие, состоящее из конечного числа множеств.
:::

:::{seealso}
Другими словами, это означает следующее: если множество $K$ компактно, то **какое бы бесконечное** покрытие мы не придумали для него, **ВСЕГДА** из этого покрытия можно выделить конечный набор множеств, которые покроют весь $K$.
:::

:::{warning}
На самом деле свойство быть компактным является *внутренним* свойством этого множества, т.е. неважно покрываем мы его открытыми множествами во всей прямой или же только открытыми в нём.
:::

:::{prf:theorem}
Пусть $K\subseteq \mathbb{R}$ — непустое множество, тогда следующие условия равносильны;

1. для любого открытого покрытия для $K$ можно всегда найти конечное подпокрытие для $K$,
2.  для любого открытого в $K$ покрытия для $K$ можно всегда найти конечное подпокрытие для $K$.

:::

:::{prf:proof}
:class: dropdown
:nonumber:

$(1) \Longrightarrow (2).$ Пусть $K$ — компактно, это значит, что для любого покрытия $\{\widetilde{\mathscr{U}}_\alpha\}_{\alpha \in A}$ множества $K$ открытыми множествами в $\mathbb{R}$ можно всегда найти конечное подпокрытие, скажем, $K \subseteq \cup_{i=1}^n \widetilde{\mathscr{U}}_i$, но тогда 
$$
K = K \cap \bigcup_{i=1}^n \widetilde{\mathscr{U}}_i= \bigcup_{i=1}^n \mathscr{U}_i
$$
но, согласно определению [](#e-neigh_in_A), каждое $\mathscr{U}_\alpha : = \widetilde{\mathscr{U}}_\alpha \cap K$ — открыто в $K$, т.е. из (1) получаем (2).

$(1) \Longleftarrow (2).$ Пусть $\{ \mathscr{U}_\alpha \}_{\alpha \in A}$ — покрытие $K$, т.е. $K = \cup_{\alpha \in A} \mathscr{U}_\alpha$, где все $\mathscr{U}_\alpha \subseteq K$ открыты в $K$, но тогда (см. Теорему [](#open_in_K)) для каждого $\alpha \in A$ существует открытое множество $\widetilde{\mathscr{U}}_\alpha$ в $\mathbb{R}$ такое, что $\mathscr{U}_\alpha= \widetilde{\mathscr{U}}_\alpha \cap K$. Тогда $K \subseteq \cup_{\alpha \in A} \widetilde{\mathscr{U}}_\alpha.$ Так как по условию (2), можно найти конечное число множеств, скажем, $\mathscr{U}_1, \ldots, \mathscr{U}_n$, таких, что $K = \cup_{i=1}^n\mathscr{U}_i$, то тогда $K \subseteq \cup_{i=1}^n \widetilde{\mathscr{U}}_i$, что и показывает (1).
:::


:::{prf:theorem}
:name: [a,b]is_compact
Любой отрезок $[a,b] \subsetneq \mathbb{R}$ конечной длины $a<b$, является компактным множеством.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Доказывать будем от противного. Допустим, что существует такое покрытие $\{\mathscr{U}_\alpha\}_{\alpha \in A}$ открытыми множествами из $\mathbb{R}$ для отрезка $I = [a,b]$, что из него нельзя выбрать конечное подпокрытие. 

Итак, пусть $I \subseteq \bigcup_{\alpha \in A} \mathscr{U}_\alpha$ и из этого покрытия нельзя выбрать конечное подпокрытие, которое бы покрыло $I$. Разобьём $I$ пополам **т.е** представим его так:
$$
[a, b] = \left[ a, \frac{a+b}{2} \right] \cup \left[\frac{a+b}{2}, b \right].
$$


По условию $I$ нельзя покрыть конечным числом множеств из $\{ \mathscr{U}_\alpha\}_{\alpha \in A}$, тогда хотя бы один из полученных отрезков, обозначим его через $I_1$ тоже нельзя покрыть конечным числом множеств из покрытия $\{ \mathscr{U}_\alpha\}_{\alpha \in A}$. Иначе бы оба полученных отрезка покрывались бы конечным числом множества из покрытия, а тогда и $I$ покрывался бы конечным числом множеств из этого покрытия, что и показывала бы компактность $I$. 

Разобьём теперь отрезок $I_1$ аналогичным образом на два равных отрезка. Так как $I_1$ нельзя покрыть конечным числом множеств из покрытия $\{ \mathscr{U}_\alpha\}_{\alpha \in A}$, то найдётся хотя бы один, скажем, $I_2$, из только что полученных, который тоже нельзя покрыть конечным числом множеств. Будем повторять эту процедуру каждый раз, пусть $I_k = [a_k,b_k]$, $k\ge 1$. В результате мы получаем бесконечную цепь вложенных друг в друга отрезков 
$$
I \supsetneq I_1 \supsetneq I_2 \supsetneq \ldots,
$$
каждый из которых нельзя покрыть конечным числом элементов множества $\{\mathscr{U}_\alpha\}_{\alpha \in A}$. Более того, их длины строго уменьшаются (каждый из отрезков по длине в два раза меньше, чем предыдущий). Тогда по Лемме о вложенных отрезках (Лемма [](#cap_of_intervals)), существует такая точка $c \in I$, что $c \in \bigcap_{k \ge 1} I_k $,
которая есть предел для последовательности их концов;
$$
\lim_{k\to \infty }a_k  = c = \lim_{n \to \infty}b_n.
$$

Тогда для любого $\varepsilon >0$ найдётся такой номер $N$, что при $k \ge N$ все $a_k, b_k \in (c - \varepsilon, c + \varepsilon)$, а по построению это значит, что и все $I_k \subseteq (c-\varepsilon, c+\varepsilon)$, $k \ge N.$

С другой стороны, так как имеется покрытие $\{\mathscr{U}_\alpha\}_{\alpha \in A}$ этого отрезка $I$, то найдётся хотя бы одно открытое множество $\mathscr{U}_\alpha$ такое, что $c \in \mathscr{U}_\alpha.$, а так как оно открытое, то для точки $c$ можно найти $\varepsilon$-окрестность $(c-\varepsilon, c+ \varepsilon) \subseteq \mathscr{U}_\alpha.$ 

Таким образом, мы получаем, что для всех $k \ge N$ есть включения
$$
I_k \subseteq (c-\varepsilon, c+ \varepsilon) \subseteq \mathscr{U}_\alpha,
$$
но это значит, что все отрезки $I_k$ покрываются всего одним открытым множеством $\mathscr{U}_\alpha$, что противоречит построению отрезков $I_k$, т.е. такое построение невозможно, что и означает компактность отрезка $I.$
:::

Теперь у нас всё готово, чтобы описать компактные множества в $\mathbb{R}$.

:::{prf:theorem} Свойства компакта
:name: properties_of_compact_in_R
Любое компактное множество $K$ в $\mathbb{R}$ обладает следующими свойствами;

1. $K$ — ограниченное множество.
2. $K$ — замкнутое множество
3. Любое замкнутое в $K$ подмножество множества $K$ компактно.
 
:::

:::{prf:proof}
:class: dropdown
:nonumber:

(1)  Рассмотрим произвольную точку $x\in K$ и рассмотрим такое открытое покрытие $\{(x-n,x+n)\}_{n=1}^\infty$ для $K$. Так как $K$ — компактно, то из этого покрытия можно выбрать конечное подпокрытие, скажем, $\{ (x-r,x+r) \}_{r=t}^N$, такое, что $K \subseteq \cup_{t=1}^N  (x-t, x+t)$. Так как $(x-p,x+p) \subseteq (x-q,x+q)$ при $p<q$, то $\cup_{t=1}^N  (x-t, x+t) = (x_N, x+N)$, т.е. $K \subseteq (x-N, x+N)$, что и означает ограниченность $K.$

(2) Пусть $y \in \overline{K}$, но $y \notin K$. Для каждого $x\in K$ рассмотрим числа $\delta_x, \varepsilon_x >0$, чтобы $\delta_x + \varepsilon_x < |x-y|$, тогда $(x-\delta_x, x+\delta_x) \cap (y-\varepsilon_x, y+\varepsilon_x) = \varnothing.$ Ясно, что $K \subseteq \cup_{x \in K} (x-\delta_x, x+\delta_x)$ и так как $K$ — компактно, то можно найти конечное множество точек $\{x_1,\ldots, x_n\}$ такое, что $K \subseteq \cup_{i=1}^n (x_i-\delta_i, x_i+\delta_i)$, где $\delta_i := \delta_{x_i}$, $1\le i \le n.$ Для всех таких $x_i$ мы выбираем $\varepsilon_i>0$ так, чтобы $(y-\varepsilon_i, y+\varepsilon_i) \cap (x_i-\delta_i, x_i+\delta_i = \varnothing$. Но тогда, полагая $\varepsilon: = \min \{\varepsilon_1, \ldots, \varepsilon_n\}$, получаем, что
$$
(y-\varepsilon, y+\varepsilon) \cap K \subseteq (y-\varepsilon, y+\varepsilon) \cap \bigcup_{i=1}^n (x_i - \delta_i, x_i+ \delta_i) = \varnothing,
$$
т.е. мы нашли $\varepsilon$-окрестность $(y-\varepsilon, y+\varepsilon)$ точки $y$, которая не пересекается с $K$. Но это означает (см. [](#limit_point), [](#closure)), что $y \notin \overline{K}$.  Поэтому если $y\in \overline{K}$, то $y \in K$, т. е. $\overline{K} = K.$



(3) Пусть $F \subseteq K$ — замкнутое подмножество в $K$, и пусть $\{\mathscr{U}_\alpha\}_{\alpha \in A}$ — покрытие $F$ открытыми множествами в $K$, т.е. $F \subseteq \cup_{\alpha \in A} \mathscr{U}_\alpha$.

Тогда имеем
$$
K = F \cup (K \setminus F) \subseteq \bigcup_{\alpha \in A} \mathscr{U}_\alpha \cup (K \setminus F),
$$
но ясно, что $K = \bigcup_{\alpha \in A} \mathscr{U}_\alpha \cup (K \setminus F)$, потому что если есть $x \in \bigcup_{\alpha \in A} \mathscr{U}_\alpha \cup (K \setminus F)$, но $x \notin 
K$, то это значит, что найдётся хотя бы один $\mathscr{U}_\alpha$, что $x \in \mathscr{U}_\alpha$, но все $\mathscr{U}_\alpha \subseteq K$ — открытые подмножества, поэтому $K = \bigcup_{\alpha \in A} \mathscr{U}_\alpha \cup (K \setminus F).$

Таким образом, мы получили покрытие для $K$, но так как $K$ — компактно, то можно найти такие, скажем, $\mathscr{U}_1, \ldots, \mathscr{U}_n$, что 
$$
K = \mathscr{U}_1 \cup \cdots \cup \mathscr{U}_n \cup (K \setminus F),
$$
но тогда 
$$
F \subseteq \mathscr{U}_1 \cup \cdots \cup \mathscr{U}_n,
$$
что означает компактность $F.$
:::

:::{prf:theorem} Критерий компактности в $\mathbb{R}$
:name: criterai_of_compacness_in_R
Множество $K \subseteq \mathbb{R}$ компактно тогда и только тогда, когда оно замкнуто и ограничено.    
:::
:::{prf:proof}
:class: dropdown
:nonumber:

(1) Согласно [](#properties_of_compact_in_R) (1), мы получаем необходимость.

(2) Если $K \subseteq \mathbb{R}$ ограничено и замкнуто, то это значит, что оно содержится в некотором отрезке $I$, который в силу [](#[a,b]is_compact) является компактным в $\mathbb{R}$. Далее, отрезок $I$ — замкнут (см. [](#[a,b]is_closed)), а так как $K = I \cap K$, то согласно [](#closed_in_A_if), $K$ — замкнут в $I$. Наконец, из [](#properties_of_compact_in_R) (3) вытекает утверждение. 
:::