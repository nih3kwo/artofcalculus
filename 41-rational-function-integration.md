# Интегрирование рациональных функций

До сих пор мы использовали либо какие-то простые наблюдения, либо какие-то трюки, чтобы интегрировать форму. Разумеется, наукой это назвать нельзя. Здесь мы систематически разработаем технику интегрирования для очень важного класса форм.

## Элементарные свойства полиномов

Напомним, что полиномом $P(x)$ от переменной $x$ над $\mathbb{R}$ называется выражение вида 
$$
\alpha_nx^n + \alpha_{n-1}x^{n-1} + \cdots + \alpha_1x + \alpha_0,
$$
где все $\alpha_i \in \mathbb{R}$ и можно положить, что $\alpha_n \ne 0$ и в таком случае говорят, что полином $P(x)$ имеет степень $n$ и пишут $\mathrm{deg}(P(x))= n.$

Множество всех полиномов от переменной $x$ над $\mathbb{R}$ обозначают так: $\mathbb{R}[x].$

:::{prf:theorem}[Делимость полиномов]
:name: div_of_polynmials
Для любых полиномов $A(x), B(x) \in \mathbb{R}[x]$ всегда существуют однозначно определённые полиномы $Q(x), R(x) \in \mathbb{R}[x]$ такие, что
$$
A(x) = B(x) Q(x) + R(x),
$$
и $\mathrm{deg}(R(x)) < \mathrm{deg}(B(x)).$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть
$$\begin{eqnarray}
A(x) &=& \alpha_nx^n + \alpha_{n-1}x^{n-1} + \cdots + \alpha_1x + \alpha_0, \\
B(x) &=& \beta_kx^k + \beta_{k-1}x^{k-1} + \cdots + \beta_1x + \beta_0,
\end{eqnarray}$$
где $n = \mathrm{deg}(A(x))$, $k = \mathrm{deg}(B(x))$, так что $\alpha_n, \beta_k \ne 0$.

Применим индукцию по $n$.

(1) Если $n =0$ (**т.е.** $A(x) = \alpha_0$) и $0=\mathrm{deg}(A(x)) < \mathrm{deg}(B(x))$, то положим $Q(x):=0$ и $R(x) : = A(x)$, **т.е.** имеем
$$
\alpha_0 = 0 \cdot B(x) + \alpha_0.
$$

(2) Если $\mathrm{deg}(A(x)) = \mathrm{deg}(B(x)) = 0$, **т.е.** $A(x) = \alpha_0, B(x) = \beta_0$, то положим $R(x) :=0$ и $R(x): = \frac{\alpha_0}{\beta_0}$, **т.е.**
$$
\alpha_0 = \frac{\alpha_0}{\beta_0} \beta_0 +0.
$$

(3) Пусть теперь $n>0$. Если $\mathrm{deg}(A(x)) < \mathrm{deg}(B(x))$, то положим $Q(x) : = 0$, а $R(x):=A(x).$

Итак, пусть теперь теорема доказана в случае $n>0$ и $\mathrm{deg}(A(x)) \ge \mathrm{deg}(B(x))$. Тогда можем записать
$$\begin{eqnarray}
A(x) &=& \alpha_nx^n + \alpha_{n-1}x^{n-1} + \cdots + \alpha_1x + \alpha_0 \\
&=& \frac{\alpha_n}{\beta_k} x^{n-k} (\beta_k x^k) + \alpha_{n-1}x^{n-1} + \cdots + \alpha_1x + \alpha_0 \\
&=& \frac{\alpha_n}{\beta_k} x^{n-k} \Bigl( B(x) - \beta_{k-1}x^{k-1} - \cdots - \beta_0  \Bigr) + \alpha_{n-1}x^{n-1} + \cdots + \alpha_1x + \alpha_0 \\
&=&  \frac{\alpha_n}{\beta_k}x^{n-k} B(x) + \widetilde{A}(x),
\end{eqnarray}$$
где $\mathrm{deg}(\widetilde{A}(x)) = n-1.$ Но тогда по предположению индукции мы можем найти такие $\widetilde{Q}(x)$ и ${R}(x)$, что
$$
\widetilde{A}(x) = \widetilde{Q}(x)B(x) + {R}(x),
$$
и $\mathrm{deg}((x))< \mathrm{deg}(B(x))$. Тогда получаем
$$\begin{eqnarray}
A(x) &=& \frac{\alpha_n}{\beta_k}x^{n-k} B(x) + \widetilde{A}(x) \\
&=& \frac{\alpha_n}{\beta_k}x^{n-k} B(x) + \widetilde{Q}(x)B(x) + {R}(x)\\
&=& Q(x) B(x) + R(x),
\end{eqnarray}$$
где $Q(x): = \frac{\alpha_n}{\beta_k}x^{n-k} + \widetilde{Q}(x)$, чем доказательство существования $Q(x)$ и $R(x)$ закончено.

(4) Докажем теперь единственность. Предположим, что
$$
A(x)  = Q_1(x) B(x) + R_1(x) =  Q_2(x) B(x) + R_2(x),
$$
где $\mathrm{deg}(R_1(x)), \mathrm{deg}(R_2(x)) < \mathrm{deg}(B(x))$. Тогда получаем
$$
\Bigl(Q_1(x) - Q_2(x)\Bigr) B(x) = R_2(x) - R_1(x),
$$
следовательно,
$$
\mathrm{deg}\left((Q_1(x) - Q_2(x)\Bigr) B(x) \right) = \mathrm{deg}(R_2(x) -R_1(x)),
$$
но
$$
\mathrm{deg}\left((Q_1(x) - Q_2(x)\Bigr) B(x) \right) = \mathrm{deg}(Q_1(x) - Q_2(x)) + \mathrm{deg}(B(x)),
$$
и так как $\mathrm{deg}(R_2(x) - R_1(x)) < \mathrm{deg}(B(x))$, то последнее равенство возможно лишь в случае, когда $Q_1(x) = Q_2(x)$, **т.е.** $Q_1(x) = Q_2(x)$, и следовательно, $R_1(x) = R_2(x)$, что и требовалось доказать.
:::

Мы считаем известными (или мы просто их принимаем) следующие два факта из алгебры:

:::{prf:theorem} Основная теорема алгебры
Всякое уравнение
$$
\alpha_n x^n + \alpha_{n-1}x^{n-1} + \cdots + \alpha_1 x + \alpha_0 =0,
$$
где все $\alpha_i \in \mathbb{C}$, $n\ge 1$, $\alpha_n \ne 0$ имеет по крайней мере один комплексный корень.
:::

:::{prf:theorem} Теорема Безу
Если $a$ — корень уравнения 
$$
\alpha_n x^n + \alpha_{n-1}x^{n-1} + \cdots + \alpha_1 x + \alpha_0 =0,
$$
то полином $P(x) = \alpha_n x^n + \alpha_{n-1}x^{n-1} + \cdots + \alpha_1 x + \alpha_0 =0$ делится без остатка на полином $x-a.$
:::


Тогда мы получаем очень важное для нас следствие:

:::{prf:theorem}
:name: any_polynomail_is_1+2
Любой полином $P(x)$, $\mathrm{deg}(P(x)) \ge 1$ с действительными коэффициентами может быть представлен в виде
$$
P(x) = (x - a_1)^{k_1} \cdots (x-a_p)^{k_p} (x^2 + b_1x + c_2)^{m_1}\cdots (x^2 + b_qx + c_q)^{m_q}, 
$$
где $k_1 + \cdots + k_p + 2m_1 + \cdots + 2m_q = \mathrm{deg}(P(x))$ и все $k_i, m_j \in \mathbb{Z}_{\ge 0}.$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Согласно теореме Безу, нужно просто доказать, что любой полином $P(x) \in \mathbb{R}[x]$ делится либо на линейный полином вида $(x-a)$, либо на квадратный $(x^2 + bx + c)$. Но по теореме Безу, если $P(x)$ имеет корень $a$, то $P(x)$ делится на $(x-a)$, потому все числа $a_1,\ldots, a_p$ — это просто все корни уравнения $P(x) = 0$.

Далее, рассмотрим теперь $P(x)$ как полином в множестве $\mathbb{C}[x]$, это возможно, потому что $\mathbb{R} \subset \mathbb{C}$. Тогда по основной теореме алгебры существует комплексное число $\zeta = \alpha + \beta \sqrt{-1}$, что $P(z) =0$. Тогда по теореме Безу $P(x)$ делится на $(x- \alpha - \beta \sqrt{-1})$.

Пусть $P(x) = \alpha_nx^n + \cdots + \alpha_1 x + \alpha_0$, тогда если $P(\zeta) =0$, где $\zeta \in \mathbb{C}$, то получаем
$$\begin{eqnarray}
P(\overline{\zeta}) &=&  \alpha_n {\overline{\zeta}}^n + \cdots + \alpha_1 \overline{\zeta} + \alpha_0 \\
&=& \overline{\alpha_n \zeta^n} + \cdots + \overline{\alpha_1 \zeta} + \overline{\alpha_0} \\
&=& \overline{\alpha_nx^n + \cdots + \alpha_1 x + \alpha_0} \\
&=& \overline{P(\zeta)} = 0.
\end{eqnarray}$$

Это означает, что $\overline{\zeta}$ тоже является корнем уравнения $P(x) = 0$, тогда по теореме Безу $P(x)$ делится на $x - \overline{\zeta} = x - (\alpha -\beta \sqrt{-1})$.

Таким образом, полином $P(x)$ делится на произведение $(x - \zeta)(x - \overline{\zeta})$.

Находим
$$
(x - \zeta)(x - \overline{\zeta}) = (x - \alpha - \beta \sqrt{-1})(x - \alpha + \beta \sqrt{-1}) = x^2 - 2 \alpha x + \alpha^2 + \beta^2,
$$
**т.е.** полином $P(x)$ делится на полином второй степени. Это завершает доказательство. 
:::


## Рациональная функция и её разложение

Мы умеем интегрировать формы вида $P(x) \mathrm{d}x$, где $P(x)$ — полином, сейчас мы хотим развить теорию интегрирования форм вида $\frac{P(x)}{Q(x)}\mathrm{d}x$, где $Q(x)$ тоже полином и всегда подразумевается, что $Q(x) \ne 0$. 

Выражения вида $\frac{P(x)}{Q(x)}$ называются **дробями**, и как и в случае числовых дробей, целесообразно рассматривать так называемые несократимые дроби. Формализацией этого желания является следующее определение. 

:::{prf:definition}
:label: rational_func
Рациональная функция от одной переменной — это класс эквивалентности дробей вида $\dfrac{P(x)}{Q(x)}$, где $P(x), Q(x)$ — полиномы, $Q(x) \ne 0$, и мы считаем, что две такие дроби эквивалентны
$$
\frac{P(x)}{Q(x)} \sim \frac{A(x)}{B(x)},
$$
если и только если $P(x) B(x) = A(x) Q(x).$
:::

Множество всех рациональных функций образует поле \footnote{Доказательство этого факта очевидно и при этом банальное, нужно лишь проверить выполнение аксиом i.1 — i.9 определения поля (см. Определение [](#field)).}, которое так и называется **полем рациональных функций** и обозначается так: $\mathbb{R}(x).$

:::{prf:remark}**
Более того, можно пойти дальше и рассматривать поля рациональных функций от нескольких переменных, **т.е.** выражений вида $\frac{P(x,y)}{Q(x,y)}$, где $P(x,y)$, $Q(x,y)$ — полиномы от двух переменных. Оказывается, что если мы ограничим множество рассматриваемых полиномов, например, чтобы знаменатель не делился на какой-то конкретный полином $F(x,y)$, то мы получаем поле рациональных функций на кривой, заданной уравнением $F(x,y)=0$. Это поле является очень важной характеристикой кривой. Более того, как мы увидим далее, именно изоморфизм полей у кривых позволяет сводить сложные интегралы к более простым. Поэтому неудивительно, что в теории интегрирования столько алгебры. }   
:::

Так как имеется процесс деления полиномов друг на друга, то введём следующее понятие:

(def4101)=
:::{prf:definition}
Дробь $\frac{P(x)}{Q(x)}$ называется **правильной**, если $\mathrm{deg}(P(x)) < \mathrm{deg}(Q(x))$.
:::

:::{warning}
Если дробь неправильная, то, поделив числитель на знаменатель (теорема [](#div_of_polynmials)), мы получим полином плюс правильная дробь. Это аналогично выделению целой части в неправильной числовой дроби.
:::


Используя теперь теорему [](#any_polynomail_is_1+2), мы можем разложить знаменатель на более простые множители. Оказывается, это влечёт разложение и самой дроби. Введём следующее понятие.

(def4102)=
:::{prf:definition}
**Простыми** дробями в поле $\mathbb{R}(x)$ называются выражения вида

1. $\dfrac{A}{(x-\alpha)^k}$, где $A,\alpha \in \mathbb{R}$, и $k\ge 1$,
2. $\dfrac{Ax + B}{(x^2 + ax + b)^n}$, где $A,B, a,b \in \mathbb{R}$, $n\ge 1$ и предполагается, что $x^2 + ax +b$ не имеет вещественных корней.

:::


:::{prf:theorem}
:name: decomp_of_fraction
Каждая правильная дробь может быть представлена в виде суммы конечного числа простых дробей.
:::

(theorem-4-8)=
:::{prf:proof}
:class: dropdown
:nonumber:
Рассмотрим дробь $\frac{P(x)}{Q(x)}$, согласно теореме [](#any_polynomail_is_1+2), мы можем записать знаменатель в виде 
$$
Q(x) = (x - a_1)^{k_1} \cdots (x-a_p)^{k_p} (x^2 + b_1x + c_2)^{m_1}\cdots (x^2 + b_qx + c_q)^{m_q}, 
$$
где $k_1 + \cdots + k_p + 2m_1 + \cdots + 2m_q = \mathrm{deg}(P(x))$ и все $k_i, m_j \in \mathbb{Z}_{\ge 0}$, и более того, согласно теореме Безу, все $a_i$ — это всё корни уравнения $Q(x) =0.$

(1) Пусть хотя бы один $k_i$ больше нуля, обозначим его просто через $k$, тогда можно записать $Q(x) = (x-a)^k \widetilde{Q}(x)$, где $a$ — это соответствующее число из чисел $a_i$. Тогда $a$ не является корнем уравнения $\widetilde{Q}(x) =0.$

Допустим теперь, что существует такое число $A$ и такой полином $\widetilde{P}(x)$, что 
$$
\frac{P(x)}{Q(x)} = \frac{A}{(x-a)^k} + \frac{\widetilde{P}(x)}{(x-a)^{k-1}\widetilde{Q}(x)}.
$$

Для доказательства этого равенства достаточно подобрать эти неизвестные $A, \widetilde{P}(x)$ так, чтобы выполнялось равенство
$$
P(x) - A \widetilde{Q}(x) = (x-a)\widetilde{P}(x).
$$

Так как $A$ это число, то оно не должно зависеть от $x$, поэтому положим в этом равенстве $x = a$, и тогда мы получаем, что
$$
P(a) - A \widetilde{Q}(a) = 0
$$
откуда $A = \frac{P(a)}{\widetilde{Q}(a)}$. Это выражение корректно, так как $a$ был выбран так, чтобы $a$ — корень уравнения $Q(x) =0$, но не корень уравнения $\widetilde{Q}(x) = 0.$

Далее, полином $\widetilde{P}(x)$ можно теперь определить следующим образом:
$$
\widetilde{P}(x): = \frac{P(x) - A \widetilde{Q}(x)}{x-a}.
$$

(2) Пусть теперь $Q(x)$ содержит хотя бы один сомножитель вида $(x^2 + bx + c)^m$, тогда запишем $Q(x)= (x^2 + bx + c)^m \widehat{Q}(x)$, где уже $\widehat{Q}(x)$ не делится на $x^2 + bx + c$. Тогда подберём числа $B,C$ и полином $\widehat{P}(x)$ так, чтобы
$$
\frac{P(x)}{Q(x)} = \frac{Bx + C}{(x^2 + bx + c)^m} + \frac{\widehat{P}(x)}{(x^2 + bx + c)^{m-1} \widehat{Q}(x)}.
$$

Это то же самое, что подобрать эти же неизвестные, чтобы выполнялось равенство
$$
P(x) - (Bx +C)\widehat{Q}(x) = (x^2 + bx + c) \widehat{P}(x).
$$

Поступим следующим образом. Разделим полиномы $P(x)$, $\widehat{Q}(x)$ на $x^2 + bx + c$ с остатком;
$$\begin{eqnarray}
P(x) &=& F(x)(x^2 + bx + c) + \alpha x + \beta, \\
\widehat{Q}(x) &=& H(x)(x^2 + bx + c) + \gamma x + \delta.
\end{eqnarray}$$

Тогда, подставляя в предыдущее равенство, получаем
$$
F(x)(x^2 + bx + c) + \alpha x + \beta - (Bx +C) \bigl( H(x)(x^2 + bx + c) + \gamma x + \delta\bigr) = (x^2 + bx + c) \widehat{P}(x).
$$

Потребуем теперь, чтобы полином
$$
R(x) = \alpha x + \beta  - (Bx + C) (\gamma x +\delta ) =0
$$
делился на $x^2 + bx + c$ без остатка.

```{warning}
Если можно будет найти такие числа, то значит, мы добьёмся того, что существуют такие $B,C$, что полином $P(x) - (Bx + C)\widehat{Q}(x)$ делится на $x^2 + bx + c$ без остатка. В таком случае, полином $\widehat{P}(x)$ находится как частное от деления полинома $P(x) - (Bx + C)\widehat{Q}(x)$ на $x^2 + bx + c$.  
```

Итак, имеем
$$\begin{eqnarray}
R(x) &=& \alpha x + \beta  - (Bx + C) (\gamma x +\delta )  \\
&=& - \gamma B x^2 + (\alpha - \delta B - \gamma C)x + (\beta - \delta C).
\end{eqnarray}$$

Разделив теперь $R(x)$ на $x^2 + bx +c $ на $x^2 + bx +c$, мы получим в остатке следующее выражение:

$$
\Bigl( (b \gamma - \delta)B - \gamma C  + \alpha \Bigr)x + c \gamma B - \delta C + \beta.
$$

Тогда мы получаем систему (относительно неизвестных $B,C$) линейных уравнений
$$
\begin{cases}
(b \gamma - \delta)B - \gamma C =- \alpha \\
c \gamma B - \delta C =- \beta.
\end{cases}
$$

Определитель этой системы имеет вид
$$
\Delta = \begin{vmatrix}
b \gamma - \delta & \gamma \\
c\gamma & -\delta
\end{vmatrix} = \delta^2 - b\gamma \delta + c \gamma^2
$$

Пусть $\gamma \ne 0$, тогда
$$
\Delta = \gamma^2 \left( \left( -\frac{\delta}{\gamma} \right)^2 + b \left(-\frac{\delta}{\gamma}\right) + c \right),
$$
но это есть значение полинома $x^2 + bx +c$ в точке $x = -\frac{\delta}{\gamma}$ и, следовательно $\Delta \ne 0$, ибо мы предположили, что $x^2 + bx +c$ не имеет корней. Таким образом, система имеет решение, и числа с необходимым требованием существуют. 

Если же $\gamma =0$, то $\Delta = \delta^2$, но так как $\widehat{Q}(x) = H(x)(x^2 + bx + c) + \gamma x + \delta$, то $\delta \ne 0$ ибо $\widehat{Q}(x)$ на $x^2 + bx +c$ не делится.

Итак, в любом случае, решение системы существует, а значит, можно подобрать так $B,C$, чтобы полином $P(x) - (Bx + C)\widehat{Q}(x)$ делится на $x^2 + bx + c$ без остатка. В таком случае полином
$$
\widehat{P}(x): = \frac{P(x) - (Bx + C)\widehat{Q}(x}{x^2 + bx + c}.
$$

Таким образом, доказательство теоремы сводится к повторному применению случаев (1) и (2), которые обеспечивают возможность последовательного выделения простых дробей из данной правильной дроби, вплоть до её исчерпывания. Это доказывает теорему.
:::

:::{prf:lemma}
:name: int_of_(x-a)^{-k}
$$
\int \frac{A}{(x-\alpha)^k} \mathrm{d}x = \begin{cases}
A \ln|x-\alpha| + C, & k =1,\\
- \frac{A}{k-1}\cdot \frac{1}{(x-\alpha)^{k-1}} + C, & k >1.
\end{cases}
$$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
С помощью замены $y =x-\alpha$ интегрирование формы $\omega = \frac{A}{(x-\alpha)^k}$ сводится к интегрированию формы $\frac{A}{y^k}$, что и даёт нужный результат, так как $\mathrm{d}y = \mathrm{d}(x-\alpha) = \mathrm{d}x.$
:::

Чтобы научится интегрировать форму $\dfrac{Ax + B}{(x^2 + ax + b)^n} \mathrm{d}x$, нам нужно сначала научится интегрировать форму $\dfrac{\mathrm{d}x}{(x^2 + \alpha^2)^n}.$

:::{prf:lemma}
:name: int_of_x^2+a^2
Для каждого $n\ge 1$ рассмотрим форму
$$
\omega_n: = \frac{\mathrm{d}x}{(x^2 + \alpha^2)^n},
$$
тогда
$$
\int \omega_{n+1} = \frac{1}{2n\alpha^2}\cdot \frac{x}{(x^2 + \alpha^2)^n} + \frac{2n-1}{2n\alpha^2} \cdot\int \omega_n, \qquad \int \omega_1 = \frac{1}{\alpha} \cdot \arctan\left( \frac{x}{\alpha}\right) + C.
$$
:::

(theorem-4-9)=
:::{prf:proof}
:class: dropdown
:nonumber:
(1) Так как $(\arctan(y))' = \frac{1}{y^2 + 1}$, то
$$\begin{eqnarray}
\int \omega_1 &=& \int \frac{\mathrm{d}x}{x^2 + \alpha^2}  = \ \frac{\mathrm{d}x}{\alpha^2\cdot\left (\left( \frac{x^2}{\alpha^2} \right) + 1\right)}\\
&=& \frac{1}{\alpha^2} \int \frac{\alpha \cdot\mathrm{d}\left(\frac{x}{\alpha}\right)}{\left( \frac{x^2}{\alpha^2} \right) + 1} = \frac{1}{\alpha} \int \frac{ \mathrm{d}\left(\frac{x}{\alpha}\right)}{\left( \frac{x}{\alpha} \right)^2 + 1} = \frac{1}{\alpha} \cdot \arctan\left( \frac{x}{\alpha}\right) + C.
\end{eqnarray}$$

(2) Пусть теперь $n \ge 1$, будем интегрировать $\omega_n$ по частям, **т.е.** воспользуемся правилом
$$
\int u \mathrm{d}v = uv - \int v \mathrm{d}u.
$$

Положили $u = \frac{1}{(x^2 + \alpha^2)^n}$, $v = x$, находим
$$
\mathrm{d}u = \left( \frac{1}{(x^2 + \alpha^2)^n} \right)'\mathrm{d}x = - \frac{2nx}{(x^2 + \alpha^2)^{n+1}}\mathrm{d}x, \qquad \mathrm{d}v = \mathrm{d}x.
$$

Тогда
$$\begin{eqnarray}
\int \omega_n &=& \int \frac{\mathrm{d}x}{(x^2 + \alpha^2)^n} = \frac{x}{(x^2 + \alpha^2)^n} + 2n \cdot \int \frac{x^2}{(x^2 + \alpha^2)^{n+1}}\mathrm{d}x \\
&=& \frac{x}{(x^2 + \alpha^2)^n} + 2n \cdot \int \frac{(x^2+\alpha^2) - \alpha^2}{(x^2 + \alpha^2)^{n+1}}\mathrm{d}x \\
&=& \frac{x}{(x^2 + \alpha^2)^n} + 2n \cdot \left( \int \frac{(x^2+\alpha^2)}{(x^2 + \alpha^2)^{n+1}}\mathrm{d}x - \alpha^2 \int  \frac{\mathrm{d}x}{(x^2 + \alpha^2)^{n+1}}\right) \\
&=& \frac{x}{(x^2 + \alpha^2)^n} + 2n \cdot \left( \int \frac{\mathrm{d}x}{(x^2 + \alpha^2)^{n}} - \alpha^2 \int  \frac{\mathrm{d}x}{(x^2 + \alpha^2)^{n+1}}\right) \\
&=&\frac{x}{(x^2 + \alpha^2)^n} + 2n\cdot \int \omega_n  - 2n\alpha^2 \int \omega_{n+1},
\end{eqnarray}$$
**т.е.** мы получили рекуррентное соотношение 
$$
\int \omega_n = \frac{x}{(x^2 + \alpha^2)^n} + 2n\cdot \int \omega_n  - 2n\alpha^2 \int \omega_{n+1},
$$
из которого и следует требуемое.    
:::

:::{prf:lemma}
:name: int_of_prime
Интеграл от формы $\frac{Ax + B}{(x^2 + ax + b)^n}\mathrm{d}x$ выражается через рациональные функции и функции $\ln$, $\arctan$.
:::

(theorem-4-10)=
:::{prf:proof}
:class: dropdown
:nonumber:
Выделим в выражении $x^2 + ax + b$ полный квадрат
$$
x^2 + ax + b = \left(x+ \frac{a}{2} \right)^2 + \left(b - \frac{a^2}{4} \right),
$$
так как по условию $x^2 + ax + b =0$ не имеет корней, то $a^2 - 4b <0$, тогда положим 
$$
c^2: = b- \frac{a^2}{4}, \qquad c = + \sqrt{b- \frac{a^2}{4}}
$$
тогда сделаем замену 
$$
y:= x+ \frac{a}{2},
$$
находим
$$\begin{eqnarray}
\mathrm{d}y &=& \left( x+ \frac{a}{2}\right)' \mathrm{d}x = \mathrm{d}x,\\
x^2 + ax + b &=& \left(x+ \frac{a}{2} \right)^2 + \left(b - \frac{a^2}{4} \right) = y^2 + c^2, \\
Ax + B &= & Ay + \left(B - \frac{Aa}{2} \right).
\end{eqnarray}$$

Рассмотрим два случая.

(1) $n = 1$, тогда получаем
$$\begin{eqnarray}
\int \frac{Ax + B}{x^2 + ax + b}\mathrm{d}x = \int \frac{Ax + \left( B - \frac{Aa}{2} \right)}{y^2 + c^2}\mathrm{d}y &=& \frac{A}{2} \int \frac{2y\mathrm{d}y}{y^2 + c^2} + \left( B - \frac{Aa}{2} \right) \int \frac{\mathrm{d}y}{y^2 + c^2} \\
&=& \frac{A}{2} \ln(y^2 + c^2) + \frac{1}{c} \cdot \left( B - \frac{Aa}{2} \right)\arctan\left(\frac{y}{c}\right) + C,
\end{eqnarray}$$
или, возвращаясь к $x$ и подставляя вместо $c$ его значение:
$$
\int \frac{Ax + B}{x^2 + ax + b)}\mathrm{d}x =  \frac{A}{2}\ln(x^2 + ax + b) + \frac{2B-Aa}{\sqrt{4b-a^2}}\arctan\left( \frac{2x+a}{\sqrt{4b-a^2}} \right) + C.
$$

(2) Пусть $n >1$, делая ту же замену, получаем
$$
\int \frac{Ax + B}{(x^2 + ax + b)^n}\mathrm{d}x = \int \frac{Ax + \left( B - \frac{Aa}{2} \right)}{(y^2 + c^2)^n}\mathrm{d}y = \frac{A}{2} \int \frac{2y\mathrm{d}y}{(y^2 + c^2)^n} + \left( B - \frac{Aa}{2} \right) \int \frac{\mathrm{d}y}{(y^2 + c^2)^n}.
$$

Видим, что второй интеграл это интеграл от формы $\omega$ который найден в лемме [](#int_of_x^2+a^2), первый же интеграл легко берётся с помощью замены $t:=y^2 + c^2 $, тогда $\mathrm{d}t = (y^2 + c^2)'\mathrm{d}y = 2y\mathrm{d}y$, следовательно $y\mathrm{d}y = \frac{1}{2}\mathrm{d}t$, и мы получаем
$$
\int \frac{2y\mathrm{d}y}{(y^2 + c^2)^n} = \int \frac{\mathrm{d}t}{t^n} = - \frac{1}{n-1}\cdot \frac{1}{t^{n-1}} +C.
$$
Тем самым лемма доказана.
:::

:::{prf:theorem}
Интеграл от формы вида $\frac{P(x)}{Q(x)}$ выражается через рациональные функции и функции $\ln, \arctan.$ 
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Действительно, если дробь неправильная, то поделив $P(x) = B(x) Q(x) + R(x)$ на $Q(x)$ мы получаем
$$
\int \frac{P(x)}{Q(x)}\mathrm{d}x = \int B(x)\mathrm{d}x + \int \frac{R(x)}{Q(x)}\mathrm{d}x.
$$

Первый интеграл находится легко, так как это интеграл от полинома, а во втором интеграле присутствует уже правильная дробь. Но согласно теореме [](#decomp_of_fraction) каждая правильная дробь представляется в виде суммы простых, тогда из лемм [](#int_of_(x-a)^{-k)}, [](#int_of_prime) вытекает утверждение теоремы.    
:::



