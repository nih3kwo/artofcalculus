---
authors:
  - name: Alyona Zarodnyuk
    affiliations:
      - Higher School of Economics
numbering:
  enumerator: 2.%s
---

# Свойства кратных интегралов. Условия интегрирования

> Лекция 2, 17.09.2024

## Свойства кратного интеграла

### Линейность

```{prf:proposition} Линейность
:name: linearity
$$f,g\in\mathcal{R}(I)\implies\forall\alpha,\beta\in\mathbb{R}, (\alpha f+\beta g)\in\mathcal{R}(I)$$

$$\int\limits_I(\alpha f+\beta g)\d x=\alpha\int\limits_I f\d x+\beta\int\limits_I g\d x$$
```

```{prf:proof}
:nonumber:
$$\begin{align*}f\in\mathcal{R}(I)\implies\forall\varepsilon>0,\exists\delta_1>0,\forall(\mathbb{T},\xi)\colon\Delta_{\T}<\delta_1,&\\\left|\sigma(f,\mathbb{T},\xi)-\int\limits_If\d x\right|<\frac{\varepsilon}{{1+|\alpha|+|\beta|}}&\end{align*}$$
$$\begin{align*}g\in\mathcal{R}(I)\implies\forall\varepsilon>0,\exists\delta_2>0,\forall(\mathbb{T},\xi)\colon\Delta_{\T}<\delta_2,&\\\left|\sigma(g,\mathbb{T},\xi)-\int\limits_If\d x\right|<\frac{\varepsilon}{1+|\alpha|+|\beta|}&\end{align*}$$

Пусть тогда $\delta=\min\{\delta_1,\delta_2\} \implies$

$$\forall\ve>0,\exist\delta,\forall(\T,\xi)\colon\Delta_\T<\delta$$

$$|\sigma_f-A_f|<\frac{\ve}{1+|\alpha|+|\beta|},\qquad |\sigma_g-A_g|<\frac{\ve}{1+|\alpha|+|\beta|}$$

тогда рассмотрим

$$|\sigma_{\alpha f+\beta g}-A_{\alpha f+\beta g}|\leq|\alpha|\cdot|\sigma_f-A_f|+|\beta|\cdot|\sigma_g-A_g|<(|\alpha|+|\beta|)\cdot\frac{\ve}{1+|\alpha|+|\beta|}<\ve$$
```

### Монотонность

```{prf:proposition} Монотонность
:label: monotonicity
$$\begin{align*}
f, g\in\mathcal{R}(I)\\
f \leq g \text{ на } I
\end{align*}\implies\int\limits_If\d x\leq\int\limits_Ig\d x$$
```

```{prf:proof}
$$\forall\ve>0,\exists\delta>0\colon\forall(\T,\xi)\colon\Delta_\T<\delta\colon\begin{align*}&\left|\int\limits_If\d x-\sigma_f\right|<\ve\\&\left|\int\limits_Ig\d x-\sigma_g\,\right|<\ve\end{align*}$$

$$\begin{align*}&\int\limits_I f\d x-\ve<\sigma_f\leq\sigma_g<\int\limits_Ig\d x+\ve\\&\implies\int\limits_If\d x<\int\limits_I g\d x+2\ve\end{align*}$$

т. к. неравенство должно быть верно $\forall\ve>0$ даже для $\ve\ll 1$, то 

$$\int\limits_If\d x\leq\int\limits_Ig\d x$$
```

### Оценка интеграла (сверху)

```{prf:proposition} Оценка интеграла (сверху)
:name: integral_upper_bound
$$f\in\mathcal{R}(I)\implies\left|\int\limits_If\d x\right|\leq\sup_I|f|\cdot|I|$$
```

```{prf:proof}
$f\in\mathcal{R}(I)\implies f$ — ограничена на $I$ [по необходимому условию](#required_condition_integral) $\implies$

$$-\sup_I|f|\leq f\leq\sup_I|f|$$

по [монотонности](#monotonicity)

$$-\sup_I|f|\cdot|I|\leq\int\limits_If\d x\leq\sup_I|f|\cdot|I|$$
```

## Необходимое условие интегрируемости

```{prf:theorem} Необходимое условие интегрируемости
:label: required_condition_integral
$I$ — замкнутый брус

$f\in\mathcal{R}(I)\implies f$ — ограничена на $I$.
```

```{prf:proof}
:nonumber:


(hashRCI-1)=
1. (от противного) Пусть $f$ неограничена на $I\implies\forall$ разбиения $\T=\{I_i\}^k_{i=1}$ бруса $I$, $\exists i_0\colon f$ неограничена на $I_{i_0}$.

---

(hashRCI-2)=
2. $f\in\mathcal{R}(I)\implies\forall\ve>0$, а значит и для $\ve=1,\exists\delta>0\colon\forall(\T,\xi)\colon\Delta_\T<\delta$ верно 

$$\left|\sigma(f,\T,\xi)-\overbrace{\int\limits_Tf(x)\d x}^A\right|< 1$$

где  $\displaystyle\exists A=\int\limits_If(x)\d x$ — конечный $\implies$

$$\overbrace{\int\limits_If(x)\d x}^A-1<\sigma(f,\T,\xi)<\overbrace{\int\limits_If(x)\d x}^A + 1\implies$$

$\sigma(f,\T,\xi)$ — ограничена

Однако с другой стороны по [пункту 1](#hashRCI-1) $\implies$ 

$$\sigma(f,\T,\xi)=\sum_{i\neq i_0}f(\xi_i)|I_i|+f(\xi_{i_0})|I_{i_0}|$$

т. к. на $I_{i_0} f(x)$ — неограниченная $\implies$ выбором подходящего $\xi_{i_0}$ можно сделать $f(\xi_{i_0})|I_{i_0}$ вместе с $\sigma(f, \T, \xi)$ сколь угодно большой $\implies$ [(1)](#hashRCI-1) и [(2)](#hashRCI-2) противоречат $\implies f$ — ограничена на $I$. 
```


## Мера по Лебегу

```{prf:definition}
:name: null_measure
Множество $M\subset \R^n$ будет называть множеством **меры нуль по Лебегу**, если $\forall \ve>0,\exists$ не более, чем счётный набор замкнутых брусков 

$$\{I_i\}\colon M\subset\bigcup_i I_i$$

и 

$$\sum_i|I_i|<\ve$$
```

```{prf:example}
$a\in\RR^n$ — множество меры нуль по Лебегу.
```

```{prf:proof}
:nonumber:

Пусть $\m{a}=\{a_1,\ldots,a_n\}\in\RR^n$.

$$\forall\ve>0,\exists I=[a_1-d,a_1+d]\times\ldots\times[a_n-d,a_n+d],\quad \m{a}\in I$$

$|I|=(2d)^n<\ve$, если $d<\frac{\sqrt[n]{\ve}}{2}$

Возьмём $d=\frac{1}{3}\sqrt[n]{\ve}, \forall \ve >0\implies|I| = (\frac{2}{3}\sqrt[n]{\ve})^2$
```

## Свойства множества меры нуль по Лебегу

```{prf:proposition} Корректность определения
:name: null-measure-property-1
1. Если $\{I_i\}$ — открытые бруски, то определение остаётся корректным.
```

```{prf:proof} 
:nonumber: 
Докажем в обе стороны:
1. открытые $\implies$ замкнутые
    Пусть $\{I_i\}$ в определении открыты, т. е. $\forall\ve>0,\exists$ не более, чем счётное $\{I_i\}\colon$
    $$M\subset \bigcup_iI_i,\quad \sum_i|I_i|<\ve$$
    Замкнём каждый из $I_i$ и получим $\overline{I_i}$, тогда $|I_i|=|\overline{I_i}|$, тогда $$M\subset\bigcup_i\overline{I_i},\quad \sum_i|\overline{I_i}|<\ve$$
2. замкнутые $\implies$ открытые
    * Пусть $\{I_i\}=\{[a_1^i,b_1^i]\times\ldots\times[a_n^i,b_n^i]\}$ — замкнутые брусы и $M\subset\bigcup_i I_i$
    * Увеличим $I_i$ до $\tilde I_i=\left[\frac{a_1^i+a_1^i}{2}-(b_1^i-a_1^i),\frac{a_1^i+b_1^i}{2}+(b_1^i-a_1^i)\right]\times\ldots$, т. е. каждую сторону $I_i$ увеличиваем в два раза, тогда если 

    $$\underbrace{\sum_{i=1}|I_i|}_{V_1}<\frac{\ve}{2^n}$$

    то

    $$\underbrace{\sum|\tilde I_i|}_{V_2=2^nV_1<\ve}<\ve$$
```

```{prf:proposition}
$M$ — множество меры нуль, $L\subset M$ — подмножество $M\implies L$ — множество меры нуль.
```

```{prf:proof}
:nonumber:
$L\subset M$ и $\forall\ve>0,\exists$ не более, чем счётное 

$$\{I_i\}\colon L\subset M\subset\bigcup_iI_i, \quad \sum|I_i|<\ve$$

по транзитивности это верно и для $L$.
```

```{prf:proposition}
Не более, чем счётное объединение множеств меры нуль — множество меры нуль.
```

```{prf:proof}
Пусть $\{M_k\}_{k=1}^\infty$ — счётное (для конечного ещё проще), т. е. $\forall i, M_k$ — множество меры нуль, то $\forall i,\exists$ не более, чем счётное $\{I^k_i\}\colon$

$$M_k\subset\bigcup_i^k,\quad \sum|I_i^k|<\ve_k=\frac{\ve}{2^k},\forall \ve_k>0$$ 

Рассмотрим $\displaystyle M=\bigcup^\infty_{k=1}M_k$, тогда 

$$M\subset\bigcup_{i,k}I_i^k,\quad \sum_{i,k}|I^k_i|<\sum^\infty_{k=1}\ve_k=\sum^\infty_{k=1}\frac{\ve}{2^k}=\ve\cdot\frac{1}{2}\cdot\frac{1}{\frac{1}{2}}=\ve$$
```

(null-measure-property-2)=
2. $M$ — множество меры нуль по лебегу, $L\subset M$ — подмножество $M\implies$ $L$ — множество меры нуль по Лебегу.

```{prf:proof}
$M$ — множество меры нуль

$\forall\varepsilon >0,\exists$ не более чем счётное $\{I_i\}$: $L\subset M\subset \bigcup I_i, \quad |\sum|I_i|<\varepsilon|$
```

(null-measure-property-3)=
3. Не более чем счётное объединение множеств меры нуль по Лебегу является множеством меры нуль.

```{prf:proof}
$\{M_i\}$ — не более чем счётный набор, где $\forall i, M_i$ — множество меры нуль. $\implies \forall i, \forall \varepsilon_i,\exists $ не более чем счётное $\{I_j^i\}$ брусов (замкнутых или открытых).

$M_i\subset U_jI^i_j$ и $\sum_j|I_j^i|<\varepsilon_i, \varepsilon_i=\frac{\varepsilon}{2^i}$

тогда $M=\bigcup M_i$ и $M\bigcup_{i,j}I^0_j$. Мы хотим, чтобы $\forall \varepsilon>0$

$$\sum_{i, j}|I^i_j|=\sum_i\left(\sum_о|I_j^i|\right)<\sum_i\varepsilon_i=\sum_i\frac{\varepsilon}{2^i}=\varepsilon\frac{1}{2}\frac{1}{1-\frac{1}{2}}=\varepsilon$

случай $\{M_i\}^N_{i=1}$ — конечный набор

$$\varepsilon_1+\dots+\varepsilon_N=\frac{N}{N+1}\varepsilon<\varepsilon$$

$$\varepsilon_i=\frac{\varepsilon}{N+1}$$
```
