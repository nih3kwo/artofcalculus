---
authors:
  - name: Alyona Zarodnyuk
    affiliations:
      - Higher School of Economics
numbering:
  enumerator: 8.%s
---

# Функциональные последовательности

> Лекция 8, 05.11.2024

```{prf:example}
$$\{f_n(x)\}^\infty_{n=1}=\frac{x}{n},\quad x\in\RR$$
```

```{prf:definition}
:name: fs_convergence_at_point
$f_n\colon X\subset\RR\to\RR$

Будем говорить, что последовательность функций $\{f_n(x)\}^\infty_{n=1}$ **сходится в точке $x_0\in X$**, если сходится числовая последовательность $\{f_n(x_0)\}^\infty_{n=1}$, т. е. 

$$\exists a_{x_0}\in\RR,\forall\ve>0,\exists N,\forall n>N,|f_n(x_0)-a_{x_0}|<\ve$$
```

```{prf:definition}
:name: fs_convergence_set
$f_n\colon X\mapsto\RR$

Множество $D\subset X\subset\RR$ точек, в которых последовательность функций $\{f_n(x)\}^\infty_{n=1}$ сходится, будем называть **множеством сходимости последовательностей функций.**
```

```{prf:definition}
:name: fs_limit_function
$f_n\colon X\subset \RR\mapsto\RR$

$D\subset X$ — множество сходящихся $\{f_n(x)\}$ и пусть $\forall x\in D,f_n(x)\to f(x)$ при $n\to\infty$, тогда $f(x)=\lim_{n\to\infty}f_n(x)$ будем называть **предельной функцией** последовательности функций $\{f_n(x)\}$
```


```{prf:definition}
:name: fs_pointwise_convergence
$D\subset\RR$ — множество

$f,f_n\colon D\to\RR$$

Будем говорить, что $\{f_n(x)\}$ **сходится поточечно** к $f(x)$ на $D$, если 

$$\forall x\in D,\forall\ve>0,\exists N,\forall n>N, |f_n(x)-f(x)|<\ve$$

т. е. $\forall x\in D$, $f_n(x)\to f(x)$ при $n\to\infty$

**Обозначение:** $f_n(x)\xrightarrow{x} f$

Иначе: $f_n(x)$ сходится поточечно к своей предельной функции на области сходимости.
```

```{prf:example}
1. $f_n(x)=\frac{x}{n}, D=\RR$

    $\forall x_0\colon f_n(x_0)=\frac{x_0}{n}\to 0$ при $n\to\infty\implies f_n(x)\xrightarrow{\RR}0$.

2. $f_n(x)=x^n, X=[0,+\infty)$

    $D=[0, 1]$ — множество сходимости $f_n(x)$.

    $$\begin{align*}
    &f_n(x)\xrightarrow{[0,1)} \text{при}\ n\to\infty\\
    &f_n(x)\xrightarrow{\{1\}} 1
    \end{align*}\implies f(x)=\begin{cases}
        0, & x\in[0,1)\\
        1, & x=1
    \end{cases}$$

:::{seealso} Замечание
$\forall n, f_n(x)$ — непрерывная функция на $D$, но $f(x)$ не является непрерывной на $D$.
:::

3. $f_n(x)=\frac{\sin(n^2 x)}{n}$ на $\RR$

    $\forall x_0\in\RR,f_n(x_0)\to 0$ при $n\to\infty$, $f_n(x)\xrightarrow{\RR}0$
    
    $f_n'(x)=n\cos(n^2x)\not\to$ на $\RR$ на $f'(x)=0$.

:::{seealso}
Производные допредельных функций не сходятся, но $f'(x)=0$.
:::

4. $f_n(x)=2(n+1)x(\underbrace{1-x^2}_{\leq 1})^n$ на $[0,1]$

    $f_n(0)=0$, $f_n(1)=0$

    $f_n(x)=2\cdot\text{const}\cdot\boxed{(n+1)\cdot q^n}\to 0$ при $n\to\infty$, т. е. $f_n(x)\xrightarrow{[0,1]}0$ 

    Рассмотрим

    $$\int\limits^1_0f(x)\d x=0,\quad\int\limits^1_0f_n(x)\d x=-\frac{2(n+1)}{2}\int\limits^1_0(1-x^2)^n\d (x^2+1)=-(1-x^2)^{n+1}\biggm|^1_0=1$$

:::{seealso}
Интеграл предельных функций $\neq$ интеграл допредельных.
:::
```

:::{seealso} Вопрос
Если ли какие-то условия, в которых можно было бы пользоваться предельными переходами не только для функций, но их производных и интегралов?

Для этого понадобится понятие равномерной сходимости.
:::

```{prf:definition}
:name: fs_uniform_convergence
$D\subset\RR$, $f_n,f\colon D\to\RR$
Будем говорить, что последовательность функций $\{f_1(x)\}$ сходится равномерно к функции $f(x)$ на $D$, если 

$$\forall\ve>0,\exist N, \forall n>N,\forall x\in D\hookrightarrow |f_n(x)-f(x)|<\ve$$

Обозначение: $f_n\overset{D}{\rightrightarrows} f$ 
```

```{prf:example}
1. $f_n(x)=\frac{x}{n}$ сходится равномерно на любом конечном отрезке в $\RR$.
2. $f_n(x)=x^n$ сходится равномерно на $\forall [0, a]$, где $0<a<1$.
3. $f_n(x)=\frac{\sin(n^2-x)}{n}$ на $\RR$ сходится равномерно.

    $\forall\ve>0,\exists N,\forall n>N,\forall x\in\RR\hookrightarrow|f_n(x)-f(x)|\leq\frac{1}{n}<\ve$
```

```{seealso} Замечание
$f_n\overset{D}{\rightrightarrows}f\implies f_n\xrightarrow{D}f$
```

```{prf:theorem} $\lim-\sup$ критерий (супремальный)
:name: supremal-criterion
$$f_n\overset{D}{\rightrightarrows}f\lim_{n\to\infty}\sup_D|f_n(x)-f(x)|=0$$
```

```{prf:proof}
:nonumber:

$(\Rightarrow)$ **Необходимость.**

$f_n\overset{D}{\rightrightarrows}f$, т. е. $\forall\ve>0,\exists N,\forall n>N,\forall x\in D, |f_n(x)-f(x)|<\frac{\ve}{2}$

так как выполняется $\forall x\in D$, то верно, что в худшем случае

$$\sup_D|f_n(x)-f(x)|\leq\frac{\ve}{2}<\ve$$

т. е. $\forall\ve>0,\exists N, \forall n>N,\sup_D|f_n(x)-f(x)|<\ve$

$(\Leftarrow)$ ***Достаточность.*

$\lim_{n\to\infty}\sup_D|f_n(x)-f(x)|=0\implies$ по определению $\lim\colon\forall\ve>0,\exists N,\forall n>N\hookrightarrow\sup_D|f_n(x)-f(x)|<\ve$, но знаем, что $|f_n(x)-f(x)|\leq\sup_D|f_n(x)-f(x)|\implies$ выполнено $\forall \ve>0,\exists N,\forall n>N,\forall x\in D\hookrightarrow|f_n(x)-f(x)|<\ve\implies f_n(x)\overset{D}\rightrightarrows f(x)$.
```