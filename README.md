# copperhead

Major work in progress

Script is intended to ping a list of ips and keep the "alive" hosts
if the host is not alive it will wait and try to ping again at a random interval (interval is the same each time through the loop)
if host is alive it will attempt a net use connection, if this fails it should remove the ip from the list as to not lock out the user
if the connection is successful, it will check for a list of existing files....this is a dev env thing
it will then copy over a list of files. keylogger, and start up link.
