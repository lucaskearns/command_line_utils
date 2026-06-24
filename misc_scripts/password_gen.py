import string
import secrets
import sys

# 23 June 2026
# Lucas Kearns

# Simple script to generate passwords in a 'secure' manner.

# Simple IO for now, can replace with argparse later for more
# sophisticated options.
pass_len = int(sys.argv[1])

# Generate string of valid chars
valid_chars = string.ascii_letters + string.digits
valid_symbols = "!@#$%&*()-+="
valid_chars += valid_symbols

# Random password generation
idxs = [secrets.randbelow(len(valid_chars)) for _ in range(pass_len)]
rand_pass = "".join([valid_chars[idx] for idx in idxs])

print(rand_pass)
