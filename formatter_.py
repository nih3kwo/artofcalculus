from pyperclip import *
from time import sleep

data = paste()
lines = data.split("\n")

for i in range(len(lines)):
    lines[i] = lines[i].replace(r"\(", "$")
    lines[i] = lines[i].replace(r"\)", "$")
    lines[i] = lines[i].replace(r"\textit{т.е.}", "т.е.")
    lines[i] = lines[i].replace(r"\bigskip", "")
    lines[i] = lines[i].lstrip()
    if lines[i].startswith(r"\section"):
        lines[i] = lines[i].replace(r"\section{", "# ").replace("}", "").replace("~", "")
    if lines[i].startswith(r"\subsection"):
        lines[i] = lines[i].replace(r"\subsection{", "## ").replace("}", "").replace("~", "")
    if lines[i].startswith(r"\subsubsection"):
        lines[i] = lines[i].replace(r"\subsubsection{", "### ").replace("}", "").replace("~", "")
    lines[i] = lines[i].replace(r"\[", "$$").replace(r"\]", "$$")

    for string in ["proposition", "lemma", "remark", "example",
                   "proof", "definition", "theorem", "corollary"]:
        replacee = r"\begin{" + string + "}"
        if replacee in lines[i]:
            if string != "proof":
                lines[i] = lines[i].replace(replacee, ":::{prf:" + string + "}")
            else:
                lines[i] = lines[i].replace(replacee, ":::{prf:" + string + "}\n:class: dropdown\n:nonumber:")
            if r"[" in lines[i] or r"\label{" in lines[i]:
                for a, b in [("[{", " "), ("}]", ""), (r"\label{", "\n:name: ")]:
                    lines[i] = lines[i].replace(a, b)
                if lines[i][-1] == "}":
                    lines[i] = lines[i][:-1]
            
        replacee = r"\end{" + string + "}"
        if replacee in lines[i]:
            lines[i] = lines[i].replace(r"\end{" + string + "}", ":::")
        

    if "--" in lines[i]:
        lines[i] = lines[i].replace("--", "—")

    if lines[i].startswith(r"\begin{mydanger}"):
        lines[i] = ":::{warning}"
    if lines[i].startswith(r"\end{mydanger}"):
        lines[i] = ":::"

    if lines[i].startswith(r"\begin{comment}"):
        lines[i] = ":::{note}"
    if lines[i].startswith(r"\end{comment}"):
        lines[i] = ":::"

    if lines[i].startswith(r"\begin{comments}"):
        lines[i] = ":::{seealso}"
    if lines[i].startswith(r"\end{comments}"):
        lines[i] = ":::"

    if r"\ie" in lines[i]:
        lines[i] = lines[i].replace(r"\ie", "т. е.")

    while r"\textit{" in lines[i]:
        italics_index = lines[i].index(r"\textit{")
        print(i, italics_index)
        lines[i] = lines[i][:italics_index] + lines[i][italics_index:].replace("}", "**", 1)
        lines[i] = lines[i].replace(r"\textit{", "**", 1)

    while r"\emph{" in lines[i]:
        italics_index = lines[i].index(r"\emph{")
        print(i, italics_index)
        lines[i] = lines[i][:italics_index] + lines[i][italics_index:].replace("}", "*", 1)
        lines[i] = lines[i].replace(r"\emph{", "*", 1)

    while r"\textbf{" in lines[i]:
        italics_index = lines[i].index(r"\textbf{")
        print(i, italics_index)
        lines[i] = lines[i][:italics_index] + lines[i][italics_index:].replace("}", "**", 1)
        lines[i] = lines[i].replace(r"\textbf{", "**", 1)

    lines[i] = lines[i].replace(r"\begin{eqnarray*}", r"$$\begin{eqnarray}")
    lines[i] = lines[i].replace(r"\end{eqnarray*}", r"\end{eqnarray}$$")
    lines[i] = lines[i].replace("eqnarray", "align*")
    
    while r"\ref{" in lines[i]:
        ind = lines[i].index(r"\ref{")
        lines[i] = lines[i][:ind] + lines[i][ind:].replace("}", ")", 1)
        lines[i] = lines[i].replace(r"\ref{", "[](#", 1)

    if "example}~" in lines[i]:
        lines[i] = lines[i].replace("~", "")

    lines[i] = lines[i].replace("i.e.,", "т. е.")

final = "\n".join(lines)
while r"\begin{enumerate}" in final:
    i = 1
    right = final.index(r"\end{enumerate}")
    ind = final.index(r"\item")
    while ind < right:
        final = final.replace(r"\item", f"{str(i)}.", 1)
        i += 1
        try: 
            ind = final.index(r"\item")
        except ValueError:
            break
    final = final.replace(r"\begin{enumerate}", "", 1).replace(r"\end{enumerate}", "", 1)


final = final.replace(r"\begin{itemize}", "").replace(r"\end{itemize}", "", 1).replace(r"\item", "*")
copy(final)
