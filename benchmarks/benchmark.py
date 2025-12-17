import time
import csv

from src.reader import CustomCsvReader
from src.writer import CustomCsvWriter


def generate_csv(path, rows=10_000, cols=5):
    with open(path, "w", encoding="utf-8") as f:
        for i in range(rows):
            row = [
                f'"Value {i},{j} ""text"""'
                for j in range(cols)
            ]
            f.write(",".join(row) + "\n")


def benchmark_custom_reader(path):
    start = time.time()
    for _ in CustomCsvReader(path):
        pass
    return time.time() - start


def benchmark_std_reader(path):
    start = time.time()
    with open(path, newline="", encoding="utf-8") as f:
        list(csv.reader(f))
    return time.time() - start


def benchmark_custom_writer(rows):
    writer = CustomCsvWriter("data/custom_out.csv")
    start = time.time()
    writer.write(rows)
    return time.time() - start


def benchmark_std_writer(rows):
    start = time.time()
    with open("data/std_out.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)
    return time.time() - start


if __name__ == "__main__":
    csv_path = "data/bench.csv"

    generate_csv(csv_path)

    custom_read = benchmark_custom_reader(csv_path)
    std_read = benchmark_std_reader(csv_path)

    rows = [["A,B", 'Text "quoted"', "Line\nBreak", 123, "End"]] * 10_000
    custom_write = benchmark_custom_writer(rows)
    std_write = benchmark_std_writer(rows)

    print("\n--- Benchmark Results ---")
    print(f"Custom Reader : {custom_read:.3f}s")
    print(f"csv.reader   : {std_read:.3f}s")
    print(f"Read Slowdown: {custom_read / std_read:.2f}x\n")

    print(f"Custom Writer: {custom_write:.3f}s")
    print(f"csv.writer   : {std_write:.3f}s")
    print(f"Write Slowdown: {custom_write / std_write:.2f}x")
