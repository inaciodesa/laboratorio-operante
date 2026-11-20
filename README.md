# Laboratório Operante

Simulação interativa de condicionamento operante e pavloviano com um rato virtual em uma câmara operante.

**Autora:** Alana Campos de Sá

**Abrir agora:** https://inaciodesa.github.io/laboratorio-operante/

## O que dá para fazer

- Observar a linha de base e montar o etograma do rato antes do treino.
- Fazer o treino ao comedouro e modelar a pressão à barra por aproximações sucessivas.
- Comparar esquemas de reforço (CRF, FR, VR, FI, VI) no registro cumulativo.
- Medir a resistência à extinção e ver a recuperação espontânea em uma nova sessão.
- Rodar supressão condicionada, bloqueio e sombreamento (modelo de Rescorla e Wagner).
- Treinar qualquer comportamento do repertório em um lugar escolhido da câmara.
- Treinar a observação: codificar o comportamento por teclas e receber a concordância e o kappa de Cohen.
- Salvar e restaurar o rato, e ajustar os parâmetros de aprendizagem.

Cada etapa traz uma explicação com o que observar, o equívoco mais comum e a equação usada no modelo.

## Como usar sem internet

Baixe [`export/laboratorio-operante.html`](export/laboratorio-operante.html) e abra com dois cliques em qualquer navegador. É um arquivo único, sem instalação e sem dependências. O arquivo [`export/laboratorio-operante.zip`](export/laboratorio-operante.zip) traz o mesmo conteúdo, pronto para enviar por e-mail.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | Código-fonte da simulação (modelo e interface em um só arquivo) |
| `exportar.py` | Gera a versão portátil em `export/` e a página em `docs/` |
| `export/` | Versão portátil, que roda offline |
| `docs/` | Cópia servida pelo GitHub Pages |
| `mobile/` | Projetos nativos Android e iOS (Capacitor); veja [`mobile/README.md`](mobile/README.md) |

Depois de editar o `index.html`, rode `python3 exportar.py`.

## Limites

Os parâmetros do modelo são ilustrativos: reproduzem a forma dos efeitos clássicos, sem ajuste a dados de um experimento específico. A simulação serve para treinar o raciocínio experimental e não substitui a observação de animais.

## Base

O laboratório parte do programa descrito em:

Graham, J., Alloway, T., & Krames, L. (1994). Sniffy, the virtual rat: Simulated operant conditioning. *Behavior Research Methods, Instruments, & Computers, 26*(2), 134–141.

É uma implementação independente. Não usa código, imagens nem o nome do programa original.

## Licença

Domínio público, pela [Unlicense](LICENSE). Qualquer pessoa pode usar, copiar, modificar e distribuir, para qualquer fim, sem pedir permissão e sem obrigação de citar.
