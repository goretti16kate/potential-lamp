// SPDX-License-Identifier: MIT

pragma solidity 0.8.17;
import "./simpleStorage.sol";

contract storageFactory is simpleStorage{

    simpleStorage[] public simpleStorageArray;
    function createSimpleStorageContract() public {
        simpleStorage simplestorage = new simpleStorage();
        simpleStorageArray.push(simplestorage);
    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageFavNum) public {
        simpleStorage simplestorage = simpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        simplestorage.store(_simpleStorageFavNum);
    }
    function sfGet(uint256 _simpleStorageIndex) public view returns(uint256) {
        simpleStorage simplestorage = simpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        return simplestorage.retrieve();
    }
}
