import fitz, json

timetables = {}

def in_box(l, t, r, b, x, y):
    return l < x < r and t < y < b

def get_rooms(words):
    global timetables
    timetables[f'{grade}/{class_no + 1}'] = [[], [], [], [], []]
    for day in range(5):
        timetables[f'{grade}/{class_no + 1}'][day] = ['0'] * 10
        for period in range(10):
            x = 130 + 68 * period
            y = 195 + 87 * day
            for word in words:
                boundaries, text = word[:4], word[4]
                if in_box(*boundaries, x, y):
                    print(f'Day {day+1}. Period {period+1}: Room {text}')
                    timetables[f'{grade}/{class_no + 1}'][day][period] = text
                # Double period
                elif in_box(*boundaries, x + 34, y):
                    print(f'Day {day+1}. Period {period+1} - {period+2}: Room {text}')
                    timetables[f'{grade}/{class_no + 1}'][day][period] = text
                    timetables[f'{grade}/{class_no + 1}'][day][period+1] = text


for grade in range(1, 7):
    print(f"==== Grade {grade} ====")
    fname = f'timetables/M{grade}.pdf'
    doc = fitz.open(fname)
    for class_no, page in enumerate(doc):
        words = page.get_text("words")
        print(f"== Class {grade}/{class_no + 1} ==")
        timetables[f'{grade}/{class_no + 1}'] = {}
        get_rooms(words)

output = open('timetables.json', 'w')
json.dump(timetables, output, indent=4)
output.close()
