
ql_symbiflow -compile -src /data/data/com.termux/files/home/fpga-examples/blink -d ql-eos-s3 -P PU64 -v helloworldfpga.v -t boolean -p quickfeather.pcf -dump binary


#scp /data/data/com.termux/files/home/fpga-examples/blink/boolean.bin imran@192.168.43.48:
