// SPDX-License-Identifier: BUSL-1.1
pragma solidity 0.8.19;

import {ARM} from "contracts/ARM.sol";

contract ARMWrapperForBitmap is ARM {

 constructor(Config memory config)  ARM(config) { }


function bitmapGet(uint128 bitmap, uint8 index) external pure returns (bool) {
    return super._bitmapGet(bitmap, index);
  }

  function bitmapSet(uint128 bitmap, uint8 index) external pure returns (uint128) {
    return  super._bitmapSet(bitmap, index);
  }

  function bitmapCount(uint128 bitmap) external pure returns (uint8) {
    return super._bitmapCount(bitmap);
  }
 
}