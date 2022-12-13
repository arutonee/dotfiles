from __future__ import annotations
import os
import re
import sys


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
