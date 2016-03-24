# Pour lancer un serveur ipython-notebook sur ubuntu

    sudo apt-get install docker.io
    sudo docker pull ipython/scipyserver
    sudo docker run -d -p 80:8888 -e "PASSWORD=gerioq" -e "USE_HTTP=1" ipython/scipyserver
    
    
voir https://registry.hub.docker.com/u/ipython/scipyserver/

Et pour avoir un serveur lua/torch sur le port 8080

    sudo docker pull arokem/itorch
    sudo docker run -d -p 8080:8888 -e "PASSWORD=gerioq" -e "USE_HTTP=1" arokem/itorch
    
    
    
