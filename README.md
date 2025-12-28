# Apl_Web_Flash_CRUD

Aplicação web CRUD desenvolvida com **Flask** e **MySQL**, utilizando banco de dados gerenciado na **Aiven** e deploy na **Render**.

O sistema permite **cadastrar, listar, atualizar e excluir alunos**, com persistência de dados em nuvem.
Aplicação publicada na Render:

🔗 https://apl-web-flash-crud.onrender.com

Banco de dados hospedado na Aiven Cloud com acesso controlado por IP.
---

## 🚀 Tecnologias Utilizadas

- Python 3
- Flask
- PyMySQL
- MySQL (Aiven Cloud)
- HTML + CSS
- Gunicorn
- Render (Deploy)

---

## ⚙️ Funcionalidades

- ✅ Listagem de alunos
- ➕ Cadastro de novos alunos
- ✏️ Atualização de dados
- ❌ Exclusão de registros
- 🔒 Conexão segura com MySQL (SSL)

---

## 🗄️ Estrutura da Tabela

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
);
