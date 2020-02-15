Image for KEA DHCP server + Mysql + REST interface

Does the world need another KEA Dhcpd server image? I could not find a suitable one
so built it.

This is a work in progress, specially need to do multistage

### Instructions

kea-admin db-init mysql -u root -p kea_db_pass  -h db

/usr/local/etc/kea