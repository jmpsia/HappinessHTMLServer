import csv
from typing import Callable, NamedTuple
from psycopg2.extensions import connection
from happiness import populate_happiness


class PopulateTask(NamedTuple):
    create_table_file_path: str
    data_file_path: str
    populate_fn: Callable[[list[dict[str, str]]], None]


def populate(task: PopulateTask, conn: connection) -> None:
    with conn.cursor() as cur:
        with open(task.create_table_file_path, encoding="utf8") as schema_file:
            cur.execute(schema_file.read())
        print(f"executed schema file {task.create_table_file_path}")
        with open(task.data_file_path, encoding="utf8") as csv_file:
            rows = list(csv.DictReader(csv_file))
            task.populate_fn(cur, rows)
        print(f"processed {task.data_file_path}")


POPULATE_TASKS: list[PopulateTask] = [
  PopulateTask("./schema/happiness.sql",
                 "./data/happiness.csv", populate_happiness),
]
