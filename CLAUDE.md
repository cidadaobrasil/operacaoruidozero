# CLAUDE.md — Operação Ruído Zero

## O que é
Painel HTML estático de operação da 5ª Cia PM (Operação Impacto "Baixo Ruído"): um único `index.html` com horários, escala, mapa-força e resenha. `preview.jpg` é a imagem de preview do WhatsApp.

## Conta e publicação
- GitHub: `cidadaobrasil/operacaoruidozero` (branch `main`) — **conta cidadaobrasil, não josemardp**.
- Push na `main` publica via GitHub Pages. Após push: conferir a página publicada e o preview do WhatsApp (meta tags og:).

## Fluxo padrão
1. Editar `index.html` (os dados de horários/escala estão embutidos no HTML — edição cirúrgica, sem reestruturar).
2. **Conferir o visual com screenshot/preview antes de entregar** (desktop e mobile) — o dono é exigente com acabamento visual; nada de layout quebrado ou "duas linhas onde era pra ser uma".
3. Commit + push na main; confirmar deploy do Pages.

## Cuidado com encoding
O HTML usa entidades (`&ccedil;` etc.) em alguns pontos — ao usar Edit, copiar o trecho exato do arquivo (não o texto renderizado).
