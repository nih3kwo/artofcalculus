# Интегрирование форм, содержащих радикалы

В этом разделе мы рассмотрим формы вида 
$$
R\left(x, \left(\frac{ax+b}{a'x+b'} \right)^{r_1}, \ldots, \left(\frac{a'x+b'}{cx+d} \right)^{r_n} \right),
$$
где $R(x_1,y_1,\ldots, y_n)$ — рациональная функция от переменных $x_1,y_1,\ldots, y_n,$ $m,n \in \mathbb{Z}$, а $r_i, p \in \mathbb{Q}.$ 

:::{prf:example}
Пусть, например $R(x,y) \in \mathbb{R}(x,y)$ — рациональная функция от двух переменных $x,y$, имеющая вид
$$
R(x,y) = \frac{y+2}{(x+1)^2 -y},
$$
тогда если мы рассмотрим форму
$$
\omega = \frac{\sqrt{x+1}  +2}{(x+1)^2 - \sqrt{x+1}}\mathrm{d}x,
$$
то видно, что $\omega = R(x, \sqrt{x+1})\mathrm{d}x.$
:::

:::{warning}
Но некоторые формы всегда имеют такой очевидный вид как в предыдущем примере.
:::

:::{prf:example}
Рассмотрим форму
$$
\omega = \frac{\mathrm{d}x}{\sqrt[3]{(x-1)(x+1)^2}}.
$$
В таком виде её уже нельзя представить как $R(x,y)\mathrm{d}x$, однако сделаем следующие преобразования
$$\begin{align*}
\omega  &=  \frac{\mathrm{d}x}{\sqrt[3]{(x-1)(x+1)^2}} \\
&=  \frac{\mathrm{d}x}{\sqrt[3]{(x-1)\frac{(x+1)^3}{(x+1)} }} \\
&=  \frac{\mathrm{d}x}{(x+1) {\sqrt[3]{\frac{x-1}{x+1}}}} \\
&= \sqrt[3]{\frac{x+1}{x-1}}\cdot \frac{1}{x+1}\mathrm{d}x, \\
\end{align*}$$
и тогда уже можно написать, что $\omega = R(x,y)\mathrm{d}x$, где $R(x,y) = \frac{y}{x+1}$.
:::

:::{prf:theorem}
Пусть $R(x,y_1,\ldots, y_n)$ — рациональная функция. Для любых рациональных чисел $r_1, \ldots, r_n \in \mathbb{Q}$ и любых $a,b,a',b' \in \mathbb{R}$, $a',b'\ne 0$ интеграл
$$
\bigintss R\left(x, \left(\frac{ax+b}{a'x+b'} \right)^{r_1}, \ldots, \left(\frac{a'x+b'}{cx+d} \right)^{r_n} \right)\mathrm{d}x
$$
выражается через рациональные функции и функции $\ln, \arctan.$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Ясно, что без ограничения общности можно считать, что все $r_i$ положительные. Пусть $r_1 = \frac{p_1}{q_1}, \ldots, r_n = \frac{p_n}{q_n}$, и пусть $q:=q_1,\ldots, q_n$, тогда
$$
q_i = \frac{q }{q_1 \cdots \widehat{q_i}\cdots q_n},
$$
где $\widehat{q_i}$ означает, что в выражении $q_1\cdots q_n$ число $q_i$ пропущено.

Сделаем тогда замену 
$$
u: = \left(\frac{ax + b}{a'x + b'} \right)^{\frac{1}{q}},
$$
тогда получаем для каждого $1\le i \le n$
$$
\left( \frac{ax+b}{a'x + b'} \right)^{\frac{p_i}{q_i}} =  \left( \frac{ax+b}{a'x + b'} \right)^{\frac{p_i\cdot q_1 \cdots \widehat{q_i}\cdots q_n}{q}} = u^{p_i\cdot q_1 \cdots \widehat{q_i}\cdots q_n} = u^{k_i},
$$
где $k_i : = p_i\cdot q_1 \cdots \widehat{q_i}\cdots q_n \in \mathbb{N}$. Таким образом, получаем
$$
R\left(x, \left(\frac{ax+b}{a'x+b'} \right)^{r_1}, \ldots, \left(\frac{a'x+b'}{cx+d} \right)^{r_n} \right) = R(x,u^{k_1},\ldots, u^{k_n}),
$$
т.е. мы избавились от иррациональности (=радикалов) в самой функции. Посмотрим тогда, что произойдёт с формой. Для этого нужно выразить $\mathrm{d}x$ через $\mathrm{d}u.$

Так как $u^q = \frac{ax + b}{a'x+b'}$, то $x = \frac{b'u^q - b}{a - a'u^q}$, а тогда 
$$
\mathrm{d}x = \left(\frac{b'u^q - b}{a - a'u^q} \right)'_u\mathrm{d}u,
$$
но ведь производная этой дроби тоже рациональная функция от $u$. Таким образом, интегрирование изначальной формы свелось к интегрированию формы вида $\widetilde{R}(u)\cdot\left(\frac{b'u^q - b}{a - a'u^q} \right)'\mathrm{d}u$, где 
$$
\widetilde{R}(u): = R\left( \frac{b'u^q- b}{a- a'u^q}, u^{k_1}, \ldots, u^{k_n} \right)
$$
рациональная функция от одной переменной $u.$ Но тогда, воспользовавшись теоремой [](#int_of_rational), мы завершаем доказательство.
:::


:::{prf:example}
Найдём 
$$
\bigintsss \frac{\sqrt{x}}{\sqrt[4]{x^3} +4} \mathrm{d}x.
$$
Мы можем положить, что $x = u^4$, так как $4$ — наименьшее общее кратное для $2,4$. Тогда находим $\mathrm{d}x = (u^4)'\mathrm{d}x = 4u^3 \mathrm{d}u$, подставляем
$$\begin{align*}
\bigintsss \frac{\sqrt{x}}{\sqrt[4]{x^3} +4} \mathrm{d}x &= \bigintsss \frac{x^{\frac{1}{2}}}{x^{\frac{3}{4}}+4} \mathrm{d}x \\
&= 4 \bigintsss \frac{u^2 \cdot u^3 \mathrm{d}u}{u^3+4} = 4 \bigintsss \frac{u^5\mathrm{d}u}{u^3+4} \\
&= 4 \bigintsss \left(u^3 - \frac{4u^2}{u^3+4} \right)\mathrm{d}u \\
&= 4\bigintsss u^3 \mathrm{d}u - 16 \bigintsss\frac{u^2 \mathrm{d}u}{u^3 +4} = 4\bigintsss u^3 \mathrm{d}u - \frac{16}{3} \bigintsss\frac{\mathrm{d}(u^3)}{u^3 +4} \\
&= u^4 - \frac{16}{3} \ln |u^3 + 4| +C,
\end{align*}$$
и тогда
$$
\bigintsss \frac{\sqrt{x}}{\sqrt[4]{x^3} +4} \mathrm{d}x = \sqrt[4]{x^3} - \frac{16}{3} \ln \left| \sqrt[4]{x^3} + 4 \right| + C.
$$
:::
