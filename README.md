\# QA API Practice



Учебный проект: API-автотесты на Python + pytest + GitHub Actions.



\## Стек

\- Python 3.12

\- requests, pytest

\- GitHub Actions (CI)



\## Что покрыто

\- Позитивные сценарии: GET /posts/{id} — статус, структура, значения

\- Негативные сценарии: 404 — статус, Content-Type, пустое тело

\- Параметризация: проверка нескольких id одним тестом

\- Фикстуры: переиспользуемая сессия с base\_url и teardown



\## Как запустить локально

```bash

python -m venv venv

venv\\Scripts\\activate      # Windows

pip install requests pytest

pytest

