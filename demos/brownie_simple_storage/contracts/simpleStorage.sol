// SPDX-License-Identifier: MIT

pragma solidity 0.8.17;

contract simpleStorage {

    uint256 favoriteNumber;

    struct People {
        uint favoriteNumber;
        string name;
    }

    People[] public people;
    mapping (string => uint) public nameToNumber;

    function retrieve() public view returns(uint) {
        return favoriteNumber;
    }

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }
    

    function addPeople(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber,_name));
        nameToNumber[_name] = _favoriteNumber;
    }
}
