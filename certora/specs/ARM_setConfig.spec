/**

@title spec file for verifying setConfig only.
Properties proven here can be assumed in ARM.spec - the high level spec file 

This spec is over ARMCallerForSetConfig

**/
using ARM as arm;
methods {

    function arm.setConfig(ARM.Config) external;
    function getConfigVersion() external returns (uint32) envfree;
    function getConfigBlockNumber() external returns (uint32) envfree;
}

/** @title setConfig updates version and blockNumber 
**/
rule setConfigUpdate() {
    env e;
    uint32 versionBefore;
    uint32 blockNumberBefore; 
   
    
    versionBefore =  getConfigVersion() ;
    blockNumberBefore =  getConfigBlockNumber() ;


    ARM.Config config;
    arm.setConfig(e, config);

    uint32 versionAfter;
    uint32 blockNumberAfter; 
    
    versionAfter =  getConfigVersion() ;
    blockNumberAfter =  getConfigBlockNumber() ;


    assert to_mathint(versionAfter) == versionBefore + 1;
    assert to_mathint(blockNumberAfter) == to_mathint(e.block.number);

}
