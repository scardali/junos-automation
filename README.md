To start nginx web-server:sudo docker run --name ansible-web -v /home/lab/nginx/srv/nginx/:/usr/share/nginx/html:ro -d -p 8080:80 nginx

To run ansible playbook: sudo docker run -it --rm -v $PWD:/project juniper/pyez-ansible ansible-playbook -i ./inventory/hosts ./get_show_commands.yml

To use Sean's auto-script that allows enabling/disabling of individual playbooks easily:
  -  First edit run.txt.  Comment out any playbooks you don't want to run
  -  Then simply run:  ./run.py

VAULT PASSWORD:  juniper1

Playbooks that can currently be configured/commented from run.txt:
   rollback
   vlan
   version
   commit
   interface
   alarm
   ethernet
   multicast
   lacp


NOTES:
-=-=-=-=-=-=-=-=-=-=-=-=-=
Code is also on GitHub (I defaulted to GitHub instead of Junipers gitlab because your VM didnt have access to the VPN). If you want to run it outside of your server, you can run:

git clone https://github.com/seanlangley/junos-automation

Then from the project root directory:

cd srv/nginx
docker-compose up

That should bring the web server online (as long as you have docker installed, which I<92>m pretty sure Joe helped you out with haha!). Then just go to localhost:8080 in the browser.


Host w/ all containers running:
WARNING: Error loading config file: /home/lab/.docker/config.json: stat /home/lab/.docker/config.json: permission denied
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS                                                 NAMES
c18c581b95bd        ansible/awx_task:latest      "/tini -- /bin/sh -câ€¦"   5 weeks ago         Up 5 weeks          8052/tc                                             awx_task_1
728d822e0996        ansible/awx_web:latest       "/tini -- /bin/sh -câ€¦"   5 weeks ago         Up 5 weeks          0.0.0.0590->8052/tcp                                awx_web_1
4206a47f3030        memcached:alpine             "docker-entrypoint.sâ€¦"   5 weeks ago         Up 5 weeks          11211/t pp                                          awx_memcached_1
c17469bf0180        ansible/awx_rabbitmq:3.7.4   "docker-entrypoint.sâ€¦"   5 weeks ago         Up 5 weeks          4369/tc 5671-5672/tcp, 15671-15672/tcp, 25672/tcp   awx_rabbitmq_1
bd49e79948b3        postgres:9.6                 "docker-entrypoint.sâ€¦"   5 weeks ago         Up 5 weeks          5432/tc                                             awx_postgres_1
468689292d88        php:fpm                      "docker-php-entrypoiâ€¦"   5 weeks ago         Up 5 weeks          9000/tc                                             web_php_1
418e14a27388        nginx:latest                 "nginx -g 'daemon ofâ€¦"   5 weeks ago         Up 5 weeks          0.0.0.0080->80/tcp
@                                                 

