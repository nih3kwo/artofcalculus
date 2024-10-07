# Интеграл ступенчатой функции

Предыдущее "определение" интеграла имеет очень много недостатков. Например, мы пользовались интуитивным пониманием площади криволинейной трапеции. 

Здесь мы дадим строгое определение интеграла.

## Разбиение промежутка

Напомним, что под промежутком мы понимаем подмножество прямой $\mathbb{R}$ одного из видов; $[a,b]$, $[(a,b]$, $[a,b)$, $(a,b)$, при этом мы считаем, что $|a|,|b| < \infty.$ Промежуток мы будем обозначать буквами $I$ или $J$, а под **длиной промежутка** будем понимать выражение, $b-a$ и если $I$ один из рассмотренных промежутков, то будем писать $|I|: = b-a.$

:::{warning}
Нам также будет полезно рассматривать пустой промежуток $I$ или, если он содержит всего одну точку, то в таком случае полагаем $|I|:=0$.
:::

:::{prf:definition}
:name: definition-4-11
Пусть $I$ — промежуток, под **разбиением** промежутка $I$ понимается **конечное** множество $\lambda(I)$ промежутков содержащихся в $I$, при этом любой $x \in I$ принадлежит одному и только одному промежутку из $\lambda.$
:::

:::{prf:example}
Пусть $I = [1,8]$, тогда следующее множество
$$
\lambda(I) : = \{ \varnothing, \{1\}, (1,3), [3,5), \{5\}, (5,8]  \}
$$
есть разбиение промежутка $I = [1,8]$, потому что любой $x \in I$ лежит в одном и только в одном из перечисленных подмножеств множества $\lambda(I)$. А если же мы положим, что
$$
\lambda'(I): = \{ \varnothing, \{1\}, [1,3), (2,7), [3,5), \{5\}, (5,8] \}
$$
то мы уже получаем не разбиение, поскольку, например, точка $2.5 \in [1,3)$ и $2.5 \in (2,7)$.

Множество $\lambda''(I) := \{[1,4), (4,8]\}$ тоже не является разбиением промежутка $I = [1,8]$ так как $4$ не принадлежит ни одному из подмножеств множества $\lambda''(I)$. Наконец, множество $\lambda'''(I) := \{(0,5], (5,8]\}$ также не является разбиением промежутка $I = [1,8]$, потому что $(0,5]$ не содержится в $I.$
:::

:::{warning}
Заметим, что пустое множество может не входить в разбиение промежутка. 
:::


:::{prf:theorem}[Конечная аддитивность длины]
Пусть $I\subsetneq \mathbb{R}$ — промежуток, а $\lambda(I)$ — его разбиение, тогда
$$
|I| = \sum_{A \in \lambda(I)}|A|.
$$
:::
:::{prf:proof}
:class: dropdown
:nonumber:
Доказывать будем по индукции, а именно по мощности разбиения. То есть для всех разбиений, в которых ровно $n$ элементов верна формула $|I| = \sum_{A \in \lambda(I)}|A|$.

(1) Если $n =0$ то значит, что $I = \varnothing$, так как любое его разбиение не должно иметь непустых элементов, но тогда формула очевидна.

(2) Если $n=1$, то это значит, что любое его разбиение имеет ровно один непустой элемент, а это значит, что $I = \{a\}$ — одноточечное множество, но и в таком случае формула тоже очевидна.

(3) Пусть формула верна для любых разбиений, в которых ровно $n\ge 1$ элементов. И допустим теперь, что у промежутка $I$ имеются разбиения, у которых $n+1$ элементов. Именно для таких разбиений мы будем доказывать формулу. Случаи, когда $I = \varnothing$ или же когда $I = \{a\}$ очень просты для рассмотрения, так как тогда все разбиения либо содержат пустое множество, либо пустое и одноточечное.

Итак, пусть $I$ — это одно из четырёх множеств $(a,b), (a,b], [a,b), [a,b]$.

Допустим, что $b \in I$ тогда $I$ — это либо $(a,b]$, либо $[a,b]$. Рассмотрим произвольное разбиение $\lambda(I)$, в котором ровно $n+1$ элементов, тогда должен найтись ровно один элемент, скажем, $B$, который содержит $b$.

С другой же стороны, $B \subseteq I$, а тогда $B$ имеет либо вид $(c,b]$, либо $[c,b]$ или же $\{b\}$, где $a \le c \le b$. Для удобства можно считать, что в последнем случае $c =b$.

Рассмотрим теперь множество $I \setminus B$, которое имеет вид либо $[a,c]$, либо $(a,c)$, либо $(a,c]$, или $[a,c)$, когда $c >a$, или же $I \setminus B$ — это точка или пустое множество. Другими словами, $I\setminus B$ — это промежуток. 

Далее, так как $I = B \cup I \setminus B$ и $B \cap I \setminus B = \varnothing$, то множество $\lambda(I) \setminus B$ является разбиением промежутка $I\setminus B$. 

Таким образом, разбиение $\lambda(I)\setminus B$ содержит уже $n$ элементов. Но согласно предположению, для промежутка $I \setminus B$ верна формула
$$
|I \setminus B| = \sum_{K \in \lambda(I) \setminus B} |K|
$$

Воспользовавшись теперь равенством,
$$
|I| =|B| + |I \setminus B|
$$
мы получим

$$
|I| = |B| + |I \setminus B| = |B| + \sum_{K \in \lambda(I) \setminus B} |K| = \sum_{A \in \lambda(I)} |A|.
$$

(4) Осталось рассмотреть случай, когда $b \notin I$, но тогда $I$ это либо $(a,b)$ либо $[a,b)$ и существует один из элементов множества $\lambda(I)$ который имеет вид либо $(c,b)$ или же $[c,b)$. Это означает, что вид множества $I \setminus B$ может принять одно из четырёх значений $[a,c]$, $(a,c)$, $(a,c]$, $[a,c)$ когда $c >a$ или же это точка или пустое множество. Остальная часть рассуждения продолжается как выше. 
:::

Эту теорему легко обобщить следующим образом.
:::{prf:lemma}
:name: additive_of_a-lenght
Пусть $\alpha: I \to \mathbb{R}$ — непрерывная функция, а $I$ — ограниченный промежуток одного из вида $(a,b), [a,b], (a,b], [a,b)$, тогда положим
$$
\alpha(I): = \alpha(b) - \alpha(a).
$$
Тогда для любого разбиения $\lambda(I)$ имеем
$$
\alpha(I) = \sum_{A \in \lambda(I)}\alpha(A).
$$
:::

:::{prf:proof} Набросок доказательства
:class: dropdown
:nonumber:
Рассуждения такие же как и в предыдущей лемме, но нужно использовать очевидное наблюдение, если $B  = [c,b] \subseteq I = [a,b]$, то $I\setminus B = [a,c)$ и тогда
$$\begin{align*}
\alpha(B) + \alpha(I \setminus B) &= \alpha(b) - \alpha (c) + \alpha (c) + \alpha(a) \\
&= \alpha(b) -\alpha(a) \\
&= \alpha(I).
\end{align*}$$
:::

## Ступенчатые функции

Сейчас мы опишем класс функций, которые ``очень просты'' для интегрирования[^ref43-1], а потом с помощью их мы уже определим интеграл в общем виде.  

:::{prf:definition}
Пусть $A \subseteq \mathbb{R}$, и пусть дана функция $f: A \to \mathbb{R}$. Говорят, что $f$ **постоянная функция**, если существует такое $\alpha \in \mathbb{R}$, что $f(x) = \alpha$ для всех $x \in A$. Если $B \subseteq A$, то говорят, что $f$ **постоянная на $B$**, если существует такое $\beta \in \mathbb{R}$, что $f(y) = \beta$ для всех $y \in B.$
:::


:::{warning}
Из этого определения следует, что если функция $f$ постоянна на **непустом** множестве $A$, то она не может принимать два или более разных значения. Однако из определения пустого множества следует, что постоянная функция на пустом множестве может принимать **любое значение!**
:::

:::{prf:definition}
Пусть дан промежуток $I \subsetneq \mathbb{R}$, и пусть дана функция $f: I \to \mathbb{R}$, и пусть $\lambda(I)$ — какое-то разбиение промежутка $I$. Говорят, что **функция $f$ есть ступенчатая функция на $I$ относительно $\lambda(I)$**, если для каждого $J \in \lambda(I)$, $f$ является постоянной на $J$. 
:::

:::{prf:example}
:name: int_1,6=10
Пусть $I = [1,6]$ и определим функцию $f: [1,6]: \to \mathbb{R}$ следующим образом
$$
f(x) = \begin{cases}
\,7, & 1 \le x < 3 \\
\,4, & x = 3 \\
\,5, & 3 < x <6 \\
\,2, & x = 6.
\end{cases}
$$
Тогда, если мы рассмотрим разбиение
$$
\lambda(I) := \Bigl\{[1,3), \{3\}, (3,6), \{6\} \Bigr\}
$$
промежутка $I$, то получаем, что $f$ — ступенчатая функция относительно этого разбиения. Рассмотрим теперь другое разбиение этого же промежутка
$$
\lambda'(I) : = \Bigl\{\varnothing, [1,2), \{2\}, (2,3), \{3\}, (3,5), [5,6),\{6\} \Bigr\}.
$$
Тогда несложно видеть, что $f$ будет тоже ступенчатой относительно этого разбиения. 
:::

Этот пример показывает, что понятие ступенчатой функции можно определить без привлечения разбиения промежутка.

:::{prf:definition}
:name: fiber
Пусть $I$ — промежуток, и пусть $\lambda(I)$, $\lambda'(I)$ — два его разбиения. Говорят, что разбиение $\lambda'(I)$ **тоньше**, чем $\lambda(I)$, если для каждого $J' \in \lambda'(I)$ найдётся такой $J \in \lambda(I)$, что $J' \subseteq J$.
:::

:::{prf:example}
Вернёмся к предыдущему примеру с промежутком $I = [1,6]$ и разбиениями   
$$\begin{align*}
\lambda(I) &:=& \Bigl\{[1,3), \{3\}, (3,6), \{6\} \Bigr\},\\
\lambda'(I) &: =& \Bigl\{\varnothing, [1,2), \{2\}, (2,3), \{3\}, (3,5), [5,6),\{6\} \Bigr\}.
\end{align*}$$

Тогда видно, что $\lambda'(I)$ тоньше, чем $\lambda(I)$.
:::

(def412)=
:::{prf:definition}
Пусть дан промежуток $I \subsetneq \mathbb{R}$ и пусть дана функция $f: I \to \mathbb{R}$. Говорят, что функция $f$ **ступенчатая на $I$**, если существует такое разбиение $\lambda(I)$, что $f$ — постоянная на $I$ относительно $\lambda(I).$
:::


:::{prf:lemma}
:name: fiber_for_functions
Пусть $I \subsetneq \mathbb{R}$ — промежуток и пусть $f:I \to \mathbb{R}$ — ступенчатая функция относительно разбиения $\lambda(I)$, тогда если имеем разбиение $\lambda'(I)$, которое тоньше, чем $\lambda(I)$, то $f$ — ступенчатая относительно $\lambda'(I).$ 
:::

:::{prf:proof}
:class: dropdown
:nonumber:
Действительно, пусть $A' \in \lambda'(I)$ — произвольный элемент разбиения, тогда найдётся такой $A \in \lambda(I)$, что $A' \subseteq A$. Тогда если $f(x) = \alpha$ для всех $x \in A$, то и $f(x') = \alpha$ для всех $A'.$
:::

:::{warning}
Таким образом, мы будем рассматривать просто ступенчатые функции на промежутке, не определяя какое-то конкретное разбиение.
:::


В связи с этим уместно ввести следующее важное для дальнейшего определение.

:::{prf:definition}
**Характеристической функцией** некоторого множества $A \subseteq X$ называется функция $\chi_A: X\to \{0,1\}$ определённая следующим образом
$$
\chi_A(x): = \begin{cases}
1 & x \in A, \\
0 & x \notin A.
\end{cases}
$$
:::

:::{prf:remark}
Таким образом, если $f: I \to \mathbb{R}$ — ступенчатая функция на промежутке $I$ и пусть $\lambda(I)$ — соответствующее разбиение промежутка $I$, тогда мы можем записать
$$
f =\sum_{A \in \lambda(I)} f(A) \cdot \chi_A.
$$
:::

:::{warning}
Из определения следует, что $\chi_{\varnothing} = 0$, так как не существует такого $x$ чтобы $x \in \varnothing.$
:::


:::{prf:lemma}
:name: chi_A+chi_B
Пусть $A$, $B$ два подмножества множества $X$, тогда 
$$\begin{align*}
\chi_{A \cup B} = \chi_A + \chi_B - \chi_{A\cap B},\\
\chi_{A \cap B} = \chi_A \cdot \chi_B,\\
\chi_{A^c} = 1 - \chi_A.
\end{align*}$$
:::

:::{prf:proof}
:class: dropdown
:nonumber: 

(1) Пусть $x \in A\cap B$, то $x\in A$, $\chi_B$, **т.е.,** $\chi_A(x) = \chi_B(x) = 1$. Если $x \notin A \cup B$, то $x\notin A$, $x\notin B$ и тогда $\chi_A(x) = \chi_B(x) = 0$. В любом из этих случаев имеем $\chi_{A \cap B}(x) = \chi_A(x) \cdot \chi_B(x).$ 

(2) Пусть $x \in A^c$, тогда $x\notin A$, тогда **т.е.,** $\chi_{A^c}=1$, $\chi_A(x) = 0$. Если $x \notin A^c$, то $x \in A$, **т.е.,** $\chi_{A^c}=0$, $\chi_A(x) = 1$, что и доказывает формулу $\chi_{A^c} = 1 - \chi_A.$

(3) Наконец, так как $(A \cup B)^c = A^c \cap A^c$, то используя результаты выше, получаем
$$\begin{align*}
\chi_{A \cup B} &= 1 - \chi_{(A\cup B)^c} \\
&= 1 - \chi_{A^c \cap B^c} \\
&= 1- \chi_{A^c} \cdot \chi_{B^c} \\
&= 1 - (1- \chi_A)(1-\chi_B) \\
&= 1 - (1-\chi_B - \chi_A + \chi_{A}\cdot \chi_B) \\
&= 1 - 1 + \chi_A + \chi_B - \chi_{A \cap B} \\
&=\chi_A + \chi_B - \chi_{A \cap B}.
\end{align*}$$
:::


:::{prf:example}

Вернёмся к примеру [](#int_1,6=10), имеем $I = [1,6]$ и функцию $f: [1,6]: \to \mathbb{R}$;
$$
f(x) = \begin{cases}
\,7, & 1 \le x < 3 \\
\,4, & x = 3 \\
\,5, & 3 < x <6 \\
\,2, & x = 6.
\end{cases}
$$
Как мы уже видели, $f$ — ступенчатая относительно разбиений
\begin{align*}
&  \lambda(I) := \Bigl\{[1,3), \{3\}, (3,6), \{6\} \Bigr\},\\
&  \lambda'(I) : = \Bigl\{\varnothing, [1,2), \{2\}, (2,3), \{3\}, (3,5), [5,6),\{6\} \Bigr\}.
\end{align*}

Тогда получаем, что
$$
f = 7 \cdot \chi_{[1,3)} + 4 \cdot \chi_{\{3\}} + 5 \cdot \chi_{(3,6)} + 2 \cdot \chi_{\{6\}},  
$$
а также
$$
f = \alpha \cdot \chi_{\varnothing} + 7 \cdot \chi_{[1,2)} + 7 \cdot \chi_{\{2\}} + 7 \cdot \chi_{(2,3)} + 4 \cdot \chi_{\{3\}} + 5 \cdot \chi_{(3,5)} + 5 \cdot \chi_{[5,6)} + 2 \cdot \chi_{\{6\}},
$$
где $\alpha \in \mathbb{R}$ — произвольное число, но так как $\chi_\varnothing = 0$, то всё корректно.
:::

:::{prf:proposition}
:name: beautefull
Пусть имеем две ступенчатые функции $f,g:I \to \mathbb{R}$ и пусть $\lambda_f(I) = \cup_{p=1}^n A_p$, $\lambda_g(I) = \cup_{q=1}^m B_q$ — разбиения промежутка $I$ такие, что $f$, $g$ — ступенчаты относительно $\lambda_f(I)$ и $\lambda_g(I)$ соответственно. Тогда $\lambda(I): = \cup_{p=1}^n \cup_{q=1}^m A_p \cap B_q$ — разбиение промежутка $I$, и более того каждая из функций $f,g$ ступенчата относительно него[^ref43-2] и
\begin{align*}
& f =  \sum_{p=1}^n\sum_{q=1}^m f(A_p) \cdot \chi_{A_p}\cdot \chi_{B_q}\\
& g=  \sum_{p=1}^n\sum_{q=1}^m g(B_q) \cdot \chi_{A_p} \cdot \chi_{B_q}.
\end{align*}
:::

:::{prf:proof}
:class: dropdown
:nonumber: 

Покажем, что это разбиение. Так как $I = \cup_{p=1}^n A_p = \cup_{q= 1}B_q$, то
$$
\cup_{p=1}^n \cup_{q=1}^m A_p \cap B_q  = \left( \cup_{p=1}^n A \right) \cap \left( \cup_{q=1}^m B_q \right) = I \cap I = I,
$$
в силу того, что $A_p \cap A_{p'} = \varnothing$ и $B_q \cap B_{q'} = \varnothing$, то $(A_p \cap B_q) \cap (A_{p'}\cap B_{q'}) = \varnothing$, $1\le p \le n$, $1\le q \le m$. Поэтому $\lambda(I)$ — разбиение промежутка $I$.


Далее, так как $\lambda_f(I)$, $\lambda_g(I)$ разбиения, то для любых $1\le p \le n$, $1\le q \le m$, имеем
$$
A_p = \cup_{q=1}^m (A_p \cap B_q), \qquad B_q = \cup_{p=1}^n (A_p \cap B_q).
$$

Наконец, так как $\chi_\varnothing = \varnothing$, и пользуясь леммой [](#chi_A+chi_B), получаем
$$\begin{align*}
f &= \sum_{p=1}^n f(A_p) \cdot \chi_{A_p} \\
&= \sum_{p=1}^n\sum_{q=1}^m f(A_p) \cdot \chi_{ \cup_{q=1}^m (A_p \cap B_q)} \\
&= \sum_{q=1}^m f(A_p) \cdot \left(\chi_{A_p \cap B_1} + \cdots + \chi_{A_p \cap B_m} \right) \\
&= \sum_{p=1}^n\sum_{q=1}^m f(A_p) \cdot \chi_{A_p \cap B_q}.
\end{align*}$$

Аналогично доказывается формула для функции $g.$

:::


:::{prf:corollary}
:name: cor_for_sum
Пусть $I \subsetneq \mathbb{R}$ — промежуток и пусть $f,g:I \to \mathbb{R}$ — ступенчатые функции на нём. Тогда функции
$$
f\pm g, \quad \max\{f,g\}, \quad f\cdot g
$$
тоже ступенчатые на $I$. Если $g(x) \ne 0$ при $x \in I$, то $\frac{f}{g}$ тоже ступенчатая функция на $I.$    
:::


:::{prf:proof}
:class: dropdown
:nonumber:

Пусть $\lambda_f(I)  =  \cup_{p=1}^n A_p$, $\lambda_g(I) =  \cup_{q=1}^m B_q$ — разбиения промежутка $I$ относительно которых $f$, $g$ — ступенчаты, соответственно. Согласно предложению [](#beautefull),
\begin{align*}
& f =  \sum_{p=1}^n\sum_{q=1}^m f(A_p) \cdot \chi_{A_p}\cdot \chi_{B_q}\\
& g=  \sum_{p=1}^n\sum_{q=1}^m g(B_q) \cdot \chi_{A_p} \cdot \chi_{B_q}.
\end{align*}

Тогда, получаем
$$\begin{align*}
f \pm g &= \sum_{p=1}^n\sum_{q=1}^m (f(A_p) \pm g(B)q) \cdot \chi_{A_p}\cdot \chi_{B_q} \\
\max\{f ,g\} &= \sum_{p=1}^n\sum_{q=1}^m \max\{f(A_p), g(B)q)\} \cdot \chi_{A_p}\cdot \chi_{B_q},\\
f \cdot g &= \sum_{p=1}^n\sum_{q=1}^m (f(A_p) \cdot g(B)q) \cdot \chi_{A_p}\cdot \chi_{B_q},\\
\frac{f}{ g} &= \sum_{p=1}^n\sum_{q=1}^m \left(\frac{f(A_p)}{ g(B_q)}\right) \cdot \chi_{A_p}\cdot \chi_{B_q},\qquad g \ne 0,
\end{align*}$$
что и требовалось доказать.
:::

## Интеграл от ступенчатой функции на промежутке

Итак, у нас всё готово, чтобы ввести следующее важное определение.

:::{prf:definition}
:label: int_of_p.c_on_I
Пусть $I \subsetneq \mathbb{R}$ — промежуток, $\lambda(I)$ — разбиение промежутка $I$ и пусть $f:I \to \mathbb{R}$ — ступенчатая функция относительно этого разбиения, **т.е.,** $f = \sum_{A \in \lambda(I)}f(A) \cdot \chi_A$. Определим **интеграл на промежутке $I$** ступенчатой функции $f:I \to \mathbb{R}$ относительно разбиения $\lambda(I)$ следующим образом
$$
\int_{\lambda(I)}f: =  \sum_{A \in \lambda(I)} f(A)\cdot |A|
$$
:::

:::{warning}
Во-первых, что стоит слева от равно нужно понимать как символ и не более того! Во-вторых, это определение может показаться некорректным если $\lambda(I)$ содержит пустое множество, но так как $|\varnothing| = 0$, то мы на самом деле получаем корректное определение.     
:::

:::{prf:remark}
:name: int_via_chi
Если $f = \chi_I$, и взяв разбиение $\lambda(I) = \{I\}$ то мы получаем следующее
$$
\int_{\lambda(I)}\chi_I = |I|.
$$
И тогда мы можем записать, что если $f = \sum_{A \in \lambda(I)}f(A) \cdot \chi_A$, то
$$
\boxed{
\int_{\lambda(I)}f = \sum_{A \in \lambda(I)} f(A) \cdot \int_{\lambda(I)}\chi_A
}
$$
:::


:::{prf:example}
:name: int_1,4=10
Пусть $f: [1,4] \to \mathbb{R}$ определена следующим образом
$$
f(x)  = \begin{cases}
\, 2 & 1 \le x <3 \\
\, 4 & x = 3 \\
\, 6 & 3< x \le 4
\end{cases}
$$
и пусть $\lambda(I) = \{ [1,3), \{3\}, (3,4] \}$, тогда
$$\begin{align*}
\int_{\lambda(I)} f  &= \alpha_{[1,3)}\cdot | [1,3) | + \alpha_{\{3\}}\cdot |\{3\}| + \alpha_{(3,4]} \cdot | (3,4] | \\
&= 2 \cdot 2 + 4 \cdot 0 + 6 \cdot 1 \\
&= 10.
\end{align*}$$

С другой стороны, рассмотрим такое разбиение $\lambda'(I) = \{ \varnothing, [1,2), [2,3), \{3\}, (3,4] \}$, нетрудно видеть, что оно тоньше разбиения $\lambda(I)$. Находим
$$\begin{align*}
\int_{\lambda'(I)}f &=\alpha_\varnothing \cdot |\varnothing| + \alpha_{[1,2)} \cdot | [1,2) | + \alpha_{[2,3)} \cdot |[2,3)| + \alpha_{\{3\}}\cdot |\{3\}| + \alpha_{(3,4]} \cdot | (3,4] | \\
&= \alpha_\varnothing \cdot 0 + 2 \cdot 1 + 2 \cdot 1 + 4 \cdot 0 + 6 \cdot 1 \\
&= 10.
\end{align*}$$

:::

Итак, мы увидели, что, взяв разбиение тоньше, значение интеграла не изменилось, очевидно, что это верно и в общем случае.

:::{prf:lemma}
Пусть $I \subsetneq \mathbb{R}$ — промежуток и пусть $f:I \to \mathbb{R}$ — ступенчатая функция относительно разбиения $\lambda(I)$, тогда если имеем разбиение $\lambda'(I)$, которое тоньше, чем $\lambda(I)$, то
$$
\int_{\lambda(I)}f = \int_{\lambda'(I)}f.
$$
:::

(theorem-4-11)=
:::{prf:proof}
:class: dropdown
:nonumber:
Пусть $\lambda(I) = \{ A_1,\ldots, A_n \}$ и пусть 
$$
\lambda'(I) : = \Bigl\{A_{11}', \ldots, A'_{1\ell_1},\ldots, A'_{n1},\ldots, A'_{n\ell_n} \Bigr\},
$$
где $A_i$ содержит только $A'_{i1},\ldots, A'_{i\ell_i}$, $1\le i \le n$. Из определения [](#fiber) тогда следует, что $A_i = A'_{i1} \cup \cdots \cup A'_{i\ell_i}$ и $|A_i| = |A'_{i1}| + \cdots + |A'_{i\ell_i}|$.

Наконец, используя лемму [](#fiber_for_functions), получаем, что
$$
f(A'_{i1}) = \cdots = f(A'_{i\ell_i}) = f(A_i), \qquad 1 \le i \le \ell.
$$

Таким образом, имеем
$$\begin{align*}
\int_{\lambda'(I)}f &= \Bigl(f(A_{11}') \cdot \left| A'_{11} \right| + \cdots + f(A_{1\ell_1})\cdot \left|A'_{i\ell_1}\right|\Bigr) + \cdots + \Bigl(f(A_{11}') \left|A_{11}'\right| + \cdots + f(A_{1\ell_1})\cdot \left|A'_{i\ell_1}\right| \Bigr) \\
&= f(A_1) \cdot \left( \left| A'_{11}  \right| + \cdots + \left| A'_{1\ell_1} \right| \right) + \cdots + f(A_n) \cdot \left( \left| A'_{n1}  \right| + \cdots + \left| A'_{n\ell_n} \right| \right) \\
&= f(A_1) |A_1| + \cdots + f(A_n)\cdot |A_n| \\
&= \int_{\lambda(I)}f.
\end{align*}$$
:::


Таким образом, мы можем ввести следующее определение, которое будем использовать в дальнейшем.

:::{prf:definition}
:label: int_of_p.c
Пусть $I \subsetneq \mathbb{R}$ — промежуток, $f:I \to \mathbb{R}$ — ступенчатая функция на нём. Определим **интеграл на промежутке $I$** ступенчатой функции $f:I \to \mathbb{R}$ следующим образом
$$
\int_If: =  \int_{\lambda(I)}f,
$$
где $\lambda(I)$ такое разбиение промежутка $I$, что $f$ является ступенчатой относительно $\lambda(I).$
:::


:::{prf:example}
Вернёмся к примеру [](#int_1,4=10). Пусть $f: [1,4] \to \mathbb{R}$ определена следующим образом
$$
f(x)  = \begin{cases}
\, 2 & 1 \le x <3 \\
\, 4 & x = 3 \\
\, 6 & 3< x \le 4
\end{cases}
$$
и пусть $\lambda(I) = \{ [1,3), \{3\}, (3,4] \}$, тогда
$$\begin{align*}
\int_{\lambda(I)} f  &= \alpha_{[1,3)}\cdot | [1,3) | + \alpha_{\{3\}}\cdot |\{3\}| + \alpha_{(3,4]} \cdot | (3,4] | \\
&= 2 \cdot 2 + 4 \cdot 0 + 6 \cdot 1 \\
&= 10.
\end{align*}$$

Тогда
$$
\int_{[1,4]}f   =10.
$$
:::

:::{prf:theorem}
:name: imprtant_for_int
Пусть $I \subsetneq \mathbb{R}$ — промежуток и $f,g:I \to \mathbb{R}$ — две ступенчатые функции на нём.

1. $$
\int_I( f \pm  g) =  \int_I f  \pm  \int_I g , \qquad \alpha, \beta \in \mathbb{R}.
$$
2. Если $f(x) \ge g(x)$ для всех $x \in I$, то
$$
\int_I f \ge \int_I g.
$$

3. Если $f(x) = \alpha$ для всех $x \in I$, то
$$
\int_I f = \alpha \cdot |I|.
$$
4. Если $I \subseteq J$ и если $\varphi: J \to \mathbb{R}$ функция, определённая следующим образом
$$
\varphi(x) : = \begin{cases}
f(x) & x \in I,\\
0 & x \notin I,
\end{cases}
$$
тогда $\varphi(x)$ — ступенчатая на $J$ и 
$$\int_J\varphi   = \int_I f.$$

5. Пусть $\{A,B\}$ — разбиение промежутка $I$, тогда если функции $f|_A:A \to \mathbb{R}$, $f|_B:B \to \mathbb{R}$ ступенчаты на $A$ и $B$ соответственно, то
$$
\int_I f  = \int_A f|_A  + \int_B f|_B .
$$


:::

(theorem-4-12)=
:::{prf:proof}
:class: dropdown
:nonumber:

Пусть $\lambda_f(I)  =  \cup_{p=1}^n A_p$, $\lambda_g(I) =  \cup_{q=1}^m B_q$ — разбиения промежутка $I$ относительно которых $f$, $g$ — ступенчаты, соответственно. Согласно предложению [](#beautefull),
\begin{align*}
& f =  \sum_{p=1}^n\sum_{q=1}^m f(A_p) \cdot \chi_{A_p}\cdot \chi_{B_q} = \sum_{p=1}^n\sum_{q=1}^m f(A_p) \cdot \chi_{A_p\cap B_q}, \\
& g=  \sum_{p=1}^n\sum_{q=1}^m g(B_q) \cdot \chi_{A_p} \cdot \chi_{B_q} = \sum_{p=1}^n\sum_{q=1}^m g(B_q) \cdot \chi_{A_p\cap B_q}.
\end{align*}

(1) Согласно следствию [](#cor_for_sum), $f\pm g = \sum_{p=1}^n\sum_{q=1}^m (f(A_p) \pm g(B_q)) \cdot \chi_{A_p\cap B_q}$, и тогда пользуясь замечанием [](#int_via_chi),
$$\begin{align*}
\int_I (f\pm g) &= \sum_{p=1}^n\sum_{q=1}^m (f(A_p) \pm g(B_q)) \cdot \int_I \chi_{A_p \cap B_q} \\
&=\sum_{p=1}^n\sum_{q=1}^m f(A_p) \cdot \int_I \chi_{A_p \cap B_q} \pm \sum_{p=1}^n\sum_{q=1}^m g(B_q) \cdot \int_I \chi_{A_p \cap B_q} \\
&= \int_I f \pm \int_I g.
\end{align*}$$

(2) Если $f(x) \ge g(x)$ для всех $x\in I$, то для любых $p,q$ таких, что $A_p \cap B_q \ne \varnothing$, имеем $f(A_p) \ge g(B_q)$. Тогда, согласно замечанию [](#int_via_chi),
$$\begin{align*}
\int_I f &:=&  \sum_{p=1}^n\sum_{q=1}^m f(A_p) \cdot \int_I \chi_{A_p \cap B_q} = \sum_{p=1}^n\sum_{q=1}^m f(A_p) \cdot |A_p \cap B_q| \\
&\ge & \sum_{p=1}^n\sum_{q=1}^m g(A_p) \cdot |A_p \cap B_q| \\
&= \sum_{p=1}^n\sum_{q=1}^m f(A_p) \cdot \int \chi_{A_p \cap B_q} \\
&=:& \int_I g.
\end{align*}$$

(3) Если $f(x) = \alpha$ для всех $x\in I$, то $f = \alpha \cdot \chi_I$, и согласно замечанию [](#int_via_chi),
$$
\int_f f = \alpha\cdot \int \chi_I = \alpha \cdot |I|.
$$

(4) Пусть $\lambda(I)$ — разбиение промежутка $I$ и $f = \sum_{A \in \lambda(I)} f(A) \cdot \chi_A$, то определим разбиение $\lambda(J)$ промежутка $J$ следующим образом
$$
\lambda(J): = \lambda(I) \cup \{J\setminus I\}
$$
положим, что $\varphi(J\setminus I) :=0$ мы получаем, что $\varphi$ — ступенчата на $J.$ Мы можем также записать
$$
\varphi = \sum_{A \in \lambda(I)} f(A) \chi_A + \varphi(J\setminus I) \chi_{J \setminus I}
$$
тогда согласно Замечанию [](#int_via_chi),
$$\begin{align*}
\int_J \varphi &= \sum_{A \in \lambda(I)} f(A) \int_J \chi_A + \varphi(J\setminus I) \int_J \chi_{J \setminus I}   \\
&= \sum_{A \in \lambda(I)} f(A) \cdot |A| + 0 \cdot |J \setminus I|\\
&= \int_I f.
\end{align*}$$

(5) Пусть $\lambda(A): = \cup_{p=1}^n A_p$, $\lambda(B) : = \cup_{q=1}^m B_q$ — разбиения промежутков $A,B$ соответственно. Тогда $\lambda : = \lambda(A) \cup \lambda(B)$ разбиение промежутка $I.$ 

Имеем
$$
f = \sum_{C \in \lambda(I)} f(C) \cdot \chi_C = \sum_{p=1}^n f(A_p)\cdot \chi_{A_p} + \sum_{q=1}^m f(B_q)\cdot \chi_{B_q} = f|_A + f|_B,
$$
тогда согласно замечанию [](#int_via_chi),
$$\begin{align*}
\int_I f &= \sum_{C \in \lambda(I)} f(C) \cdot \int_I \chi_C \\
&= \sum_{C \in \lambda(I)} f(C) \cdot |C| \\
&= \sum_{p=1}^n f(A_p) \cdot |A_p| + \sum_{q=1}^m f(B_q)\cdot |B_q| \\
&= \int_A f|_A + \int_B f|_B.
\end{align*}$$
:::

[^ref43-1]: Отметим, что эти функции также ещё называются **кусочно-постоянными**, в англоязычной литературе они так и называются, **piecewise constant functions.**
[^ref43-2]: Этому простому и элегантному наблюдению я обязан одной очень красивой девушке!