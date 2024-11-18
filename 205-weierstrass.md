---
authors:
  - name: Alyona Zarodnyuk
    affiliations:
      - Higher School of Economics
numbering:
  enumerator: 5.%s
---

# Теорема Вейерштрасса о непрерывности на компакте. Колебания функции

> Лекция 5, 15.10.2024

## Теорема Вейерштрасса о непрерывной функции на компакте

```{prf:theorem} Теорема Вейерштрасса о непрерывности на компакте функции
:name: weierstrass-continuous-function-on-compact
$K\subset \RR^n$ — компакт, $f\colon K\mapsto\RR$

$f\in C(K)\implies$ $f$ ограничена на $K$ и достигает своего наибольшего и наименьшего значения на $K$.
```

```{prf:proof}
$f$ — ограничена? Докажем от противного, т. е. предположим, что $f$ неограничена.

$K$ — компакт, $\exists\{x_m\}_{m=1}^\infty\subset K$, что $|f(x_m)|>m$. $\implies K$ ограничена $\implies\exists c,||x||\leq c,\implies\{x_m\}^\infty_{m=1}$ — ограничена $\implies\{x^i_m\}^\infty_{m=1}$ ограничена $\forall i=\overline{1,\ldots n}$.

$$|x^i|\leq||x||=\sqrt{(x')^1+\ldots+(x^n)^2}\leq c$$

Получаем, что по теореме Больцано-Вейерштрасса (из $\forall$ ограниченной последовательности можно выделить сходящуюся подпоследовательность)

$\{x_m\}=\{(x_m^1,x_m^2,\ldots,x_m^n)\}\implies y\{x'_m\}_{m=1}^\infty\exists$ сходящаяся последовательность $\{x_{m_{j_1}}^1\}, x'_{m_{j_1}}\to a_1$, $j_1\to\infty$, $\{x_{m_{j_1}}\}=\{(\underset{\to a_1}{x^1_{m_{j_1}}},x^2_{m_{j_1}},...,x^n_{m_{j_1}})\}$. 

Выберем в ограниченной $\{x^1_{m_{j_1}}\}$ сходящуюся подпоследовательность $\{x_{m_{j_2}}^2\}$. $x^2_{m_{j_2}}\to a_2$. $\{x_{m_{j_2}}\}=\{(x_{m_{j_2}}^1,x_{m_{j_2}}^2,\ldots,x_{m_{j_2}}^n)\}$

$\{x_{m_{j_n}}\}^\infty_{j_n=1},x_{m_{j_n}}\to(a_1,\ldots, a_n)=a\implies x_{m_{j_n}}\to a$, т. е. $a$ предел $K$, но $K$ — компакт $\implies a\in K$

$\exists\lim_{j_n\to\infty}f(x_{m_{j_n}})=f(a)$, по условию непрерывности функции $f$ на $K$. С другой стороны, $f(x_{m_{j_n}})\to\infty$ при $j_n\to\infty$.

$|f(x_{m_{j_n}})|>m_{j_n}\implies$ противоречие.

Теперь докажем достижимость $\sup$.

Есть последовательность $\{y_m\}^\infty_{m=1}$. $\sup_K f-\frac{1}{m}\leq f(y_m)\leq\sup_K f$. По первому пункту можно выделить $y_{m_{j_n}}\to a$.

$$\underset{j_n\to\infty}{\sup_K f-\frac{1}{m_{j_n}}}\leq f(y_{m_{j_n}})\leq\sup_K f$$

по непрерывности получаем

$$\sup_K f\leq f(a)\leq\sup_K f\implies f(a)=\sup_K f$$

Для $\inf$ доказывается аналогично.
```

## Расстояние 

```{prf:definition}
Расстояние между двумя множествами $X$ и $Y$ будем называть число $\rho(X, Y)$:

$$\rho(X, Y)=\inf_{\overset{x\in X}{y\in Y}}||x-y||$$
```

```{prf:example}
1. $X\cap \underbrace{Y}_{\neq\varnothing} Y\implies\rho(X, Y)=0$.
2. $\rho(X, Y)=0\overset{?}\implies X\cap Y\neq\varnothing$ — нет.
    Контрпример: $X=(0, 1), Y=(1, 2)$ — не компакты.
```

```{prf:theorem}
$$\left.\begin{align*}
  K_1,K_2\subset\RR^n \text{— компакты}\\
  K_1\cap K_2=\varnothing
\end{align*}\right\}\implies\rho(K_1,K_2)>0$$
```

```{prf:proof}
:nonumber:
Функция $f(x,y)-||x-y||$ определена на $K_1\times K_2\subset\RR^n\times\RR^n=\RR^{2n}$, причём $f$ — непрерывная функция.

По теореме Вейерштрасса эта функция достигает своего максимального и минимального значений, т. е. существуют $x_0\in K_1,y_0\in K_1\colon f(x_0,y_0)=\rho(K_1,K_2)$, а $f(x_0, y_0)=0$ тогда и только тогда, когда $x_0=y_0$.
```

## Колебания функции

$M\subset\RR^n$ — множество.

```{prf:definition}
:name: function_fluctuations_on_set
**Колебанием** $f$ на множестве $M$ будем называть число $\omega(f, M)$:

$$\omega(f, M):=\sup_{x,y\in M}|f(x)-f(y)|=\sup_{x\in M} f(x)-\inf_{y\in M} f(y)$$
```

```{prf:definition}
:name: function_fluctuations_at_point
**Колебанием** $f$ в точке $x_0\in M$ будем называть число $\omega(f, x_0)$:

$$\omega(f, x_0):=\lim_{r\to 0^+}\omega(f,B^M_r(x_0)),$$

где

$$B^M_r(x_0)=B_r(x_0)\cap M$$
```

```{prf:definition} 
:name: continuity_at_point
$f\colon M\mapsto\RR$ **непрерывна** в $x_0\in M$, если $\forall\ve>0,\exists\delta>0,\forall x\in B^M_\delta(x_0)\cap M\hookrightarrow|f(x)-f(x_0)|<\ve$.
```

```{prf:theorem} О непрерывности колебаний в точке функции
:name: fluctuation-continuity-at-point
$x_0\in M\subset\RR^n$, $f\colon M\mapsto\RR$.

$f$ — непрерывна в точке $x_0\iff\omega(f, x_0)=0$.
```

```{prf:proof}
$(\Rightarrow)$ **Необходимость.**

$f$ непрерывна в $x_0\in M\implies\forall\ve>0,\exists\delta>0,\forall x\in B^M_\delta(x_0)\cap M\implies|f(x)-f(x_0)|<\frac{\ve}{3}$

Рассмотрим

$$\omega(f,x_0)=\lim_{\delta\to0^+}\omega(f, B_\delta^M(x_0))$$

$$\begin{align*}
\omega(f,B^M_\delta(x_0))&=\sup_{x,y\in B^M_\delta(x_0)}|f(x)-f(y)|
\\&=\sup_{x,y\in B^M_\delta(x_0)}|f(x)-f(x_0)+f(x_0)-f(y)|
\\&\leq 2\sup_{x\in B^M_\delta(x_0)}|f(x)-f(x_0)|\leq 2\ve<\ve
\end{align*}$$

т. е. при $\ve\to0\implies\delta\to 0$

$$\omega(f, B^M_\delta(x_0))\to0\implies\omega(f, x_0)=0$$

$(\Leftarrow)$ **Достаточность.**

$$0=\omega(f,x_0):=\lim_{\delta\to0^+}\omega(f,B^M_\delta(x_0))$$

$\forall\ve>0,\exists\delta>0,\forall x,y\in B^M_\delta(x_0),$

$$\omega(f,B_\delta^M(x_0))=\sup_{x,y\in B^M_\delta(x_0)}|f(x)-f(y)|<\ve$$

тогда возьмём $y=x_0$

$$\begin{align*}|f(x)-f(x_0)|&\leq\sup_{x\in B^M_\delta(x_0)}|f(x)-f(x_0)|\\&\leq\sup_{x,y\in B^M_\delta(x_0)}|f(x)-f(y)|<\ve\end{align*}$$

Получаем, что $\forall\ve>0\exists\delta>0\colon\forall x\in B_\delta^M(x_0)\implies |f(x)-f(x_0)|<\ve \implies f(x)$ непрерывна в точке $x_0$.
```

```{prf:definition}
:name: almost_everywhere
Если какое-то свойство не выполняется только на множестве меры нуль по Лебегу, то будем говорить, что оно выполняется **почти всюду**.
```

```{prf:example}
$f(x)=\begin{cases}
1, & x\in\RR\setminus\ZZ\\
0, & x\in\ZZ
\end{cases}$

$\ZZ$ — счётное $\implies f$ имеет разрывы в не более, чем счётном множестве точек $\implies f$ непрерывна почти всюду на $\RR$.
```

```{prf:theorem} Критерий Лебега
:name: Lebegue-criterion
$I\subset\RR^n$ — замкнутый невырожденный брус, $f\colon I\mapsto\RR$.

$f\in\mathcal{R}(I)\iff f$ — ограничена на $I$ и $f$ непрерывна почти всюду на $I$.
```

```{prf:proof}
:nonumber:


* **Необходимость**

Если $f$ интегрируема, то она ограничена по необходимому условию интегрируемости. Осталось показать, что множества разрыва меры нуль. От противного: пусть это не так.

Обозначим множество всех точек разрыва ф-ии $f$ на $I$ за $T$ и заметим, что $T = \displaystyle\bigcup_{k\in\mathbb{N}}T_k$, где\\
$T_k = \{x\in I | \omega(f, x) \ge \frac{1}{k}\}$. Если $T$ не меры нуль, то существует $T_{k_0}$ не меры нуль (если они все меры нуль, то по свойству множеств меры нуль счетное объединение таких множеств тоже было бы меры нуль).

Для произвольного разбиения $\T = \{I_i\}_{i=1}^m$ бруска $I$ разобъем эти бруски на две кучи: первая $A = \{I_i | I_i\cap T_{k_0} \ne \varnothing, \omega(f, I_i) \ge \frac{1}{2k_0}\}$ и вторая $B = \T\backslash A$. Покажем что $A$ является покрытием множества $T_{k_0}$, т.е. $T_{k_0} \subset \displaystyle\bigcup_{i: I_i\in A} I_i$ любая точка $x\in T_{k_0}$ является либо

*[a)] внутренней для некоторого бруска $I_i$. В этом случае $\omega(f, I_i) \ge \omega(f, x) \ge \frac{1}{k_0} > \frac{1}{2k_0}$, т.е. $I_i \in A$, либо
*[b)] точка $x$ лежит на границе некоторого количества брусков (не более чем $2^n$ штук). Тогда хотя бы на одном из них колебание $\omega(f, I_i) \ge \frac{1}{2k_0}$ (т.е. $I_i \in A$): если бы такого не нашлось, то в любой малой окрестности $B_{\ve}(x)$ выполняется следующее:
\begin{equation*}
\omega(f, x) \le \sup_{x', x''\in B_{\ve}(x)} |f(x')-f(x'')| \le \sup_{x'\in B_{\ve}(x)}|f(x')-f(x)| + \sup_{x''\in B_{\ve}(x)}|f(x)-f(x'')| < \frac{1}{2k_0} + \frac{1}{2k_0} = \frac{1}{k_0}
\end{equation*}
т.е. $x\not\in T_{k_0}$ —- **противоречие**.


Таким образом, каждая точка $x\in T_{k_0}$ покрывается некоторым бруском $I_i \in A$, т.е. $A$ - покрытие $T_{k_0}$. Тогда существует $c: \displaystyle\sum_{i:I_i\in A}|I_i| \ge c > 0$ для всех разбиений $\T$ (если бы меняя разбиения мы могли получить сумму объемов этих брусков сколь угодно маленькую, то получилось бы, что $T_{k_0}$ меры нуль)

Возьмем два набора отмеченных точек $\xi^1$ и $\xi^2$. На брусках из кучки $B$ будем их брать одинаковыми, т.е. для $I_i\in B \,\, \xi_i^1 = \xi_i^2$. А на брусках из кучки $A$ будем брать такие, чтобы 
\begin{equation*}
f(\xi_i^1) - f(\xi_i)^2 \ge \frac{1}{3k_0} \text{ (у нас там колебания} \ge 1/2k_0, \text{ так что такие найдутся)}
\end{equation*}

Получаем:
\begin{equation*}
\begin{aligned}
|\sigma(f, \T, \xi^1) - \sigma(f, \T, \xi^2) 
= \left|\sum_i(f(\xi_i^1) - f(\xi_i^2))|I_i|\right|\\
= \left|\sum_{i: I_i\in A}(f(\xi_i^1) - f(\xi_i^2))|I_i| + \sum_{i:I_i\in B}(f(\xi_i^1) - f(\xi_i^2))|I_i|\right|\\
= \left|\sum_{i: I_i\in A} (f(\xi_i^1) - f(\xi_i^2))|I_i|\right| \ge \frac{1}{3k_0} \sum_{i:I_i\in A}|I_i| \ge \frac{c}{3k_0} > 0
\end{aligned}
\end{equation*}
т.е. интегральные суммы не могут стремиться к одному и тому же числу, значит $f$ не интегрируема —- **противоречие**.

* **Достаточность**

Для любого $\ve > 0$ рассмотрим $T_{\ve} = \{x\in I| \omega(f, x) \ge \ve\}$. Покажем, что это множество - компакт. Ограниченность очевидна (подмножества бруска), а замкнутость проверим от противного. Пусть $a$ - предельная точка $T_{\ve}: \,\, a\not\in T_{\ve}$. Т.к. она предельная, то существует $\{x^k\}: x^k \in B_{\frac{1}{k}}(a)$. Т.к. $B_{\frac{1}{k}}$ - открытые шары, то наши точки лежат в них с окрестностями, т.е. сущесвтуют $\delta_k : B_{\delta_k}(x_K) \subset B_{\frac{1}{k}}(a)$. Тогда
\begin{equation*}
\omega(f, B_{\frac{1}{k}}(a)) \ge \omega(f, B_{\delta_k}(x_K)) \ge \omega(f, x_k) \ge \ve
\end{equation*}
Переходя к пределу $k\to\infty : \omega(f, a) \ge \ve$, т.е. $a\in T_{\ve}$ - противоречие. Значит $T_{\ve}$ - замкнуто, и, следовательно, компактно.

Множество $T_{\ve}$ - множество меры нуль (как подмножество множества меры нуль). Значит, его можно покрыть не более чем счетным объединением открытых брусков $I_i: \displaystyle\sum_i|I_i| < \ve$. Т.к. это открытое покрытие, а $T_{\ve}$ - компакт, то существует конечное подпокрытие: $T_{\ve} \subset \displaystyle\bigcup_{i=1}^m I_i$, при этом $\displaystyle\sum_{i=1}^m |I_i| < \ve$.

Обозначим три множества: $C_1 = \displaystyle\bigcup_{i=1}^mI_i, \quad C_2 = \displaystyle\bigcup_{i=1}^mI_i', C_3 = \displaystyle\bigcup_{i=1}^mI_i''$, где $I_i', I_i''$ - бруски, полученные гомотетией с центром в центре $I_i$ с коэффициентом 2 и 3 соответственно.

Заметим, что

*[a)] $|C_3| \le \displaystyle\sum_{i=1}^m|I_i''|| = 3^n \displaystyle\sum_{i=1}^m|I_i| < 3^n \ve$
*[b)] расстояние $\rho(\partial C_2, \partial C_3) = \delta_1 > 0$ (теорема про расстояние между компактами)
*[c)] Множество $K = I\backslash(C_2\backslash \partial C_2)$ - компакт. Кстати, любое множество с диаметром меньше $\delta_1$ либо польностью лежит в $C_3$, либо полностью в $K$.
*[d)] $T_{\ve} \cap K = \varnothing$, т.к. $T_{\ve} \subset C_1 \subset C_2$. Следовательно, $\forall x\in K \,\, \omega(f, x) < \ve$. Тогда по теореме Кантора-Гейне $\exists \delta_2 > 0: \,\, \forall x\in K \,\, \omega(f, B_{\delta_2}(x)) < \ve + \ve = 2\ve$
\end{itemize}

Выберем $\delta = \min\{\delta_1, \delta_2\}$. Тогда для любых разбиений $\T_1 = \{I_k^1\}, \T_2 = \{I_i^2\}: \lambda{\T_1} < \delta, \lambda(\T_2) < \delta$

Рассмотрим пересечение этих разбиений $\T = \T_1 \cap \T_2$, т.е. такое разбиение $\T = \{I_{ik}\}$, что $I_k^1 = I_{i_1k} \bigsqcup\ldots\bigsqcup I_{i_mk}$ и $I_i^2 = I_{ik_1} \bigsqcup \ldots\bigsqcup I_{ik_l}$. Очевидно $\lambda(\T) < \delta$.

Для произвольных наборов отмеченных точек:
\begin{equation*}
|\sigma(f, \T_1, \xi^1) - \sigma(f, \T_2, \xi^2)| \le |\sigma(f, \T_1, \xi^1) - \sigma(f, \T, \xi)| + |\sigma(f, \T_2, \xi^2) - \sigma(f, \T, \xi)|
\end{equation*}

Рассмотрим отдельное слагаемое:
\begin{equation*}
\begin{aligned}
|\sigma(f, \T_1, \xi^1) - \sigma(f, \T, \xi)| = \left|\sum_{i, j}(f(\xi_i^1) - f(\xi_{ij}))|I_{ij}\right|\
\le \sum_{I_{ij}\in C_3}|f(\xi_i^1) - f(\xi_{ij})||I_{ij}| + \sum_{I_{ij\in K}}|f(\xi_i^1)-f(\xi_{ij})||I_{ij}|\le 2M\cdot e^n\ve + 2\ve |I| = \epsilon(2M\cdot 3^n + 2|I|)
\end{aligned}
\end{equation*}
т.к. $f$ ограничена некоторой константой $M$ и см пункты $a), d)$, то

Т.к. для $(\T_2, \xi^2)$ все выкладки аналогичные, то получаем:

\begin{equation*}
|\sigma(f, \T_1, \xi^1) - \sigma(f, \T, \xi)| \le \epsilon(2M\cdot 3^n + 2|I|)
\end{equation*}

Следовательно, существует предел $\displaystyle\lim_{\lambda(\T)\to0}\sigma(f, \T, \xi)$ (Критерий коши для функций)
\end{itemize} \qed

```

```{prf:definition}
:name: intersection_of_two_decompositions
$\TT_1=\{I^1_k\}$ — разбиение $I$, $\TT_2=\{I^2_m\}$ — разбиение $I\implies$ **пересечением** $\TT_1\cap\TT_2$ будем называть множество всех брусов $\{I_{ij}\}$ таких, что $\forall I_{ij}$

1. $\exists k\colon I_{ij}$ входит в разбиение $I^1_k$
2. $\exists m\colon I_{ij}$ входит в разбиение $I^2_k$
3. $\{I_{ij}\}$ — разбиение $I$.
```

```{prf:definition}
:name: decomposition_shredding
Разбиение $\TT_1=\{I^1_k\}$ будем называть **измельчением** разбиения $\TT_2=\{I^2_m\}$, если $\forall k,\exists m\colon I^1_k$ входит в разбиение $I^2_m\implies\TT_1\cap\TT_2$ является измельчением $\TT_1$ и $\TT_2$.
```