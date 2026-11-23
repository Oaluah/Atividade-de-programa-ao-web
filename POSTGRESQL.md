# PostgreSQL

## Preparar o ambiente

Instale as dependências:

```powershell
pip install -r requirements.txt
```

Crie um banco chamado `vitrine_produtos` no PostgreSQL. Copie `.env.example` para `.env` e preencha a senha correta. O arquivo `.env` é local e não deve ser enviado ao Git.

## Transferir os dados do SQLite

Com o `.env` ainda ausente ou com `DB_ENGINE=sqlite`, exporte os dados atuais:

```powershell
python manage.py dumpdata --natural-foreign --natural-primary --exclude contenttypes --exclude auth.permission --exclude admin.logentry --indent 2 --output db-export.json
```

Depois de configurar o `.env` para PostgreSQL, rode:

```powershell
python manage.py migrate produtos 0004
python manage.py migrate produtos 0005 --fake
python manage.py migrate
python manage.py loaddata db-export.json
```

A migração `0005` adiciona produtos de demonstração quando o banco está vazio. Marcá-la como aplicada sem executá-la evita duplicar esses produtos ao importar o conteúdo do SQLite.

Para conferir a conexão:

```powershell
python manage.py check --database default
```

Se estiver usando variáveis de ambiente em vez de `.env`, configure `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` e `DB_PORT` antes de iniciar o Django.
