store = {}

def set_value(key,value):
    store[key] = value

def get_value(key):
    if key in store:
        return store[key]
    return None

def delete_value(key):
    if key in store:
        del store[key]
        return 1
    return 0

def exists(key):
    if key in store:
        return 1
    return 0

def run():
    while True:
        command = input("redis> ")

        if command == "EXIT":
            break

        parts = command.split()

        if len(parts) == 0:
            continue

        operation = parts[0].upper()

        if operation == "SET":
            if len(parts) != 3:
                print("ERR wrong number of arguments for SET")
                continue

            key = parts[1]
            value = parts[2]
            set_value(key, value)
            print("OK")

        elif operation == "GET":
            if len(parts) != 2:
                print("ERR wrong number of arguments for GET")
                continue

            key = parts[1]
            value = get_value(key)
            print(value)

        elif operation == "DEL":
            if len(parts) != 2:
                print("ERR wrong number of arguments for DEL")
                continue

            key = parts[1]
            is_delete = delete_value(key)
            print(is_delete)

        elif operation == "EXISTS":
            if len(parts) != 2:
                print("ERR wrong number of arguments for EXISTS")
                continue

            key = parts[1]
            is_exists = exists(key)
            print(is_exists)

        else:
            print("ERR unknown command")

if __name__ == "__main__":
    run()
