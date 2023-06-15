// SPDX-License-Identifier: BUSL-1.1
pragma solidity 0.8.19;

import {ARM} from "contracts/ARM.sol";

contract ARMCallerForSetConfig  {

  ARM arm;


  function getConfigVersion() external view returns (uint32 version) {
    uint32 blockNumber; ARM.Config memory config;
    (version, blockNumber , config )  = arm.getConfigDetails();

  }


  function getConfigBlockNumber() external view returns (uint32 blockNumber) {
    uint32 version; ARM.Config memory config;
     (version, blockNumber , config )  = arm.getConfigDetails();

  }
 
}