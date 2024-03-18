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