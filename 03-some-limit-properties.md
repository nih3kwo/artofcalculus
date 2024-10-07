# Некоторые свойства пределов

## Арифметика предела

:::{prf:theorem} Арифметика предела
:name: a+b,ca,ab
Пусть $(a_n), (b_n)$ — две последовательности, причём $\lim_{n\to \infty} a_n =a$ и $\lim_{n\to \infty}b_n =b$. Тогда:
* $\lim_{n\to \infty}(a_n + c) = a+c$ и $\lim_{n\to \infty}(ca_n) = ca$ для любого числа $c\in \mathbb{R};$
* $\lim_{n\to \infty}(a_n +b_n) = a+b;$
* $\lim_{n\to \infty}(a_nb_n) = ab;$
* если $a\ne 0$ и $a_n \ne 0$ для всех $n\in \mathbb{N}$, то $\lim_{n\to \infty}\frac{1}{a_n} = \frac{1}{a}.$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
(1) Пусть $a_n':=a_n+c$, $n\in \mathbb{N}$. По определению получаем, что для любого $\varepsilon > 0$ найдётся такой $N$, что $|a_n - a| < \varepsilon$. Имеем $|a_n -a| = |a_n+c - a - c| = |a_n' - (a+c)|$, то есть для того же $N$ мы получаем, что при $n>N$, $|a_n' - (a+c)| < \varepsilon$, что и доказывает, что $\lim_{n\to \infty}(a_n + c) = a+c$.

Пусть теперь $a'_n: = ca_n$, $n\in \mathbb{N}$. Ясно, что если $c =0$, то мы получаем постоянную последовательность $\{0,0,...\ldots,\}$ и мы уже знаем, что она сходится к $0.$ Пусть $c \ne 0.$ Так как $\lim_{n\to \infty}a_n = a$, то для любого $\varepsilon>0$ есть такой номер $N$, что $|a_n - a|<\varepsilon$ для всех $n>N$. Значит, если мы рассмотрим $\varepsilon':=\frac{\varepsilon}{|c|}$, то и для такого $\varepsilon'$ мы тоже знаем такой номер $N'$, что $|a_n - a|< \varepsilon'$. Умножив обе части этого неравенства на $|c|$, мы получаем $|c||a_n - a| <|c|\varepsilon'$, что равносильно неравенству $|a_n' - ca| < \varepsilon$, что и доказывает требуемое.

(2) Возьмём какое-нибудь число $\varepsilon>0$ и положим $\varepsilon':= \frac{\varepsilon}{2}$, тогда, согласно определению предела, у нас есть номера $N,M$ такие, что неравенства $|a_n - a|< \varepsilon'$ и $|b_m - b|<\varepsilon'$ выполнены для всех $n>N$, $m>M$. Пусть $K:=\max{N,M}$, $k>K$.

Имеем
$$
 |(a_k + b_k) - (a+b)| = |(a_k-a) + (b_k-b)|\le |a_k-a| + |b_k-b| < \varepsilon' + \varepsilon' = \varepsilon,
$$
что и означает, что для любого $\varepsilon>0$ мы нашли номер $K$ такой, что для всех $k>K$ имеет место неравенство $|(a_k + b_k) - (a+b)|< \varepsilon$, что и доказывает требуемое.

(3) Заметим, что 
$$
a_nb_n - ab = (a_n-a)(b_n-b) + a(b_n -b) + b(a_n -a).
$$

Докажем, что $\lim_{n\to \infty}(a_nb_n - ab) = 0$, тогда по [](#lim(a_n-a)=0) будет следовать требуемое.

Согласно только что доказанным пунктам, имеем
$$\begin{align*}
 \lim_{n\to \infty}(a_nb_n - ab) &=& \lim_{n\to \infty}\Bigl( (a_n-a)(b_n-b) + a(b_n -b) + b(a_n -a) \Bigr) \\
&=& \lim_{n\to \infty} (a_n-a)(b_n-b) + a \lim_{n\to \infty}(b_n -b) + b \lim_{n\to \infty}(a_n -a),
\end{align*}$$
по [](#lim(a_n-a)=0), $\lim_{n\to \infty}(b_n -b) =0$, $\lim_{n\to \infty}(a_n -a)=0$, значит, $\lim_{n\to \infty}(a_nb_n - ab) = \lim_{n \to \infty}(a_n-a)(b_n-b).$ Покажем, что этот предел равен нулю. Так как $\lim_{n\to \infty} a_n =a$ и $\lim_{n\to \infty}b_n =b$, то для любого $\varepsilon>0$, есть номера $N,M$ такие, что $|a_n - a| <\varepsilon$ и $|b_m -b| < \varepsilon$ для всех $n >N$, $m>M$. Пусть теперь $\varepsilon':=\sqrt{\varepsilon},$ тогда и для такого числа мы тоже знаем номера $N',M'$ такие, что $|a_n - a| <\varepsilon'$ и $|b_m -b| < \varepsilon'$ для всех $n >N'$, $m>M'$. Пусть $K:= \max{N',M'}$, тогда для $k>K$ мы получаем
$$
 |(a_k-a)(b_k-b)| = |a_k -a||b_k - b| < \varepsilon' \cdot \varepsilon' = \varepsilon, 
$$
что и доказывает бесконечную малость последовательности $(a_n-a)(b_n-b)$, т. е. $\lim_{n \to \infty}(a_n-a)(b_n-b) = 0$ и значит, $\lim_{n\to \infty}(a_nb_n - ab) = 0 \Longleftrightarrow \lim_{n\to \infty}a_nb_n = ab.$

(4) Достаточно доказать, что $\lim_{n \to \infty} \frac{1}{b_n} = \frac{1}{b}$. Тогда из предыдущего пункта будет следовать требуемое. Далее без ограничения общности будем считать, что $b>0$, так как в случае $b<0$ мы умножим последовательность $(b_n)$ на $-1$ и по пункту (1) сведём задачу к той, когда $b>0.$

Так как $\lim_{n\to \infty} b_n =b>0$, то по [](#separate) найдётся такой $N_0$, что для всех $n>N_0$ будет иметь место неравенство $b_n > \frac{b}{2}>0$. 

Далее, так как $\lim_{n\to \infty} b_n =b$, то по определению предела для любого $\varepsilon>0$ найдётся такой номер $N$, что для всех $n>N$ выполнено $|b_n - b|<\varepsilon.$

Пусть $M: = \max{N_0, N}$, тогда для любого $m>M$, получаем
$$
\left| \frac{1}{b_m} - \frac{1}{b} \right| = \frac{|b_m-b|}{b_mb},
$$
так как $b_n >\frac{b}{2}$ для всех $n>N_0$, то $\frac{1}{b_m} < \frac{2}{b}$ для всех $m >M$, и тогда мы получаем 
$$
\left| \frac{1}{b_m} - \frac{1}{b} \right| = \frac{|b_m-b|}{b_mb} \le \frac{|b_m-b|}{\frac{b^2}{2}} < \frac{2\varepsilon}{b^2},
$$
что и доказывает требуемое.
:::
:::{prf:proposition}
Пусть дана последовательность $(a_n)$ такая что $a_n \ge 0$, $n\ge 1$ и $\lim_{n \to \infty} a_n = a$, $a \ge 0$. Тогда $\lim_{n \to \infty}\sqrt{a_n} = \sqrt{a}.$    
:::
:::{prf:proof}
:class: dropdown
:nonumber:
(1) Пусть $\lim_{n \to \infty}a_n = 1$, тогда для любого $\varepsilon>0$ можно найти такой $N$, что $1 - \varepsilon <a_n<1 + \varepsilon$ для всех $n >N$. Тогда, если $\varepsilon<1$, то получаем $\sqrt{1-\varepsilon} < \sqrt{a_n} <\sqrt{1+\varepsilon}$. Далее, так как $\sqrt{1+\varepsilon} < 1 + \varepsilon$, и $1-\varepsilon < \sqrt{1-\varepsilon}$ при любом $0 <\varepsilon<1$ то мы получаем
$$
1 -\varepsilon < \sqrt{1-\varepsilon} < \sqrt{a_n} < \sqrt{1+\varepsilon} < 1 + \varepsilon
$$
для всех $n > N$ что влечёт $\lim_{n \to \infty}\sqrt{a_n} =1$. 

Пусть $\varepsilon >1$, тогда мы получаем что $1 - \varepsilon <0$ и $0 < a_n  < 1 +\varepsilon$ для всех $n >N$, но также мы получаем что и $0 < \sqrt{a_n} < 1 + \varepsilon$, что также можно записать так $1- \varepsilon < \sqrt{a_n} < 1 + \varepsilon$.

Итак, мы показали, что если $\lim_{n \to \infty}a_n = 1$ то и $\lim_{n \to \infty}\sqrt{a_n} = 1.$

(2) Пусть $\lim_{n \to \infty}a_n = a \ne 1,0.$ Тогда $\lim_{n \to \infty} \frac{a_n}{a} = 1$, и тогда $\lim_{n \to \infty}\sqrt{\frac{a_n}{a}} = 1$. Умножая на $\sqrt{a}$ обе части и воспользовавшись арифметикой предела, получаем $\sqrt{a} \lim_{n \to \infty}\sqrt{\frac{a_n}{a}} = \lim_{n \to \infty}\sqrt{a_n} = \sqrt{a}$.

(3) пусть $a = 0$, тогда для любого $\varepsilon>0$ можно найти такой $N$, что $-\varepsilon < a_n <\varepsilon$, для всех $n>N$. Тогда $-\sqrt{\varepsilon} < 0 < \sqrt{a_n} < \sqrt{\varepsilon}$, что и показывает $\lim_{n\to \infty} \sqrt{a_n} = 0.$
:::

## Лемма о зажатой последовательности

:::{prf:lemma} **Лемма о зажатой последовательности**
:name: squeezy
Пусть даны такие последовательности $(a_n), (b_n), (c_n)$, что $a_n<b_n<c_n$ для всех $n$, $\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = a$, тогда $\lim_{n \to \infty} b_n = a.$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
По определению предела, для любого $\varepsilon >0$, существуют такие номера $N,M$, что $|a_n - a| < \varepsilon$ и $|c_m - a|< \varepsilon$ для всех $n>N$, $m>M$. Пусть $K:=\max\{N,M\}$, тогда для любого $k>K$, $|a_k - a| < \varepsilon$ и $|c_k - a|< \varepsilon$. Мы получили совокупность неравенств
$$
a - \varepsilon < a_k < a+ \varepsilon, \qquad a -\varepsilon < c_k < a+ \varepsilon, \qquad \forall k >K,
$$
но тогда мы получаем $a- \varepsilon < a_k < b_k < c_k < a + \varepsilon$, т. е. для любого $\varepsilon>0$ мы нашли такое $K$, что для всех $k>K$, $a- \varepsilon < b_k < a+ \varepsilon$ или то же самое, что и $|b_k -a|< \varepsilon$, но это и означает, что $\lim_{n \to \infty}b_n = a$, что и требовалось доказать.
:::

:::{prf:example}
:name: sqrtnn1
Покажем, что $\lim_{n\to \infty}\sqrt[n]{n} = 1$. Имеем $n = \left(1+ (\sqrt[n]{n}-1) \right)^n$, тогда по биному Ньютона получаем
$$
n = 1 + \binom{n}{2} (\sqrt[n]{n} - 1)^2 + \cdots + (\sqrt[n]{n} - 1)^n,
$$
тогда
$$
n > \binom{n}{2} (\sqrt[n]{n} - 1)^2 = \frac{n(n-1)}{2} (\sqrt[n]{n} - 1)^2, 
$$
откуда получаем 
$$
0 < (\sqrt[n]{n} - 1) < \sqrt{\frac{2}{n-1}},
$$
и так как $\lim_{n\to \infty} 0 = 0$ и $\lim_{n\to \infty} \frac{2}{n-1} = 0$, то по лемме о зажатой последовательности [](#squeezy), получаем $\lim{n\to \infty} (\sqrt[n]{n} - 1) = 0$, а тогда используя предложение [](#lim(a_n-a)=0) мы получаем требуемое.   

:::


:::{prf:lemma} **Переход к пределу в неравенствах**
:name: aleb
Пусть даны такие последовательности $(a_n), (b_n)$, что $a_n<b_n$ для всех $n$, $\lim_{n \to \infty} a_n =a$ и $\lim_{n \to \infty} b_n = b$. Тогда $a\le b$. 
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $\varepsilon_0:=a-b >0$. Согласно определению предела, мы можем для $\frac{\varepsilon_0}{2}$ найти такие $N,M$, что $|a_n - a|<\frac{\varepsilon_0}{2}$, $|b_m-b|<\frac{\varepsilon_0}{2}$ для всех $n>N$, $m>M$.  Пусть $K:=\max\{N,M\}$, тогда для любого $k>K$
$$\begin{align*}
\varepsilon_0 &=& a-b\\
&=& a-a_k + a_k - b_k+b_k - b \\
&\le &a-a_k + b_k-b \\
&<&\varepsilon_0
\end{align*}$$
что даёт противоречие.

:::