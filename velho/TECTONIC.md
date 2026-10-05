
# CONFLITOS DO PREÂMBULO COM O TECTONIC (para o professor)

O Tectonic não instala fontes, apenas usa ficheiros locais. É preverível copiar a fonte
```latex
\setmainfont{EBGaramond}[ % Sem espaço
  %% IMPORTANTE:  %%  %%  %%  %%  %%
  Path=./auxiliares/ebgaramond/,
  Extension=.ttf,
  UprightFont=*-Regular,
  BoldFont=*-Bold,
  ItalicFont=*-Italic,
  BoldItalicFont=*-BoldItalic,
  %%  %%  %%  %%  %%  %%  %%  %%  %%
```
to the preamble, including the static fonts in the extra includes zip

To make biber work, download the latex/ directory from the newest biblatex sources (https://ctan.org/tex-archive/macros/latex/contrib/biblatex/latex), place them into a folder (e.g. biblatex/) and compile with `-Z search-path=biblatex/` at the tail of the V2 command

`german` doesn't work in `\setotherlanguages{}`. Remove it. No, `ngerman` doesn't work either.

`pythontex` is non-reproducible and relies on multi-stage compilation, thus it will throw a missing file error in compilation. Remove it from the preamble.

To keep logs, run --keep-logs
