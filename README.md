# Laboratorio-6

## Callbacks en Python
Para esta primera parte de laboratorio se descargaron los dos archivos correspondientes, siendo estos el de eventos y el de data_manager. El archivo de eventos se le pasó como un módulo al de data_manager con el fin de que este pudiera recibir los parametros de la clase EventManager, luego se acomodó la librería de threading arriba del código y de definió una condición de para que para cuando se cumpla el programa se pueda terminar exitosamente con el comando "Ctrl + C" . Para presentar a través del EventManager que los datos han cambiado se le agregó una función print_updated_data() con el parámetro de data que se encarga de devolver los datos actualizados gracias a el real_time_data_manager.event_manager.subscribe(), además de que la variable con los cambios se logró definir para que recibiera la información de manera correcta.

Ejempo de ejecución del código:

![image](https://github.com/DanielValverde0203/Laboratorio-6/assets/143844258/b0976d28-552e-4d5c-bd2b-57a9e65c8ad1)


## Funciones Lambda en Python


En esta parte del laboratorio se trabajó con el archivo llamado calcualdora, el cual se debía modificar de tal manera que realizara las operaciones matemáticas con una respectiva función lambda. En primer lugar se modificó la función de ejecutar_operacion() para que se pudiera invocar cada operación correspondiente, para ello se eliminaron los if y elif y se remplazaron por un try y expect que ya contenía el paramentro, el cual se le otorga por medio de un parametro llamado operations definido dentro del main y un callback que devuelve los numeros ya introducidos de antes para que este pueda llamar a la función lambda que necesita para realizar la operación solicitada. Con respecto a las operaciones matemáticas, se definió cada una como una función lambda que recibía como parametro el numero 1 "x" y el numero 2 "y" y luego ejecutaba su función específica para luego devolverla como result, o de ser el caso algun error en particular.

Ejemplo de ejecución del código:

![Screenshot 2023-12-02 190350](https://github.com/DanielValverde0203/Laboratorio-6/assets/143844258/c1581aac-4ad4-4857-b629-4d2c1bc48b82)



## Conclusiones

1. El uso de callbacks permite pasarle argumentos a otras funciones que no los poseen, esto para facilitar la forma en la que se reciben, operan y modifican los parametros con la finalidad de devolver ya sea uno o varios resultados diferentes con mayor facilidad.
2. Las funciones lambda permiten operar con parametros para que estos realicen una acción específica sin la necesidad de tener que definir una funcion normal y tener que pasarle otros parametros, facilitando así la manera en la que se devuelve la salida de un código o se realiza algún cálculo.
3. La forma en la que se manejan los módulos ahora es mucho más clara, puesto que se entiende que no muy distino de una librería esto le permite al código recibir parámetros específicos, entenderlos y saber que hacer con ellos posteriormente sin la necesidad de tener que modificar tanto el código para acoplarlo a nuevos parámetros.


