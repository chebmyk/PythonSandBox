class CodeBuilder:
    def __init__(self, root_name):
        root_name = str(root_name).capitalize()
        self._class = f"class {root_name}:"
        self._init = f"def __init__(self):"
        self._fields = []


    def add_field(self, name, value):
        self._fields.append([name, value])
        return self

    def __str__(self):
        result = f"{self._class}\n"
        result += f"\t{self._init}\n"
        for f in self._fields:
            result+=f"\t\tself.{f[0]} = {f[1]}\n"

        return result


cb = CodeBuilder('Person').add_field('name', '""')

print(cb)