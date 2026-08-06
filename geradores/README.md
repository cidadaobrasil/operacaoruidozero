# Geradores dos guias "Barulho na casa vizinha"

Gera o guia em PDF sobre a lei do silêncio, um por município da área da 5ª Cia
PM. É material de orientação ao cidadão, distinto do painel de operação que fica
na raiz deste repositório (`index.html`).

## Como gerar

Precisa de `reportlab` (`pip install reportlab`) e das fontes Arial do Windows.

```
python build_guias.py                    # gera os quatro
python build_guias.py guararapes         # gera só um
python build_guias.py rubiacea guararapes
```

Os PDFs saem em `pdf/`, ao lado do script. Municípios disponíveis:
`valparaiso`, `guararapes`, `rubiacea`, `bento-de-abreu`.

## Como mudar alguma coisa

**Dado de um município** (telefone, legislação, texto da mediação): está no
dicionário `MUNICIPIOS`, no topo do `build_guias.py`. É a única parte que muda
de um guia para o outro.

**Layout, cores, textos comuns:** estão no corpo do script e valem para os
quatro de uma vez.

**Município novo:** acrescente uma entrada em `MUNICIPIOS` com os mesmos campos.
Nada mais precisa mudar.

## Histórico

Estes scripts existiam em **um único lugar no mundo** até 06/08/2026: uma pasta
chamada `tmp` na máquina de casa, fora de qualquer repositório e sem cópia
remota. O nome da pasta convidava a apagar, e a perda seria silenciosa.

Dois problemas foram corrigidos ao trazê-los para cá:

**Caminho absoluto.** A saída apontava para `C:\projetos\Sites basicos`, o que
prendia o script a uma máquina e a um lugar específico do disco. Passou a ser
relativo ao próprio arquivo.

**Quatro cópias do mesmo script.** Eram quatro arquivos de 602 linhas que
divergiam em apenas 12 linhas cada, todas de conteúdo municipal. Mudar o layout
exigia repetir a alteração nos quatro, e bastava esquecer um para os guias
saírem diferentes entre si. Viraram um script só, de 733 linhas, com os dados
municipais num dicionário.

A unificação foi verificada gerando os quatro PDFs e comparando com os
anteriores: **as 16 páginas ficaram idênticas pixel a pixel**.

## Detalhe de conteúdo, não de código

O texto da mediação comunitária tem duas formas: Guararapes, por ser sede do
NUMEC, não leva a ressalva "Embora o fato tenha ocorrido em...". **Bento de
Abreu usa a mesma frase de Guararapes mesmo não sendo sede.** Isso vem dos
scripts originais e foi preservado de propósito, para a refatoração não alterar
o PDF. Se estiver errado, é decisão de conteúdo: mude o campo `mediacao`
daquele município para `_mediacao_outra_cidade("Bento de Abreu")`.

As fontes ainda apontam para `C:\Windows\Fonts`, aceitável porque o material é
produzido em máquina Windows. Se um dia rodar em outro sistema, é o próximo
ponto a ajustar.
