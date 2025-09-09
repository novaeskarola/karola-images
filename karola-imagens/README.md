# Karola Imagens — Template de Repositório

Este repositório serve como **padrão** para hospedar imagens da loja e usar as URLs no banco de dados (Supabase).  
Você pode clonar este template, renomear as pastas e fazer upload das suas imagens.

---

## Estrutura de pastas recomendada

```
/produtos/<SKU>/<cor>/arquivo.jpg
/banners/
/logos/
/icones/
/mockups/
/outros/
```

- **SKU**: identificador único do produto (ex.: `VEST-MIDI-001`).
- **cor**: use `slug` em minúsculas e sem acento (ex.: `azul-marinho`, `preta`, `off-white`).

> Dica: para variantes (cor/tamanho), crie uma pasta por **cor** e nomeie os arquivos com sufixos de ângulo/ordem:  
> `vestido-midi-azul-frente-1.jpg`, `vestido-midi-azul-costas-2.jpg`.

---

## Três formas de URL (escolha uma)

### 1) Link direto (Raw)
Abra a imagem no GitHub → **Raw** → copie a URL:
```
https://raw.githubusercontent.com/<usuario>/<repo>/main/produtos/<SKU>/<cor>/arquivo.jpg
```

### 2) GitHub Pages (ativar em Settings → Pages)
```
https://<usuario>.github.io/<repo>/produtos/<SKU>/<cor>/arquivo.jpg
```

### 3) jsDelivr (recomendado)
Rende melhor e evita rate-limit:
```
https://cdn.jsdelivr.net/gh/<usuario>/<repo>@main/produtos/<SKU>/<cor>/arquivo.jpg
```
Link **imutável** por commit específico (ideal para catálogos “congelados”):
```
https://cdn.jsdelivr.net/gh/<usuario>/<repo>@<SHA>/produtos/<SKU>/<cor>/arquivo.jpg
```

---

## Convenções de nomes de arquivo

- minúsculas, sem espaços; use `-` como separador.
- formate: `slug-do-produto-<ângulo|detalhe>-<ordem>.jpg`
- `jpg` para fotos (qualidade 80–85), `png` apenas se precisar de transparência, `webp` quando quiser reduzir muito o tamanho.
- evite imagens acima de **5 MB**.

---

## Como popular o Supabase

Exemplo de tabela `product_images`:
```sql
-- ajuste os nomes dos campos conforme seu schema
create table if not exists product_images (
  id bigserial primary key,
  product_id bigint not null,
  variant_id bigint,
  sku text,
  url text not null,
  alt text,
  sort_order int default 1,
  is_primary boolean default false,
  is_active boolean default true,
  created_at timestamp with time zone default now()
);
```

Insert de exemplo:
```sql
insert into product_images (product_id, variant_id, sku, url, alt, sort_order, is_primary)
values
  (123, 12301, 'VEST-MIDI-001', 'https://cdn.jsdelivr.net/gh/<usuario>/<repo>@main/produtos/VEST-MIDI-001/azul/vestido-midi-azul-frente-1.jpg', 'Vestido midi azul — frente', 1, true),
  (123, 12301, 'VEST-MIDI-001', 'https://cdn.jsdelivr.net/gh/<usuario>/<repo>@main/produtos/VEST-MIDI-001/azul/vestido-midi-azul-costas-2.jpg', 'Vestido midi azul — costas', 2, false);
```

> Alternativa: utilize o arquivo **`product_images_template.csv`** deste repo e importe via Supabase (Table Editor → Import data).

---

## Script opcional: gerar lista de links jsDelivr

Na pasta `tools/` há um script que varre `produtos/` e imprime os links no formato jsDelivr.  
Basta rodar localmente (Python 3.9+):
```
python tools/build_jsdelivr_links.py --user SEUUSUARIO --repo NOME-DO-REPO --branch main
```

Saída esperada (exemplo):
```
VEST-MIDI-001/azul/vestido-midi-azul-frente-1.jpg -> https://cdn.jsdelivr.net/gh/SEUUSUARIO/NOME-DO-REPO@main/produtos/VEST-MIDI-001/azul/vestido-midi-azul-frente-1.jpg
```

---

## Checklist rápido
- [ ] Repo **público**
- [ ] Pastas por **SKU** e **cor**
- [ ] Nomes de arquivos padronizados
- [ ] Escolhi meu tipo de URL (Raw / Pages / **jsDelivr**)
- [ ] Preenchi `alt`/ordem e importei o CSV no Supabase

---

Feito com ❤ para a loja Karola Novaes.
