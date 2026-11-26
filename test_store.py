from main import set_value, get_value,delete_value, exists

set_value("name", "Alex")

assert get_value("name") == "Alex"
assert exists("name") == 1
assert delete_value("name") == 1
assert exists("name") == 0
assert get_value("name") is None
assert delete_value("name") == 0

print("All tests have passed")
