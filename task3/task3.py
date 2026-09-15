from pydantic import BaseModel
import json


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

tests_path = input("Введите путь к файлу с тестами ")
values_path = input("Введите путь к файлу с результатами тестов ")
report_path = input("Введите путь сохранения тестов и их результатов ")

tests_root = Root.model_validate(json.loads(open(tests_path).read()))
values_root = RootValue.model_validate(json.loads(open(values_path).read()))

for i in values_root.values:
    update_test_value(i.id, i.value, tests_root.tests)

with open(report_path, "w", encoding="utf-8") as f:
    json.dump(tests_root.model_dump(exclude_unset=True, exclude_none=False), f, ensure_ascii=False, indent=2)
