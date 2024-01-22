# Правило Лопиталя

:::{prf:theorem}[Лопиталь]
:name: Lop
Пусть $f,g$ — дифференцируемы на $(a,b)$ и $g' \ne 0$ на $(a,b)$ и выполнено одно из двух условий

1. $\lim\limits_{x \to x_0-} f(x) = \lim\limits_{x \to x_0 -}g(x) = 0$, 
2. $\lim\limits_{x \to x_0-}g(x) = \infty.$


Тогда если $\lim\limits_{x \to x_0-} \dfrac{f'(x)}{g'(x)} = A$, то $\lim\limits_{x \to x_0-} \dfrac{f(x)}{g(x)} = A.$
:::

:::{warning}
Требование про то чтобы $\lim_{x\to x_0-}f(x) = \infty$ во втором условии вообще говоря излишне.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
(1) Пусть $f(x_0) = g(x_0) = 0$, тогда наши функции $f,g$ непрерывны в $x_0$. Тогда по теореме Коши [](#Coushy_for_functions),
\begin{equation}\label{for_Lop}
\frac{f(x)}{g(x)} = \frac{f(x) - f(x_0)}{g(x) - g(x_0)} = \frac{f'(y)}{g'(y)},    
\end{equation}
где $y \in (x, x_0)$. Так как $\lim_{x \to x_0} \frac{f'(x)}{g'(x)} = A$, то для любого $\varepsilon >0$, можно найти такое $\delta>0$, что для любого $x_0-\delta < z < x_0$, получаем
$$
\left| \frac{f'(z)}{g'(z)} -A\right| < \varepsilon.
$$

Пусть теперь $x \in (x_0 - \delta, \delta)$, то воспользовавшись ([](#for_Lop)),
$$
\left| \frac{f(x)}{g(x)} - A \right| = \left| \frac{f'(z)}{g'(z)} -A \right| < \varepsilon,
$$
что и доказывает требуемое.

(2) Так как функции дифференцируемы на $(a,b)$ и $g' \ne 0$ на $(a,b)$, то по теореме Коши [](#Coushy_for_functions), 
$$
\frac{f(b) -f(a)}{g(b) - g(a)} = \frac{f'(c)}{g'(c)},
$$
перепишем его в виде
$$
(f(b) - f(a)) g'(c) = f'(c) (g(b) - g(a)),
$$
поделим на $g(b)$, получаем
$$
\left(\frac{f(b)}{g(b)} - \frac{f(a)}{g(b)} \right) g'(c) = f'(c) \left(1 - \frac{g(a)}{g(b)} \right)
$$
теперь поделим всё на $g'(c)$
$$
\frac{f(b)}{g(b)} - \frac{f(a)}{g(b)}  = \frac{f'(c)}{g'(c)}\left(1 - \frac{g(a)}{g(b)} \right)
$$
получаем
$$
\frac{f(b)}{g(b)}  = \frac{f'(c)}{g'(c)}\left(1 - \frac{g(a)}{g(b)} \right) + \frac{f(a)}{g(b)}.
$$

Имеем $(x_0 - \theta, x_0 + \theta) \cap \mathbb{R}_{< x_0} = (x_0 -\theta, x_0).$ Поэтому получаем, что если $\lim\limits_{x \to x_0-} \dfrac{f'(x)}{g'(x)} = A$, то для любого $\varepsilon>0$ найдётся такой $y$, что для любого $z \in (y, x_0)$ имеем 
$$
\left| \frac{f'(z)}{g'(z)} - A \right| < \varepsilon.
$$

С другой стороны, это неравенство также означает что в какой-то окрестности $x_0$ функция $\frac{f'(z)}{g'(z)}$ ограничена, **т.е.,** можно записать $\left| \dfrac{f'(z)}{g'(z)} \right|<C$, например, можно положить, что $C:=|A|+1.$

Фиксируем $y$, так как $\lim_{x \to x_0-}g(x) = \infty$, то $\lim_{x \to x_0-}\frac{1}{g(x)} = 0$, то для уже выбранного выше $\varepsilon>0$ можно найти такое $\delta>0$, что для любого $x \in (x_0 - \delta, x_0)$, получаем
$$
\left| \frac{g(y)}{g(x)} \right| < \varepsilon, \qquad \left| \frac{f(y)}{g(x)}  \right| < \varepsilon.
$$

Имеем
$$\begin{eqnarray}
\left| \frac{f(x)}{g(x)} -A\right| &=& \left| \frac{f'(c)}{g'(c)}- A - \frac{f'(c)}{g'(c)} \cdot \frac{g(y)}{g(x)}  + \frac{f(y)}{g(x)}\right| \\
&\le & \left|\frac{f'(c)}{g'(c)}- A \right| + \left| \frac{f'(c)}{g'(c)} \cdot \frac{g(y)}{g(x)}\right| + \left|  \frac{f(y)}{g(x)}\right| \\
&<& \varepsilon + C\cdot \varepsilon + \varepsilon \\
&=& (C+2)\varepsilon,
\end{eqnarray}$$
что и доказывает требуемое.
:::