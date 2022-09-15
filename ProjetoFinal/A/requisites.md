Para rodar o docker tive que aumentar o map_max_count da imagem do elastic:

```sh
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```