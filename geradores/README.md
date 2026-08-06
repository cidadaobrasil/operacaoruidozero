# Geradores dos guias "Barulho na casa vizinha"

Scripts que produzem o guia em PDF sobre a lei do silêncio, um por município da
área da 5ª Cia PM. É material de orientação ao cidadão, distinto do painel de
operação que fica na raiz deste repositório (`index.html`).

## Por que estão aqui

Até 06/08/2026 estes quatro scripts existiam em **um único lugar no mundo**:
uma pasta chamada `tmp` na máquina de casa do Josemar, fora de qualquer
repositório. Não havia cópia remota. O nome da pasta convidava a apagar, e a
perda seria silenciosa e definitiva.

Foram trazidos para cá porque o tema é o mesmo da Operação Ruído Zero e este
repositório já é institucional (`cidadaobrasil`).

## Como gerar

Precisa de `reportlab` (`pip install reportlab`) e das fontes Arial do Windows.

```
python build_barulho_guararapes_mobile.py
```

O PDF sai em `pdf/`, ao lado do script. Um script por município:

| Script | Município |
|---|---|
| `build_barulho_mobile.py` | versão base (sem município no nome do arquivo) |
| `build_barulho_guararapes_mobile.py` | Guararapes |
| `build_barulho_rubiacea_mobile.py` | Rubiácea |
| `build_barulho_bento_de_abreu_mobile.py` | Bento de Abreu |

Os quatro são quase idênticos: divergem em cerca de 24 linhas, que são a
legislação municipal e os dados locais. Mudança de layout precisa ser repetida
nos quatro, ou eles saem diferentes entre si.

## Ajuste feito ao versionar

O caminho de saída era absoluto (`C:\projetos\Sites basicos`), o que prendia o
script a uma máquina e a um lugar específico do disco. Passou a ser relativo ao
próprio arquivo (`Path(__file__).resolve().parent`), então funciona em qualquer
máquina e em qualquer pasta. Testado gerando o PDF de Rubiácea depois da
mudança.

As fontes ainda apontam para `C:\Windows\Fonts`, o que é aceitável porque o
material é produzido em máquina Windows; se um dia rodar em outro sistema, é o
próximo ponto a ajustar.
