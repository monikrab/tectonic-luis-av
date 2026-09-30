<h1 align="center">Tutorial de LaTeX com Tectonic</h1>
<h1 align="center">Física — 12º Ano</h1>


#### 1. Exemplo

O professor deve ter te enviado uns ficheiros de exemplo de um relatório escrito em LaTeX, contudo, não o conseguirás compilar imediatamente com o Tectonic, devido a umas incompatibilidades com o preâmbulo do professor (o ficheiro que contém as definições de compilação do LaTeX). Por isso, terás de usar a minha versão do exemplo.

Primeiro, instala o `git` no teu computador. O Git é um software que faz gestão de versões de software, que nos ajuda a evitar guardar ficheiros como `ficheiro` > `ficheiro-melhorado` > `ficheiro-final` > `ficheiro-final-melhorado`, ...

Se estiveres no Linux (Manjaro ou CachyOS), abre o terminal e executa:

```bash
sudo pacman -S git
```

No Windows, abre este site: <https://github.com/git-for-windows/git/releases/download/v2.56.0.windows.1/Git-2.56.0-64-bit.exe>. Deve começar a instalar um ficheiro .exe, que deves executar, seguindo as suas instruções. Garante que não desmarcas a opção de adicionar o Git à variável de ambiente PATH (estará ligada por defeito).

Depois disto, abre um terminal, executa o comando `cd [pasta]` para entrares na pasta em que queres guardar o exemplo (por ex.: "Downloads") e executa

```bash
git clone https://github.com/monikrab/tectonic-luis-av 
```





## Para o professor
## CONFLITOS DO PREÂMBULO COM O TECTONIC

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
