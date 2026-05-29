data = input("input the data:")
UNIQUE_ELEMENTS_LIMIT = 10

if len(set(data)) > UNIQUE_ELEMENTS_LIMIT:
    print(True)
else:
    print(False)