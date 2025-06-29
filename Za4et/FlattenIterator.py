# 4. Напишите класс FlattenIterator, который принимает вложенный список (любой глубины) и итеративно возвращает все элементы в плоском виде.

# nested_list = [1, [2, [3, 4], 5], 6]
# flat = FlattenIterator(nested_list)
# for num in flat:
#     print(num)
#(!) Решение не должно использовать рекурсию в next, а работать итеративно

class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = []
        self._prepare_stack(nested_list)
    def _prepare_stack(self, nested):
        stack = [nested]
        while stack:
            current = stack.pop()
            if isinstance(current, list):
                stack.extend(reversed(current))
            else:
                self.stack.append(current)
    def __iter__(self):
        return self
    def __next__(self):
        if not self.stack:
            raise StopIteration
        return self.stack.pop(0)

nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
for num in flat:
    print(num)