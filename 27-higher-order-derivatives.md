# Высшие дифференциалы

Рассмотрим дифференцируемое отображение $F: \mathbb{R}^n \to \mathbb{R}^m$ в каком-то открытом $\mathscr{U} \subseteq \mathbb{R}^n$, т. е. для каждой точки $\m{p} \in \mathscr{U}$ у нас есть линейное отображение $(\mathrm{d}F)_{\m{p}}: \mathbb{R}^n\to \mathbb{R}^m$. Так как линейные отображения из $\mathbb{R}^n$ в $\mathbb{R}^m$ — это просто матрицы размера $n\times m$, то дифференцируемость отображения $F$ в $\mathscr{U}$ означает, что у нас есть отображение
$$
\mathrm{d}F: \mathscr{U} \to \mathrm{Mat}_{n\times m}(\mathbb{R}), \qquad \m{p} \mapsto (\mathrm{d}F)_{\m{p}}.
$$

С другой стороны, пространство матриц $\mathrm{Mat}_{n\times m}(\mathbb{R})$ есть векторное пространство, которое можно отождествить (=изоморфно) с $\mathbb{R}^{nm}$.

Тогда мы можем поставить вопрос о дифференцируемости отображения $\mathrm{d}F$ и получить уже отображение
$$
\mathrm{d}^2(F): = \mathrm{d}(\mathrm{d}F): \mathscr{U}' \to \mathrm{Mat}_{n \times nm}(\mathbb{R}),
$$
где $\mathscr{U}'$ открыто в $\mathscr{U}$.

Таким образом, мы получаем отображения (если они существуют)
$$
F:=\mathrm{d}^0F,\quad  \mathrm{d}F,\quad \mathrm{d}^2(F): = \mathrm{d}(\mathrm{d}F), \ldots, 
$$
среди которых $\mathrm{d}^k(F)$ при $k>1$ называются **высшими дифференциалами.**


## Явная формула для высших дифференциалов и формальный символизм

Итак, пусть у нас есть $n$-раз дифференцируемая функция $f:\mathbb{R}^n \to \mathbb{R}$ в окрестности $\mathscr{U}$ точки $\m{a}$. Мы знаем, что
$$
(\mathrm{d}f)_\m{a}(\m{h}) = \begin{pmatrix}
f'_{x_1}(\m{a}) & \ldots & f'_{x_n}(\m{a})
\end{pmatrix} \begin{pmatrix}
h_1 \\ \vdots \\ h_n
\end{pmatrix} = f_{x_1}'(\m{a})h_1 + \cdots + f_{x_n}'(\m{a})h_n.
$$

Найдём $(\mathrm{d}^n(f))_\m{a}(\m{h}): = \mathrm{d}(\mathrm{d}^{n-1}f)_\m{a}(\m{h})$. Для этого нам понадобиться следующий формализм.

Пусть $C^\infty(\mathbb{R}^n)$ есть множество гладких (=бесконечно дифференцируемых) дифференцируемых функций $f:\mathbb{R}^n \to \mathbb{R}$. Рассмотрим следующие отображения:
$$
\frac{\partial}{\partial x_i}: C^\infty(\mathbb{R}^n) \to C^\infty(\mathbb{R}^n), \qquad f\mapsto f'_{x_i}, \quad 1 \le i \le n.
$$

Тогда у нас возникают их композиции 
$$
\frac{\partial^k}{\partial x_{i_k} \cdots \partial x_{i_1}}:=\dfrac{\partial}{\partial x_{i_k}} \circ \cdots \circ \dfrac{\partial}{\partial x_{i_1}}:  C^\infty(\mathbb{R}^n) \to C^\infty(\mathbb{R}^n), \qquad f \mapsto \frac{\partial^k f}{\partial x_{i_k} \cdots \partial x_{i_1}}.
$$




:::{prf:theorem}
:name: differential_formula
Если функция $f:\mathbb{R}^n \to \mathbb{R}$ в окрестности точки $\m{a}$ $m$ раз дифференцируема, то для каждого $1 \le k \le m$
$$
\boxed{
(\mathrm{d}^kf)_\m{a}(\m{h})=     \left.\left(\frac{\partial}{\partial x_1} h_1 + \cdots + \frac{\partial }{\partial x_n}h_n \right)^k\right|_{\m{a}} \cdot f
}$$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Доказательство будет идти по индукции. Если $m=1$, то мы получаем просто определение дифференциала. Пусть формула верна при $1 \le k<m$, имеем
$$
(\mathrm{d}^kf)(\m{h}) = \sum_{p_1 + \ldots + p_n = k} \dfrac{k!}{p_1! \cdots p_n!} \frac{\partial^k f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}} h_1^{p_1}\cdots h_n^{p_n}
$$

Дифференцируем теперь это равенство, получаем
$$\begin{align*}
(\mathrm{d}^{k+1}f)(\m{h}) &=& (\mathrm{d}(\mathrm{d}^kf))(\m{h}) \\
&=& \sum_{p_1 + \ldots + p_n = k} \dfrac{k!}{p_1! \cdots p_n!} \mathrm{d}\left( \frac{\partial^k f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}} h_1^{p_1}\cdots h_n^{p_n}\right) \m{h}\\
&=& \sum_{p_1 + \ldots + p_n = k} \dfrac{k!}{p_1! \cdots p_n!} \left(\mathrm{d}\left( \frac{\partial^k f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}} \right)(\m{h}) \right)\cdot h_1^{p_1}\cdots h_n^{p_n} 
\end{align*}$$
Теперь применяя формулу дифференциала, мы получим
$$
(\mathrm{d}^{k+1}f)(\m{h}) = \sum_{p_1 + \ldots + p_n = k} \dfrac{k!}{p_1! \cdots p_n!} \left( \frac{\partial^{k+1}f}{\partial x_1^{p_1+1} \cdots \partial x_n^{p_n}}h_1 + \cdots +  \frac{\partial^{k+1}f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n+1}}h_n \right)\cdot h_1^{p_1}\cdots h_n^{p_n}. 
$$

Фиксируем набор $(p_1,\ldots, p_n)$ и рассмотрим соответствующую сумму
$$
S(p_1,\ldots, p_n): = \frac{\partial^{k+1}f}{\partial x_1^{p_1+1} \partial x_2^{p_2} \cdots \partial x_n^{p_n}}h_1^{p+1}h_2^{p_2}\cdots h_n^{p_n} + \cdots +  \frac{\partial^{k+1}f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n+1}}h_1^{p_1}h_2^{p_2} \cdots h_n^{p_n+1}.
$$
тогда первое слагаемое этой суммы также присутствует в следующих суммах

$$
\begin{matrix}
S(p_1+1, p_2-1,p_3,\ldots, p_n), \\
S(p_1+1, p_2,p_3-1,\ldots, p_n), \\
\vdots \\
S(p_1+1, p_2,p_3,\ldots, p_n-1).
\end{matrix}
$$

Тогда коэффициент при $\frac{\partial^{k+1}f}{\partial x_1^{p+1}\partial x_2^{p_2} \cdots \partial x_n^{p_n}} h_1^{p_1+1}h_2^{p_2}\cdots h_n^{p_n}$ есть следующее выражение
$$
K = \frac{k!}{p_1! p_2! \cdots p_n!} + \frac{k!}{(p_1+1)!p_2! \cdots p_n!} + \cdots + \frac{k!}{(p_1+1)!p_2! \cdots (p_n-1)!}
$$
имеем
$$\begin{align*}
K &=&   \frac{k!}{p_1! p_2! \cdots p_n!} + \frac{k!}{(p_1+1)!p_2! \cdots p_n!} + \cdots + \frac{k!}{(p_1+1)!p_2! \cdots (p_n-1)!} \\
&=& \frac{k!}{p_1! (p_2-1)! \cdots (p_n-1)!}\left( \frac{1}{p_2p_3 \cdots p_n} + \frac{1}{(p_1+1)p_2\cdots p_n} + \cdots + \frac{1}{(p_1+1)p_2 \cdots p_{n-1}}\right) \\
&=& \frac{k!}{p_1! (p_2-1)! \cdots (p_n-1)!} \cdot \frac{p_1+1 +p_2+ \cdots+ p_n}{(p_1+1)p_2\cdots p_n} \\
&=& \frac{k!(k+1)}{(p_1+1)! p_2! \cdots p_n!} \\
&=& \frac{(k+1)!}{(p_1+1)! p_2! \cdots p_n!}.
\end{align*}$$

Таким образом, рассуждая аналогично для остальных мономов, мы можем тогда записать
$$
(\mathrm{d}^{k+1}f)(\m{h}) = \sum_{p_1 + \ldots + p_n = k+1} \dfrac{(k+1)!}{p_1! \cdots p_n!} \frac{\partial^{k+1} f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}} h_1^{p_1}\cdots h_n^{p_n},
$$
что и доказывает утверждение.

:::