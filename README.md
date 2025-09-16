# Python Import Favorite Links

Este projeto contém um script Python simples (`import.py`) que lê uma lista de URLs de um arquivo de texto (`links.txt`) e a converte em um arquivo HTML (`import.html`) formatado para ser importado como favoritos (bookmarks) pela maioria dos navegadores web.

## Funcionalidades

  * Lê uma lista de URLs a partir de um arquivo `links.txt`.
  * Formata cada URL em uma tag `<bookmark>` HTML.
  * Envolve a lista em tags `<bookmarks>` para compatibilidade de importação.
  * Gera um arquivo `import.html` pronto para ser usado.

## Estrutura do Repositório

```
/
│
├── import.py       # O script principal Python
├── links.txt       # Arquivo de entrada (adicione seus links aqui)
├── import.html     # Arquivo de saída gerado pelo script
└── README.md       # Este arquivo
```

## Como Usar

1.  **Prepare seus links:**

      * Abra o arquivo `links.txt` em um editor de texto.
      * Adicione ou cole os links que deseja importar.
      * **Importante:** Certifique-se de colocar **apenas um URL por linha**.

2.  **Execute o Script:**

      * Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado em seu sistema.
      * Abra um terminal ou prompt de comando, navegue até a pasta onde o script está localizado.
      * Execute o script:
        ```bash
        python import.py
        ```

3.  **Importe no seu Navegador:**

      * Após a execução, um novo arquivo chamado `import.html` será criado na mesma pasta.
      * Abra seu navegador (Google Chrome, Mozilla Firefox, Microsoft Edge, etc.).
      * Vá até o gerenciador de Favoritos (Bookmarks).
      * Procure a opção "Importar favoritos" ou "Importar bookmarks".
      * Quando solicitado, escolha a opção "Arquivo HTML de favoritos" (ou similar) e selecione o arquivo `import.html` que você acabou de gerar.
      * Seus links do `links.txt` estarão agora na sua barra de favoritos.

## Observações sobre o Script

  * O script `import.py` no repositório define a função `get_links` duas vezes. A segunda definição (que utiliza o módulo `csv`) é a que está funcional e sobrescreve a primeira.
  * A importação do módulo `requests` existe no script, mas não é utilizada na versão atual.
  * O módulo `csv` é usado para ler o `links.txt`. Para este caso de uso (um link por linha), uma leitura de linha padrão (como `f.readlines()`) também seria uma alternativa viável.
