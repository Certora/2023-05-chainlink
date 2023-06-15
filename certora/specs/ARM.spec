
/**

@title verification of ARM with summarization of _setConfig
**/

methods {
    function isCursed() external returns (bool) envfree;
    // need to check in a modular way - here we just track if it was called 
    function  _setConfig(ARM.Config memory config) internal  => setConfigCalled(); 
}




// a mirror to track owner 
ghost address g_owner;  

hook Sload address val s_owner STORAGE {
    require g_owner == val; 
}


// just track that _setConfig has been called 
ghost  bool _setConfigCalled; 
function setConfigCalled()  {
     _setConfigCalled = true;  
}


/// @title  Validity of when ARM can change from isCursed to no isCurded
/// @notice This property is implemented as a parametric rule - it is each on every public\external function 

rule isCursedTurnedOff() {
    method f;
    calldataarg args;
    env e;
    bool isCursedBefore = isCursed();
    f(e,args);
    assert isCursedBefore => isCursed() || f.selector == sig:ownerUnvoteToCurse(ARM.UnvoteToCurseRecord[]).selector; 
}

/// @title  If config has been called then it is by the owner 
/// @notice This property is using the summarization of  _setConfig and a hook on _owner that keeps a mirror of it in a ghost 
rule onlyOwnerCanCallSetConfig() {
    require _setConfigCalled == false;   

    method f;
    calldataarg args;
    env e;
    f(e,args);

    assert (_setConfigCalled  => g_owner == e.msg.sender);
}






