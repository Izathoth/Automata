# Automata

**Automata** é um script Python projetado para automatizar o processo de download, extração e organização de arquivos. O projeto realiza as seguintes tarefas:

1. **Download de Arquivos**: Baixa um arquivo ZIP a partir de um link fornecido pelo usuário.
2. **Extração de Conteúdo**: Descompacta o arquivo ZIP para uma pasta especificada.
3. **Organização de Arquivos**: Classifica e move os arquivos extraídos para pastas baseadas em suas extensões (Imagens, Documentos, Vídeos, Áudio e Outros).
4. **Geração de Relatório**: Cria um relatório em formato TXT com a lista de arquivos e suas respectivas pastas.

## Funcionalidades

- **Download**: Suporte para arquivos ZIP a partir de URLs fornecidas.
- **Extração**: Descompacta arquivos ZIP para uma pasta local.
- **Organização**: Classifica arquivos em categorias baseadas em suas extensões.
- **Relatório**: Gera um relatório detalhado da organização dos arquivos.

## Requisitos

- Bibliotecas Python: `requests`, `zipfile`, `shutil`
