# Полином Тейлора от одной переменной

Рассмотрим полином $P(x) \in \mathbb{R}[x]$. Говорят, что полином $P(x)$ **разложен в точке $a$ по степеням $(x-a)$**, если существуют такие $c_0, c_1, \ldots, c_n$, где $n = \mathrm{deg}(P(x))$, что $P(x) = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots + c_n(x-a)^n$. 

Нетрудно видеть, что эти коэффициенты можно найти следующим образом
$$
c_0 = P(a), \quad c_1 = P'(a), \quad c_2 = \frac{1}{2}P''(a), \quad c_3 = \frac{1}{6}P'''(a), \ldots,  c_n = \frac{1}{n!}P^{(n)}(a).
$$

Таким образом, получаем
$$
P(x) = P(a) + P'(a)(x-a) + \frac{1}{2} P''(a)(x-a)^2 + \cdots + \frac{1}{n!}P^{(n)}(a)(x-a)^n.
$$


:::{prf:definition}
Пусть $f(x)$ есть $n$-раз дифференцируема в точке $a\in \mathbb{R}$. Полином вида 
$$
T_f(x): = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!}(x-a)^k
$$
называется **полиномом Тейлора для функции $f$**.
:::


:::{prf:theorem}
Если $f$ есть $n$-раз дифференцируемая функция в точке $a$, то
$$
f(x) = T_f(x) + o((x-a)^n), \qquad x \to a.
$$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $r(x): = f(x) - T_f(x)$, очевидно, что $r(a) = r'(a) = \cdots = r^{(n)}(a) = 0$. По правилу Лопиталя [](#Lop)
$$\begin{align*}
\lim_{x \to a} \frac{r(x)}{(x-a)^n} &=& \lim_{x \to a} \frac{r'(x)}{n(x-a)^{n-1}} \\
&=& \lim_{x \to a} \frac{r''(x)}{n(n-1)(x-a)^{n-2}} = \cdots \\
&=& \lim_{x \to a} \frac{r^{(n-1)}(x)}{n!(x-a)}
\end{align*}$$
Дальше правило Лопиталя применять вообще говорят нельзя, так как по условию известно, что существует лишь $f^{(n)}(a)$, а в окрестности она может не существовать. 

Воспользуемся теперь определением, получаем
$$
r^{(n)}(x) = \lim_{x \to a} \frac{r^{(n-1)}(x) - r^{(n-1)}(a)}{(x-a)} = \lim_{x \to a} \frac{r^{(n-1)}(x)}{(x-a)},
$$
потому что $r^{(n-1)}(a) = 0$, но тогда
$$
\lim_{x \to a} \frac{r^{(n-1)}(x)}{n!(x-a)} = \lim_{x \to a} \frac{r^{(n)}(x)}{n!} = 0,
$$
что и доказывает требуемое.
:::

:::{prf:theorem} Общий вид остаточного монома 
:name: gen_monom
Пусть $f$ есть $n$ раз дифференцируема в каждой точке отрезка $[a,x]$, функция $f^{(n)}$ непрерывна на $[a,x]$ и дифференцируема на интервале $(a,x)$. Пусть $g(x)$ непрерывна на $[a,x]$ и дифференцируема на $(a,x)$, причём $g\ne 0$ на $(a,x)$. Тогда существует такое $c\in (a,x)$, что
$$
f(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!}(x-a)^k + r_n(x,a),
$$
где 
$$
r_n(x,a) = \frac{1}{n!}\frac{f^{(n+1)}(c)}{g'(c)}\bigl(g(x) - g(a)\bigr)(x-c)^n.
$$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть
$$\begin{align*}
\psi(t) &:=& f(x) - \sum_{k=0}^n \frac{f^{(k)}(t)}{k!}(x-t)^k \\
&=& f(x) - \left(f(t) + f'(t)(x-t) + \cdots + \frac{1}{n!}f^{(n)}(t)(x-t)^n \right) 
\end{align*}$$
где $a \le t \le x$.

Тогда
$$
\psi(x) = 0, \qquad \psi(a) = f(x) - \sum_{k=0}^n \frac{f^{(k)}(a)}{k!}(x-a)^k,
$$
**т.е.,** $r_n(x,a) = \psi(a)$.

Согласно условиям, $\psi(t)$ дифференцируема на $[a,x]$, тогда по теореме Коши [](#Coushy_for_functions), существует такое $c \in (a,x)$, что
$$
\frac{\psi(x)-\psi(a)}{g(x) - g(a)} = \frac{\psi'(c)}{g'(c)},
$$
тогда
$$
\psi(a) = - \frac{\psi'(c)}{g'(c)}(g(x) - g(c))
$$
поэтому
$$
r_n(x,a)= - \frac{\psi'(c)}{g'(c)}(g(x) - g(c)).
$$

Имеем
$$\begin{align*}
\psi'(t) &= & - \left( f(t) + f'(t)(x-t) + \frac{1}{2!}f''(t)(x-t)^2 + \frac{1}{3!}f'''(t)(x-t)^3 + \cdots \frac{1}{n!}f^{(n)}(t) (x-t)^n \right)' \\
&=& -f'(t) \\
&& - f''(t)(x-t) + f'(t) \\
&& - \frac{1}{2!}f'''(t)(x-t)^2 + f''(t)(x-t) \\
&&  - \frac{1}{3}f^{(4)}(x-t)^3 + \frac{1}{3!}f'''(t)(x-t)^3 \\
&& \cdots - \frac{f^{(n+1)}(t)}{n!}(x-t)^n \\
&=& - \frac{f^{(n+1)}(t)}{n!}(x-t)^n.
\end{align*}$$

Таким образом,
$$
r_n(x,a) =\frac{1}{n!}\frac{f^{(n+1)}(c)}{g'(c)}\bigl(g(x) - g(a)\bigr)(x-c)^n,
$$
что и требовалось доказать.    
:::


:::{prf:corollary} Остаточный моном в форме Коши
$$
\boxed{
r_n(x,a) = \frac{f^{(n+1)}(c)}{n!}(x-a)(x-c)^n, \quad a < c <x.}
$$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Нужно положить $g(x) = x-t$ в теореме [](#gen_monom).
:::

:::{prf:corollary} Остаточный моном в форме Лагранжа.
:name: monom_in_Langrange
$$
\boxed{
r_n(x,a) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}, \qquad a < c <x.
}
$$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Нужно положить $g(x) = (x-t)^{n+1}.$
:::