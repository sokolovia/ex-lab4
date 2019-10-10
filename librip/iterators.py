# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.my_items = list(items)
        self.my_items = sorted(set(self.my_items), key=self.my_items.index)
        if 'ignore_case' in kwargs:
            ignore_case = kwargs['ignore_case']
        else:
            ignore_case = False
        if ignore_case == False:
            temp = self.my_items.copy()
            index_list = []
            for i in range(len(temp)):
                if type(temp[i]) == str:
                    temp[i] = temp[i].lower()
                    index_list.append(i)
            temp_set = sorted(set(temp), key=temp.index)
            for item in temp_set:
                for i in index_list:
                   if item == temp[i]:
                        index_list.remove(i)
                        break
            index_list.reverse()
            for i in index_list:
                self.my_items[i] = None
            self.my_items = [x for x in self.my_items if x != None]
        self.my_len = len(self.my_items)
        self.i = 0

    def __next__(self):
        # Нужно реализовать __next__
        if self.i == self.my_len:           
            raise StopIteration
        else:    
            self.i+=1
            return(self.my_items[self.i-1])
            
    def __iter__(self):
        return self
