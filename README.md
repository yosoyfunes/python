python
======

> Archivos de python


**COMANDOS BASICOS GIT**

```bash
$ git config --global user.name "John Doe"
$ git config --global user.email "johndoe@example.com"
```

**COMENZANDO CON UN NUEVO REPOSITORIO**

```bash
$ git init
$ git status >> para it controlando los cambios que vas haciendo
$ git add . || git add -A   >> con el punto '.' agrego los modificados, con -A agrego los modificados y archivos nuevos
$ git commit -m "Comentario a guardar"
$ git commit -a >> abre un editor y podes hacer comentarios mas extensos
```

**ENVIANDO LOS CAMBIOS**

```bash
$ git remote add origin https://github.com/yosoyfunes/python.git
$ git push origin master
```

    PUSH -> Enviar cambios

    PULL -> Recibir cambios


**ACTIALIZAR UN REPOSITORIO FORKEADO**

> Actualizar un proyecto "forkeado" en Github*

*Agrego upstream como una nueva rama que tiene el repositorio original*

```bash
$ git remote add upstream https://github.com/original/proyecto.git
```

*actualizo los datos en mi rama upstream*

```bash
$ git fetch upstream
```

*paso los archivos de la rama upstream a mi rama master*

```bash
$ git merge upstream/master
```

*si quiero actualizar mi repositorio GitHub hago push*

```bash
$ git push origin
```

**VER EL HISTORIAL DE CAMBIOS**

```bash
$ git log
$ git log --oneline >> los veo en una linea
```

**ENTORNO GRAFICO**

```bash
$ gitk
$ git-gui
```

**VOLVER A UN PUNTO ANTERIOR**

```bash
$ git log > c:\logs\log.txt  (para salvar los logs)
$ git checkout {HASH}
```
