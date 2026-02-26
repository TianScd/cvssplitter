#!/usr/bin/env python3
"""
Utilidad para ver información de archivos CSV
"""

import pandas as pd
import sys
import os


def inspect_csv(csv_file):
    """
    Inspecciona un archivo CSV y muestra información sobre sus columnas.
    
    Args:
        csv_file: Ruta del archivo CSV a inspeccionar
    """
    if not os.path.exists(csv_file):
        print(f"❌ Error: El archivo '{csv_file}' no existe.")
        return
    
    try:
        # Leer el archivo CSV
        df = pd.read_csv(csv_file)
        
        print(f"📊 === Información del archivo: {csv_file} ===")
        print(f"📏 Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
        print(f"💾 Tamaño en memoria: {df.memory_usage(deep=True).sum():,} bytes")
        
        print(f"\n📋 Columnas disponibles:")
        for i, col in enumerate(df.columns, 1):
            non_null = df[col].count()
            total = len(df)
            null_count = total - non_null
            dtype = str(df[col].dtype)
            
            print(f"  {i:2d}. {col:<20} | Tipo: {dtype:<10} | No nulos: {non_null}/{total} | Nulos: {null_count}")
        
        print(f"\n📝 Primeras 3 filas:")
        print(df.head(3).to_string(index=False))
        
        # Mostrar filas con valores únicos para cada columna
        print(f"\n🔢 Valores únicos por columna:")
        for col in df.columns:
            unique_count = df[col].nunique()
            total_count = len(df)
            print(f"  {col}: {unique_count} únicos de {total_count} total ({unique_count/total_count*100:.1f}%)")
        
        # Buscar columnas que podrían ser divididas
        print(f"\n✂️  Columnas candidatas para división (contienen espacios, comas, etc.):")
        delimiters = [' ', ',', ';', '-', '_', '|', ':']
        candidates = []
        
        for col in df.select_dtypes(include=['object']).columns:
            for delim in delimiters:
                if df[col].str.contains(delim, na=False).any():
                    # Contar cuántas filas contienen el delimitador
                    count = df[col].str.contains(delim, na=False).sum()
                    candidates.append((col, delim, count))
        
        if candidates:
            for col, delim, count in candidates:
                delim_name = {'':' (espacio)', ',': '(coma)', ';': '(punto y coma)', '-': '(guión)', '_': '(guión bajo)', '|': '(pipe)', ':': '(dos puntos)'}.get(delim, f'({delim})')
                print(f"  '{col}' con '{delim}' {delim_name}: {count}/{len(df)} filas ({count/len(df)*100:.1f}%)")
        else:
            print("  No se encontraron columnas candidatas obvias.")
        
        print(f"\n💡 Ejemplo de uso:")
        if candidates:
            col, delim, _ = candidates[0]
            print(f"  python csv_splitter.py {csv_file} -c \"{col}\" -d \"{delim}\" -n \"parte1\" \"parte2\"")
        else:
            print(f"  python csv_splitter.py {csv_file} -c \"columna_a_dividir\" -d \" \" -n \"parte1\" \"parte2\"")
            
    except Exception as e:
        print(f"❌ Error al procesar el archivo: {str(e)}")


def main():
    """Función principal."""
    if len(sys.argv) != 2:
        print("📊 CSV Inspector")
        print("================")
        print("Uso: python csv_inspector.py <archivo.csv>")
        print("\nEste script analiza un archivo CSV y muestra información útil sobre sus columnas,")
        print("incluyendo sugerencias para dividir columnas.")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    inspect_csv(csv_file)


if __name__ == "__main__":
    main()