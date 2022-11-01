# service-users

[![Lint, Test and Deploy](https://github.com/grupo4taller2/service-users/actions/workflows/lint-test-deploy.yml/badge.svg?branch=main)](https://github.com/grupo4taller2/service-users/actions/workflows/lint-test-deploy.yml)

[![Codecov Test coverage](https://codecov.io/gh/grupo4taller2/service-users/branch/main/graph/badge.svg?token=C3GAHNA3D0)](https://codecov.io/gh/grupo4taller2/service-users)

---

> In order to trigger the alembic migrations, you run the `alembic upgrade head` command.
When you make any change to a database table, you capture that change by running `alembic
revision --autogenerate -m "Some description"` - this will generate a new file in the 
versions directory which you should always check.


> alembic -c ./alembic/alembic.ini revision --autogenerate -m "First table"
