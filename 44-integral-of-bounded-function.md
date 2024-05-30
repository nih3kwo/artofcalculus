# Интеграл от ограниченной функции на промежутке

Пусть теперь $f:I \to \mathbb{R}$ будет ограниченной функцией на промежутке $I\subsetneq \mathbb{R}$. Мы хотим распространить на такой класс функций понятие интеграла. Чтобы это сделать, мы обратимся к ограниченным последовательностям. Мы знаем (см. Теорема [](#from_bounded_sequence)), что у любой ограниченной последовательности имеется верхний и нижний пределы ($\lim \sup$, $\lim \inf$ соответственно.) 

С определением интеграла для ограниченной функции на промежутке мы будем поступать аналогичным образом. Позже мы объясним почему нужны именно ограниченные функции.

:::{prf:definition}
Пусть $f,g: I \to \mathbb{R}$ — две функции, мы говорим, что $g$ **мажорирует** $f$ на $I$, если $g(x) \ge f(x)$ для всех $x \in I$ или же мы говорим, что $f$ **минорирует** $g$ на $I.$ Множество всех функций которые мажорируют $f$ на промежутке $I$ обозначим через $M(f)$, множество всех функций которые минорируют $f$ на промежутке $I$ обозначим через $m(f).$
:::


## Верхний и нижний интегралы

Введём теперь понятия верхнего и нижнего интеграла по аналогии с верхним и нижним пределами последовательности.

:::{prf:definition}
:name: Riemann_int
Пусть $f: I \to \mathbb{R}$ — ограниченная функция на промежутке $I \subsetneq \mathbb{R}$. Определим **верхний интеграл функции $f$ на промежутке $I$** следующим образом
$$
\sup \int_I f  : = \inf  \left\{ \int_I g  , \, g \in M_{p.c}(f)\right\},
$$
а **нижний интеграл функции $f$ на промежутке $I$** мы определим следующим образом
$$
\inf \int_I f  : = \sup  \left\{ \int_I g  , \, g \in m_{p.c}(f) \right\}.
$$
:::

:::{prf:lemma}
:name: inf_int<sup_int
Пусть $f:I \to \mathbb{R}$ — ограниченная функция на промежутке $I \subsetneq \mathbb{R}$, числами $a,b$,**т.е.,** $a \le f(x) \le b$ для всех $x \in I$. Тогда
$$
a\cdot |I| \le \inf \int_I f  \le \sup \int_I f \le b \cdot |I|.
$$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Рассмотрим функции $a,b:I \to \mathbb{R}$, $a(x) := a$, $b(x): =b$, $x\in I$. Тогда $a \in m(f)$, $b \in M(f)$, тогда по определению $\sup, \inf$ (см. Определение [](#sup,inf)), получаем
$$
\sup \int_I f\le \int_I b = b \cdot |I|, \qquad \inf \int_I f \ge \int_I a = a\cdot |I|.
$$

Покажем теперь, что 
$$\inf \int_I f \le \sup \int_I f.$$

Пусть $h\in m(f)$, $g\in M(f)$, и они — ступенчатые функции, тогда $h \le g$ и по теореме [](#imprtant_for_int) (2), получаем 
$$
\int_I h \le \int_I g.
$$

Отсюда вытекает
$$
\inf \int_I f :=\sup \left\{ \int_I h, \, h \le g \right\} \le \inf \left\{ \int_I g,\, g \ge h\right\} =: \sup \int_If,
$$
что и требовалось доказать.
:::

:::{prf:corollary}
Верхний и нижний интеграл от ограниченной функции всегда существует.
:::

:::{prf:proof}
:class: dropdown
:nonumber: Пусть $f:I \to \mathbb{R}$ — ограниченная функция, скажем $a\le f(x) \le b$, $x \in I$, на ограниченном промежутке $I \subsetneq \mathbb{R}$. По только что доказанной лемме (см. Лемма [](#inf_int<sup_int)), имеем
$$
\inf \int_I f, \,\sup \int_If \in [A,B], \qquad A: = a \cdot |I|, \, B:=b\cdot |I|,
$$
что и доказывает утверждение.
:::



Таким образом следующее определение корректно.

:::{prf:definition} Интеграл Римана от ограниченной функции
:name: int_of_bounded
Пусть $f:I \to \mathbb{R}$ — ограниченная функция на ограниченном промежутке $I \subsetneq \mathbb{R}$, тогда если
$$
\inf \int_I f = \sup \int_I f
$$
то мы определим **интеграл Римана от ограниченной функции $f$** следующим образом
$$
\int_I f: = \inf \int_I f = \sup \int_If .
$$
:::

:::{prf:remark}
:name: why_bounded
Теперь ясно почему мы рассматриваем только ограниченные функции на ограниченном промежутке. Ведь в противном случае, верхний или нижний интегралы просто могут не существовать.    
:::



:::{prf:lemma}
:name: int_coinside
Пусть $f: I \to \mathbb{R}$ — ступенчатая функция на ограниченном промежутке $I \subsetneq \mathbb{R}$, тогда она интегрируема по Риману, и более того интеграл Римана от неё это то же самое, что и интеграл от ступенчатой функции (см. определение [](#int_of_p.c)).
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Так как $f$ — ступенчата и $f(x) \le f(x)$ для всех $x \in I$, то $f\in M_{p.c}(f)$, $f \in m_{p.c.}(f)$, а тогда 
$$
\sup \int_I f \le \int_I f, \qquad \inf \int_I f \ge \int_I f,
$$
**т.е.,**
$$
\sup \int_I f \le \int_I f \le \inf \int_I f,
$$
но согласно лемме [](#inf_int<sup_int), 
$$
\inf \int_I f \le \sup \int_I f
$$
откуда получаем, что
$$
\inf \int_I f = \sup \int_I f,
$$
что и доказывает утверждение.
:::


Другими словами, для ступенчатой функции, определение интеграла которое мы дали для произвольных ограниченных функций совпадает с определением интеграла от ступенчатой функции. Таки образом, мы расширили определение интеграла [](#int_of_p.c) на более широкий класс функций.

## Верхние и нижние суммы Римана

Здесь мы докажем важные свойства интеграла от ограниченной функции.

(def416)=
:::{prf:definition}
Пусть $f:I \to \mathbb{R}$ — ограниченная функция на ограниченном промежутке $I \subsetneq \mathbb{R}$ и пусть $\lambda(I)$ — некоторое разбиение промежутка $I$. Определим **верхнюю и нижнюю суммы Римана** следующим образом
$$
{U}(f, \lambda(I)): = \sum_{\substack{A \in \lambda(I) \\ A \ne  \varnothing}} \sup_{x\in A} f(x)\cdot |A|
$$
и
$$
{L}(f, \lambda(I)): = \sum_{\substack{A \in \lambda(I) \\ A \ne  \varnothing}} \inf_{x\in A} f(x)\cdot |A|
$$
:::

:::{warning}
Условие, что $A \ne \varnothing$ здесь очень существенно, ведь если $A = \varnothing$, то $f(x)$ — это **любое число**, и тогда $\sup_{x\in \varnothing} f(x), \sup_{x\in \varnothing} f(x)= \pm \infty.$
:::

:::{prf:remark}
:name: U=int
Для данной ограниченной функции $f:I \to \mathbb{R}$ и для данного разбиения $\lambda: = \lambda(I)$ мы рассмотрим функции $\overline{f_\lambda}, \underline{f_\lambda}: I\to \mathbb{R}$, определённые следующим образом
$$
\overline{f_\lambda}(x): = \sup_{x\in A, A \in \lambda(I)} f(x),\qquad \underline{f_\lambda}(x): = \inf_{x\in A, A \in \lambda(I)} f(x).
$$

Из этой конструкции следует, что $\overline{f_\lambda} \in M_{p.c}(f,\lambda(I))$ и $\underline{f_\lambda} \in m_{p.c}(f,\lambda(I)).$ Тогда воспользовавшись определениями [](#int_of_p.c_on_I), [](#int_of_p.c), можно записать
$$
U(f,\lambda(I)) = \int_I \overline{f_\lambda}, \qquad L(f,\lambda(I)) = \int_I \underline{f_\lambda}.
$$
:::



:::{prf:lemma}
:name: intg>U
Пусть $f: I \to \mathbb{R}$ — ограниченная функция на ограниченном промежутке $I \subsetneq \mathbb{R}$ и пусть $g,h$ — ступенчатые функции на $I$ и $g \in M(f), h \in m(f)$, тогда
$$
\int_I g \ge U(f, \lambda_g(I)), \qquad \int_I h \le L(f, \lambda_h(I)),
$$
где $\lambda_g(I)$, $\lambda_h(I)$ — разбиения промежутка $I$ относительно которых $g,h$ ступенчаты, соответственно.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Согласно определениям [](#int_of_p.c_on_I), [](#int_of_p.c) имеем
$$\begin{align*}
\int_I g &: =& \int_{\lambda_g(I)}g = \sum_{A \in \lambda_g(I)}g(A)\cdot |A|,\\
\int_I h &: =& \int_{\lambda_h(I)}h = \sum_{B \in \lambda_h(I)}h(B)\cdot |B|,
\end{align*}$$
а так как $g \in M(f)$, $h\in m(f)$, то для всех $A \in \lambda_g(I)$, $B \in \lambda_h(I)$ имеем $g(A) \ge f(x)$, $h(B)\le f(y)$, $x \in A$, $y \in B$ но тогда
$$\begin{align*}
\int_I g &: =& \int_{\lambda_g(I)}g = \sum_{A \in \lambda_g(I)}g(A)\cdot |A| \ge \sum_{\substack{A \in \lambda_f(I) \\ A \ne  \varnothing}} \sup_{x\in A} f(x)\cdot |A| =: U(f, \lambda_g(I)),\\
\int_I h &: =& \int_{\lambda_h(I)}h = \sum_{B \in \lambda_h(I)}h(B)\cdot |b| \le \sum_{\substack{B \in \lambda_h(I) \\ B \ne  \varnothing}} \inf_{y\in B} f(y)\cdot |B| =: L(f, \lambda_g(I)),
\end{align*}$$
что и требовалось доказать.
:::



:::{prf:corollary}
Пусть $f:I \to \mathbb{R}$ — ограниченная функция на ограниченном промежутке $I$, тогда
$$
\sup \int_I f = \inf \Bigl\{ U(f, \lambda(I))\, : \, \mbox{$\lambda(I) $— разбиение промежутка $I$} \Bigr\}
$$
и
$$
\inf \int_I f = \sup \Bigl\{ L(f, \lambda(I))\, : \, \mbox{$\lambda(I) $— разбиение промежутка $I$} \Bigr\}.
$$   
:::

:::{prf:proof}
:class: dropdown
:nonumber: Мы докажем первое утверждение, так как второе доказывается аналогично.

Пусть $\lambda(I)$ —произволбное разбиение промежутка $I$, тогда рассмотрим множество $M_{p.c}(f, \lambda(I))$ всех ступенчатых относительно разбиения $\lambda(I)$ функции которые мажорируют функцию $f$ (**соотв.** минорируют функцию f).

(1) Покажем, что 
$$
\sup \int_I f \ge \inf_{\lambda(I)} \{U(f, \lambda(I))\}.
$$

Для любой $g\in M(f, \lambda(I))$, по лемме [](#intg>U), 
$$
U(f, \lambda(I)) \le \int_I g,
$$
тогда используя определение инфинума, имеем
$$
\int_I g \ge U(f,\lambda(I)) \ge \inf\{U(f,\lambda(I))\}
$$
для любой $g\in M(f, \lambda(I))$. Так как это неравенство верно для любого разбиения $\lambda(I)$, то получаем
$$
\sup \int_I f: = \inf \left\{ \int_I g\, :\, g \in M_{p.c}(f) \right\} \ge \inf\{U(f,\lambda(I))\},
$$
а это мы и хотели показать.

(2) Покажем, что

$$
\sup \int_I f \le \inf_{\lambda(I)} \{U(f, \lambda(I))\}.
$$

Согласно определению [](#Riemann_int),
$$
\sup\int_I f : = \inf  \left\{ \int_I g  , \, g \in M_{p.c}(f)\right\} \le \int_I \overline{f_\lambda} = U(f,\lambda(I)),
$$
здесь мы воспользовались замечанием [](#U=int). Это завершает доказательство.
:::

## Основные свойства интеграла

Здесь мы покажем основные свойства интеграла, которые будут необходимы нам для дальнейшего.

:::{prf:theorem}
:name: mega_theorem_for_int
Пусть $I \subsetneq \mathbb{R}$ — ограниченный промежуток и пусть $f,g: I \to \mathbb{R}$ — ограниченные функции на нём и при этом они интегрируемы на нём по Риману.


1. Функция $f+g$ интегрируема на $I$ и более того
$$
\int_I (f+g) = \int_I f + \int_I g.
$$
2. Для любого $\alpha \in \mathbb{R}$, функция $\alpha\cdot f$ — интегрируема на $I$ и более того
$$
\int_I \alpha\cdot f = \alpha \cdot \int_I f.
$$
3. Функция $f-g$ интегрируема на $I$ и более того
$$
\int_I(f-g)  = \int_I f - \int_I g.
$$
4. Если $f(x) \ge 0$ для всех $x\in I$, то
$$
\int_I f \ge 0.
$$
5. Если $f(x) \ge g(x)$ для всех $x \in I$, то
$$
\int_I f \ge \int_I g.
$$
6. Если $f(x) = \alpha$ для всех $x \in I$, то
$$
\int_I f = \alpha\cdot |I|.
$$
7. Пусть $J \subsetneq \mathbb{R}$ — ограниченный промежуток, и $I \subseteq J$ и пусть $\varphi:J \to \mathbb{R}$ — функция определённая следующим образом
$$
\varphi(x): = \begin{cases}
f(x), & x\in I,\\
0, & x \notin I.
\end{cases}
$$
Тогда $\varphi$ — интегрируема на $J$ и более того
$$
\int_J \varphi = \int_I f.
$$
8. Пусть $\{A,B\}$ — разбиение $I$, тогда функции $f|_A$, $f|_B$ — интегрируемы на $A$, $B$ соответственно и более того
$$
\int_I f = \int_A f|_A + \int_B f|_B.
$$

:::
:::{prf:proof}
:class: dropdown
:nonumber:

Пусть $\overline{f}$ (**соотв.** $\underline{f}$) — функция из $M_{p.c}(f)$ (**соотв.** из $m_{p.c}(f)$). Тогда, ясно, что $\overline{f}+\overline{g} \in M_{p.c}(f+g)$ и $\underline{f}+ \underline{g} \in m_{p.c}(f+g).$

Если $f$ — интегрируема по Риману на $I$, то, согласно определению [](#int_of_bounded)
$$
\int_I f = \sup \int_I f = \inf \int_I f.
$$

Тогда по определению $\inf$, $\sup$ для любого $\varepsilon >0$ найдутся такие $\overline{f} \in M_{p.c}(f)$, $\underline{f} \in m_{p.c}(f)$ что
\begin{equation}\label{non_for_Th}
\int_I f + \varepsilon = \sup \int_I f+ \varepsilon > \int_I \overline{f}, \qquad \int_I f - \varepsilon = \inf \int_I f - \varepsilon < \int_I \underline{f}.    
\end{equation}


(1) Покажем что $f+g$ интегрируема по Риману. Воспользуемся определением [](#int_of_bounded), Теоремой [](#imprtant_for_int) и полученными выше неравенствами
$$\begin{align*}
\sup \int_I (f+g) &\le& \int_I (\overline{f}+\overline{g}) \\
&=& \int_I \overline{f} + \int_I \overline{g} \\
&< & \int_I f + \varepsilon + \int_I g + \varepsilon \\
&=& \int_I f + \int_I g + 2 \varepsilon.
\end{align*}$$

Аналогично, получаем
$$
\inf \int_I(f+g) > \int_If + \int_I g - 2\varepsilon.
$$

Теперь, по лемме [](#inf_int<sup_int), получаем
$$
\int_If + \int_I g - 2\varepsilon < \inf \int_I(f+g) \le \sup \int_I (f+g) < \int_I f + \int_I g + 2 \varepsilon,
$$
в частности имеем
\begin{align*}
& -2\varepsilon < \inf\int_I(f+g) - \left( \int_I f + \int_I g \right)<2\varepsilon,\\
& -2\varepsilon < \sup\int_I(f+g) - \left( \int_I f + \int_I g \right)<2\varepsilon
\end{align*}
для любого $\varepsilon>0$, но это и означает, что
$$
\inf \int_I(f+g) = \int_I f + \int_I g, \qquad \sup \int_I (f+g) = \int_If + \int_I g,
$$
**т.е.,**
$$
\inf \int_I(f+g) = \sup \int_I (f+g) = \int_If + \int_I g,
$$
что и доказывает утверждение.

(2) Покажем, что $\alpha f$ интегрируема по Риману. Нам нужно рассмотреть несколько случаев в зависимости от числа $\alpha.$

Пусть $\alpha = 0$, тогда $\alpha f=0$ — постоянная функция и тогда по лемме [](#int_coinside), интеграл Римана от функции $\alpha f$ тоже самое, что и интеграл от ступенчатой функции $\alpha \cdot f$ который равен $\alpha = 0.$

Пусть $\alpha >0$, то $\alpha \overline{f} \in M_{p.c}(\alpha f)$, $\alpha \underline{f} \in m_{p.c}(f)$. Тогда
по определению $\inf$, $\sup$, теореме [](#imprtant_for_int), и полученным выше неравенствам, получаем
$$\begin{align*}
\sup \int_I \alpha f &\le & \int_I \alpha \cdot \overline{f} \\
&=& \alpha \int_I \overline{f} < \alpha\left( \int_If + \varepsilon \right),\\
\inf \int_I \alpha f &\ge & \int_I \alpha \cdot \underline{f} \\
&=& \alpha \int_I \underline{f} > \alpha\left( \int_If - \varepsilon \right),
\end{align*}$$
пользуясь теперь леммой [](#inf_int<sup_int), имеем
$$
\alpha \int_I f - \alpha \varepsilon  < \inf \int_I \alpha f \le \sup \int_I \alpha f < \alpha \int_I f + \alpha \varepsilon.
$$
В частности, получаем
$$
\alpha \int_I f - \alpha \varepsilon  < \inf \int_I \alpha f < \alpha \int_I f + \alpha \varepsilon,\qquad \alpha \int_I f - \alpha \varepsilon  <  \sup \int_I \alpha f < \alpha \int_I f + \alpha \varepsilon,
$$
для любого $\varepsilon >0.$ Это и означает, что
$$
\inf \int_I \alpha f = \alpha \int_I f, \qquad \sup \int_I \alpha f = \alpha \int_I f,
$$
**т.е.,**
$$
\int_I \alpha f = \alpha \int_I f.
$$

Пусть теперь $\alpha <0$, тогда можно записать $\alpha = - |\alpha|$ и в таком случае, если $|\alpha|\overline{f} \in M_{p.c}(|\alpha| f)$, то $\alpha f = - |\alpha| f \in m_{p.c}(-|\alpha| f)$. Аналогично, если $|\alpha| \overline{f} \in m_{p.c}(|\alpha| f)$, то $\alpha f = - |\alpha|f \in M_{p.c}(\alpha f)$.

Тогда получаем
$$
\sup \int_I \alpha f = \sup \int_I -|\alpha|f \le \int_I \alpha \underline{f}  <- |\alpha| \int_I f + \varepsilon,
$$
аналогично
$$
\inf \int_I \alpha f = \inf \int_I - |\alpha| f \ge \int \alpha \overline{f} > - |\alpha| \int \overline{f} - \varepsilon.
$$

Таким образом пользуясь леммой [](#inf_int<sup_int), получаем
$$
\alpha \int_I f -\varepsilon < \inf \int_I \alpha f \le \sup \int_I \alpha f < \alpha \int_I f + \varepsilon,
$$
откуда и следует утверждение.

(3) Это сразу следует из (1) и (2) применённого к $f+(-g)$.

(4) Так как $f(x) \ge 0$ для всех $x \in I$, то нулевая функция $0:I \to \mathbb{R}$, $x \mapsto 0$, $x\in I$ принадлежит множеству $m_{p.c}(f)$, но тогда
$$
\inf \int_I f \ge \int_I 0 = 0,
$$
но так как $f$ интегрируема по Риману, то
$$
\int_I f = \inf \int_I f \ge 0.
$$

(5) Это сразу следует из (3) и (4) где нужно рассмотреть функцию $h = f-g.$

(6) Ясно, что функция $f(x) =\alpha$ — ступенчата на $I$, но тогда по лемме [](#int_coinside) она интегрируема по Риману, и более того, согласно Теореме [](#imprtant_for_int) 3., имеем

$$
\int_I f = \alpha \cdot |I|,
$$
то и требовалось показать.

(7) Для данных $\overline{f}\in M_{p.c}(f)$, $\underline{f} \in m_{p.c}(f)$  определим $\overline{F}, \underline{F}:J \to \mathbb{R}$ следующим образом
$$
\overline{F}(x): = \begin{cases}
\overline{f}(x), & x \in I,\\
0, & x\notin I,
\end{cases} \qquad  \underline{F}(x): = \begin{cases}
\underline{f}(x), & x \in I,\\
0, & x\notin I,
\end{cases}
$$
тогда $\overline{F}\in M_{p.c}(F)$ и $\underline{F} \in m_{p.c}(F)$. Тогда для любого $\varepsilon>0$ (см. неравенства [](#non_for_Th)), пользуясь теоремой [](#imprtant_for_int) 4., получаем
$$
\sup \int_J F \le \int_J \overline{F} = \int_I \overline{F} = \int_I \overline{f}< \int_I f + \varepsilon
$$
и
$$
\inf \int_J F \ge \int_J \underline{F} = \int_I \underline{F} = \int_I \underline{f} > \int_I f -\varepsilon.
$$

Таким образом, для любого $\varepsilon>0$ мы получили
$$
\int_I f - \varepsilon < \inf \int_J F \le \sup_J F < \int_I + \varepsilon,
$$
откуда следует, что
$$
\int_J F = \int_I f.
$$

(8) Если функции $f|_A$, $f|_B$ интегрируемы по Риману, то утверждение сразу следует из (1) и (7). Действительно, рассмотрим функции 
$$
F_A(x): = \begin{cases}
f|_A(x), & x \in A,\\
0, & x \notin A
\end{cases} \qquad F_B(x) = \begin{cases}
f_B(x), & x \in B,\\
0, & x \notin B,
\end{cases}
$$
тогда $f = F_A + F_B$, и тогда согласно (1), (7) получаем
$$
\int_I f = \int_I(F_A + F_B) = \int_I F_A  + \int_I F_B = \int_A f|_A + \int_B f|_B,
$$
что и требовалось показать.

Итак, мы должны показать, что если функция $f$ интегрируема по Риману на $I$, то и функции $f|_A, f|_B$ тоже интегрируемы по Риману на $A$ и $B$, соответственно.

Выберем произвольный $\varepsilon>0$ и рассмотрим две произвольные функции $\overline{f} \in M_{p.c}(f)$, $\underline{f} \in m_{p.c}(f)$. Ясно, что $\overline{f}_A \in M_{p.c.}(f|_A)$ и $\underline{f}|_A \in m_{p.c}(\underline{f}).$ 

Имеем
$$
\int_A \underline{f}_A \le \inf \int_A f|_A \le \sup \int_A f|_A \le \int_A \underline{f}|_A.
$$
и
$$
\int_B \underline{f}_B \le \inf \int_B f|_B \le \sup \int_B f|_B \le \int_B \underline{f}|_B.
$$

Тогда воспользовавшись Теоремой [](#imprtant_for_int) 5., получаем
$$
\int_I \overline{f} = \int_A \overline{f}_A + \int_B \overline{f}_B,
$$
и
$$
\int_I \underline{f} = \int_A \underline{f}_A + \int_B \underline{f}_B.
$$

Тогда используя неравенства ([](#non_for_Th)), имеем
$$
\int_I f - \varepsilon < \left( \int_A \underline{f}|_A + \int_B \underline{f}_B \right) \le \left( \int_A \overline{f}|_A + \int_B \overline{f}_B \right) < \int_I f + \varepsilon,
$$
отсюда вытекает следующие неравенства\footnote{Действительно если мы имеем $x-\varepsilon < x \le z < x+\varepsilon$, то $0 \le z-y < x-y+\varepsilon$, но так как $x-\varepsilon <y$, то $x-y<\varepsilon$ откуда $0 \le z - y \le 2 \varepsilon.$}
$$
0 \le \left( \int_A \overline{f}|_A + \int_B \overline{f}_B \right) -  \left( \int_A \underline{f}|_A + \int_B \underline{f}_B \right) \le 2 \varepsilon,
$$
или то же самое, что и следующие неравенства
$$
0 \le \left( \int_A \overline{f}|_A - \int_A \underline{f}|_A  \right) + \left( \int_B \overline{f}_B  -\int_B \underline{f}_B \right) \le 2 \varepsilon.
$$

Так как $\overline{f}|_A \ge \underline{f}|_A$, $\overline{f}|_B \ge \underline{f}|_B$, то согласно теореме [](#imprtant_for_int) 2., получаем что обе скобки в положительны, а значит 
$$
0 \le \int_A \overline{f}|_A - \int_A \underline{f}|_A  \le 2 \varepsilon
$$
и
$$
0 \le \int_B \overline{f}_B  - \int_B \underline{f}_B \le 2 \varepsilon
$$
для любого $\varepsilon>0.$

Теперь вернёмся к неравенствам полученным выше
$$
\int_A \underline{f}_A \le \inf \int_A f|_A \le \sup \int_A f|_A \le \int_A \underline{f}|_A.
$$
и
$$
\int_B \underline{f}_B \le \inf \int_B f|_B \le \sup \int_B f|_B \le \int_B \underline{f}|_B.
$$

Получаем, что
$$
0 \le \sup \int_A f|_A - \sup \int_A f|_A \le 2\varepsilon, \qquad 0 \le \sup \int_B f|_B - \sup \int_B f|_B \le 2\varepsilon,
$$
а так как это верно для любого $\varepsilon>0$ это означает, что 
$$
\sup \int_A f|_A = \sup \int_A f|_A, \qquad \sup \int_B f|_B = \sup \int_B f|_B
$$
что и означает интегрируемость функций $f|_A$, $f|_B$ по Риману.
:::