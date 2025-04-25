import json

input_file = "video_game_sales_forecasting_cleaned.ipynb"
output_file = "video_game_sales_forecasting_final_cleaned.ipynb"

# Función recursiva para eliminar todas las claves "id" del diccionario
def remove_ids(obj):
    if isinstance(obj, dict):
        obj = {k: remove_ids(v) for k, v in obj.items() if k != "id"}
    elif isinstance(obj, list):
        obj = [remove_ids(i) for i in obj]
    return obj

# Cargar el archivo .ipynb
with open(input_file, "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Eliminar todos los "id"
notebook_cleaned = remove_ids(notebook)

# Guardar el archivo limpio
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(notebook_cleaned, f, indent=2, ensure_ascii=False)

print(f"✅ Archivo limpio guardado como: {output_file}")
