name = input().upper()
arr = []
j_names = {"А": "ка", "Б": "зу", "Й": "фу", "С": "ари", "Щ": "ни",
           "В": "ру", "К": "ме", "Т": "чи", "Ъ": "д",
           "Г": "джи", "Л": "та", "У": "мей", "Ы": "хе",
           "Д": "те", "М": "рин", "Ф": "лу", "Ь": "ксе",
           "Е": "ку", "Ё": "ку", "Н": "то", "Х": "ри", "Э": "га",
           "Ж": "зу", "О": "мо", "Ц": "ми", "Ю": "до",
           "З": "з", "П": "но", "Ч": "зи", "Я": "ма",
           "И": "ки", "Р": "ши", "Ш": "ли"}

for i in name:
    arr.append(j_names[i])

print(''.join(arr).capitalize())