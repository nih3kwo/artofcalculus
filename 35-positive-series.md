---

numbering:
  enumerator: 2.2.%s

---

# 2.2 Положительные ряды

(c3def16)=
Перейдём теперь к рядам с положительными элементами. Будем говорить, что ряд $(x_n)$ **положительный**, если все $x_n >0$.

Специфика таких рядов проявляется сразу же.

:::{prf:theorem} Критерий сходимости положительного ряда
:name: criteria_for_positive_series
Положительный ряд $(x_n)$ сходится тогда и только тогда, когда последовательность $(s_n)$ его частичных сумм ограничена.
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Действительно, в таком случае последовательность $(s_n)$ его частичных сумм строго возрастает, тогда если последовательность $(s_n)$ ограничена, то по [теореме Вейрштрасса](#Weierstrass) она имеет предел, т.е. ряд сходится. С другой стороны, пусть ряд сходится, тогда $\lim_{n\to \infty} s_n =s$, т.е. для любого $\varepsilon >0$ найдётся такой номер $N$, что при всех $n \ge N$, $s-\varepsilon < s_n < s+ \varepsilon$, но $(s_n)$ — возрастающая, значит все $s_i < s + \varepsilon$, т.е. последовательность $(s_n)$ ограничена.
:::

## Признаки сравнения

Из этого критерия вытекают многочисленные следствия.

:::{prf:corollary} Признак сравнения 1
:name: cor1_for_series
Пусть $(x_n)$, $(x_n')$ — два положительных ряда, при этом $x_n \le x_n'$ почти для всех $n$. Если ряд $(x_n')$ сходится, то сходится и ряд $(x_n)$. Если же ряд $(x_n)$ расходится, то расходится и ряд $(x_n').$
:::
:::{prf:proof}
:class: dropdown
:nonumber: 

Если неравенства $x_n\le x_n'$ не выпонены для каких-то конечных значений $n$, скажем, $n = n_1,\ldots, n_\ell$, то рассмотрим ряды $(y_n)$, $(y_n')$, определённые следующим образом:
$$
y_n = \begin{cases}
x_n, & n \ne n_1,\ldots, n_\ell,\\
0, & n = n_1,\ldots, n_\ell,
\end{cases} \qquad  y'_n = \begin{cases}
x'_n, & n \ne n_1,\ldots, n_\ell,\\
0, & n = n_1,\ldots, n_\ell
\end{cases} 
$$
которые почти похожи на ряды $(x_n)$ и $(x_n')$ соответственно. Согласно [](#almost_for_series), ряды $(y_n)$, $(y_n')$ имеют тот же характер сходимости, как и ряды $(x_n)$, $(x_n')$ соответственно. Поэтому исследование характера сходимости рядов $(x_n)$, $(x_n')$ сводится к исследованию характера рядов $(y_n)$, $(y_n')$. Это означает, что мы без ограничения общности можем считать, что неравенства $x_n \le x_n'$ выполняются для всех $n\ge 1.$

(1) Пусть ряд $(x_n')$ сходится, тогда по [](#criteria_for_positive_series), последовательность его частичных сумм $(s_n')$ ограничена, скажем, числом $\alpha$, т.е. $s'_n < \alpha$ для всех $n.$ С другой стороны, по условию, $x_n \le x_n'$, тогда в силу положительности рядов
$$
s_n = x_1 + \cdots + x_n \le x_1' + \cdots + x_n' = s_n' < \alpha
$$
для всех $n$, т.е. последовательность частичных сумм ряда $(x_n)$ ограничена, тогда по [](#criteria_for_positive_series), ряд $(x_n)$ сходится.

(2) Пусть ряд $(x_n)$ расходится, тогда по [](#criteria_for_positive_series), последовательность $(s_n)$ неограничена. Так как последовательность $(s_n)$ возрастает, то неограниченность означает, что для любого числа $M \in \mathbb{N}$ найдётся такой номер $n\in \mathbb{N}$, что все $s_n, s_{n+1}, \ldots > M$. С другой стороны, как мы уже видели, $s_n' \ge s_n$, таким образом, для всех $m \ge n$ получаем $s'_m \ge s_m > M$, т.е. последовательность $(s_n')$ неограничена, а тогда по [](#criteria_for_positive_series), ряд $(x_n')$ расходится.
:::

:::{prf:corollary} Признак сравнения 2
Пусть ряды $(x_n)$, $(y_n)$ положительные и, начиная с некоторого $N$, выполняются неравенства 
$$
\frac{y_{n+1}}{y_n} \le \frac{x_{n+1}}{x_n}.
$$
Тогда если ряд $(x_n)$ сходится, то ряд $(y_n)$ тоже сходится. Если же ряд $(y_n)$ расходится, то расходится и ряд $(x_n).$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $\lambda = \frac{x_N}{y_N}$, тогда, согласно [](#ariph_for_series), если ряд $(y_n)$ сходится, то сходится и ряд $(\lambda y_n)$, но $N$-ый элемент ряда $(\lambda y_n)$ есть $\lambda y_N = \frac{x_N}{y_N}y_N = x_N$. Поэтому без ограничения общности, мы можем считать, что $x_N = y_N.$ Тогда из неравенства $\frac{y_{N+1}}{y_N} \le \frac{x_{N+1}}{x_N}$ следует, что $y_{N+1} \le x_{N+1}$.

Далее, из неравенства $\frac{y_{N+2}}{y_{N+1}} \le \frac{x_{N+2}}{x_{N+1}}$ получаем $x_{N+1}y_{N+2} \le y_{N+1} x_{N+2}$, но $y_{N+1} \le x_{N+1}$ и в силу положительности всех элементов получаем 
$$
x_{N+1}y_{N+2} \le y_{N+1} x_{N+2} \le x_{N+1}x_{N+2}
$$
тогда $y_{N+2} \le x_{N+2}$, и, продолжая, мы по индукции получаем, что $y_n \le x_n$ для всех $n \le N$. Теперь, воспользовавшись признаком сравнения 1 ([](#cor1_for_series)), мы завершаем доказательство.
:::

:::{prf:corollary} Предельный признак сравнения
:name: critical_for_series
Пусть $(x_n)$, $(x_n')$ два положительных ряда, тогда если существует конечный предел
$$
\lim_{n \to \infty} \frac{x_n}{x_n'} = q, \qquad 0 < q < \infty
$$
то оба ряда сходятся или расходятся одновременно.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Согласно [определению предела последовательности](#limit_of_sequence), равенство $\lim_{n \to \infty} \frac{x_n}{x_n'} = q$ означает, что для любого $\varepsilon >0$ найдётся такой номер $N$, что верны неравенства
$$
q-\varepsilon < \frac{x_n}{x_n'} < q+ \varepsilon, \qquad n \ge N.
$$

Таким образом, почти для всех $n\ge 1$ имеем $x_n < (q+\varepsilon)x_n'$, тогда по признаку сравнения 1 ([](#cor1_for_series)), ряды $(x_n)$, $((q+\varepsilon)x_n')$ имеют одинаковый характер сходимости, а согласно [](#ariph_for_series), характер сходимости ряда $((q+\varepsilon)x_n')$ такой же, как у ряда $(x_n')$, что и завершает доказательство.
:::

## Варианты Даламбера и Коши

:::{prf:corollary} Признаки сравнения Даламбера[^footnote342]
:name: Dalamber_criteria_for_series
Пусть дан положительный ряд $(x_n)$.

1. Если
$$
\frac{x_{n+1}}{x_n} \le q <1, \qquad n \ge 0,
$$
то ряд $(x_n)$ сходится; если же
$$
\frac{x_{n+1}}{x_n} \ge 1, \qquad n \ge 0,
$$
то ряд $(x_n)$ расходится.

2. Если 
$$
\lim_{n \to \infty} \frac{x_{n+1}}{x_n} = q
$$
то ряд $(x_n)$ при $q<1$ сходится, а при $1 < q \le \infty$ расходится.

:::

:::{prf:proof}
:class: dropdown
:nonumber: 
Мы воспользуемся [](#almost_for_series) в случае необходимости и тогда можем считать, что неравенства выполнены для всех $n \ge 0.$

(1) Имеем для каждого $n \ge 2$
$$
x_n = x_1 \cdot \frac{x_2}{x_1}\cdot \frac{x_3}{x_2} \cdots \frac{x_{n-1}}{x_{n-2}}\cdot \frac{x_n}{x_{n-1}},
$$
по условию
$$
\frac{x_2}{x_1}, \frac{x_3}{x_2}, \ldots, \frac{x_n}{x_{n-1}} \le q < 1,
$$
тогда
$$
x_n = x_1 \cdot \frac{x_2}{x_1}\cdot \frac{x_3}{x_2} \cdots \frac{x_{n-1}}{x_{n-2}}\cdot \frac{x_n}{x_{n-1}} \le x_1 q^{n-1}.
$$

С другой стороны, (см. [](#geometric_series_and_ML_series)) ряд $(q^n)$ сходится при $q<1$, а тогда по предложению [](#ariph_for_series) ряд $(x_1q^n)$ тоже сходится. Наконец, по признаку 1 ([](#cor1_for_series)) ряд $(x_n)$ сходится.

(2) Если же 
$$
\frac{x_2}{x_1}, \frac{x_3}{x_2}, \ldots, \frac{x_n}{x_{n-1}} > 1,
$$
то
$$
x_n \ge x_1, \qquad n \ge 2.
$$

Ряд $(y_n)$, где все $y_n = x_1$, очевидно, расходится, тогда по признаку 1 ([](#cor1_for_series)), ряд $(x_n)$ тоже расходится.

(3) Пусть $\lim_{n \to \infty} \frac{x_{n+1}}{x_n}= q$, тогда по [](#limit_of_sequence) для любого $\varepsilon >0$ существует такой $N$, что для всех $n \ge N$ имеют место неравенства
$$
q - \varepsilon < \frac{x_{n+1}}{x_n} < q + \varepsilon.
$$

Если $q<1$, то пусть $q+\varepsilon <1$, тогда для всех $n \ge N$, $\frac{x_{n+1}}{x_n} < 1$, тогда по доказанному признаку (1) ряд $(x_n)$ сходится.

Если $q>1$, то возьмём $\varepsilon >0$ такое, что $q-\varepsilon >1$. Но
$$
\frac{x_{n+1}}{x_n} > q - \varepsilon
$$
при каких-то $n \ge N$, поэтому для $N\le n_0 < n$ получаем
$$
x_n=  \frac{x_n}{x_{n-1}} \cdot \frac{x_{n-1}}{x_{n-2}} \cdots \frac{x_{n_0 +1}}{x_{n_0}} x_{n_0} > (q-\varepsilon)^{n-n_0} x_{n_0},
$$
а так как $q - \varepsilon >1$ и (см. [](#geometric_series_and_ML_series)) ряд $(q-\varepsilon)^{n}$ расходится, то по [](#ariph_for_series) получаем, что ряд $(x_n)$ расходится.

Тем самым признаки Даламбера полностью доказаны.
:::


:::{prf:theorem} Радикальный признак Коши
Пусть $(x_n)$ — положительный ряд. 

1. Если для почти всех $n \ge 1$
$$
\sqrt[n]{x_n} < q < 1,
$$
то ряд $(x_n)$ сходится.

2. Если для почти всех $n \ge 1$
$$
\sqrt[n]{x_n} \ge 1
$$
то ряд $(x_n)$ расходится.

3. Если
$$
\lim_{n\to \infty } \sqrt[n]{x_n} = q,
$$
то при $q<1$ ряд $(x_n)$ сходится, а при $q>1$ расходится, и при этом $\lim_{n \to \infty} x_n = \infty.$

:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пользуясь [](#almost_for_series), мы можем считать, что неравенства выполнены для всех $n \ge 1.$

(1) Если $\sqrt[n]{x_n}<q$, то $x_n <q^n$, а так как $q<1$, то согласно [](#geometric_series_and_ML_series) и [признаку сравнения](#cor1_for_series) получаем, что ряд $(x_n)$ сходится. 

(2) Если $\sqrt[n]{x_n}\ge 1$, то $x_n \ge 1$, но ряд $(n)$ расходится, а тогда согласно [признаку сравнения](#cor1_for_series) ряд $(x_n)$ расходится.

(3) Пусть $q<1$. Возьмём такой $\varepsilon>0$, чтобы $q<q+\varepsilon <1$. Тогда по [определению предела](#limit_of_sequence) найдётся такой $N$, что при всех $n \ge N$ мы получаем
$$
\sqrt[n]{x_n} < q+\varepsilon <1,
$$
тогда $x_n < (q+\varepsilon)^n$ почти для всех $n$, а так как (см. [](#geometric_series_and_ML_series)) ряд $((q+\varepsilon)^n)$ сходится при $q+\varepsilon<1$, то согласно [признаку сравнения](#cor1_for_series) ряд $(x_n)$ сходится.

Пусть теперь $q>1$, то выберем такое $\varepsilon>0$, чтобы $q-\varepsilon >1$, тогда получаем, что $\sqrt[n]{x_n} > q-\varepsilon >1$, начиная с какого-то $n$, **т.е.** $x_n > (q-\varepsilon)^n$ почти для всех $n\ge 1$, но (см. [](#geometric_series_and_ML_series)) ряд $((q-\varepsilon)^n)$ расходится при $q-\varepsilon>1$, то согласно [признаку сравнения](#cor1_for_series), ряд $(x_n)$ расходится.

Тем самым радикальный признак Коши полностью доказан.
:::

:::{prf:remark}
Для положительного ряда $(x_n)$ выражения 
$$
\mathscr{D}_n: = \frac{x_{n+1}}{x_n}, \qquad \mathscr{C}_n: = \sqrt[n]{x_n},
$$
называют **вариантой Даламбера** и **вариантой Коши**, соответственно.
:::

:::{warning}
В предыдущих двух признаках (Даламбера и Коши) не рассматривался случай, когда обе варианты равны $1$, оказывается, в этом случае эти признаки не работают! Сейчас мы приведём пример.
:::

:::{prf:example}
**Рядом Дирихле** называют ряд вида $\left( \frac{1}{n^\alpha} \right)$, где $\alpha \in \mathbb{R}_+$. Позже мы докажем, что этот ряд сходится при $\alpha >1$ и расходится при $\alpha \le 1$. При этом, в обоих случаях (когда $\alpha >1$ или когда $\alpha <1$) имеем
$$
\lim_{n\to \infty} \mathscr{D}_n = \lim_{n \to \infty} \frac{x_{n+1}}{x_n} = \lim_{n\to \infty} \left(\frac{n}{n+1} \right)^\alpha  = \left( \lim_{n \to \infty} \frac{n}{n+1} \right)^\alpha =1,
$$
так же, как (см. [](#sqrtnn1))
$$
\lim_{n\to \infty} \mathscr{C}_n =  \lim_{n\to \infty} \sqrt[n]{x_n} = \lim_{n \to \infty}\sqrt[n]{\frac{1}{n^\alpha}} = \left( \frac{1}{\lim\limits_{n\to \infty}\sqrt[n]{n}}\right)^\alpha =1.
$$

Таким образом, существуют как сходящиеся, так и расходящиеся ряды, для которых верны равенства $\lim_{n\to \infty}\mathscr{D}_n= 1$, $\lim_{n \to \infty}\mathscr{C}_n = 1.$
:::

## Инвариантность суммы

Докажем инвариантность суммы сходящегося положительного ряда при произвольной перестановке его элементов.

:::{prf:theorem}
:name: comm_for_positive_series
Пусть $(x_n)$ — сходящийся положительный ряд с суммой $\mathsf{S}$. Тогда полученный в результате произвольной перестановки его элементов новый (заново перенумерованный) ряд также сходится и имеет ту же сумму $\mathsf{S}.$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $x_1' = x_{n_1}, \ldots, x_k' = x_{n_k}, \ldots,$ и пусть $n: = \max \{n_1,\ldots, n_k\}$, рассмотрим тогда частичные суммы
$$
\mathsf{S}_n: = x_1 + \cdots + x_n, \qquad \mathsf{S}'_k: = x_1' + \cdots + x_k',
$$
так как $1\le n_1, \ldots, n_k \le n$ и $(x_n)$ — положительный ряд, то
$$
\mathsf{S}_k' \le \mathsf{S}_n.
$$

Но, положительный ряд $(x_n)$ сходится, а тогда по [критерию сходимости положительного ряда](#criteria_for_positive_series), последовательность $(\mathsf{S}_n)$ ограничена, и более того $\mathsf{S}_n \le \mathsf{S}$ для всех $n$. Таким образом, для всех $k$ получаем
$$
\mathsf{S}_k' \le \mathsf{S}_n \le \mathsf{S},
$$
**т.е.** последовательность $(\mathsf{S}_k')$ частичных сумм ряда $(x_k')$ ограничена, а тогда по [критерию сходимости положительного ряда](#criteria_for_positive_series), ряд $(x_k')$ — сходится, **т.е.** существует предел $\lim_{k \to \infty} \mathsf{S}_k' = \mathsf{S}'$. Тогда по Лемме [](#aleb), $\mathsf{S}' \le \mathsf{S}.$

Рассмотрим теперь ряд $(x_k')$, тогда на ряд $(x_n)$ можно посмотреть как на ряд который получился из ряда $(x_k')$ в результате какой то перестановки элементов $x_k'$. Тогда, рассуждая аналогичным образом, мы приходим к выводу, что 
$\mathsf{S}_m \le \mathsf{S}_k'$, и по [](#aleb), получаем $\mathsf{S} \le \mathsf{S}'$.

Наконец, из полученных неравенств $\mathsf{S}' \le \mathsf{S}$, $\mathsf{S} \le \mathsf{S}'$ вытекает, что $\mathsf{S} = \mathsf{S}'$. Это завершает доказательство теоремы.
:::

[^footnote342]: Оригинальное написание: *Признак **д'Аламбера***.