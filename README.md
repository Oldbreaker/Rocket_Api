## Preguntas

se encuentran las primeras 4 preguntas de la prueba en el archivo request.py

## Proyecto

El proyecto del backend de usuarios esta basado como api usando las librerias de django y django_restframework.

Todos las vistas requieren que se este autenticado como un adminUser

- Crear un superuser para utilizarlo como usuario. # python manage.py createsuperuser

Decide también usar jwt para poder la utenticación de las clases

## instalar

En los requeriments se encuentran todas las dependencias necesarias
`pip install -r requirements.txt`

## Proyecto

El proyecto del backend de usuarios esta basado como api usando las librerias de django y django_restframework.

Todos las vistas requieren que se este autenticado como un adminUser

- Crear un superuser para utilizarlo como usuario. # python manage.py createsuperuser

Decide también usar jwt para poder la utenticación de las clases

## URL del proyecto

- localhost:8000/users/create creación de un nuevo usuario:

  - Requiere Authorization Bearer token = token generado por localhost:8000/api/token/

  ```javascript
  {
  "username": "",
  "password": "",
  "email":"",
  "first_name":"",
  "last_name":""
  }
  ```

- localhost:8000/users/get/<int:pk> Obtener un usuario por id:
  - Requiere Authorization Bearer token = token generado por localhost:8000/api/token/

-localhost:8000/users/delete/<int:pk> Eliminar un usuario por id:

- Requiere Authorization Bearer token = token generado por localhost:8000/api/token/

-localhost:8000/users/update/<int:pk> Modificar un usuario por id:

- Requiere Authorization Bearer token = token generado por localhost:8000/api/token/

```javascript
{
"username": "",
"password": "",
"email":"",
"first_name":"",
"last_name":""
}
```

- localhost:8000/api/token/ Genera el TOKEN para autenticación (duración de token 60 minutos):

  - Crear un superuser para utilizarlo como usuario. # python manage.py createsuperuser

  ```javascript
  {
  "username": "",
  "password": ""
  }
  ```

- localhost:8000/api/token/refresh/ Refresh del token:
  ```javascript
  {
  "refresh":"Token"
  }
  ```
