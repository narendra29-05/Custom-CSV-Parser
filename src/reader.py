class CustomCsvReader:
    """
    A streaming CSV reader implemented from scratch.
    Supports quoted fields, escaped quotes, and embedded newlines.
    """

    def __init__(self, file_path, delimiter=","):
        self.file_path = file_path
        self.delimiter = delimiter
        self.file = open(file_path, "r", encoding="utf-8")
        self.in_quotes = False
        self.eof = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.eof:
            raise StopIteration

        row = []
        field = ""

        while True:
            char = self.file.read(1)

            if char == "":
                self.eof = True
                break

            if char == '"':
                if self.in_quotes:
                    next_char = self.file.read(1)
                    if next_char == '"':
                        field += '"'
                    else:
                        self.in_quotes = False
                        if next_char:
                            self.file.seek(self.file.tell() - 1)
                else:
                    self.in_quotes = True

            elif char == self.delimiter and not self.in_quotes:
                row.append(field)
                field = ""

            elif char == "\n" and not self.in_quotes:
                row.append(field)
                return row

            else:
                field += char

        if field or row:
            row.append(field)
            return row

        self.file.close()
        raise StopIteration
