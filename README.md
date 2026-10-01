
<h1 align="center">Tutorial de LaTeX com Tectonic</h1>
<h2 align="center">Física — 12º Ano</h2>


### 0. Fundamentos

Para conseguries escrever relatórios sobre os teus trabalhos, o professor está a mandar-te instalar um software de que provavelmente nunca ouviste falar, chamado Latex (estilizado como LaTeX, lê-se 'latek', o X é um χ grego maiúsculo), porquê? *Não posso só usar o Word ou o Google Docs para escrever os meus relatórios?*

Teoricamente... podes. Contudo, isto não é tão boa ideia como podes imaginar. Este slide explica a diferença entre os dois softwares bastante bem:

<p align="center">
  <img src="imagens/word_vs_latex.png" width="750">
</p>

Se fosses fazer os relatórios com um processador de texto normal, provavelmente demorarias bastante mais tempo, e ficaria menos visualmente apelativo.  


### 1. Que faz o LaTeX? Como posso fazer um documento?

O LaTeX é um software de composição tipográfica de documentos, que funciona à base de código. Escreverás o texto com comandos de formatação num ficheiro `.tex`, e depois compilarás para um PDF de alta qualidade. O funcionamento do LaTeX pode ser dividido em três partes:

- Separação de conteúdo e formatação: Concentras-te apenas no que estás a escrever (parágrafos, fórmulas, etc.), enquanto o sistema cuida automaticamente da tipografia, espaçamentos, paginação.

- Fórmulas matemáticas: É a ferramenta padrão para escrever equações matemáticas complexas claramente formatas em qualidade.

- Referências automáticas: Faz gestão automática de figuras e bibliografia.

Para exemplificar um documento básico em LaTeX com tudo isto:

```latex
% O simbolo de por cento serve como comentário.
% Tudo à frente deste não é visto pelo compilador

\documentclass{article} % Tipo de documento (neste caso, artigo científico)

% Carrega o BibLaTeX, que gere a bibliografia
\usepackage[backend=biber,style=numeric]{biblatex}
% Usa o ficheiro de referências bibliografia.bib
\addbibresource{bibliografia.bib}

% Seleciona a língua portuguesa
\usepackage[portuguese]{babel}

% Exemplo de formatação: pôr o fundo negro e o texto branco
\usepackage{xcolor}
\pagecolor{black}
\color{white}

% Tudo atrás deste comando é referido como "preâmbulo"
\begin{document}


% Secção do documento
\section{Vantagens do \LaTeX}

% Lista
\begin{itemize}
    % Item da lista
    \item \textbf{Separação de conteúdo e formatação}: Concentras-te apenas no que estás a escrever (parágrafos, fórmulas, etc.), enquanto o sistema cuida automaticamente da tipografia, espaçamentos, paginação.

    \item \textbf{Fórmulas matemáticas}: É a ferramenta padrão para escrever equações matemáticas complexas claramente formatas em qualidade. Por exemplo:

    % Fórmula
    % Os cifrões ($$) denota o início e fim da equação.

    $$
        f(x) = \int_{-\infty}^{\infty} \left( \sum_{n=1}^{\infty} \frac{\alpha_n}{n^2} \right) e^{-\frac{(x-\mu)^2}{2\sigma^2}} \, dx
    $$

    % Um cifrão ($) faz o mesmo, mas comprime
    % a equação para caber na altura duma linha
    $
        f(x) = \int_{-\infty}^{\infty} \left( \sum_{n=1}^{\infty} \frac{\alpha_n}{n^2} \right) e^{-\frac{(x-\mu)^2}{2\sigma^2}} \, dx
    $

    \item \textbf{Referências automáticas:} Faz gestão automática de figuras e bibliografia. Podemos citar um livro: \cite{knuth1984}. % Adiciona uma referência
\end{itemize}



\printbibliography
\end{document}
```

Isto resulta no seguinte documento (print cortada, o resultado final é em tamanho A4):

<p align="center">
  <img src="imagens/demo_latex.png" width="600">
</p>





<br>
<br>
<h2 align="center">Para o professor</h2>

### CONFLITOS DO PREÂMBULO COM O TECTONIC

O Tectonic não instala fontes, apenas usa ficheiros locais. É preverível copiar a fonte para a diretoria dos auxiliares.
No preâmbulo, altere o comando `\setmainfont` de modo a incluir:
```latex
\setmainfont{EBGaramond}[ % Tudo junto, não 'EB Garamond'
  %%  %%  %%  %%  %%  %%  %%  %%  %%
  Path=./auxiliares/ebgaramond/,
  Extension=.ttf,
  UprightFont=*-Regular,
  BoldFont=*-Bold,
  ItalicFont=*-Italic,
  BoldItalicFont=*-BoldItalic,
  %%  %%  %%  %%  %%  %%  %%  %%  %%
  ...
```

Para o Biber funcionar, tem de estar instalado localmente. Contudo, o Tectonic tem conflitos de versão com o BibLaTeX do Arch. Isto pode ser aliviado se a sua localização for especificada à hora da compilação. Use a opção `-Z search-path=auxiliares/biblatex/` quando for compilar.
**AVISO:** não funciona com o BibLaTeX 3.22, pois o Tectonic ainda usa o TeX Live 2025. Use a versão 3.21 do SourceForge (presente nas pastas demo/ e auxilares/).

A opção `german` não funciona no comando `\setotherlanguages{}`. `ngerman` também não funciona.

O `pythontex` não funciona com o Tectonic porque o pacote exige a execução de comandos e scripts externos intermediários durante a compilação. Deve ser removido do preâmbulo.

O Tectonic pode escrever ficheiros log com a opção --keep-logs.
