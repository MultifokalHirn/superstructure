# superstructure
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
**a tool for Erkenntnis through dialectical notetaking**

## motivation
- could not find a tool to help me gain Erkenntnis
- need a tool to help me gain Erkenntnis
- had to create a tool to help me gain Erkenntnis myself

## caveats
- a computer program, as a thing in itself, can neither fully replicate nor contain the absolute 
- designing the basic logical structure is difficult, because when talking about the Gegenstand of a Begriff, that Gegenstand is not actually a Gegenstand, but itself just a Begriff, an object in computer land
- isomorphism to the (real) Whole is thus currently not part of the roadmap
- what we can do however, is to facilitate the Erkenntnisprozess in your Bewusstsein
- any (future) claims of the opposite are either ironic, or should be ignored

## setup
```console
python3 -mvenv env
source env/bin/activate
pip3 install -r requirements-dev.txt
```

## testing
```console
source env/bin/activate
python3 -mpytest tests
```
## running
terminal 1
```console
redis-server
```
terminal 2
```console
source env/bin/activate
python3 main.py
```

redis-server
## license

[MIT](https://github.com/MultifokalHirn/superstructure/blob/master/LICENSE)
