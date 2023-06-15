/***

Spec file to verify bitmap related functions. This spec is checked against certora/helpers/ARMWrapperForBitmap.sol which exposes the internal bitmap functions

to run this spec use configuration certora/conf/ARM_bitvector.conf 


***/

methods{ 

    function bitmapGet(uint128 bitmap, uint8 index) external  returns (bool) envfree;
    function bitmapSet(uint128 bitmap, uint8 index) external returns (uint128) envfree;
    function bitmapCount(uint128 bitmap) external  returns (uint8) envfree; 

}

/**
@title Once a bit is set it can not be unset
**/
rule onceSetAlwaysSet() {
    uint128 bitmap;
    uint8 index;
    bool isSet = bitmapGet(bitmap, index);
    uint128 index2;
    uint128 updatedBitmap = bitmapSet(bitmap, index);
    assert isSet => bitmapGet(updatedBitmap, index);
}


/**
@title bitmapCount increase on change 
**/
rule counterIncrease() {
    uint128 bitmap;
    uint8 index;
    uint8 beforeCounter = bitmapCount(bitmap);
    uint128 updatedBitmap = bitmapSet(bitmap, index);
    assert bitmapCount(updatedBitmap) >= beforeCounter && to_mathint(bitmapCount(updatedBitmap)) <= beforeCounter + 1;
}