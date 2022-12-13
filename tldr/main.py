from __future__ import annotations
import os
import re
import sys

class Trio:
    def __init__(self, pre: str, atom, post: str):
        self.pre = pre
        self.atom = atom
        self.post = post

        self.symbols = {
            '\\{': '{',
            '\\}': '}',
            '\\,': ',',
            chr(2): '\\'
        }

    @staticmethod
    def from_string(string: str, pre: str="", post: str="") -> Trio:
        s = string.replace(r'\\', chr(2))
        split_by_commas = re.split(r'(?<!\\),', s)
        upper_level_split_by_commas = []
        final = []
        starts = 0
        for part in split_by_commas:
            if starts == 0: upper_level_split_by_commas.append(part)
            else:
                upper_level_split_by_commas[-1] += ',' + part
                starts -= len(re.findall(r'(?<!\\)}', part))
            starts += len(re.findall(r'(?<!\\){', part))

        for expr in upper_level_split_by_commas:
            start_brace = re.search(r'(?<!\\){', expr)
            end_brace = re.search(r'}(?!\\)', expr[::-1])
            start = None
            end = None
            if start_brace: start = start_brace.span()[0]
            if end_brace: end = len(expr) - end_brace.span()[0]
            if start and end:
                final.append(Trio.from_string(expr[start+1:end-1],expr[:start],expr[end:]))
            else:
                final.append(expr)

        return Trio(pre, final, post)

    def generate_combinations(self):
        combos = []
        for v in self.atom:
            if type(v) is str:
                combos.append(v)
            elif type(v) is Trio:
                combos += v.generate_combinations()
        for symbol in self.symbols:
            self.pre = self.pre.replace(symbol, self.symbols[symbol])
            self.post = self.post.replace(symbol, self.symbols[symbol])
            for i in range(len(combos)):
                combos[i] = combos[i].replace(symbol, self.symbols[symbol])
        return [self.pre + v + self.post for v in combos]

    def __repr__(self):
        return f'Trio(\'{self.pre}\' <- {self.atom} -> \'{self.post}\')'


def clear_screen():
    for _ in range(20): print()

def display_entry(entries, index):
    clear_screen()
    print('\n'.join(entries[index][1:]))

def display_page(entries, page_num, entries_per_page):
    page_offset = page_num * entries_per_page
    selected = False
    while not selected:
        clear_screen()
        while page_offset >= len(entries):
            page_offset -= entries_per_page
        if page_offset < 0:
            page_offset = 0
        end = page_offset+entries_per_page
        if end >= len(entries): end = len(entries)
        page_len = end-page_offset
        for i,entry in enumerate(entries[page_offset:end]):
            print(f"{i}: {entry[0]}")
        print("""
{0-9}: Open entry
n[ext]: Next page
p[rev[ious]]: Previous page
/{search}: Search
q: Quit
          """)
        uin = input("Selection: ").lower()
        if uin in ["n", "next"]:
            page_offset += entries_per_page
        elif uin in ["p", "prev", "previous"]:
            page_offset -= entries_per_page
        elif uin.startswith("/"):
            print("This feature will be added later.")
        elif uin == "q":
            print("Goodbye!")
            sys.exit()
        else:
            if uin in map(lambda n: str(n), range(page_len)):
                selected = True
                display_entry(entries, page_offset + int(uin))

def main():
    entry_path = os.path.dirname(__file__) + "/entries"
    if len(sys.argv) == 1:
        print("Search feature will be added later.")
    elif len(sys.argv) == 2:
        file_location = f"{entry_path}/{sys.argv[1]}"
        if not os.path.exists(file_location):
            return print(f"There is no entry for {sys.argv[1]}")
        with open(file_location, "r") as f:
            entries = list(map(lambda e: e.split("\n"), f.read().split("\n\n")))
        display_page(entries, 0, 10)
    else:
        print("Script documentation will be added later.")

if __name__ == "__main__":
    main()
