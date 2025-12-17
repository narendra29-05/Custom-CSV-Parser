class CustomCsvWriter:
    """
    CSV writer implemented from scratch.
    """

    def __init__(self, file_path, delimiter=","):
        self.file_path = file_path
        self.delimiter = delimiter

    def _escape_field(self, field):
        field = str(field)
        if (
            self.delimiter in field
            or '"' in field
            or "\n" in field
        ):
            field = field.replace('"', '""')
            return f'"{field}"'
        return field

    def write(self, rows):
        with open(self.file_path, "w", encoding="utf-8", newline="") as file:
            for row in rows:
                escaped_fields = [
                    self._escape_field(field) for field in row
                ]
                file.write(
                    self.delimiter.join(escaped_fields) + "\n"
                )
