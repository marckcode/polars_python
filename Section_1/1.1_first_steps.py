import polars as pl
import random
import string

def generate_random_string(length: int) -> str:
    return "".join(random.choice(string.ascii_letters) for i in range(length))

data = {}
for i in range(1, 11):
    data[f"column_{i}"] = [generate_random_string(50) for _ in range(5)]
    
df  = pl.DataFrame(data)
# print(df)

# Set the amount of columns that is showed to minus one 
# (to print all of them), and lower the string length that is displayed to four.

with pl.Config(tbl_cols=-1, fmt_str_lengths=4):
    print(df)
    
    
@pl.Config(ascii_tables=True)
def write_ascii_frame_to_stdout(df: pl.DataFrame) -> None:
    print(str(df))
    
@pl.Config(verbose=True)
def function_that_im_debugging(df: pl.DataFrame) -> None:
    # Polars operation you want to see the verbose logging of
    print(str(df))