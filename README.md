# USD to CLP API
## Api para convertir de dolares a pesos

Antes de iniciar la api, instala las librerías con el siguiente código.
Asegúrate de estar en la carpeta del proyecto.
> pip install -r requirements.txt

Para iniciar el servidor, ejecuta lo siguiente.
> python manage.py runserver

## Modo de uso

La api se usa desde la url http://127.0.0.1:8000/30/usd/clp

Su respuesta será
> {"value": 23995.4}

* 2: Este es el valor de la cantidad que se va a convertir de la moneda de
origen a la moneda de destino. En este caso, la cantidad es 30.
* usd: Este es el código de la moneda de origen. En este caso, la moneda de 
origen es el dólar estadounidense.
* clp: Este es el código de la moneda de destino. En este caso, la moneda de
destino es el peso chileno.

Estos valores se pueden cambiar según sea necesario.
