# Salvador 500, cartilha digital

Material de estudo sobre o Plano Salvador 500, elaborado por Beatriz Cal Lucchesi Cerqueira Bispo, João Carlos Santiago, Julia Silva da Costa Maltez, Juliana Thereza Vieira Carvalho Maia, Paulo Henrique de Oliveira Menezes e Sofia Leal de Carvalho Peixoto (Laboratório Urbano / FAUFBA).

## O que tem aqui

- `index.html` e `img/`: o site pronto. É isso que o GitHub Pages publica.
- `fonte/`: os arquivos usados para gerar o `index.html`.
  - `fonte/src/app.js`: conteúdo e componentes (capítulos, mapas, gráficos).
  - `fonte/src/style.css`: aparência.
  - `fonte/src/img/`: imagens.
  - `fonte/scripts/build.py`: junta tudo num `index.html`.

## Como atualizar

Edite os arquivos em `fonte/src/` e rode, a partir da pasta `fonte/`:

```
python3 scripts/build.py files ../index.html
```

Depois copie as imagens novas de `fonte/src/img/` para `img/` (exceto `logo-mask.webp`, que já vai embutida) e envie as mudanças para o GitHub. O GitHub Pages publica sozinho a cada envio para a branch `main`.
