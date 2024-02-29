

# DataIngestionAPI



## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado Python 3.8 o superior. Puedes descargarlo desde [python.org](https://www.python.org/).

## Configuración del Entorno de Desarrollo


### 1. Clonar el Repositorio

Primero, clona este repositorio en tu máquina local usando:

```
    git clone https://github.com/jgonzalezef/AnalyticsEngineAPI.git
```

### 2. Crear un Entorno Virtual

```
    python -m venv nombredelentorno
```

### 3. Activar el Entorno Virtual

* En Windows:
```
    .\nombredelentorno\Scripts\activate
```

* En Unix o MacOS::
```
    source nombredelentorno/bin/activate
```

### 4. Instalar Dependencias
```
    pip install -r requirements.txt
```

### 5.Renombrar el archivo
- ``.env.template`` por ``.env`` y configurar variables de entorno.
```
     PORT= puerto en el que correra la api
```

### 6. Ejecutar la Aplicación
```
    python main.py
```
