#!/usr/bin/env python3
"""
Versión simple del CSV Column Splitter

Script simplificado para dividir una columna CSV rápidamente.
Ideal para uso interactivo.
"""

import pandas as pd
import os


def split_csv_simple(csv_file, column_name, delimiter=' ', new_col1='columna1', new_col2='columna2'):
    """
    Versión simplificada para dividir una columna CSV.
    
    Args:
        csv_file: Archivo CSV a procesar
        column_name: Nombre de la columna a dividir
        delimiter: Delimitador (por defecto: espacio)
        new_col1: Nombre de la primera columna nueva
        new_col2: Nombre de la segunda columna nueva
    
    Returns:
        DataFrame con las columnas divididas
    """
    try:
        # Leer CSV
        df = pd.read_csv(csv_file)
        print(f"📁 Archivo: {csv_file}")
        print(f"📊 Filas: {len(df)}, Columnas: {len(df.columns)}")
        
        # Verificar que existe la columna
        if column_name not in df.columns:
            print(f"❌ Error: La columna '{column_name}' no existe.")
            print(f"💡 Columnas disponibles: {', '.join(df.columns)}")
            return None
        
        # Dividir la columna
        split_data = df[column_name].str.split(delimiter, n=1, expand=True)
        
        # Asignar nuevas columnas
        df[new_col1] = split_data[0] if 0 in split_data.columns else ''
        df[new_col2] = split_data[1] if 1 in split_data.columns else ''
        
        # Eliminar columna original
        df = df.drop(columns=[column_name])
        
        # Guardar resultado
        output_file = csv_file.replace('.csv', '_dividido.csv')
        df.to_csv(output_file, index=False)
        
        print(f"✅ Éxito: Columna '{column_name}' dividida en '{new_col1}' y '{new_col2}'")
        print(f"💾 Guardado en: {output_file}")
        
        return df
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None


def main():
    """Función principal interactiva."""
    print("🔧 CSV Column Splitter - Versión Simple")
    print("=" * 40)
    
    # Solicitar archivo
    csv_file = input("📁 Archivo CSV: ").strip()
    
    if not os.path.exists(csv_file):
        print(f"❌ El archivo '{csv_file}' no existe.")
        return
    
    # Mostrar columnas disponibles
    try:
        df_temp = pd.read_csv(csv_file)
        print(f"\n💡 Columnas disponibles:")
        for i, col in enumerate(df_temp.columns, 1):
            print(f"   {i}. {col}")
    except:
        print("❌ Error al leer el archivo.")
        return
    
    # Solicitar parámetros
    column_name = input("\n📋 Columna a dividir: ").strip()
    delimiter = input("✂️  Delimitador [espacio]: ").strip() or ' '
    new_col1 = input("📝 Nombre columna 1 [columna1]: ").strip() or 'columna1'
    new_col2 = input("📝 Nombre columna 2 [columna2]: ").strip() or 'columna2'
    
    print("\n🚀 Procesando...")
    result = split_csv_simple(csv_file, column_name, delimiter, new_col1, new_col2)
    
    if result is not None:
        print("\n📊 Primeras filas del resultado:")
        print(result.head().to_string(index=False))


if __name__ == "__main__":
    main()