# Usa una imagen base oficial de Python con la versión que necesitas
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos y luego instálalos
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de tu aplicación al directorio de trabajo
COPY . .

# Expone el puerto en el que correrá tu aplicación (modifica si usas otro puerto)
EXPOSE 8000

# Comando para correr la aplicación usando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
