
# Verification with Certora Prover 

A basic setup and example for verification of ARM.sol.

This folder contains specification files and helper contract in addition to  Prover configuration files.  

The verification is built in a modular way:

- specs/ARMBitmap.spec to verify bitmap related functions (bitmapGet, bitmapSet, bitmapCount ) using the bitvector capabilities of Prover. 

-  specs/ARM_setConfig.spec is structured to verify only the setConfig functionality

- specs/ARM.spec contains a summarization of setConfig and should store all high-level rules of ARM 

to run the prover, from the project root folder run:

```
certoraRun certora/conf/ARM.conf
``` 
or any other configuration file. 

See [docs.certora.com](http://docs.certora.com) for more information. 