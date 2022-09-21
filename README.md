# service-users

> In order to trigger the alembic migrations, you run the `alembic upgrade head` command.
When you make any change to a database table, you capture that change by running `alembic
revision --autogenerate -m "Some description"` - this will generate a new file in the 
versions directory which you should always check.