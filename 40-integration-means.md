# Способы интегрирования

Здесь мы рассмотрим некоторые способы для интегрирования дифференциальных форм от одной переменной. Мы также приведём примеры форм, интегралы от которых невозможно выразить через элементарные функции.

Отметим также, что мы будем говорить об интегралах **лишь для непрерывных функций**. Если функция задана конкретно и имеет точки разрыва, то рассматривать её будем лишь в промежутках её непрерывности. Поэтому мы освобождаемся от необходимости всякий раз оговаривать существование интегралов: 

:::{warning}
Рассматриваемые нами интегралы все существуют!
:::

## Замена переменных

Рассмотрим дифференциальную форму $\omega  = f(x) \mathrm{d}x \in \Omega^1(\mathbb{R})$, и пусть $x$ есть некоторая функция от нового переменного $t$, **т.е.** $x = \varphi(t)$.

:::{prf:theorem}
:name: replace_in_int
Если $x = \varphi(t)$ — дифференцируемая функция на некотором промежутке $I \subseteq \mathbb{R}$, то
$$
\int f(x) \mathrm{d}x = \int f(\varphi(t)) \varphi'(t) \mathrm{d}t.
$$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Если $\varphi:\mathbb{R} \to \mathbb{R}$ — дифференцируемая функция, то мы получаем
$$
\mathrm{d} x = \mathrm{d} \varphi(t) = \varphi'(t)\mathrm{d}t,
$$
и тогда получаем
$$
\int f(x) \mathrm{d}x = \int f(\varphi(t)) \varphi'(t) \mathrm{d}t,
$$
что и требовалось доказать.
:::

:::{prf:example}
Покажем, что 
$$
\int x^\alpha \mathrm{d}x = \frac{x^{\alpha+1}}{\alpha+1} + C, \qquad \alpha \in \mathbb{R}, \alpha \ne -1.
$$

Пусть $y(x) = x^{\alpha+1}$, тогда, рассматривая эту функцию в промежутке, в котором она дифференцируема, согласно лемме [](#intdF=F) имеем
$$
\int \mathrm{d}y = y+ C' \Longleftrightarrow \int \mathrm{d} x^{\alpha +1} = x^{\alpha +1} + C'.
$$

Далее, $y'(x) = (\alpha +1) x^\alpha$, тогда согласно теореме [](#replace_in_int), получаем
$$
\int \mathrm{d}y = \int (\alpha +1) x^{\alpha} \mathrm{d}x =  x^{\alpha +1} + C'.
$$

Наконец, согласно предложению [](#linearity_of_int), получаем
$$
\int (\alpha +1) x^{\alpha} \mathrm{d}x =  x^{\alpha +1} + C' \Longleftrightarrow (\alpha +1) \int x^\alpha \mathrm{d}x = x^{\alpha +1} + C',
$$
и полагая $C: = \frac{C'}{\alpha +1}$, мы получаем требуемое.
:::

## Интегрирование по частям

Докажем следующую формулу, которая называется **правилом интегрирования по частям**.

:::{prf:theorem}[Интегрирование по частям]
Пусть $u = u(x)$, $v= v(x)$ — две функции от $x$, имеющие непрерывные производные $u'= u'(x)$, $v' = v'(x)$. Тогда имеет место формула
$$
\int u \mathrm{d}v = uv - \int v \mathrm{d}u.
$$
:::

(theorem-4-7)=
:::{prf:proof}
:class: dropdown
:nonumber:

Согласно ([](#dffdx)), а также правилу Лейбница (Теорема [](#ariph_for_der) 2), имеем 
$$\begin{align*}
\mathrm{d}(uv) &= (uv)' \mathrm{d}x \\
&= u'v \mathrm{d}x + uv'\mathrm{d}x \\
&= v \bigl( u'\mathrm{d}x\bigr) + u \bigl( v'\mathrm{d}x \bigr) \\
&= v \mathrm{d}u + u \mathrm{d}v.
\end{align*}$$
Таким образом, $u\mathrm{d}v = \mathrm{d}(uv) - v \mathrm{d}u$. Тогда, используя линейность интеграла (Предложение [](#linearity_of_int)) и Лемму [](#intdF=F), получаем
$$\begin{align*}
\int u \mathrm{d}v &= \int \Bigl(  \mathrm{d}(uv) - v \mathrm{d}u \Bigr) \\
&= \int \mathrm{d}(uv) - \int v \mathrm{d}u \\
&= uv - \int v \mathrm{d}u,
\end{align*}$$
что и требовалось доказать.    
:::

:::{warning}
Следует заметить, что более формально мы должны были бы записать
$$
\int \mathrm{d}(uv) - \int v \mathrm{d}u = uv + C - \int v \mathrm{d}u,
$$
но выражение $C - \int v \mathrm{d}u$ есть неопределённый интеграл для формы $v\mathrm{d}u$, поэтому его можно записать просто как $\int v \mathrm{d}u.$
:::


:::{prf:example}
Рассмотрим типичные примеры на использование этого правила.


1. Рассмотрим форму $\ln(x) \mathrm{d}x$, положим $u = \ln(x)$ и $v = x$, тогда получаем
$$ 
\int \ln(x) \mathrm{d}x =  \ln(x)\cdot x - \int x \mathrm{d}(\ln (x)),
$$
так как $\mathrm{d}(\ln(x)) = (\ln(x))'\mathrm{d}x = \frac{1}{x}\mathrm{d}x$, то получаем
$$\begin{align*}
\int \ln(x) \mathrm{d}x &= \ln(x) \cdot x - \int \frac{x}{x}\mathrm{d}x \\
&= x \ln(x) - \int \mathrm{d}x \\
&= x\ln(x) - x + C.   
\end{align*}$$
2. Рассмотрим форму $\arctan(x) \mathrm{d}x$, полагая $u = \arctan(x)$, $v = x$, получаем
$$
\int \arctan(x) \mathrm{d}x = \arctan(x) \cdot x  - \int x \mathrm{d}(\arctan(x)),
$$
так как 
$$
\mathrm{d}(\arctan(x)) = (\arctan(x))'\mathrm{d}x = \frac{\mathrm{d}x}{1+ x^2},
$$
то получаем
$$\begin{align*}
\int \arctan(x) \mathrm{d}x &= x \arctan(x) - \int \frac{x\mathrm{d}x}{1+x^2} \\
&= x \arctan(x) - \frac{1}{2} \int \frac{\mathrm{d}(x^2)}{1+x^2} \\
&= x \arctan(x) - \frac{1}{2} \int \frac{\mathrm{d}(x^2+1)}{1+x^2}\\
&= x \arctan(x) - \frac{1}{2} \ln(1+x^2) + C.
\end{align*}$$
3. Рассмотрим форму $\omega = x^2 \sin(x) \mathrm{d}x$. Если мы теперь просто положим, что $u = x^2 \sin(x)$, а $v = x$, то, во-первых, мы находим
$$
\mathrm{d}u = u'\mathrm{d}x = (x^2 \sin(x))'\mathrm{d}x = 2x \sin(x) \mathrm{d}x + x^2 \cos(x) \mathrm{d}x,
$$
и тогда мы получаем
$$\begin{align*}
\int x^2 \sin(x) \mathrm{d}x &= x^3 \sin(x) - \int x \bigl( 2x \sin(x) +x^2 \cos(x)  \bigr)\mathrm{d}x    \\
&= x^3 \sin(x) - 2 \int x^2 \sin(x) \mathrm{d}x - \int x^3 \cos(x)  \mathrm{d}x
\end{align*}$$
откуда
$$
\int x^2 \sin(x) \mathrm{d}x = \frac{x^3}{3}\sin(x) -  \int x^3 \cos(x)  \mathrm{d}x.
$$

Таким образом, задача свелась к нахождению интеграла от формы $x^3 \cos(x)\mathrm{d}x$ и если опять положить, что $u= x^3 \cos(x)$, $v = x$, то, как нетрудно проверить, задача уже сведётся к интегрированию формы $x^4 \sin(x)\mathrm{d}x.$

Таким образом, интегрировать первоначальную форму $x^2 \sin(x) \mathrm{d}x$ нужно другим способом. Для этого достаточно вспомнить, что $\mathrm{d}(-\cos(x)) = \sin(x) \mathrm{d}x$. Таким образом, форму можно преобразовать следующим образом
$$
\omega = x^2 \sin(x) \mathrm{d}x = x \mathrm{d}(-\cos (x)),
$$
тогда, если положить, что $u = x$, а $v = - \cos(x)$, то получаем
$$\begin{align*}
\int \omega &= \int u \mathrm{d}(v) = uv - \int v \mathrm{d}u \\
&= x (- \cos(x)) - \int (-\cos(x))\mathrm{d}x \\
&= - x \cos(x) + \int \cos(x) \mathrm{d}x \\
&= - x \cos(x) + \sin(x) +C.
\end{align*}$$

:::