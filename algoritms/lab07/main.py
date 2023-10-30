class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)

    def get_values(self):
        values = []
        for bucket in self.table:
            for pair in bucket:
                values.append(pair[1])
        return values


# Создаем хеш-таблицу и добавляем элементы в таблицу
ht = HashTable()
ht.insert('key1', 'value1')
ht.insert('key2', 'value2')
ht.insert('key3', 'value3')

# Получаем значения из таблицы и выводим их
values = ht.get_values()
for value in values:
    print(value)
