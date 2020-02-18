g++ -I /usr/local/include/kea -L /usr/local/lib -fpic -shared -o example.so \
    load_unload.cc pkt4_receive.cc version.cc \
    -lkea-dhcpsrv -lkea-dhcp++ -lkea-hooks -lkea-log -lkea-util -lkea-exceptions