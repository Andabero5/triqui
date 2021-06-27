# **Instrucciones de ejecución**
1. Tener instalado python (se puede descargar en su pagina oficial, click [aquí](https://www.python.org/downloads/)) )
2. desde el directorio del programa ejecutar el entorno vitual que contiene las librerias necesarias. abrir la consola y escribir
```
env/Scripts/activate
```
   - si no desea trabajar con el entorno vitual, debera ejecutar las siguientes lineas de comando en la consola, para instalar las librerias necesarias.
```python
pip install pygame
```
```python
pip install numpy
```
```python
pip install pymysql
```
3. Debera instalar MySql para tener compatibilidad con la base de datos (se puede descargar en su pagina oficial, click [aquí](https://dev.mysql.com/downloads/windows/installer/8.0.html)) )
4. debera importar las tablas que se encuentran en la carpeta [db](db) a un proyecto en MySql
5. Para validar sus datos en la base de datos debera cambiar los datos contenidos en la clase Database conteenida en [player.py](player.py)
   