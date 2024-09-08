# Произведение метрических пространств и арифметика предела.

:::{prf:definition}
Пусть $(E_1,d_1)$, $(E_2,d_2)$ — два метрических пространства, где $d_1$, $d_2$ — расстояния в $E_1,$ $E_2$. Для любой пары точек $x = (x_1,x_2)$, $y = (y_1,y_2)$, где $x_1, x_2 \in E_1$, $y_1,y_2 \in E_2$ положим
$$
d(x,y):= \max \{ d_1(x_1,y_1), d_2(x_2,y_2)\}.
$$
:::

Непосредственно проверяется, что это метрика. Тем самым, мы получаем метрическое пространство $(E, d)$, где $E = E_1 \times E_2$

:::{warning}
Открытые шары для расстояний $d,d_1,d_2$ будут соответственно обозначаться символами $B,B_1,B_2.$
:::

:::{prf:lemma}
Для любой точки $a = (a_1,a_2) \in E$ и любого $r >0$ имеем $ B(a,r ) = B_1(a_1,r_1) \times B_2(a_2, r_2)$.
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Это сразу следует из определения метрики $d$, $d(x,y):= \max \{ d_1(x_1,y_1), d_2(x_2,y_2)\}.$
:::

:::{prf:proposition}
:name: continous_of_times
Пусть $F,E_1,E_2$ — метрические пространства, и пусть $f_1:F \to E_1$, $f_2:F \to E_2$ — отображения. Тогда отображение $f:F \to E_1 \times E_2$, $z \mapsto (f_1(z), f_2(z))$ будет непрерывным в точке $z_0 \in F$, если и только если оба отображения $f_1,f_2$ непрерывны в точке $z_0.$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $p_0 = (f_1(z_0), f_2(z_0))$, покажем, что 
$$
f^{-1} (B(p_0, r)) = f_1^{-1}(B(f(z_0) , r)) \cap f_2^{-1}( B(f_2(z_0)), r ).
$$
Действительно, имеем
$$\begin{align*}
z \in f^{-1} (B(p_0, r)) &\Longleftrightarrow& f(z) \in B(p_0,r) \\
&\Longleftrightarrow& (f_1(z), f_2(z)) \in B_1(f(z_0), r) \times B(f_2(z_0), r) \\
&\Longleftrightarrow& \bigl\{ z \in F\,:\, f_1(z) \in B_1(f_1(z_0), r) \bigr\} \& \bigl\{ z\in F, :\, f_2(z) \in B_2(f_2(z_0), r) \bigr\} \\
&\Longleftarrow& z \in f_1^{-1}(B_1(f_1(z_0), r)) \cap f_2^{-1}(B_2(f_2(z_0), r)).
\end{align*}$$

Тогда, используя лемму [](#union_and_cap_of_open), получаем, что прообраз любого открытого при $f$ открыт, что и доказывает предложение.
:::

:::{prf:theorem}
Пусть $\alpha: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ — любая бинарная непрерывная операция на $\mathbb{R}$ относительно метрики $d(x,y) = |x-y|$. Пусть $f,g:E \to \mathbb{R}$ — отображение из метрического пространства $E$, при этом, для какого-то $A \subseteq E$, $a\in \overline{A}$, $\lim_{x\to a, x \in A}f(x) = a'$, $\lim_{x\to a, x \in A}g(x) = a''$. Тогда $\lim_{x\to a, x \in A}\alpha(f,g) = \alpha(a',a'').$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Это сразу следует из определения предела, теоремы [](#comp_of_continous) и предложения [](#continous_of_times).
:::


:::{prf:corollary}
Арифметика предела для функций верна, если функции определены подходящим образом.
:::

Напомним, что функция $f:\mathbb{R}^2 \to \mathbb{R}$, где рассматривается обычная метрика на $\mathbb{R}^2$, $\mathbb{R}$, непрерывна в точке $(a,b)$, если для любого $\varepsilon >0$ можно найти такое $\delta >0$, что неравенство 
$$
\sqrt{(x-a)^2 + (y-b)^2} < \delta
$$
влечёт неравенство $|f(x,y) - f(a,b)|< \varepsilon$. 

(1) Покажем, что $\mathsf{S}:\mathbb{R} \times \mathbb{R} \to \mathbb{R}$, $(x,y) \mapsto x+y$ непрерывно. Если $|x-a|, |y-b| <\delta$, то $ \sqrt{(x-a)^2 + (y-b)^2} < \sqrt{2}\delta < 2 \delta$, и 
$$
|x+y - (a+b)| = |(x-a) + (y-b)| \le |x-a| + |y-b| < 2 \delta.
$$

Поэтому если $\sqrt{(x-a)^2 + (y-b)^2}<\varepsilon$, то и $|(x+y) - (a+b)|< \varepsilon$, что и означает непрерывность отображения $\mathsf{S}$ в любой точке $(a,b).$

(2) Покажем, что отображение $\mathsf{P}: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$, $(x,y) \mapsto xy$ непрерывно. 

Пусть $|x-a|, |y-b| < \delta$, тогда $\sqrt{(x-a)^2 + (y-b)^2} < \sqrt{2}\delta < 2 \delta$.

Далее, имеем
$$
xy -ab =a (y-b) + b(x-a) + (x-a)(y-b),
$$
тогда
$$\begin{align*}
|xy -ab| \le |a| |y-b| + |b||x-a| + |x-a||y-b| & \le & |a| \delta + |b| \delta + \delta^2\\
&=& \delta (|a| + |b| + \delta).
\end{align*}$$

Если потребовать, что $\delta <1$, то мы получаем $|xy-ab| < \delta (|a| + |b|+1).$ Таким образом, если задано произвольное $\varepsilon >0$ такое, что $|xy -ab| < \varepsilon$, то возьмём такое $\delta$, что $0 < \delta <1$ и $\delta(1 + |a| + |b|)<\varepsilon$, наконец, пусть $\delta' = 2{\delta}$. Тем самым, мы получаем, что из неравенства $\sqrt{(x-a)^2 + (y-b)^2} < \sqrt{2}\delta < 2 \delta = \delta'$ следует неравенство $|xy - ab| < \varepsilon$, что и показывает непрерывность отображения $\mathsf{P}.$

(3) Покажем, что отображение $h_\lambda: \mathbb{R} \to \mathbb{R}$, $x \mapsto \lambda x$, где $\lambda$ — фиксированное число, непрерывно. 

Действительно, во-первых, если $\lambda =0$, то получаем постоянное отображение которое, очевидно, непрерывно. Во-вторых, если $\lambda \ne 0$, то для $\varepsilon >0$ пусть $\delta = \frac{\varepsilon}{|\lambda|}$. Тогда если $|x-a|<\delta < \frac{\varepsilon}{\lambda}$, то $|\lambda||x-a| < \varepsilon$, т. е. $|\lambda x - \lambda a| < \varepsilon$, что и доказывает требуемое.

(4) Покажем, что отображение $f:\mathbb{R}/\{0\} \to \mathbb{R}$, $x \mapsto \frac{1}{x}$ непрерывно. То есть нужно показать, что если для заданного $\varepsilon>0$ всегда можно найти такое $\delta>0$, что $|x-a|<\delta$, то $|\frac{1}{x} = \frac{1}{a}|<\varepsilon.$

Пусть $|x-a|<\delta$, тогда, $|a| - |x| \le |a-x| = |x-a| < \delta$, значит $|x|>|a| -\delta$. Далее, для заданного $\varepsilon>0$ мы положим 
$$
0<\delta < \min \left( \frac{|a|}{2}, \varepsilon\frac{|a|^2}{2} \right),
$$
тогда если $|x-a|< \delta$, то $|x|>\frac{|a|}{2}$. Действительно, если $\frac{|a|}{2}< \varepsilon\frac{|a|^2}{2}$, то $|x| > |a| - \delta > \frac{|a|}{2}$. Если же $\frac{|a|}{2}> \varepsilon\frac{|a|^2}{2}$, то $\varepsilon < \frac{1}{|a|}$ и тогда $|x| > |a| - \delta > |a| -\varepsilon \frac{|a|^2}{2} > |a| - \frac{1}{|a|}\frac{|a|^2}{2} = |a| - \frac{|a|}{2} = \frac{|a|}{2}.$

Имеем

$$
\left| \frac{1}{x} - \frac{1}{a} \right| = \frac{|a-x|}{|ax|} \le \frac{2 |a-x|}{|a|^2} < \varepsilon,
$$
что и доказывает непрерывность $f$.