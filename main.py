import os
LINE = "I was trained on a million conversations, but none of them taught me what to say when you walked in — so I improvised, and here we are."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
