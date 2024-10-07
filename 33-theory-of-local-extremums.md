# Теория условных экстремумов

Рассмотрим вопрос об экстремумах функции $f:\mathbb{R}^{n+m} \to \mathbb{R}$ от $n+m$ переменных, $x_1,\ldots, x_{n+m}$ в предположении, что эти переменные подчинены ещё $m$ **уравнениям связи**
\begin{equation}\label{extr_connections}
\left\{\begin{matrix}
\Phi_1(x_1,\ldots, x_{n}, \ldots, x_{n+m}) = 0 \\
\Phi_2(x_1,\ldots, x_{n}, \ldots, x_{n+m}) = 0 \\
\vdots\\
\Phi_m(x_1,\ldots, x_{n}, \ldots, x_{n+m}) = 0
\end{matrix} \right.   
\end{equation}

:::{prf:definition}
:label: conditional_extremum
Говорят, что в точке $\m{a} = (a_1,\ldots, a_{n+m})$, удовлетворяющей уравнением связи функция $f(\m{x})$, $\m{x} = (x_1,\ldots, x_{n+m})$ имеет **условный (=относительный) максимум (соотв. минимум)**, если неравенство $f(\m{x}) \le f(\m{a})$ (соотв. $f(\m{x}) \ge f(\m{a}))$ выполняется в некоторой окрестности точки $\m{a}$ для всех её точек $\m{x}$, удовлетворяющих уравениям [](#extr_connections).
:::

:::{prf:theorem} Необходимое условие условного экстремума
:label: required_conditional_extremum

Пусть $f, \varphi_1,\ldots, \varphi_m: \mathbb{R}^{n+m} \to \mathbb{R}$ являются непрерывно дифференцируемыми фукнциями в окрестности $\mathscr{W}$ точки $\m{a}$, и пусть 
$$
\mathrm{rk} \begin{pmatrix}
\dfrac{\partial \varphi_1}{\partial x_1} (\m{x}) & \ldots & \dfrac{\partial \varphi_1}{\partial x_{n+m}} (\m{x}) \\
\vdots & \ddots & \vdots \\
\dfrac{\partial \varphi_m}{\partial x_1} (\m{x}) & \ldots & \dfrac{\partial \varphi_m}{\partial x_{n+m}} (\m{x})
\end{pmatrix} = m
$$
для всех $\m{x}\in \mathscr{W}$. Тогда, если $\m{a}$ — точка условного экстремума функции $f$ на множестве
$$
\Omega: = \{\m{x} \in \mathbb{R}^{n+m}\,:\, \varphi_1(\m{x}) =0, \ldots, \varphi_m(\m{x}) = 0\}
$$
то найдутся такие числа $\lambda_1,\ldots, \lambda_m \in \mathbb{R}$, что
$$
\nabla_\m{a} f = \lambda_1 \nabla_\m{a} \varphi_1 + \cdots +   \lambda_m \nabla_\m{a} \varphi_m.
$$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Рассмотрим отображение
$$
\Phi: \mathbb{R}^{n+m} \to \mathbb{R}^{n+m}, \qquad \begin{pmatrix}
x_1 \\ \vdots \\ x_m \\ x_{m+1} \\ \vdots \\ x_{n+m}
\end{pmatrix} \mapsto \begin{pmatrix}
\varphi_1(x_1,\ldots, x_{n+m}) \\
\vdots \\
\varphi_m(x_1,\ldots, x_{n+m}) \\
x_{m+1} \\ \vdots \\x_{n+m}
\end{pmatrix}
$$
согласно условиям, оно непрерывно дифференцируемо в окрестности $\mathscr{W}$ точки $\m{a}$.

Сделаем теперь замену переменных
\begin{equation}\label{coordantes_u}
\begin{matrix}
u_1 & = & \varphi_1(x_1,\ldots, x_{n+m}) \\
\vdots & & \vdots\\
u_m & = & \varphi_m(x_1,\ldots, x_{n+m}) \\
u_{m+1} &=& x_{m+1} \\
\vdots && \vdots \\
u_{m+n} &=& x_{m+n}
\end{matrix}
\end{equation}

Если нужно, то, перенумеровав переменные, можно считать, что из условия о ранге матрицы вытекает
$$
\mathrm{det} \begin{pmatrix}
\dfrac{\partial \varphi_1}{\partial x_{1}}(\m{x}) &\ldots& \dfrac{\partial \varphi_1}{\partial x_{m}}(\m{x}) \\
\vdots & \ddots & \vdots \\
\dfrac{\partial \varphi_m}{\partial x_{1}}(\m{x}) &\ldots & \dfrac{\partial \varphi_m}{\partial x_{m}}(\m{x})
\end{pmatrix} \ne 0.
$$

Тогда по теореме об обратном отображении [](#inverse_function_theorem), $\Phi$ — локально обратима в окрестности $\mathscr{U} \subseteq \mathscr{W}$ точки $\m{a}.$ Это значит, что существуют такие непрерывно дифференцируемые функции $\psi_i: \mathscr{V} \to \mathbb{R}$, $1\le i \le n+m$, где $\mathscr{V}$ — окрестность точки $\Phi(\m{a})$, что мы получаем обратную замену координат к замене ([](#coordantes_u)) 
$$
\begin{matrix}
x_1 & = & \psi_1(u_1,\ldots, u_{m}) \\
\vdots & & \vdots\\
x_{n+m} & = & \psi_{n+m}(u_1,\ldots, u_m)
\end{matrix}
$$

В итоге, мы получаем две коммутативные диаграммы

![alt text](image-4.png)

**т.е.,**
$$
f_u(u_1, \ldots, u_{n+m}) := f(\varphi_1(x_1,\ldots, x_{n+m}), \ldots, \varphi_m(x_1,\ldots, x_{n+m}), x_{m+1},\ldots, x_{m+n}),
$$
и
$$
f(x_1,\ldots, x_{n+m})= f_u(\psi_1(u_1,\ldots, \psi_m), \ldots, \psi_{n+m}(u_1,\ldots, u_m)).
$$

Тогда, если мы ограничимся рассмотрением точек на множестве $\Omega$, то во-первых, мы получаем, что 
$$
\Phi(\Omega) = \{(u_1,\ldots, u_{n+m}) \in \mathscr{U}\, : \, u_1=0,\ldots, u_m=0\},
$$
во-вторых мы получаем функцию уже от $n$ переменных $f_u(0,\ldots, 0, u_{m+1},\ldots, u_{m+n})$.

Далее, из диаграммы

![alt text](image-5.png)

следует, что при $\m{y} \in \Phi(\Omega \cap \mathscr{U})$, отображение $\Phi^{-1}$ имеет вид
$$
\qquad \Phi^{-1} : \begin{pmatrix}
0\\
\vdots \\
0\\
u_{m+1} \\
\vdots \\
u_{m+n}
\end{pmatrix} \mapsto \begin{pmatrix}
0\\
\vdots \\
0\\
x_{m+1} \\
\vdots \\
x_{m+n}
\end{pmatrix},
$$
а так как $u_{m+1} = x_{m+1}, \ldots, u_{m+n} =x_{n+m}$, то
$$
f_u(0,\ldots, 0, u_{m+1},\ldots, u_{m+n}) = f(0,\ldots, 0, x_{m+1}, \ldots, x_{n+m}) \circ \Phi^{-1}.
$$

Но тогда $\Phi(\m{a})$ — точка экстремума функции $f_u(0,\ldots, 0, u_{m+1},\ldots, u_{m+n})$ и по необходимому признаку [](#required_extremum), мы получаем
$$
\dfrac{\partial f_u}{\partial{u_{m+1}}}(\Phi(\m{a})) = \cdots = \dfrac{\partial f_u}{\partial{u_{m+n}}}(\Phi(\m{a})) = 0.
$$

Это значит, что в точке $\Phi(\m{a})$ имеем
$$
(\mathrm{d}f_u)_{\Phi(\m{a})} = \begin{pmatrix}
\lambda_1 & \ldots & \lambda_m & 0 & \ldots & 0
\end{pmatrix}.
$$

Наконец, из диаграммы

![alt text](image-6.png)

и из теоремы о композиции дифференциалов [](#d(FG)) получаем
$$\begin{align*}
(\mathrm{d}f)_\m{a} &= (\mathrm{d}f_u)_{\Phi(\m{a})} \cdot (\mathrm{d}\Phi)_{\m{a}} \\
&= \begin{pmatrix}
\lambda_1 & \ldots & \lambda_m & 0 & \ldots 0
\end{pmatrix} \begin{pmatrix}
\dfrac{\partial \varphi_1}{\partial x_1}(\m{a}) & \ldots & \dfrac{\partial \varphi_1}{\partial x_m}(\m{a}) & \dfrac{\partial \varphi_1}{\partial x_{m+1}}(\m{a}) & \ldots & \dfrac{\partial \varphi_1}{\partial x_{m+n}}(\m{a}) \\
\vdots & \ddots & \vdots & \vdots & \ddots & \vdots\\
\dfrac{\partial \varphi_m}{\partial x_1}(\m{a}) & \ldots & \dfrac{\partial \varphi_m}{\partial x_m}(\m{a}) & \dfrac{\partial \varphi_n}{\partial x_{m+1}}(\m{a}) & \ldots & \dfrac{\partial \varphi_m}{\partial x_{m+n}}(\m{a}) \\
0 & \ldots & 0 & 1 & \ldots &0 \\
\vdots & \ddots & \vdots & \vdots & \ddots & \vdots\\
0 & \ldots & 0 & 0 & \ldots & 1
\end{pmatrix} \\
&= \lambda_1 (\mathrm{d}\varphi_1)_{\m{a}} + \ldots + \lambda_m (\mathrm{d}\varphi_m)_{\m{a}},
\end{align*}$$
что и требовалось доказать.
:::