from pydantic import BaseModel
import json
import argparse

parser = argparse.ArgumentParser(
        description='Обработка json'
)
parser.add_argument(
    'tests',
    help='Производимые тесты'
)
parser.add_argument(
    'values',
    help='Результаты тестов'
)
parser.add_argument(
    'report',
    help='Объединение'
)


class TestValues(BaseModel):
    id: int
    value: str


class RootValue(BaseModel):
    values: list[TestValues]


class TestNode(BaseModel):
    id: int
    title: str
    value: str | None = None
    values: list["TestNode"] = []


class Root(BaseModel):
    tests: list[TestNode]


def update_test_value(id, val, val_lst):
    for k in val_lst:
        if k.id == id:
            k.value = val
        elif len(k.values) > 0:
            update_test_value(id, val, k.values)


TestNode.model_rebuild()
TestValues.model_rebuild()
args = parser.parse_args()

tests_root = Root.model_validate(json.loads(open(args.tests).read()))
values_root = RootValue.model_validate(json.loads(open(args.values).read()))

for i in values_root.values:
    update_test_value(i.id, i.value, tests_root.tests)

with open(args.report, "w", encoding="utf-8") as f:
    json.dump(tests_root.model_dump(exclude_unset=True, exclude_none=False), f, ensure_ascii=False, indent=2)
