import fitz


# Dla output path podać ścieżkę folderu docelowego bez nazwy pliku

def pdf_fill(char, pdf_path, output_path):
    doc = fitz.open(pdf_path)
    class_fields = ['race', 'profession', 'true_profession', 'status', 'character_class', 'hp', 'destiny_points',
                    'hero_points', 'speed', 'name', 'age', 'eye_color', 'hair_color', 'height']

    for i in range(2):
        page = doc.load_page(i)
        for field in page.widgets():
            if field.field_name in class_fields:
                field.field_value = str(getattr(char, field.field_name))
                field.update()

    output_path += f"{char.name} {char.true_profession}.pdf"
    doc.save(output_path)
    doc.close()
