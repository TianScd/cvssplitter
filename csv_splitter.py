#!/usr/bin/env python3
"""
CSV Column Splitting Tool

Script para dividir una columna de CSV en dos columnas separadas.
"""

import pandas as pd
import argparse
import sys
from pathlib import Path


def split_csv_column(input_file, output_file, column_name, delimiter, new_columns):
    """
    Divide una columna de CSV en dos columnas nuevas.
    
    Args:
        input_file: Ruta del archivo CSV de entrada
        output_file: Ruta del archivo CSV de salida
        column_name: Nombre de la columna a dividir
        delimiter: Delimitador para dividir la columna
        new_columns: Lista con los nombres de las dos nuevas columnas
    """
    try:
        # Leer el archivo CSV
        df = pd.read_csv(input_file)
        print(f"Archivo leído exitosamente: {input_file}")
        print(f"Dimensiones: {df.shape}")
        
        # Verificar que la columna existe
        if column_name not in df.columns:
            print(f"Error: La columna '{column_name}' no existe en el archivo.")
            print(f"Columnas disponibles: {list(df.columns)}")
            return False
        
        # Dividir la columna
        # Usar str.split con n=1 para dividir solo en la primera ocurrencia del delimitador
        split_data = df[column_name].str.split(delimiter, n=1, expand=True)
        
        # Si la división resulta en menos de 2 columnas, rellenar con valores vacíos
        if split_data.shape[1] == 1:
            split_data[1] = ''
        
        # Asignar los nombres de las nuevas columnas
        df[new_columns[0]] = split_data[0]
        df[new_columns[1]] = split_data[1]
        
        # Eliminar la columna original (opcional)
        df = df.drop(columns=[column_name])
        
        # Guardar el resultado
        df.to_csv(output_file, index=False)
        print(f"Archivo guardado exitosamente: {output_file}")
        print(f"Columna '{column_name}' dividida en '{new_columns[0]}' y '{new_columns[1]}'")
        
        return True
        
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {input_file}")
        return False
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return False


def main():
    """Función principal con interfaz de línea de comandos."""
    parser = argparse.ArgumentParser(
        description='Divide una columna de CSV en dos columnas separadas'
    )
    
    parser.add_argument(
        'input_file', 
        help='Archivo CSV de entrada'
    )
    
    parser.add_argument(
        '-o', '--output', 
        default=None,
        help='Archivo CSV de salida (por defecto: input_modificado.csv)'
    )
    
    parser.add_argument(
        '-c', '--column', 
        required=True,
        help='Nombre de la columna a dividir'
    )
    
    parser.add_argument(
        '-d', '--delimiter', 
        default=',',
        help='Delimitador para dividir la columna (por defecto: coma)'
    )
    
    parser.add_argument(
        '-n', '--new-columns', 
        nargs=2,
        required=True,
        help='Nombres de las dos nuevas columnas (ejemplo: -n "col1" "col2")'
    )
    
    args = parser.parse_args()
    
    # Definir archivo de salida si no se especifica
    if args.output is None:
        input_path = Path(args.input_file)
        output_name = input_path.stem + '_modificado' + input_path.suffix
        args.output = input_path.parent / output_name
    
    # Mostrar información de la operación
    print("=== CSV Column Splitting Tool ===")
    print(f"Archivo de entrada: {args.input_file}")
    print(f"Archivo de salida: {args.output}")
    print(f"Columna a dividir: {args.column}")
    print(f"Delimitador: '{args.delimiter}'")
    print(f"Nuevas columnas: {args.new_columns}")
    print("-" * 40)
    
    # Ejecutar la división
    success = split_csv_column(
        args.input_file,
        args.output,
        args.column,
        args.delimiter,
        args.new_columns
    )
    
    if success:
        print("¡Operación completada exitosamente!")
        sys.exit(0)
    else:
        print("La operación falló.")
        sys.exit(1)


if __name__ == "__main__":
    main()