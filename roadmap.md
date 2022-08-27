# Conceptos a tener en cuenta

## ¿Que es una API?

Una API (interfaz de programacion de aplicaciones) es un conjunto de reglas que determinan
como las apliaciones o los dispositivos pueden conectarse y comunicarse entre si.

## ¿Que es REST?

Representational state transfer es un estilo de  arquitectura de software para sistemas hipermedia distribuidos como la World Wide Web.
Principalmente el termino REST se referia a un conjunto de principios de arquitectura. pero hoy en día es utilizado para describir cualquier interfaz entre sistemas que utilice directamente el protocolo HTTP para obtener datos o indicar la ejecucion de operaciones sobre los datos, en cualquier formato sin las abstracciones adicionales de los protocolos basados en patrones de intercambios de mensajes.

### Principios de diseño REST

1. Interfaz uniforme: Todas las solicitudes de API para el mismo recurso deben ser iguales, independientemente de la procedencia de la solicitud. LA API REST debe asegurarse de que el mismo dato, como el nombre de direccion de e-mail, de un usuario, pertenezca a un unico identificador uniforme de recurso (URI). Los recursos no deben ser demasiado grande, pero deben contener toda la información que el cliente pueda necesitar.

2. Separacion entre el cliente y servidor: las aplicaciones de cliente y de servidor deben ser independientes entre si. La unica informacion que la apliacion de cliente debe conocer es el URI del recurso solicitado. No puede interactuar con la aplicacion de servidor de ninguna otra forma. De misma forma, una aplicacion de servidor no debe modificar la aplicacion del cliente mas alla de entregarle los datos solicitados via HTTP.

3. Sin estado. Las API REST son sin estado, lo que significa que cada solicitud debe incluir toda la información necesaria para procesarla. En otras palabras, las API REST no requieren ninguna sesión en el lado del servidor. Las aplicaciones de servidor no pueden almacenar ningún dato relacionado con una solicitud de cliente.

4. Capacidad de almacenamiento en memoria caché. Siempre que sea posible, los recursos deben poder almacenarse en la memoria caché en el lado del cliente o el servidor. Las respuestas de servidor también necesitan contener información de si el almacenamiento en memoria caché está permitido para el recurso entregado. El objetivo es mejorar el rendimiento en el lado del cliente, al mismo tiempo que aumenta la escalabilidad en el lado del servidor.

5. Arquitectura de sistema de capas. En las API REST, las llamadas y respuestas pasan por diferentes capas. Como regla general, no debe suponer que las aplicaciones de cliente y de servidor se conectan directamente entre sí. Puede haber una serie de intermediarios diferentes en el bucle de comunicación. Las API REST deben diseñarse para que ni el cliente ni el servidor puedan notar si se comunican con la aplicación final o con un intermediario.

6. Código bajo demanda (opcional). Generalmente, las API REST envían recursos estáticos, pero en algunos casos, las respuestas también pueden contener un código ejecutable (como applets de Java). En estos casos, el código solo debería ejecutarse bajo demanda.

URI: Un identificador de recursos uniforme o URI (uniform resource identifier) es una cadena de caracteres que identifica los recursos (físicos o abstractos) de una red de forma unívoca. La diferencia respecto a un localizador de recursos uniforme (URL) es que estos últimos hacen referencia a recursos que pueden variar en el tiempo.

## ¿Que es una API RESTful?

Es una API que esta implementada con la arquitectura REST.

## ¿Que es WSGI?

WSGI son las siglas de Web Server Gateway Interface. Es una especificación que describe cómo se comunica un servidor web con una aplicación web, y cómo se pueden llegar a encadenar diferentes aplicaciones web para procesar una solicitud/petición (o request). Es un estandar de Python.

[WSGI](https://medium.com/@nachoad/que-es-wsgi-be7359c6e001)

## ¿Que es ASGI?


## Pydantic y Starlette



Paper de Roy Fielding sobre REST: https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf
