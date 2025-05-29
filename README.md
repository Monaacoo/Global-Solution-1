# 🔐 Investigação de Logs

Este projeto foi desenvolvido para a prova de global solution de coding for security, está simulando um ataque cibernético que comprometeu sua estrutura de auditoria. O sistema foi infectado com diversos arquivos `.log` criptografados em **base64**, espalhados por múltiplas pastas e subpastas. Seu principal objetivo é encontrar o autor do ataque, identificado pela assinatura especial `@author: r1g312`.

---

## 📂 Descrição do Problema

- Todos os arquivos `.log` estão criptografados em base64.
- Um dos arquivos contém a **assinatura do autor do ataque**.
- A estrutura original de diretórios precisa ser mantida.
- O script decodifica todos os arquivos `.log` e salva em uma nova estrutura de pastas.
- Ao encontrar o arquivo com a assinatura, ele é salvo na raiz do projeto como `author.txt`.

---

## ✅ Funcionalidades

- 🗂️ Acesso e leitura recursiva de diretórios e arquivos.
- 🔓 Decodificação dos conteúdos utilizando `base64.b64decode()`.
- 🗃️ Criação de nova estrutura de diretórios com arquivos decodificados.
- 🔎 Busca pela assinatura do autor do ataque.
- 💾 Salvamento do arquivo original com a assinatura em `author.txt`.
- ⚙️ Execução via linha de comando.
- ⚠️ Tratamento de exceções para arquivos e pastas inválidas.

---

## 🛠️ Pré-requisitos

- Python 3.6 ou superior
- Recomendado: ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

---

Lembrete: Antes de executar, apague a pasta de decodificados e o arquivo author.txt, eles serão gerados automaticamente depois de executar o código.

## Estrutura de Pastas

Após a execução, será criada uma pasta chamada decodificados/ com a estrutura original e arquivos descriptografados.

Se o autor for encontrado, será criado o arquivo author.txt na raiz do projeto, contendo:

- O conteúdo decodificado do arquivo com a assinatura.

- O caminho de origem do arquivo onde a assinatura foi encontrada.


