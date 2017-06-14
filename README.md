# python
Archivos de python


# COMANDOS BASICOS GIT #

$ git config --global user.name "John Doe"
$ git config --global user.email "johndoe@example.com"

COMENZANDO CON UN NUEVO REPOSITORIO

$ git init
$ git status >> para it controlando los cambios que vas haciendo
$ git add . || git add -A   >> con el punto '.' agrego los modificados, con -A agrego los modificados y archivos nuevos
$ git commit -m "Comentario a guardar"
$ git commit -a >> abre un editor y podes hacer comentarios mas extensos

ENVIANDO LOS CAMBIOS

$ git remote add origin https://github.com/yosoyfunes/python.git
$ git push origin master

PUSH -> Enviar cambios
PULL -> Recibir cambios

ACTIALIZAR UN REPOSITORIO FORKEADO



VER EL HISTORIAL DE CAMBIOS

$ git log
$ git log --oneline >> los veo en una linea

ENTORNO GRAFICO

$ gitk
$ git-gui

VOLVER A UN PUNTO ANTERIOR

$ git log > c:\logs\log.txt  (para salvar los logs)
$ git checkout {HASH}
