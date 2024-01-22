# Дифференциалы высокого порядка

Пусть дана функция $f: \mathbb{R}^n \to \mathbb{R}$ такая, что в открытом $\mathscr{U}$ у неё существуют все её частные производные $f_{x_i}' = \frac{\partial f}{\partial x_i}$. Пусть далее $\mathscr{V} \subseteq \mathscr{U}$ открыто, и пусть всюду в $\mathscr{V}$ её частные производные дифференцируемы, тогда мы получаем:
:::{prf:definition}
Частные производные высокого порядка определяются как частные производные от частных производных, т. е.
$$\begin{eqnarray}
\frac{\partial^2 f}{\partial x_i \partial x_j} &:=& \frac{\partial }{\partial x_i}\left( \frac{\partial f}{\partial x_j} \right) = (f_{x_j}')'_{x_i} =: f''_{x_ix_j}. 
\end{eqnarray}$$
:::

:::{warning}
Выражение (если оно имеет смысл) 
$$
\frac{\partial f}{\partial x_i \partial x_j}
$$
называется **смешанной производной**.
:::

:::{prf:theorem} Шварц 
Пусть $f:\mathbb{R}^2 \to \mathbb{R}$ имеет в окрестности $\mathscr{U}$ точки $\m{a} \in \mathbb{R}^2$ смешанные производные. Если эти производные непрерывны в этой точке, то они равны в этой точке, т. е.
$$
\left.\frac{\partial f}{\partial x \partial y}\right|_\m{a} = \left.\frac{\partial f}{\partial y \partial x}\right|_\m{a}.
$$
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $\m{a} = (a_1,a_2)^\top$, тогда, по определению ([](#partial_i(o))),
$$\begin{eqnarray}
\left. \frac{\partial^2 f}{\partial x \partial y}\right|_\m{a} &=& \left. \frac{\partial}{\partial x}\left( \frac{\partial f}{\partial y} \right) \right|_\m{a} \\
&=& \lim_{t \to 0} \left( \frac{\frac{\partial f}{\partial y}(a_1+t, a_2) - \frac{\partial f}{\partial y}(a_1,a_2)  }{t}  \right) \\
&=& \lim_{t \to 0}\left( \frac{ \lim\limits_{s\to 0} \dfrac{f(a_1+t, a_2 +s) -f(a_1+t,a_2)}{s}  - \lim\limits_{s\to 0} \dfrac{f(a_1,a_2+s) -f(a_1,a_2)}{s} } {t}  \right) \\
&=& \lim_{t\to 0} \lim_{s \to 0} \dfrac{f(a_1+t, a_2 +s) -f(a_1+t,a_2) - f(a_1,a_2+s) +f(a_1,a_2)}{ts} \\
&=&\lim_{t\to 0} \lim_{s \to 0} \frac{\Phi(t,s)}{ts},
\end{eqnarray}$$
где 
$$
\Phi(t,s):= f(a_1+t, a_2 +s) -f(a_1+t,a_2) - f(a_1,a_2+s) +f(a_1,a_2).
$$

Аналогично, получаем
$$
\left. \frac{\partial^2 f}{\partial y \partial x}\right|_\m{a} =  \lim_{s\to 0} \lim_{t \to 0} \frac{\Phi(t,s)}{ts}.
$$

Пусть 
$$\begin{eqnarray}
u(\tau) &: =& f(a_1 + \tau, a_2 + s) - f(a_1+ \tau, a_2), \qquad (a_1 + \tau, a_2) \in \mathscr{U} ,\\
v(\sigma) &: =& f(a_1 + t, a_2 + \sigma) - f(a_1, a_2+\sigma), \qquad (a_1, a_2+\sigma) \in \mathscr{U} ,
\end{eqnarray}$$

тогда
$$
\Phi(t,s) = u(t) - u(0) = v(s) - v(0).
$$

Далее, так как по условию, $f$ имеет смешанные производные, значит она имеет и частные производные, а это значит, что $u(\tau)$, $v(\sigma)$ — дифференцируемы на отрезках $[0,t]$ и $[0,s]$, соответственно. Тогда, по теореме Лагранжа [](#Langrange) найдутся такие $\tau_0 \in (0, t)$ и $\sigma_0 \in (0, s)$, что
$$\begin{eqnarray}
\Phi(t,s) &=& u(t) - u(0) = u'(\tau_0)t,\\
\Phi(t,s) &=& v(s) - v(0) = v'(\sigma_0)s.
\end{eqnarray}$$

С другой стороны, 
$$\begin{eqnarray}
u'(\tau_0) &=& \frac{\partial}{ \partial x}\Bigl( f(a_1 + \tau_0, a_2 + s) - f(a_1+ \tau_0, a_2)\Bigr) \\
&=& f'_x(a_1 + \tau_0, a_2 + s) - f'_x(a_1+ \tau_0, a_2).
\end{eqnarray}$$

Аналогично, находим
$$\begin{eqnarray}
v'(\sigma_0) &=& \frac{\partial}{ \partial y}\Bigl( f(a_1+t, a_2 + \sigma_0) - f(a_1, a_2+\sigma_0)\Bigr) \\
&=& f'_y(a_1 + t, a_2 + \sigma_0) - f'_x(a_1, a_2+\sigma_0).
\end{eqnarray}$$

Пусть теперь
$$\begin{eqnarray}
w(\alpha) &:=& f'_y(a_1 + \alpha, a_2 + \sigma_0), \qquad 0 \le \alpha \le t \\
g(\beta) &: =& f'_x(a_1 + \tau_0, a_2 + \beta), \qquad 0 \le \beta \le s.
\end{eqnarray}$$

Тогда
$$\begin{eqnarray}
w(t)- w(0) &=& f'_y(a_1 + t, a_2 + \sigma_0) - f'_x(a_1, a_2+\sigma_0)= v'(\sigma_0),\\
g(s) - g(0) &=& f'_x(a_1 + \tau_0, a_2 + s) - f'_x(a_1+ \tau_0, a_2) = u'(\tau_0).
\end{eqnarray}$$

По условию, $f$ имеет смешанные частные производные на $\mathscr{U}$, тогда это значит, что $w$ и $g$ дифференцируемы на отрезках $[0,t]$ и $[0,s]$ соответственно. Тогда по теореме Лагранжа [](#Langrange), существуют такие $\alpha_0 \in (0,t)$ и $\beta_0 \in (0,s)$, что
$$\begin{eqnarray}
w(t)- w(0) &=& w'(\alpha_0) t = f''_{xy}(a_1+\alpha_0, a_2+\sigma_0)ts,\\
g(s) -g(0) &=& g'(\beta_0)s = f''_{yx}(a_1 + \tau_0,a_2+\beta_0)ts.
\end{eqnarray}$$

Таким образом, получаем
$$\begin{eqnarray}
\Phi(t,s) &=& u'(\tau_0)t \\
&=& (g(s) - g(0))t \\
&=& g'(\beta_0)ts \\
&=& f''_{yx}(a_1 + \tau_0,a_2+\beta_0)st
\end{eqnarray}$$
и
$$\begin{eqnarray}
\Phi(t,s) &=& v'(\sigma_0)s \\
&=& (w(t) - w(0))s \\
&=& w'(\alpha_0)st \\
&=& f''_{xy}(a_1 + \alpha_0,a_2+\sigma_0)st.
\end{eqnarray}$$

Ясно, что если $t,s \to 0$ то и $\alpha_0, \beta_0, \tau_0, \sigma_0 \to 0$, но тогда из-за предположения о непрерывности смешанных производных получаем
$$\begin{eqnarray}
\lim_{t\to 0} \lim_{s \to 0} \frac{\Phi(t,s)}{ts} &=&  \lim_{t\to 0} \lim_{s \to 0} f''_{xy}(a_1 + \alpha_0,a_2+\sigma_0) \\
&=& \lim_{t \to 0} f''_{xy}(a_1 + \alpha_0,a_2) \\
&=& f''_{xy}(a_1,a_2),
\end{eqnarray}$$
и
$$\begin{eqnarray}
\lim_{s\to 0} \lim_{t \to 0} \frac{\Phi(t,s)}{ts} &=& \lim_{s\to 0} \lim_{t \to 0}f''_{yx}(a_1 + \tau_0,a_2+\beta_0)\\
&=& \lim_{s\to 0}f''_{yx}(a_1,a_2+\beta_0) \\
&=& f''_{yx}(a_1,a_2),
\end{eqnarray}$$
что и доказывает утверждение.     
:::


:::{prf:theorem} Юнг 
:name: Yong
Пусть у функции $f:\mathbb{R}^2 \to \mathbb{R}$ в окрестности в точке $\m{a} = (a_1,a_2)^\top$ существуют частные производные $f'_{x}$ и $f'_{y}$. Если эти частные производные дифференцируемы в точке $\m{a}$, то
$$
f''_{xy}(a_1,a_2) = f''_{yx}(a_1,a_2).
$$
:::

%Нужно сказать про отличие от предыдущей.

:::{prf:proof}
:class: dropdown
:nonumber:
Сохраним те же обозначения, как и в доказательстве предыдущей теоремы и рассмотрим 
$$
\Phi(t,t):= f(a_1+t, a_2 +t) -f(a_1+t,a_2) - f(a_1,a_2+t) +f(a_1,a_2).
$$

Повторим те же рассуждения, что и в предыдущем доказательстве. 

Пусть 
$$\begin{eqnarray}
u(\tau) &: =& f(a_1 + \tau, a_2 + t) - f(a_1+ \tau, a_2), \qquad (a_1 + \tau, a_2) \in \mathscr{U} ,\\
v(\tau) &: =& f(a_1 + t, a_2 + \tau) - f(a_1, a_2+\tau), \qquad (a_1, a_2+\sigma) \in \mathscr{U} ,
\end{eqnarray}$$

тогда
$$
\Phi(t,t) = u(t) - u(0) = v(t) - v(0).
$$

Далее, так как по условию $f$ имеет смешанные производные, значит, она имеет и частные производные, а это значит, что $u(\tau)$, $v(\tau)$  дифференцируемы на отрезке $[0,t]$. Тогда по теореме Лагранжа [](#Langrange) найдётся такое $\tau_0 \in (0, t)$, что
$$\begin{eqnarray}
\Phi(t,t) &=& u(t) - u(0) = u'(\tau_0)t,\\
\Phi(t,t) &=& v(t) - v(0) = v'(\tau_0)t.
\end{eqnarray}$$

По условию $f'_x$, $f'_y$ дифференцируемы в окрестности точки $\m{a}$, тогда
$$\begin{eqnarray}
f'_x(\m{a} + \m{h}) &=& f'_x(\m{a}) + (\mathrm{d}f_x')_\m{a} \m{h} + o(\m{h}), \\
f'_y(\m{a} + \m{h}) &=& f'_y(\m{a}) + (\mathrm{d}f_y')_\m{a} \m{h} + o(\m{h}),
\end{eqnarray}$$
при $\m{h} \to \m{0}.$

Тогда получаем
$$\begin{eqnarray}
u'(\tau_0) &=& f'_x(a_1 + \tau_0, a_2 + t) - f'_x(a_1+ \tau_0, a_2) \\
&=& f'_x(a_1,a_2) + \begin{pmatrix}
f''_{xx}(a_1,a_2) & f''_{xy}(a_1,a_2) 
\end{pmatrix} \begin{pmatrix}
\tau_0 \\ t
\end{pmatrix} + \omega_1(\tau_0, s) \sqrt{\tau_0^2 +t^2} \\
&& - f_x'(a_1,a_2) - \begin{pmatrix}
f''_{xx}(a_1,a_2) & f''_{xy}(a_1,a_2) 
\end{pmatrix} \begin{pmatrix}
\tau_0 \\ 0
\end{pmatrix} - \omega_2(\tau_0, 0) \sqrt{\tau_0^2 +0^2} \\
&=& f''_{xy}(a_1,a_2) t + \omega_1(\tau_0, t) \sqrt{\tau_0^2 +t^2}- \omega_2(\tau_0, 0) |\tau_0|.
\end{eqnarray}$$

Аналогично, получаем
$$\begin{eqnarray}
v'(\tau_0) &=& f'_y(a_1 + t, a_2 + \tau_0) - f'_y(a_1, a_2+\tau_0) \\
&=& f_y'(a_1, a_2) + \begin{pmatrix}
f''_{yx}(a_1,a_2) & f''_{yy}(a_1,a_2) 
\end{pmatrix} \begin{pmatrix} t\\ \tau_0
\end{pmatrix} + \omega_3(t,\tau_0)\sqrt{t^2 +\tau_0^2} \\
&&- f'_y(a_1,a_2) - \begin{pmatrix}
f''_{yx}(a_1.a_2) & f''_{yy}(a_1,a_2)
\end{pmatrix} \begin{pmatrix}
0 \\ \tau_0
\end{pmatrix} - \omega_4(0,\tau_0)|\tau_0| \\
&=& f''_{yx}(a_1,a_2)t + \omega_3(t,\tau_0)\sqrt{t^2 +\tau_0^2} - \omega_4(0,\tau_0)|\tau_0|.
\end{eqnarray}$$

Так как $\Phi(t,t) = u'(\tau_0)t = v'(\tau_0)t$, то мы получаем
$$
\Bigl( f''_{xy}(a_1,a_2) t + \omega_1(\tau_0, t) \sqrt{\tau_0^2 +t^2}- \omega_2(\tau_0, 0) |\tau_0| \Bigr) t = \Bigl( f''_{yx}(a_1,a_2)t + \omega_3(t,\tau_0)\sqrt{t^2 +\tau_0^2} - \omega_4(0,\tau_0)|\tau_0| \Bigr)t,
$$
разделим обе части равенства на $t^2$
$$
f''_{xy}(a_1,a_2) + \omega_1(\tau_0, t) \sqrt{1+ \left(\frac{\tau_0}{t}\right)^2}- \omega_2(\tau_0, 0) \frac{|\tau_0|}{t}=  f''_{yx}(a_1,a_2) + \omega_3(t,\sigma_0)\sqrt{1 +\left(\frac{\sigma_0}{t}\right)^2} - \omega_4(0,\sigma_0)\frac{|\sigma_0|}{t},
$$


Ввиду того, что $0 \tau_0 <t$, то $\sqrt{t^2 + (\frac{\tau_0}{t})^2}$, $\frac{\tau_0}{t}$ — ограниченные функции, и так как $\omega_1, \omega_2, \omega_3, \omega_4 \in o(1)$ при $t \to 0$, мы получаем равенство
$$
f''_{xy}(a_1,a_2) =  f''_{yx}(a_1,a_2),
$$
что и требовалось доказать.    
:::


:::{prf:definition}
Пусть $f:\mathbb{R}^n \to \mathbb{R}$ — дифференцируема в окрестности точки $\m{a}$. Говорят, что $f$ **дважды дифференцируема в точке $\m{a}$**, если все её частные производные $f'_{x_i}$ дифференцируемы в точке $\m{a}$.

Пусть $f$ — $m$ раз дифференцируема в окрестности точки $\m{a}$. Говорят, что **$f$ есть $m+1$ раз дифференцируемой в точке $\m{a}$**, если все частные производные $m$-го порядка $\frac{\partial^m f}{\partial x_{i_1} \cdots \partial x_{i_m}}$ дифференцируемы в точке $\m{a}$.
:::

:::{prf:corollary}
:name: f''xy=f''yx
Если $f:\mathbb{R}^n \to \mathbb{R}$ есть $m$-раз дифференцируема в точке $\m{a}$, то значения производных порядка $m$ не зависят от порядка дифференцирования.
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Это следует из теоремы Юнга [](#Yong) с помощью индукции.


:::