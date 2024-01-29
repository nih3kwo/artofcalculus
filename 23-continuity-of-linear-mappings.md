# Непрерывность линейных отображений

Напомним, что линейное отображение $L: \mathbb{R}^n \to \mathbb{R}^m$ — это такое отображение, что
$$
L(\alpha \m{v} + \beta \m{u}) = \alpha L(\m{v}) + \beta L(\m{u}),
$$
для любых $\m{v}, \m{u} \in \mathbb{R}^n$, $\alpha,\beta \in \mathbb{R}$.

Заметим, что 
$$
L(\m{0}_n) = \m{0}_m,
$$
где $\m{0}_k$ — нулевой вектор векторного пространства $\mathbb{R}^k$.


:::{prf:definition}
Говорят, что линейное отображение $L: \mathbb{R}^n \to \mathbb{R}^m$ ограничено, если существует такое $K \ge 0$, что для любого $\m{v} \in \mathbb{R}^n$, $|| L(\m{v}) || \le K ||\m{v}||.$
:::

:::{prf:proposition}
:name: contous_of_linear
Пусть $L: \mathbb{R}^n \to \mathbb{R}^m$ — линейное отображение. Тогда следующие утверждения равносильны:

1. $L$ — непрерывно.
2. $L$ — непрерывно в нуле.
3. Существует такое $C > 0$, что $|| L(\m{v})| \le C ||\m{v}||$ для любого $\m{v} \in \mathbb{R}^n$

:::
:::{prf:proof}
:class: dropdown
:nonumber:
(1) $\Longrightarrow$ (2). Это просто следует из того, что если $L$ непрерывно, то оно непрерывно во всех точках $\mathbb{R}$, в частности и в нуле тоже.

(2) $\Longrightarrow$ (3). Если $L$ непрерывно в нуле, то это значит, что для любого $\varepsilon >0$ можно всегда найти такое $\delta>0$, что из $||\m{h}|| <\delta$ будет следовать $||L(\m{h})|| <\varepsilon$. Пусть $\varepsilon = 1$, тогда мы всегда найдём такой $\delta>0$, что если $|| \m{h} || < \delta$, то $|| L(\m{h})|| < 1$. Зафиксируем такое $\delta.$

Возьмём теперь произвольный ненулевой вектор[^ref231] $\m{v}$, тогда имеем
$$\begin{align*}
|| L(\m{v}) || &=& \left\| \frac{2}{\delta} || \m{v} || L\left(  \frac{\delta \m{v}}{2 || \m{v} ||}\right) \right\| \\
&=&  \frac{2}{\delta} || \m{v}|| \cdot \left\| L\left(  \frac{\delta \m{v}}{2 || \m{v} ||}\right) \right\| < \frac{2}{\delta} || \m{v}||
\end{align*}$$
потому что 
$$
\left\|\frac{\delta \m{v}}{2 || \m{v} ||} \right\| = \frac{\delta}{2} < \delta,
$$
и так как $\delta$ фиксировано, мы получаем требуемое.

(3) $\Longrightarrow$ (1). Имеем
$$
|| L(\m{v}) - L(\m{u}) || = || L(\m{v} - \m{u}) || \le K || \m{u} - \m{v} ||,
$$
тогда если $||\m{u} - \m{v}|| < \delta$, то $|| L(\m{v}) - L(\m{u}) ||< K \delta$,
поэтому для любого $\varepsilon >0$, если мы положим, что $0<\delta < \frac{\varepsilon}{K}$, то мы и получаем непрерывность $L$.
:::




:::{prf:lemma}
:name: linear_is_contious
Любое линейное отображение $L: \mathbb{R}^n \to \mathbb{R}^m$ непрерывно. 
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $L$ задаётся матрицей $(a_{i,j})_{1\le i \le n, 1 \le j \le m}$, тогда

$$
L(\m{v}) = \begin{pmatrix}
a_{11} & \ldots & a_{1n} \\
\vdots & \ddots & \vdots \\
a_{m1} & \ldots & a_{mn}
\end{pmatrix}   \begin{pmatrix}
v_1 \\ \vdots \\ v_n
\end{pmatrix} = \begin{pmatrix}
a_{11}v_1 + \cdots + a_{1n}v_n \\
\vdots \\
a_{m1}v_1 + \cdots + a_{mn}v_n 
\end{pmatrix} = (u_1, \ldots, u_m)^\top =:\m{u} \in \mathbb{R}^m,
$$ 
тогда
$$\begin{align*}
||L(\m{v})|| &=& ||\m{u}|| \\
&=& \sqrt{(a_{11}v_1 + \cdots + a_{1n}v_n)^2 + \cdots + (a_{m1}v_1 + \cdots + a_{mn}v_n)^2} \\
&\le & \sqrt{ m } \max_{1 \le k \le m} \left| a_{k1}v_1 + \cdots + a_{kn}v_n  \right| \\
&\le & \sqrt{ m } \max_{1 \le k \le m} \left( |a_{k1}| \cdot |v_1| + \cdots + |a_{kn}| \cdot |v_n| \right) \\
&\le & \sqrt{ m } \max_{1 \le k \le m} \left(|a_{k1}| \cdot || \m{v}|| + \cdots + |a_{kn}| \cdot || \m{v}||  \right) \\
&=& \sqrt{ m } \max_{1 \le k \le m}\left(|a_{k1}|  + \cdots + |a_{kn}|   \right) \cdot || \m{v}|| \\
&=& K || \m{v}||,
\end{align*}$$
где $K: = \sqrt{ m } \max_{1 \le k \le m}\left(|a_{k1}|  + \cdots + |a_{kn}|   \right)$, тогда по Предложению [](#contous_of_linear) оно непрерывно. 
:::

[^ref221]: [Аксиома Выбора](#axiom-of-choice) позволяет.