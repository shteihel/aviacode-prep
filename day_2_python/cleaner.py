import os

# Путь к папке с данными
folder_path = "dataset"

# Получаем список файлов и сортируем их
files = os.listdir(folder_path)
files.sort()

print(f"Всего файлов: {len(files)}")

counter = 1

# Проходим по каждому файлу
for filename in files:
    # Проверка: если это картинка (jpg, png, jpeg)
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        
        # Старый полный путь
        old_path = os.path.join(folder_path, filename)
        
        # Получаем расширение (например .jpg)
        _, extension = os.path.splitext(filename)
        
        # Новое имя: 001.jpg, 002.png ...
        new_filename = f"turbine_{counter:03d}{extension}"
        
        # Новый полный путь
        new_path = os.path.join(folder_path, new_filename)
        
        # ПЕРЕИМЕНОВАНИЕ
        os.rename(old_path, new_path)
        
        print(f"✅ {filename} -> {new_filename}")
        counter += 1
    else:
        print(f"❌ Пропущен (не картинка): {filename}")

print("Готово! Датасет чист.")
print('Красавчик!')
