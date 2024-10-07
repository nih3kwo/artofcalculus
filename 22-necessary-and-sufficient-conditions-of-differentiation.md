# Необходимые и достаточные условия дифференцируемости

Что касается необходимых условия дифференцируемости, то мы их уже знаем. Но для удобства мы сделаем из этого следующую теорему:

:::{prf:theorem}
Если функция $f:\mathbb{R}^n \to \mathbb{R}$ дифференцируема на каком-то открытом $\mathscr{U} \subseteq \mathbb{R}^n$ или в фиксированной точке $\m{x}$, то она имеет в этой точке частные производные по всем переменным.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $f:\mathbb{R}^n \to \mathbb{R}$, дифференцируемая на каком-то открытом $\mathscr{U} \subseteq \mathbb{R}^n$ или в фиксированной точке $\m{x}$. Тогда её дифференциал $(\mathrm{d}f)_\m{x}$ в точке $\m{x}$ задаётся матрицей размера $n\times 1$, $(\mathrm{d}f)_\m{x} = \begin{pmatrix}
a_1 & \ldots & a_n
\end{pmatrix}$, где все $a_i$ есть функции от $\m{x}$. Наша цель — найти эти $a_i$. Пусть $\m{h} = (h_1, \ldots, h_n)^\top \in \mathscr{U} \subseteq \mathbb{R}^n$, тогда получаем
$$\begin{align*}
f(\m{x} + \m{h}) - f(\m{x}) &=& (\mathrm{d}f)_\m{x}(\m{h}) + o(||\m{h}||) \\
&=& \begin{pmatrix}
a_1 & \ldots & a_n
\end{pmatrix} \begin{pmatrix}
h_1 \\ \vdots \\ h_n  \end{pmatrix} + o(||\m{h}||) \\
&=& a_1h_1 + \cdots + a_nh_n + o(||\m{h}||).
\end{align*}$$

Видно, что $a_i$ не зависит от координат вектора $\m{h}$ кроме $h_i$ т. е. чтобы найти $a_i$, нам достаточно рассмотреть вектор $\m{h}_i = h_i \m{e}_i$, где $\m{e}_i$ — базисный вектор. В таком случае, $||\m{h}_i|| = |h_i|$, и тогда для каждого $1 \le i \le n$ мы получаем
$$
f(\m{x} + h_i \m{e}_i) - f(\m{x}) = a_ih_i + o(|h_i|),
$$
таким образом, 
$$
a_i = \lim_{h_i \to 0} \frac{f(\m{x} + h_i \m{e}_i) - f(\m{x})}{h_i},
$$
такое выражение называется **частной производной функции по переменной $x_i$** и обозначается либо как $\frac{\partial f}{\partial x_i}$, либо как $f'_{x_i}$, т. е. 
$$
\frac{\partial f}{\partial x_i}: = \lim_{h_i \to 0} \frac{f(\m{x} + h_i \m{e}_i) - f(\m{x})}{h_i},
$$
если же мы хотим знать её значение в точке $\m{x}_0$, то получаем
$$
\frac{\partial f}{\partial x_i}(\m{x}_0): = \lim_{h_i \to 0} \frac{f(\m{x}_0 + h_i \m{e}_i) - f(\m{x}_0)}{h_i}.
$$
:::


Таким образом, в случае функции $f:\mathbb{R}^n \to \mathbb{R}$, дифференциал в точке $\m{x}_0$ находится по формуле
$$
(\mathrm{d}f)_{\m{x}_0}: = \begin{pmatrix}
\frac{\partial f}{\partial x_1}(\m{x}_0) & \ldots & \frac{\partial f}{\partial x_n}(\m{x}_0)
\end{pmatrix}.
$$



Мы сейчас обобщим теорему Лагранжа о конечных приращениях. Ради краткости мы будем говорить, что вектор $\m{v} = (v_1,\ldots, v_n)^\top$ **лежит между нулём и вектором** $\m{h} = (h_1,\ldots, h_n)^\top$, если $0\le v_i \le h_i$. $1\le i \le n.$

:::{prf:theorem} Формула конечных приращений
:name: gen_of_Langrange
Пусть $\mathscr{U} \subseteq \mathbb{R}^n$ — открытое множество, $f:\mathscr{U} \to \mathbb{R}$ — функция, у которой во всех точках множества $\mathscr{U}$ имеются конечные частные производные по всем переменным. Тогда для любых $\m{a}, \m{a} + \m{h} \in \mathscr{U}$ справедливо равенство
$$
f(\m{a} + \m{h}) - f(\m{a}) = \sum_{k =1}^n f'_{x_k}({\m{a} + \m{v}_k}) \cdot h_k,
$$
где $\m{v}_1, \ldots, \m{v}_n$ — некоторые векторы, расположенные между нулём и вектором $\m{h}.$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть

$$
\begin{matrix}
f_1 & = & f(a_1 + h_1, a_2, \ldots, a_n) - f(a_1, \ldots, a_n), \\
f_2 & = & f(a_1 + h_1, a_2+h_2,a_3 \ldots, a_n) - f(a_1+h_1, \ldots, a_n),\\
f_3 &=& f(a_1+h_1, a_2+h_2, a_3+h_3,a_4,\ldots, a_n) - (a_1 + h_1, a_2+h_2,a_3 \ldots, a_n),\\
\vdots &  & \vdots \\
f_n & = & f(a_1 + h_1, \ldots, a_n+h_n) - f(a_1, \ldots, a_n),
\end{matrix}
$$
тогда $f(\m{a} + \m{h}) - f(\m{a}) = f_1 + \cdots + f_n.$

Пусть 
$$
\varphi_k(t): = f(a_1 + h_1, \ldots, a_{k-1}+h_{k-1},a_k+t_k, a_{k+1}, \ldots, a_n) - f(a_1 + h_1, \ldots, a_{k-1}+h_{k-1}, a_k,\ldots, a_n).
$$

Для удобства мы запишем в векторном виде, т. е. в таком виде
$$
\varphi_k(t): = f(\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1} + t\m{e}_k) - f(\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1})
$$

Тогда получаем
$$\begin{align*}
\varphi_k(t) - \varphi_k(t_0) &=& f(\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1} + t\m{e}_k) - f(\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1}) \\
&-& -f(\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1} + t_0\m{e}_k) + f(\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1}) \\
&=& f(\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1} + t\m{e}_k) - f(\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1} + t_0\m{e}_k),
\end{align*}$$
в частности
$$
\varphi_k(h_k) - \varphi_k(0) = f_k.
$$

Пусть $\m{x}_0 := \m{a}+ h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1}+t_0\m{e}_k$, тогда 
$$\begin{align*}
\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1} + t\m{e}_k &=& \m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1} + (t-t_0)\m{e}_k \\
&+& \m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1} + t_0\m{e}_k \\
&=& \m{x}_0 + (t-t_0) \m{e}_k
\end{align*}$$

Таким образом, мы можем написать
$$\begin{align*}
\varphi_k(t) - \varphi_k(t_0) &=&  f(\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1} + t\m{e}_k) - f(\m{a} + h_1 \m{e}_1 + \cdots + h_{k-1}\m{e}_{k-1} + t_0\m{e}_k) \\
&=& f(\m{x}_0 + (t-t_0) \m{e}_k) - f(\m{x}_0),
\end{align*}$$
а тогда
$$\begin{align*}
\varphi_k'(t_0) &:=& \lim_{t \to t_0} \frac{\varphi_k(t) - \varphi_k(t_0)}{t-t_0} \\
&=& \lim_{t \to t_0} \frac{f(\m{x}_0 + (t-t_0) \m{e}_k) - f(\m{x}_0)}{t-t_0} \\
&=:& \left.\frac{\partial f}{\partial x_k}\right|_{\m{x}_0} = f'_{x_k}(\m{x}_0).
\end{align*}$$

Это значит, что функция $\varphi_k(t)$ дифференцируема на отрезке $[0,h_k]$, потому что по условию существуют все частные производные в $\mathscr{U}$. 

Применим теперь к каждой $\varphi_k(t)$ теорему Лагранжа (теорема [](#Langrange)); существует $\theta_k \in (0, h_k)$ такое, что
$$
\varphi_k'(\theta_k) = \frac{\varphi_k(h_k) - \varphi_k(0)}{h_k}, 
$$
тогда, если $\m{v}_k:= \m{a}+ h_1 \m{e}_1  + \cdots + h_{k-1}\m{e}_{k-1} + \theta_k\m{e}_k$, то для каждого $1\le k \le n$ мы получили
$$
f_k = \varphi_k(h_k) - \varphi_k(0) = \varphi_k'(\theta_k)h_k = f'_{x_k}(\m{a} + \m{v}_k)h_k, 
$$
где все $\m{k}$ расположены между $\m{a}$ и $\m{a}+ \m{h}$, тогда окончательно получаем
$$\begin{align*}
f(\m{a} + \m{h}) - f(\m{a}) &=& f_1 + \cdots + f_n \\
&=& f'_{x_1}(\m{a} + \m{v}_1)h_1 + \cdots + f'_{x_n}(\m{a} + \m{v}_n)h_n \\
&=& \sum_{k =1}^n f'_{x_k}({\m{a} + \m{v}_k}) \cdot h_k,
\end{align*}$$
что и требовалось доказать.
:::




:::{prf:theorem} Достаточные условия дифференцируемости
Пусть функция $f$ имеет конечные частные производные по всем координатам в окрестности точки $\m{a}$. Если они непрерывны в точке $\m{a}$, то $f$ дифференцируема в этой точке.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $\mathscr{U}$ — окрестность точки $\m{a}$, и пусть $\m{a} + \m{h} \in \mathscr{U}$. Согласно формуле конечных приращений, (теорема [](#gen_of_Langrange)) мы имеем
$$
f(\m{a} + \m{h}) - f(\m{a}) = \sum_{k=1}^n  f'_{x_k}({\m{a} + \m{v}_k})\cdot h_k,
$$
где $\m{a} + \m{v}_k \in \mathscr{U}$, $1 \le k \le n$.

По условию, все частные производные непрерывны и конечны, тогда для любого $\varepsilon >0$ из $||\m{v}_k|| < \delta$ следует $|f'_{x_k}({\m{a} + \m{v}_k}) - f'_{x_k}(\m{a})| < \varepsilon$. Другими словами, можно сказать, что
$$
f'_{x_k}({\m{a} + \m{v}_k}) = f_{x_k}'(\m{a}) + \varepsilon_k(\m{h}),
$$
где $\varepsilon_k(\m{h}) \to 0$ когда $\m{h} \to 0.$

Таким образом, получаем
$$
f(\m{a} + \m{h}) - f(\m{a}) = \sum_{k=1}^n \bigl( f'_{x_k}(\m{a}) + \varepsilon_k(\m{h})  \bigr)h_k = \sum_{k=1}^n f'_{x_k}(\m{a}) h_k + \alpha(\m{h}),
$$
где $\alpha(\m{h}): = \sum_{k=1}^n \varepsilon_k(\m{h}) h_k$. Ясно, что
$$
\frac{\alpha(\m{h})}{|| \m{h} ||} = \sum_{k=1}^n \varepsilon_k(\m{h}) \frac{h_k}{||\m{h} ||}.
$$

Наконец, согласно ([](#mledleM)), 
$$
|| \m{h} || = \sqrt{h_1^2 + \cdots + h_n^2} \ge  \max_{1\le i \le n} |h_i|,
$$
тогда 
$$
\frac{h_k}{|| \m{h}||} < \frac{h_i}{ \max_{1\le i \le n} |h_i|} \le \frac{\max_{1\le i \le n} |h_i|}{\max_{1\le i \le n} |h_i|} = 1 
$$
т. е. все дроби $\frac{h_k}{||\m{h}||}$ ограничены. Далее, так как $\varepsilon_k(\m{h})$ бесконечно малые, мы получаем
$$
f(\m{a} + \m{h}) - f(\m{a}) = \sum_{k=1}^n f'_{x_k}(\m{a}) h_k + o(||\m{h}||),
$$
а это и означает, что $f$ дифференцируема.
:::