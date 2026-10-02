
<h1 align="center">Tutorial de LaTeX com Tectonic</h1>
<h2 align="center">Física — 12º Ano</h2>


### 0. Fundamentos

Para conseguries escrever relatórios sobre os trabalhos que farás na disciplina, o professor está a mandar-te instalar uma coisa de que provavelmente nunca ouviste falar, chamado Latex (estilizado como LaTeX; lê-se 'lateq', porque o X é um χ (qui) grego)—porquê? *Não posso só escrever os meus relatórios no o Word ou no Google Docs?*

Teoricamente... podes. Contudo, isto não é tão boa ideia como poderás imaginar. Esta imagem explica a diferença entre estes dois tipos de aplicações bastante bem:

<p align="center"><img src="imagens/word_vs_latex.png" width="750"></p>

Ou seja, se tentasses escrever os relatórios num processador de texto normal (como o Word), provavelmente demorarias mais tempo, o resultado ficaria menos visualmente apelativo, e (bastante) pior formatado.


### 1. Mas o que faz o LaTeX? Como posso fazer um documento?

O LaTeX é um programa de composição tipográfica de documentos, que funciona à base de código. Isto significa que tu escreves (melhor, *descreves*) o teu documento com comandos de formatação num ficheiro `.tex`, e executas a compilação (tradução) para PDF. Não te preocupes se nunca escreveste código! O formato em si é muito básico, os comandos são todos palavras em inglês que já deves conhecer. Não é comparavel a uma linguagem de programação 'a sério'.

Quando às funcionalidades do LaTeX, e como escrever código TeX, terás de ter em mente três aspetos:

- **Separação de conteúdo e formatação**: O utilizador concentra-se apenas no que está a escrever (parágrafos, fórmulas, etc.), enquanto o programa cuida automaticamente da tipografia e espaçamentos.

- **Fórmulas matemáticas**: É a ferramenta padrão para escrever expressões matemáticas a computador. Irrespetivamente da complexidade, ficam legíveis e em alta definição.

- **Referências automáticas**: O LaTeX fará a gestão automática das figuras (imagens) e bibliografia dos teus documentos.

Para exemplificar, incluí um documento básico em LaTeX com tudo isto:

```latex
% O simbolo '%' faz com que tudo à sua frente seja ignorado pelo LaTeX

% Todos os documentos LaTeX têm um tipo básico: artigo, livro, carta, etc.

\documentclass{article}
% |
% `-> Este é um artigo, tem Secções, mas não tem Capítulos como um livro


% O LaTeX, por si só, é bastante básico, para coisas mais complexas, carregamos Pacotes
% Cada pacote adiciona os seus próprios comandos, que facilitam certas coisas, como exemplos:

\usepackage[portuguese]{babel}%  -> Suporte para várias línguas (como o português)

\usepackage[backend=biber,style=authortitle]{biblatex}%  -> Gestor de bibliografia avançado

\usepackage{xcolor}%  -> Definições de cor do documento


% Alguns exemplos de comandos:

% Do 'xcolor'
\pagecolor{black}
\color{white}

% Do BibLaTeX - usa o ficheiro bibliográfico .bib (será-te útil!)
\addbibresource{bibliografia.bib}

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

    \item \textbf{Referências automáticas}: Faz gestão automática de figuras e bibliografia. Podemos citar um livro: \cite{livroLatex}. % Adiciona uma referência
\end{itemize}



\printbibliography
\end{document}
```

Isto resulta no seguinte documento (print cortada, o resultado final é em tamanho A4):

<p align="center">
  <img src="imagens/demo_latex.png" width="750">
</p>


### 2. Está bem, convenceste-me. Como é que instalo isto?

Depende. **Se estiveres no Linux** (que, já agora, eu <u>recomendo usares</u> se estiveres disposto a fazer um pequeno esforço), abre o teu terminal e executa o comando

```bash
sudo pacman -S tectonic biber
```

*Quem não tem familiaridade com o uso da linha de comandos, pode começar por ler este pequeno guia: <https://promovaweb.com/glossario/cli>, e outros do mesmo site*

Este comando instalará o Tectonic, a nossa *engine* (motor) e *distribuição* de LaTeX. Uma engine é o programa que contém o sistema básico de LaTeX, usado para compilar o teu texto. A distribuição é o pacote completo que gere e instala todas as ferramentas e adicionais (bibliotecas, fontes) especificados em cada documento. Também instala o Biber, que age juntamente com o BibLaTeX para criar a bibliografia.

**Se estiveres no Windows**, abre o PowerShell, e cola e executa o seguinte comando:

```pwsh
md "C:\Tectonic" -f; [Environment]::SetEnvironmentVariable("Path", "$([Environment]::GetEnvironmentVariable("Path","User"));C:\Tectonic", "User")
```

Agora, vai ao site <https://tectonic-typesetting.github.io/latest.html>, e, na lista no fundo da página, clicka no título 'tectonic...windows-msvc.zip". Será transferido um arquivo `.zip`, que deverás extrair (com o botão direito no ficheiro no Explorador, clicka em 'Extrair Tudo'), e gravar o resultante `tectonic.exe` na pasta `C:\Tectonic`.


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
