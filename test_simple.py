#!/usr/bin/env python3
"""
Demo para probar el csv_splitter_simple
"""

from csv_splitter_simple import split_csv_simple

def test_simple():
    """Prueba de la función split_csv_simple."""
    print("🧪 Probando CSV Column Splitter Simple...")
    
    # Probar con el archivo de ejemplo
    result = split_csv_simple(
        csv_file='ejemplo.csv',
        column_name='nombre_completo',
        delimiter=' ',
        new_col1='primer_nombre',
        new_col2='apellido_paterno'
    )
    
    if result is not None:
        print("\n✅ Test completado exitosamente!")
    else:
        print("\n❌ Test falló")

if __name__ == "__main__":
    test_simple()