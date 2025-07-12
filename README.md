# 📚 Library API

Uma API RESTful completa para gerenciamento de livros e autores, construída com Django REST Framework. Este projeto demonstra as principais funcionalidades de uma API, incluindo operações CRUD, autenticação, filtros, busca e paginação.

---

## ✨ Funcionalidades

* **Autores (Author):**
    * `POST /api/authors/`: ➕ Criar um novo autor.
    * `GET /api/authors/`: 📖 Listar todos os autores (com paginação e filtros).
    * `GET /api/authors/{id}/`: 🔍 Obter detalhes de um autor específico.
    * `PATCH /api/authors/{id}/`: ✏️ Atualizar parcialmente um autor.
    * `DELETE /api/authors/{id}/`: 🗑️ Excluir um autor.

* **Livros (Book):**
    * `POST /api/books/`: ➕ Criar um novo livro.
    * `GET /api/books/`: 📖 Listar todos os livros (com paginação e filtros).
    * `GET /api/books/{id}/`: 🔍 Obter detalhes de um livro específico.
    * `PATCH /api/books/{id}/`: ✏️ Atualizar parcialmente um livro.
    * `DELETE /api/books/{id}/`: 🗑️ Excluir um livro.

---

## 🔒 Autenticação e Permissões

* **Autenticação Básica (Basic Auth) e de Sessão (Session Auth):** Suporte para autenticação via credenciais (usuário/senha).
* **`IsAuthenticatedOrReadOnly`:** 👮‍♂️
    * Requisições **GET** (leitura) são acessíveis publicamente para qualquer um.
    * Requisições **POST, PATCH, DELETE** (escrita/modificação) **exigem autenticação** de um usuário válido.

---

## 🔎 Filtros, Busca e Ordenação

As listagens de `Autores` e `Livros` podem ser customizadas usando parâmetros de query:

* **Busca (`?search=termo`):** 🌐
    * `Autores`: Busca por `name` e `biography`.
    * `Livros`: Busca por `title`, `description` e `isbn`.
    * Exemplo: `/api/books/?search=inovacao`

* **Filtros Exatos (`?campo=valor` - apenas para Livros):** 🎯
    * `Livros`: Filtros por `author` (ID do autor) e `publication_date`.
    * Exemplo: `/api/books/?author=1&publication_date=2020-01-01`

* **Ordenação (`?ordering=campo` ou `?ordering=-campo`):** ⬆️⬇️
    * `Autores`: Ordena por `name` ou `birth_date`.
    * `Livros`: Ordena por `title` ou `publication_date`.
    * Exemplo: `/api/books/?ordering=-publication_date` (ordem decrescente)

---

## 📄 Paginação

Todas as listagens de recursos (`/api/authors/` e `/api/books/`) são paginadas para otimizar o desempenho em grandes volumes de dados.

* **Padrão:** 🔟 10 itens por página.
* **Parâmetros de Query:**
    * `?page=N`: ➡️ Acessa uma página específica.
    * `?page_size=M`: 📏 Define o número de itens por página.
    * Exemplo: `/api/books/?page=2&page_size=5`

---

## 🛠️ Configuração e Instalação

Para configurar e rodar o projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/library_api.git](https://github.com/SEU_USUARIO/library_api.git)
    cd library_api
    ```
    *Substitua `SEU_USUARIO` pelo seu usuário do GitHub.*

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    # venv\Scripts\activate   # Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *Se você ainda não criou o `requirements.txt`, execute `pip freeze > requirements.txt` AGORA.*

4.  **Execute as migrações do banco de dados:**
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

5.  **Crie um superusuário (para acesso ao admin e testes de autenticação):**
    ```bash
    python3 manage.py createsuperuser
    ```
    *Siga as instruções para criar nome de usuário e senha.*

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python3 manage.py runserver
    ```
    A API estará acessível em `http://127.0.0.1:8000/`.

---

## 📖 Documentação da API (Swagger UI)

A API é auto-documentada usando `drf-spectacular`. Você pode acessar a interface interativa do Swagger UI para testar os endpoints:

* **Swagger UI:** [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/) 📝

---

## 👨‍💻 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT.

---