# Дифференциал композиции




:::{prf:theorem}
:name: d(FG)
Пусть $F: \mathbb{R}^n \to \mathbb{R}^k$ дифференцируема в $\m{a} \in \mathbb{R}^n$, $G: \mathbb{R}^k \to \mathbb{R}^m$ дифференцируемо в $\m{b}= F(\m{a})$. Тогда $H: = G \circ F :\mathbb{R}^n \to \mathbb{R}^m$ дифференцируемо в $\m{a}$ и 
$$
(\mathrm{d}H)_\m{a} = (\mathrm{d}G)_{\m{b}} \cdot (\mathrm{d}F)_\m{a},
$$
где подразумевается обычное умножение матриц.
:::


:::{prf:proof}
:class: dropdown
:nonumber:

Так как отображения дифференцируемо, мы имеем
$$
F(\m{a} + \m{h}) - F(\m{a}) = (\mathrm{d}F)_\m{a}(\m{h}) + \alpha(\m{h}) \cdot || \m{h}||,
$$ 
и
$$
G(F(\m{a}) + \m{v})) - G(F(\m{a})) = (\mathrm{d}G)_{F(\m{a})}(\m{v}) + \beta(\m{v}) ||\m{v}||
$$
где $\lim_{\m{h} \to \m{0}_n} \alpha (\m{h}) = \m{0}_k$, $\lim_{\m{v} \to \m{0}_k} \beta (\m{v}) = \m{0}_m$.

Мы можем положить $\beta(\m{0}_k) = \m{0}_m$ или доопределить её таким образом, видно, что на равенства это не повлияет. Тем самым, $\beta$ может считаться непрерывной в $\m{0}_k$.

Пусть $\m{v}: = F(\m{a} + \m{h}) - F(\m{a})$, тогда $G(F(\m{a}) + \m{v})) - G(F(\m{a}) = G(F(\m{a}+\m{h})) -G(F(\m{a}))$. 

Имеем

$$\begin{eqnarray}
G(F(\m{a}+\m{h})) -G(F(\m{a})) &=& (\mathrm{d}G)_{F(\m{a})}\bigl(F(\m{a}+ \m{h}) - F(\m{a})\bigr)  \\
&+& \beta\Bigl( F(\m{a} +\m{h}) - F(\m{a}) \Bigr) \cdot || F(\m{a} + \m{h}) - F(\m{a})|| \\
&=& (\mathrm{d}G)_{F(\m{a})} \Bigl( (\mathrm{d}F)_\m{a}(\m{h}) + \alpha(\m{h}) \cdot || \m{h}||\Bigr) \\
&+& \beta \Bigl(F(\m{a} + \m{h}) - F(\m{a})\Bigr) \cdot \Bigl\| (\mathrm{d}F)_\m{a}(\m{h}) + \alpha(\m{h}) \cdot || \m{h}|| \Bigr\|
\end{eqnarray}$$
из-за линейности $(\mathrm{d}G)_{F(\m{a})}$ получаем
$$\begin{eqnarray}
G(F(\m{a}+\m{h})) -G(F(\m{a})) &=&\Bigl((\mathrm{d}G)_{F(\m{a})} \circ (\mathrm{d}F)_\m{a}\Bigr) (\m{h}) + (\mathrm{d}G)_{F(\m{a})}((\alpha(\m{h})) \cdot || \m{h}|| \\
&+& \beta \Bigl(F(\m{a} + \m{h}) - F(\m{a}) \Bigr) \cdot \Bigl\| (\mathrm{d}F)_\m{a}(\m{h}) + \alpha(\m{h}) \cdot || \m{h}|| \Bigr\|     
\end{eqnarray}$$
вынесем теперь $|| \m{h}||$, получаем
$$\begin{eqnarray}
G(F(\m{a}+\m{h})) -G(F(\m{a})) &=&\Bigl((\mathrm{d}G)_{F(\m{a})} \circ (\mathrm{d}F)_\m{a}\Bigr) (\m{h})\\
&+&\left( (\mathrm{d}G)_{F(\m{a})}\bigl((\alpha(\m{h})\bigr) + \beta \Bigl(F(\m{a} + \m{h}) - F(\m{a}) \Bigr) \cdot \left\| \frac{(\mathrm{d}F)_\m{a}(\m{h})}{|| \m{h} ||} + \alpha(\m{h})  \right\| \right) || \m{h} ||.     
\end{eqnarray}$$

Так как $(\mathrm{d}F)_\m{a}: \mathbb{R}^n \to \mathbb{R}^k$ линейно, то по Лемме [](#linear_is_contious) и Предложению [](#contous_of_linear) оно ограничено, то есть $|| (\mathrm{d}F)_\m{a})(\m{h}) || \le K ||\m{h}||$. Далее, так как $(\mathrm{d}G)_{F(\m{a})}: \mathbb{R}^k \to \mathbb{R}^m$ линейно, то по Лемме [](#linear_is_contious) оно непрерывно, и так как мы положили, что $\beta$ непрерывна в $\m{0}_k$, тогда 
$$\begin{eqnarray}
\lim_{\m{h} \to \m{0}_n}(\mathrm{d}G)_{F(\m{a})}\bigl((\alpha(\m{h})\bigr) &=& (\mathrm{d}G)_{F(\m{a})}\bigl( \lim_{\m{h} \to \m{0}_n} (\alpha(\m{h})\bigr) = \m{0}_m,\\
\lim_{\m{h} \to \m{0}_n} \beta \Bigl(F(\m{a} + \m{h}) - F(\m{a}) \Bigr) &=& \beta (\m{0}_k) = \beta(\m{0}_m). 
\end{eqnarray}$$

Далее, 
$$
\left\| \frac{(\mathrm{d}F)_\m{a}(\m{h})}{|| \m{h} ||} + \alpha(\m{h})  \right\| \le \left\| \frac{(\mathrm{d}F)_\m{a}(\m{h})}{|| \m{h} ||} \right\| + \| \alpha(\m{h}) \| \le K + \| \alpha(\m{h}) \|,
$$
так как $\lim_{\m{h} \to \m{0}_n}\alpha(\m{h}) = \m{0}_k$, то согласно Предложению [](#xn->x=||xn||->||x||), Теореме [](#f<g=>lim):
$$
0 \le \lim_{\m{h} \to \m{0}_n}\left\| \frac{(\mathrm{d}F)_\m{a}(\m{h})}{|| \m{h} ||} + \alpha(\m{h})  \right\| =C \le K.
$$

Итак, пусть
$$
\omega (\m{h}): = \lim_{\m{h} \to \m{0}_n}\left( (\mathrm{d}G)_{F(\m{a})}\bigl((\alpha(\m{h})\bigr) + \beta \Bigl(F(\m{a} + \m{h}) - F(\m{a}) \Bigr) \cdot \left\| \frac{(\mathrm{d}F)_\m{a}(\m{h})}{|| \m{h} ||} + \alpha(\m{h})  \right\| \right),
$$
тогда мы показали, что
$$
\lim_{\m{h} \to \m{0}_n} \omega (\m{h}) = \m{0}_m. 
$$

Окончательно мы получили, что
$$
G(F(\m{a}+\m{h})) -G(F(\m{a})) =\Bigl((\mathrm{d}G)_{F(\m{a})} \circ (\mathrm{d}F)_\m{a}\Bigr) (\m{h}) +   \omega (\m{h}) || \m{h} ||,
$$
что и доказывает утверждение.
:::