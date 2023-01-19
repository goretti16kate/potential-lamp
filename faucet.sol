// SPDX-License-Identifier: MIT

pragma solidity 0.8.17;

contract faucet {

    receive() external payable {}

    function withdraw(uint amount) public {
        require(amount <= 10000000000000000000);
        payable(msg.sender).transfer(amount);
    }
}
