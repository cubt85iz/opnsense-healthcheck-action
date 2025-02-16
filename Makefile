install:
	cp -v actions_healthchecks.conf /usr/local/opnsense/service/conf/actions.d/
	cp -Rv healthchecks /usr/local/opnsense/scripts/

clean:
	rm /usr/local/opnsense/service/conf/actions.d/actions_healthchecks.conf
	rm /usr/local/opnsense/scripts/healthchecks/healthchecks.py
	rmdir /usr/local/opnsense/scripts/healthchecks
