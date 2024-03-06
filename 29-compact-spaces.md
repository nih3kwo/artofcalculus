# Компактные пространства

:::{prf:definition}
Пусть $X$ — произвольное непустое множество. Множество $(\mathscr{U}_\lambda)_{\lambda \in \Lambda}$ подмножеств множества $X$ называется его **покрытием**, если $X = \bigcup_{\lambda \in \Lambda} \mathscr{U}_\lambda$.    
:::

Имеется и другое, более широкое понимание этих терминов: множество $(\mathscr{U}_\lambda)_{\lambda \in \Lambda}$ подмножеств множества $Y$ называется **покрытием** множества $X\subseteq Y$, если $X \subseteq \bigcup_{\lambda \in \Lambda} U_\lambda$.


:::{prf:definition}
:label: c3def4
Метрическое пространство $E$ называется **компактным**, если оно удовлетворяет $\boxed{\text{аксиоме Бореля — Лебега}}$: для каждого покрытия $(\mathscr{U}_\lambda)_{\lambda \in \Lambda}$ пространства $E$ открытыми множествами (=открытое покрытие) существует конечное подсемейство $(\mathscr{U}_\lambda)_{\lambda \in L}$ (где $L \subseteq \Lambda$, и $L$ — конечное множество), являющееся покрытием пространства $E.$
:::

:::{prf:definition}
**Компактом** (или компактным множеством) в метрическом пространстве $(E,d)$ называется такое множество $K$, для которого метрическое подпространство $(K,d|_K)$ пространства $(E,d)$ компактно.
:::


:::{prf:lemma}
:label: c3proof4
Подпространство $K$ в метрическом пространстве $(E,d)$ — компакт тогда и только тогда, когда из любого его покрытия множествами, открытыми в $E$, можно выделить конечное подпокрытие этими же множествами.
:::

:::{prf:proof}
:class: dropdown
:nonumber:

(1) Пусть $(K,d|_K)$ — компактное подпространство в $(E,d)$, и пусть $\{ \mathscr{U}_\alpha \}_{\alpha \in A}$ — его покрытие, т. е. $K = \cup_{\alpha \in A} \mathscr{U}_\alpha$, где все $\mathscr{U}_\alpha \subseteq K$ открыты в $K$, но тогда (Предложение [](#open_in_subset)) для каждого $\alpha \in A$ существует открытое множество $\widetilde{\mathscr{U}}_\alpha$ в $E$ такое, что $\widetilde{\mathscr{U}_\alpha} = \mathscr{U}_\alpha \cap K$. Тогда $K \subseteq \cup_{\alpha \in A} \widetilde{\mathscr{U}}_\alpha$. Так как $K$ — компакт, то можно найти конечное число множеств, скажем, $\mathscr{U}_1, \ldots, \mathscr{U}_n$, таких, что $K = \cup_{i=1}^n\mathscr{U}_i$, но тогда $K \subseteq \cup_{i=1}^n \widetilde{\mathscr{U}}_i$.

(2) Пусть для любого покрытия $\{\widetilde{\mathscr{U}}_\alpha\}_{\alpha \in A}$ множества $K$ открытыми множествами из $E$ можно всегда найти конечное подпокрытие, скажем, $K \subseteq \cup_{i=1}^n \widetilde{\mathscr{U}}_i$, но тогда 
$$
K = K \cap \bigcup_{i=1}^n \widetilde{\mathscr{U}}_i= \bigcup_{i=1}^n \mathscr{U}_i
$$
при этом (см. Предложение [](#open_in_subset)) каждое $\mathscr{U}_\alpha : = \widetilde{\mathscr{U}}_\alpha \cap K$ — открыто в $K$.
:::




:::{prf:lemma}
:name: metric=hausdorff
Любое метрическое пространство удовлетворяет $\boxed{\textbf{аксиоме отделимости Хаусдорфа}}$; для любых двух различных точек найдутся их непересекающиеся окрестности.
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $(E,d)$ — метрическое пространство, и пусть $x_1,x_2 \in E$ — две его различные точки. Нужно показать, что найдутся два открытых множества $\mathscr{U}_1, \mathscr{U}_2 \subset E$ такие, что $x_1\in \mathscr{U}_1$, $x_2\in \mathscr{U}_2$ и $\mathscr{U}_1\cap \mathscr{U}_2 = \varnothing.$

Пусть $y \in B(x_1,r_1) \cap B(x_2,r_2)$, тогда $d(x_1,y)<r_1$ и $d(x_2,y)<r_2$. По неравенству треугольника, получаем
$$
d(x_1,x_2) \le d(x_1,y) + d(x_2,y)< r_1 +r_2.
$$

Это означает, что $B(x_1,r_1) \cap B(x_2,r_2) \ne \varnothing$, если и только если $r_1+r_2 > d(x_1,x_2)$, а если $r_1+r_2 \le d(x_1,x_2)$, то $B(x_1,r_1) \cap B(x_2,r_2) = \varnothing$. Таким образом, для данных двух различных точек $x_1,x_2$ полагаем $\mathscr{U}_1: = B(x_1,r_1)$, $\mathscr{U}_2:=B(x_2,r_2)$ и требуем, чтобы $r_1+r_2 \le d(x_1,x_2)$. Это доказывает хаусдорфовость метрических пространств. 
:::

:::{prf:corollary}
:name: point_is_closed
В любом метрическом пространстве $(E,d)$ точка — замкнутое множество.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $y \in \overline{\{x\}}$ тогда для любого $r>0$, $B(y,r) \cap \{x\} \ne \varnothing$, т. е. для любого $r >0$ $x \in B(y,r)$, учитывая выполнения аксиомы отделимости в метрических пространствах получаем, что такое возможно, только если $x =y$, что и доказывает требуемое.
:::


:::{prf:theorem} Свойства компакта
:name: properties_of_compact
В метрическом пространстве $(E,d)$ любой компакт обладает следующими свойствами:

1. Компакт — ограниченное множество, т. е. найдётся такой шар $B(a,r) \subseteq E$, что $K \subseteq B(a,r)$.
2. Компакт — замкнутое множество, т. е. он содержит все свои точки прикосновения ($\overline{K} = K$).
3. Замкнутое подмножество компакта самое является компактом.
 
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $(E,d)$ — метрическое пространство, $K$ — компакт в $E$.

(1)  Согласно Аксиоме Выбора, мы можем взять точку $x\in K$. Рассмотрим бесконечную последовательность шаров $(B(x,n))_{n=1}^\infty$ в $K$, очевидно, что это — покрытие для $K$, и более того $E = \cup_{n \ge 1} B(x,n)$. Так как $K$ — компакт, то из этого покрытия можно выбрать конечное подпокрытие, скажем, $\{B(x,r)\}_{r=t}^N$, такое, что $K \subseteq \cup_{t=1}^N B(x,r)$. Так как $B(x,p) \subseteq B(x,q)$ при $p<q$, то $\cup_{t=1}^N B(x,r) = B(x,N)$, что и показывает ограниченность $K.$

(2) Пусть $y \in \overline{K}$, но $y \notin K$. Тогда по Лемме \ref{metric=hausdorff}, для каждого $x\in K$ можно найти два таких шара $B(x, r_x)$, $B(y, \varepsilon_x)$, что $B(x, r_x) \cap B(y, \varepsilon_x) = \varnothing.$ Ясно, что $K \subseteq \cup_{x \in K} B(x,r_x)$. Так как $K$ -- компакт, то можно найти конечное множество точек $\{x_1,\ldots, x_n\}$ такое, что $K \subseteq \cup_{i=1}^n B(x_i, r_i)$, где $r_i = r_{x_i}$, $1\le i \le n.$ Для всех таких $x_i$, мы уже имеем шары $B(y, \varepsilon_i)$, $B(y,\varepsilon_i) \cap B(x_i, r_i) = \varnothing$, где $\varepsilon_i := \varepsilon_{x_i}$. Но, тогда полагая $\varepsilon: = \min \{\varepsilon_1, \ldots, \varepsilon_n\}$, получаем, что
\[
  B(y, \varepsilon) \cap K \subseteq B(y, \varepsilon) \cap \bigcup_{i=1}^n B(x_i,r_i) = \varnothing,
\]
\textit{т.е.,} мы нашли окрестность $B(y, \varepsilon)$ точки $y$, которая не пересекается с $K$. Но это означает см. Определение \ref{limit_point}, Лемма \ref{closure}), что $y \notin \overline{K}$.  Поэтому если $y\in \overline{K}$, то $y \in K$, \ie $\overline{K} = K.$

(3) Пусть $F \subseteq K$ — замкнутое подмножество в $K$, и пусть $\{\mathscr{U}_\alpha\}_{\alpha \in A}$ — покрытие $F$ открытыми множествами из $E$, т. е. $F \subseteq \cup_{\alpha \in A} \mathscr{U}_\alpha$.

Тогда имеем
$$
K \subseteq F \cup (E \setminus F) \subseteq \bigcup_{\alpha \in A} \mathscr{U}_\alpha \cup (E \setminus F),
$$
т. е. мы получили покрытие для $K$, но так как $K$ — компакт, то можно найти такие, скажем, $\mathscr{U}_1, \ldots, \mathscr{U}_n$, что 
$$
K \subseteq \mathscr{U}_1 \cup \cdots \cup \mathscr{U}_n \cup (E \setminus F),
$$
но тогда 
$$
F \subseteq \mathscr{U}_1 \cup \cdots \cup \mathscr{U}_n,
$$
что означает компактность $F.$
:::


:::{prf:theorem}
:name: image_of_compact
Пусть $f:E\to E'$ — непрерывное отображение между метрическими пространствами, тогда если $X$ — компактно, то $f(X)$ — компактно.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $\{\mathscr{U}'_\alpha\}_{\alpha \in A}$ — покрытие $f(E)$ открытыми в $E'$ множествами, тогда $\{f^{-1}(\mathscr{U}'_\alpha)\}_{\alpha \in A}$ — покрытие $E$, и так как $f$ — непрерывно, то по Теореме [](#preimage_of_open), это покрытие открытыми множествами в $E.$ Так как $X$ — компактно, то можно найти конечное подпокрытие, скажем, $\{f^{-1}(\mathscr{U}'_i)\}_{i=1}^n$, но тогда $\{\mathscr{U}_i\}_{i=1}^n$ — покрытие для $f(X)$, что и показывает компактность $f(X).$
:::


## Компактность в $\mathbb{R^n}$

**(Прямоугольным) параллелепипедом в $\mathbb{R^n}$** будем называть множество 
$$
\mathcal{P}: = [a_1, b_1] \times \cdots \times [a_n, b_n].
$$


:::{prf:proposition}
:name: cub_is_compact
Параллелепипед $\mathcal{P}$ — компакт в $\mathbb{R}^n$, где рассматривается евклидова метрика.
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Доказывать будем от противного. Допустим, что существует такое покрытие $\{\mathscr{U}_\alpha\}_{\alpha \in A}$ открытыми множествами из $\mathbb{R}^n$ для параллелепипеда $\mathcal{P}$, что из него нельзя выбрать конечное подпокрытие. 

Итак, пусть $\mathcal{P} \subseteq \bigcup_{\alpha \in A} \mathscr{U}_\alpha$ и из этого покрытия нельзя выбрать конечное подпокрытие которое бы покрыло $\mathcal{P}$. Разобьём каждый отрезок $[a_k, b_k]$ пополам **т.е.,** представим его так
$$
[a_k, b_k] = \left[ a_k, \frac{a_k+b_k}{2} \right] \cup \left[\frac{a_k +b_k}{2}, b_k \right] \qquad 1 \le k \le n,
$$
тогда $\mathcal{P}$ разобьётся на $2^n$ параллелепипедов. По условию, $\mathcal{P}$ нельзя покрыть конечным числом множеств из $\{ \mathscr{U}_\alpha\}_{\alpha \in A}$, тогда найдётся хотя бы один из полученных параллелепипедов, обозначим его через $\mathcal{P}_1$, который тоже нельзя покрыть конечным числом множеств из покрытия $\{ \mathscr{U}_\alpha\}_{\alpha \in A}$.

Разобьём теперь параллелепипед $\mathcal{P}_1$ аналогичным образом на $2^n$ параллелепипедов. Так как $\mathcal{P}_1$ нельзя покрыть конечным числом множеств из покрытия $\{ \mathscr{U}_\alpha\}_{\alpha \in A}$, то найдётся хотя бы один, скажем $\mathcal{P}_2$, из только что полученных, который тоже нельзя покрыть конечным числом множеств. Будем повторять эту процедуру каждый раз. В результате мы получаем бесконечную цепь вложенных друг в друга параллелепипедов 
$$
\mathcal{P} \supsetneq \mathcal{P}_1 \supsetneq \mathcal{P}_2 \supsetneq \ldots
$$
каждый из которых нельзя покрыть конечным числом элементов множества $\{\mathscr{U}_\alpha\}_{\alpha \in A}$, и где каждый из них описывается следующим образом
$$
\mathcal{P}_i = \left[a_i^{(1)}, b_i^{(1)} \right] \times \cdots \times \left[a_i^{(n)}, b_i^{(n)} \right], \qquad i \ge 1,
$$
при этом, по построению, получаем $n$ систем вложенных друг в друга отрезков
\begin{align*}
& \left[ a_1^{(1)}, b_1^{(1)} \right] \supseteq \left[ a_2^{(1)}, b_2^{(1)} \right] \supseteq \left[ a_3^{(1)}, b_3^{(1)} \right] \supseteq \ldots \\
& \left[ a_1^{(2)}, b_1^{(2)} \right] \supseteq \left[ a_2^{(2)}, b_2^{(2)} \right] \supseteq \left[ a_3^{(2)}, b_3^{(2)} \right] \supseteq \ldots 
\end{align*}
у которых длины строго уменьшаются (каждый из отрезков по длине в два раза меньше чем его соседний слева отрезок). Тогда по Лемме о вложенных отрезках (Лемма [](#cap_of_intervals)), для каждой из этих $n$ систем есть своя общая точка, $c_i \in \bigcap_{k \ge 1} [ a_k^{(i)}, b_k^{(i)} ] $, которая есть предельная для последовательности их концов; 

$$
\begin{matrix}
a_1^{(1)} & a_2^{(1)} & a_3^{(1)}& \ldots  & \to & c_1 & \leftarrow & \ldots & b_3^{(1)} & b_2^{(1)}  \\
a_1^{(2)} & a_2^{(2)} & a_3^{(2)}& \ldots  & \to & c_2 & \leftarrow & \ldots & b_3^{(1)} & b_2^{(1)}  \\
\vdots & \vdots &\vdots & \ddots && \vdots && && \\
a_1^{(n)} & a_2^{(n)} & a_3^{(n)}& \ldots  & \to & c_n & \leftarrow & \ldots & b_3^{(1)} & b_2^{(1)}  
\end{matrix}
$$

тогда для любого $\varepsilon >0$ и для каждого $1\le p \le n$, найдётся такой номер $M_p$, что при $m \ge M_p$ все $a_m^{(p)}, b_m^{(p)} \in (c_p - \varepsilon, c_p + \varepsilon)$. Пусть $M: = \max_{1 \le p \le n}\{M_p\}$, тогда при $m > M$ все $a_m^{(p)}, b_m^{(p)} \in (c_p - \varepsilon, c_p + \varepsilon)$ при любом $1\le p \le n.$

Рассмотрим теперь параллелепипед

$$
\mathcal{P}_\varepsilon(\m{c}):= [c_1 - \varepsilon, c_1 + \varepsilon] \times \cdots \times [c_n - \varepsilon, c_n + \varepsilon]
$$
где $\m{c}: = (c_1,\ldots, c_n)$. Тогда, для всех $m>M$, получаем что все параллелепипеды $\mathcal{P}_m \subset \mathcal{P}_\varepsilon(\m{c})$.

С другой стороны, 

$$
\m{c} = (c_1,\ldots, c_n) \in \bigcap_{i \ge 1} \mathcal{P}_i \subset \mathcal{P} \subseteq \bigcup_{\alpha \in A} \mathscr{U}_\alpha
$$
тогда найдётся хотя бы одно $\mathscr{U}_\alpha$ содержащее это точку $\m{c}$, так как $\mathscr{U}_\alpha$ открыто, то найдётся шар $B(c, r)$ такой, что $B(\m{c}, r) \subseteq \mathscr{U}_\alpha$.

Пусть теперь $0 < \varepsilon < \dfrac{r}{\sqrt{n}}$, тогда получаем, что для каждого $m>M$

$$
\mathcal{P}_m \subseteq \mathcal{P}_\varepsilon(\m{c}) \subseteq B(\m{c}, r) \subseteq \mathscr{U}_\alpha.
$$

Но это означает что, каждый из $\mathcal{P}_m$ при $m >M$ можно покрыть всего одним элементом $\mathscr{U}_\alpha$, что противоречит выбору таких параллелепипедов, **т.е.,** первоначальный параллелепипед можно тогда покрыть конечным числом элементов множества $\{\mathscr{U}_\alpha\}$, что означает его компактность.    
:::


:::{prf:theorem} Критерий компактности в $\mathbb{R}^n$
:name: criterai_of_compacness
Множество $K \subseteq \mathbb{R}^n$ компактно тогда и только тогда когда оно замкнуто и ограничено.    
:::
:::{prf:proof}
:class: dropdown
:nonumber:

(1) Согласно Теореме [](#properties_of_compact) (1) мы получаем необходимость.

(2) Если $K \subseteq \mathbb{R}^n$ ограниченно и замкнуто, то это значит, что оно содержится в некотором шаре, скажем, $B(\m{x}, r)$ который содержится целиком внутри параллелепипеда
$$
\mathcal{P} = [x_1- r,x_1+r] \times \cdots \times [x_n-r, x_n+r]
$$
где $\m{x} = (x_1, \ldots, x_n)$. Так как $K$ — замкнуто, то из предложения [](#cub_is_compact) и Теоремы [](#properties_of_compact) (3) вытекает утверждение. 
:::

:::{prf:corollary}
:name: sphere_is_compact
В пространстве $\mathbb{R}^n$ сфера $S^n: =\{(x_1,\ldots, x_n): x_1^2 + \cdots +x_n^2 =r^2\}$ — компакт.
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Очевидно, что сфера $S^n$ ограничена, так как $S^n \subseteq B(\m{0}_n, r')$, где $r'>r$. Покажем замкнутость. Отображение
$$
f: \mathbb{R}^n \to \mathbb{R}, \qquad (x_1,\ldots, x_n) \mapsto x_1^2 + \cdots + x_n^2 - r^2
$$
для фиксированного $r>0$ очевидно непрерывно, тогда $S^n= f^{-1}(\{0\})$, но точка, согласно Следствию [](#point_is_closed), $0$ — замкнутое множество в $\mathbb{R}$ в евклидовой метрики. Таким образом $S^n$ — органично и замкнуто, а значит — компакт.
:::



:::{prf:theorem}
:name: general_Weistrass
На компактном множестве всякая непрерывная функция ограничена и достигает наибольшего и наименьшего значений.
:::
Другими словами, если $f:K \to \mathbb{R}$ — непрерывная функция, $K$ — компактно, то найдутся такие $a,b \in X$, что $f(a) \le f(x) \le f(b)$ для любого $x \in X$.

:::{prf:proof}
:class: dropdown
:nonumber:
Согласно Теореме [](#image_of_compact) $f(K)$ — компактно в $\mathbb{R}$, тогда согласно Теореме [](#criterai_of_compacness) оно ограничено. Тогда согласно принципу полноты Вейерштрасса (Теорема [](#W=complete)) существуют $m:=\inf f(X)$, $M:= \sup f(X).$ Но, по теореме [](#criterai_of_compacness) $f(X)$ также и замкнуто, тогда по Лемме [](#closure), $m,M \in f(X)$, откуда и следует существование таких точек $a,b\in X$, что $f(a) \le f(x) \le f(b)$ при всех $x\in X.$
:::