#! /bin/sh

python ropper/Ropper.py --type all --all --badbytes 00c0c1f5f6f7f8f9fafbfcfdfeff2c -r -a MIPSBE -I 0x80004000 --console -f ../TC7230-EB.01.bin
