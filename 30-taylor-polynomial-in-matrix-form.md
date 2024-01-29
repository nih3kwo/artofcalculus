# Полином Тэйлора в матричной записи (гессианы)

Мы будем рассматривать функции $f:\mathbb{R}^n \to \mathbb{R}$. При этом мы считаем, что $\mathbb{R}^n$ снабжено евклидовой нормой.

Напомним теорему [](#Taylor_in_many)
Пусть $f:\mathbb{R}^n \to \mathbb{R}$ есть $m+1$ раз дифференцируемая функция в окрестности точки $\m{a} \in \mathbb{R}^n$, то для всех $\m{h}$ из окрестности точки $\m{0}_n$ верно 
$$
f(\m{a} + \m{h}) = f(\m{a}) + (\mathrm{d}f)_\m{a} \m{h} + \frac{1}{2!} (\mathrm{d}^2f)_\m{a}\m{h} + \cdots + \frac{1}{m!} (\m{d}^mf)_\m{a}\m{h} + \frac{1}{(m+1)!} (\m{d}^{m+1}f)_{\m{a}+ \theta \m{h}}\m{h},
$$
где $0 < \theta < 1$ и она зависит от $\m{a}, \m{h}$ и $m$.

Получаем следующее
:::{prf:corollary}
:name: cor_for_Peano_in_many
Пусть $f:\mathbb{R}^n \to \mathbb{R}$ есть $m$ раз дифференцируема функция в окрестности точки $\m{a}$ и все её частные производные непрерывны в этой точке, тогда
$$
f(\m{a} + \m{h}) = f(\m{a}) + (\mathrm{d}f)_\m{a} \m{h} + \frac{1}{2!} (\mathrm{d}^2f)_\m{a}\m{h} + \cdots + \frac{1}{m!} (\m{d}^mf)_\m{a}\m{h} + o(\| \m{h} \|^m), \qquad \m{h} \to \m{0}_n.
$$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
По теореме [](#Taylor_in_many), 
$$
f(\m{a} + \m{h}) = f(\m{a}) + (\mathrm{d}f)_\m{a} \m{h} + \frac{1}{2!} (\mathrm{d}^2f)_\m{a}\m{h} + \cdots + \frac{1}{(m-1)!} (\m{d}^{m-1}f)_\m{a}\m{h} + \frac{1}{m!} (\m{d}^{m}f)_{\m{a}+ \theta \m{h}}\m{h},
$$
рассмотрим последний моном (самый правый) этого полинома, имеем
$$
(\m{d}^{m}f)_{\m{a}+ \theta \m{h}}(\m{h})= (\m{d}^{m}f)_{\m{a}}(\m{h}) +  \Bigl( (\m{d}^{m}f)_{\m{a}+ \theta \m{h}}(\m{h}) - (\m{d}^{m}f)_{\m{a}} (\m{h}) \Bigr).
$$

Согласно Теореме [](#differential_formula), 
$$
(\mathrm{d}^mf)_{\m{b}}(\m{h}) = \sum_{p_1 + \ldots + p_n = m} \dfrac{m!}{p_1! \cdots p_n!} \left.\frac{\partial^m f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}}\right|_{\m{b}} \cdot h_1^{p_1}\cdots h_n^{p_n},
$$
тогда, получаем
$$\begin{align*}
(\m{d}^{m}f)_{\m{a}+ \theta \m{h}}(\m{h}) &=& (\m{d}^{m}f)_{\m{a}}(\m{h}) +  \Bigl( (\m{d}^{m}f)_{\m{a}+ \theta \m{h}}(\m{h}) - (\m{d}^{m}f)_{\m{a}} (\m{h}) \Bigr) \\
&=& (\m{d}^{m}f)_{\m{a}}(\m{h}) + \sum_{p_1 + \ldots + p_n = m} \dfrac{m!}{p_1! \cdots p_n!}\left( \left.\frac{\partial^m f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}}\right|_{\m{a}+\theta \m{h}} - \left.\frac{\partial^m f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}}\right|_{\m{a}} \right)\cdot h_1^{p_1}\cdots h_n^{p_n} \\
&=& (\m{d}^{m}f)_{\m{a}}(\m{h})\\
&&+ \|h \|^m \sum_{p_1 + \ldots + p_n = m} \dfrac{m!}{p_1! \cdots p_n!}\left( \left.\frac{\partial^m f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}}\right|_{\m{a}+\theta \m{h}} - \left.\frac{\partial^m f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}}\right|_{\m{a}} \right) \frac{h_1^{p_1}}{\|h\|^{p_1}} \cdots \frac{h_n^{p_n}}{\|h\|^{p_n}}.
\end{align*}$$

Так как $\| h \|: = \sqrt{h_1^2 + \cdots + h_n^2}$, то 
$$
\frac{h_1^{p_1}}{\| \m{h}\|^{p_1}}, \ldots, \frac{h_1^{p_1}}{\| \m{h}\|^{p_1}} \le 1 
$$
далее, так как все частные производные непрерывны в точке $\m{a}$, то по критерию непрерывности [](#criteria_of_continous),
$$
\lim_{\m{h} \to \m{0}_n} \left( \left.\frac{\partial^m f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}}\right|_{\m{a}+\theta \m{h}} - \left.\frac{\partial^m f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}}\right|_{\m{a}} \right) = 0, 
$$
при каждом разбиении $m = p_1 + \cdots + p_n$, таким образом, 
$$
\lim_{\m{h} \to \m{0}_n} \sum_{p_1 + \ldots + p_n = m} \dfrac{m!}{p_1! \cdots p_n!}\left( \left.\frac{\partial^m f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}}\right|_{\m{a}+\theta \m{h}} - \left.\frac{\partial^m f}{\partial x_1^{p_1} \cdots \partial x_n^{p_n}}\right|_{\m{a}} \right) = 0,
$$
а это и означает, что 
$$
(\m{d}^{m}f)_{\m{a}+ \theta \m{h}}(\m{h}) = (\m{d}^{m}f)_{\m{a}}(\m{h}) + \omega(\m{h}) \|h\|^m, \quad \m{h} \to \m{0}_n,
$$
где $\lim_{\m{h} \to \m{0}_n} \omega(\m{h}) = \m{0}_n$, **т.е.,**
$$
(\m{d}^{m}f)_{\m{a}+ \theta \m{h}}(\m{h}) = (\m{d}^{m}f)_{\m{a}}(\m{h}) + o(\|h\|^m), \quad \m{h} \to \m{0}_n,
$$
но тогда
$$\begin{align*}
f(\m{a} + \m{h}) &=& f(\m{a}) + (\mathrm{d}f)_\m{a} \m{h} + \frac{1}{2!} (\mathrm{d}^2f)_\m{a}\m{h} + \cdots + \frac{1}{(m-1)!} (\m{d}^{m-1}f)_\m{a}\m{h} + \frac{1}{m!} (\m{d}^{m}f)_{\m{a}+ \theta \m{h}}\m{h} \\
&=&f(\m{a}) + (\mathrm{d}f)_\m{a} \m{h} + \frac{1}{2!} (\mathrm{d}^2f)_\m{a}\m{h} + \cdots + \frac{1}{(m-1)!} (\m{d}^{m-1}f)_\m{a}\m{h} + \frac{1}{m!}\left( (\mathrm{d}^mf)_\m{a} (\m{h}) + o(\|\m{h}\|^m) \right) \\
&=&f(\m{a}) + (\mathrm{d}f)_\m{a} \m{h} + \frac{1}{2!} (\mathrm{d}^2f)_\m{a}\m{h} + \cdots + \frac{1}{m!} (\m{d}^mf)_\m{a}\m{h} + o(\| \m{h} \|^m), \qquad \m{h} \to \m{0}_n
\end{align*}$$

что и требовалось доказать.
:::

:::{prf:definition}
Пусть функция $f:\mathbb{R}^n \to \mathbb{R}$ дважды дифференцируема в точке $\m{a}$, тогда матрица
$$
\m{H}_\m{a}(f): = \begin{pmatrix}
\left.\dfrac{\partial^2 f}{\partial x_1^2}\right|_{\m{a}} & \left.\dfrac{\partial^2 f}{\partial x_1 \partial x_2}\right|_{\m{a}} &\ldots & \left.\dfrac{\partial^2 f}{\partial x_1 \partial x_n}\right|_{\m{a}} \\
\left.\dfrac{\partial^2 f}{\partial x_2 \partial x_1}\right|_{\m{a}} & \left.\dfrac{\partial^2 f}{\partial x_2^2}\right|_{\m{a}} & \ldots & \left.\dfrac{\partial^2 f}{\partial x_2 \partial x_n}\right|_{\m{a}} \\
\vdots & \vdots & \ddots & \vdots \\
\left.\dfrac{\partial^2 f}{\partial x_n \partial x_1}\right|_{\m{a}} & \left.\dfrac{\partial^2 f}{\partial x_n \partial x_2}\right|_{\m{a}} & \ldots &\left.\dfrac{\partial^2 f}{ \partial x_n^2}\right|_{\m{a}}
\end{pmatrix}
$$
называется матрицей Гессе или гессианом функции $f$ в точке $\m{a}$.
:::

:::{warning}
Так как функция дважды дифференцируема в точке $\m{a}$, то по теореме Юнга [](#Yong) гессиан — симметричная матрица.
:::

:::{prf:theorem}
:name: Tayl_for_2
Если функция $f:\mathbb{R}^n \to \mathbb{R}$ — дважды дифференцируема в точке $\m{a}$, то
$$
f(\m{a} + \m{h}) =f(\m{a}) + \nabla_\m{a}(f)(\m{h}) + \frac{1}{2} \m{h}^\top \m{H}_\m{a}(f) \m{h} + o(\|\m{h}\|^2), \qquad \m{h} \to \m{0}_n.
$$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Согласно Следствию [](#cor_for_Peano_in_many), 
$$
f(\m{a} + \m{h}) = f(\m{a}) + (\mathrm{d}f)_\m{a} \m{h} + \frac{1}{2} (\mathrm{d}^2f)_\m{a}\m{h} + o(\| \m{h} \|^2), \qquad \m{h} \to \m{0}_n,
$$
но $(\mathrm{d}f)_\m{a} \m{h} = \nabla_\m{a}(f)(\m{h})$. Далее, по Теореме [](#differential_formula),
$$\begin{align*}
(\mathrm{d}^kf)_\m{a}(\m{h})  &=& \left.\left(\frac{\partial}{\partial x_1} h_1 + \cdots + \frac{\partial }{\partial x_n}h_n \right)^2\right|_{\m{a}} \cdot f \\
&=& \sum_{i=1}^n \left.\dfrac{\partial^2 f}{\partial x_i^2} \right|_\m{a} h_i^2 + 2 \sum_{1\le i < j \le n}  \left.\dfrac{\partial^2 f}{\partial x_i \partial x_j} \right|_{\m{a}} h_ih_j,
\end{align*}$$
где $\m{h} = (h_1, \ldots, h_n)^n$, но последнее выражение можно записать в матричном виде следующим образом
$$
(h_1, \ldots, h_n)^\top \begin{pmatrix}
\left.\dfrac{\partial^2 f}{\partial x_1^2}\right|_{\m{a}} & \left.\dfrac{\partial^2 f}{\partial x_1 \partial x_2}\right|_{\m{a}} &\ldots & \left.\dfrac{\partial^2 f}{\partial x_1 \partial x_n}\right|_{\m{a}} \\
\left.\dfrac{\partial^2 f}{\partial x_2 \partial x_1}\right|_{\m{a}} & \left.\dfrac{\partial^2 f}{\partial x_2^2}\right|_{\m{a}} & \ldots & \left.\dfrac{\partial^2 f}{\partial x_2 \partial x_n}\right|_{\m{a}} \\
\vdots & \vdots & \ddots & \vdots \\
\left.\dfrac{\partial^2 f}{\partial x_n \partial x_1}\right|_{\m{a}} & \left.\dfrac{\partial^2 f}{\partial x_n \partial x_2}\right|_{\m{a}} & \ldots &\left.\dfrac{\partial^2 f}{ \partial x_n^2}\right|_{\m{a}}
\end{pmatrix} \begin{pmatrix}
h_1 \\ \vdots \\ h_n
\end{pmatrix}  =  \m{h}^\top \m{H}_\m{a}(f) \m{h} ,
$$
и так как матрица симметрична, это завершает доказательство.
:::