<table>
    <tr>
        <th> Comando </th>  
        <th>Descripcion </th>
    </tr>
    <tr>
        <td> git init </td>
        <td> Inicializamos cualquier carpeta en nuestro sistema y se volvera un repositorio </td>
    </tr>
    <tr>
        <td rowspan=4> git status</td>
        <td>Ver el estado actual de nuestros archivos dentro del repositorio</td>
    </tr>
    <tr>
        <td>Si el archivo esta rojo: No se esta haciendo seguimiento</td>
    </tr>
    <tr>
        <td>Si el archivo esta verde: Esta en el area de preparacion (staging) listo para ser commiteado</td>
    </tr>
    <tr>
        <td>Si el archivo esta amarillo: Significa que ya se le esta haciendo seguimiento pero ha sido editado</td>
    </tr>
    <tr>
        <td rowspan=3>git add [ . | -A | <nombre_archivo> ] </td>
        <td>.      Agregara todos los archivos en este nivel y subniveles al estado de preparacion (staging)</td>
    </tr>
    <tr>
        <td>-A     Agregara TODOS LOS ARCHIVOS DE TODO EL REPOSITORIO que ha sido alterado</td>
    </tr>
    <tr>
        <td>nombre_archivo Agregara solamente ese archivo al area de preparacion</td>
    </tr>
    <tr>
        <td>git commit -m "MENSAJE" </td>
        <td>Registrara los cambios realizados al repositorio de manera PERMANENTE</td>
    </tr>
    <tr>
        <td>git remote add origin <URL_REPO></td>
        <td>Se vincula el repositorio local con el repositorio creado en github, gitlab, etc</td>
    </tr>
    <tr>
        <td>git push [ -u | --set-upstream ] origin <NOMBRE_RAMA></td>
        <td>Si es la primera vez en el repositorio se tiene que vincular la rama local con la rama remota y eso se hace mediante el comando `-u origin` las siguientes veces que querramos subir cambios no es necesario repetir esta opcion</td>
    </tr>    
    <tr>
        <td>git pull </td>
        <td>Descargo los ultimos cambios de mi repositorio a mi local en la rama que me encuentre</td>
    </tr>    
    <tr>
        <td>git branch</td>
        <td>Lista las ramas que tengo en mi repositorio</td>
    </tr>    
    <tr>
        <td>git branch <NOMBRE_RAMA></td>
        <td>Cambio de rama en mi repositorio</td>
    </tr>
      
</table>