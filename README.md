
<h1 align="center">Tutorial de LaTeX com Tectonic</h1>
<h2 align="center">Física — 12º Ano</h2>


### 0. Fundamentos

O professor está a mandar-te instalar um software de que provavelmente nunca ouviste falar, chamado $\LaTeX$. Porquê?


Depois disto, abre um terminal, executa o comando `cd [pasta]` para entrares na pasta em que queres guardar o exemplo (por ex.: "Downloads") e executa

```bash
git clone https://github.com/monikrab/tectonic-luis-av 
```




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
