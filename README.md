## Agrupamiento jerárquico
El algoritmo presentado realiza agrupamientos jerárquicos según la cercanía entre los datos.

 - Buscamos las coordenadas mas cercanas entre si y formamos un grupo.
 - Realizamos nuevamente una búsqueda de cercanía entre coordenadas y el grupo ya establecido.
 - Se repite el proceso de forma recursiva hasta que solo quede un grupo.
 - Para aprovechar cálculos ya realizados se usa un diccionario que guarda el valor de los cálculos de distancia entre grupos o coordenadas.
 - Se guardan los datos de cada grupo realizado, estos se usaran para realizar una gráfica animada.

![Inicio de agrupacion](https://github.com/AndresMorales-gif/agrupacion_jerarquica/blob/master/imgReadme/inicio_agrupamiento.png)
![Agrupamiento](https://github.com/AndresMorales-gif/agrupacion_jerarquica/blob/master/imgReadme/agrupamiento.png)
![Terminando agrupamiento](https://github.com/AndresMorales-gif/agrupacion_jerarquica/blob/master/imgReadme/terminando_agrupamiento.png)