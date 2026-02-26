# CSV Column Splitting Tool

Una herramienta en Python para dividir una columna de un archivo CSV en dos columnas separadas.

## Descripción

Este script toma un archivo CSV con una columna que contiene datos separados por un delimitador y los divide en dos columnas independientes. Es útil cuando tienes datos combinados que necesitas separar, como nombres completos, direcciones, o cualquier información concatenada.

## Requisitos

- Python 3.7 o superior
- pandas

## Instalación

1. Clona o descarga este proyecto
2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Comando básico
```bash
python csv_splitter.py archivo_entrada.csv -c "columna_a_dividir" -n "columna1" "columna2"
```

### Ejemplos

#### Ejemplo 1: Dividir nombres completos
```bash
python csv_splitter.py personas.csv -c "nombre_completo" -d " " -n "nombre" "apellido"
```

#### Ejemplo 2: Dividir direcciones
```bash
python csv_splitter.py direcciones.csv -c "direccion_completa" -d "," -n "calle" "ciudad"
```

#### Ejemplo 3: Especificar archivo de salida
```bash
python csv_splitter.py datos.csv -c "info" -d ";" -n "parte1" "parte2" -o datos_divididos.csv
```

## Parámetros

- `input_file`: Archivo CSV de entrada (requerido)
- `-c, --column`: Nombre de la columna a dividir (requerido)
- `-n, --new-columns`: Nombres de las dos nuevas columnas (requerido)
- `-d, --delimiter`: Delimitador para dividir la columna (por defecto: coma)
- `-o, --output`: Archivo de salida (por defecto: input_modificado.csv)

## Características

- ✅ Divide una columna en exactamente dos columnas
- ✅ Manejo de diferentes delimitadores
- ✅ Preserva la estructura original del CSV
- ✅ Elimina la columna original después de la división
- ✅ Manejo de errores y validación de entrada
- ✅ Si no puede dividir, rellena con valores vacíos
- ✅ Solo divide en la primera ocurrencia del delimitador

## Ejemplo de archivo CSV

### Antes (entrada):
```csv
id,nombre_completo,edad
1,Juan Pérez,25
2,María García,30
3,Pedro López,28
```

### Después (salida):
```csv
id,edad,nombre,apellido
1,25,Juan,Pérez
2,30,María,García
3,28,Pedro,López
```

## Notas importantes

1. El script divide solo en la primera ocurrencia del delimitador
2. Si una fila no puede dividirse, se rellena con valores vacíos
3. La columna original se elimina del resultado final
4. Asegúrate de que el nombre de la columna coincida exactamente (caso sensible)

## Manejo de errores

El script incluye manejo de errores para los casos más comunes:
- Archivo no encontrado
- Columna no existe en el CSV
- Errores de formato del archivo

## Herramientas adicionales

### CSV Inspector
Para analizar un archivo CSV antes de dividir columnas:
```bash
python csv_inspector.py archivo.csv
```

Este inspector te mostrará:
- Información básica del archivo (dimensiones, tipos de datos)
- Lista de columnas con estadísticas
- Columnas candidatas para división
- Ejemplos de uso sugeridos

### Versión Simple
Para uso interactivo rápido:
```bash
python csv_splitter_simple.py
```

## Licencia

Este proyecto está disponible bajo licencia MIT.