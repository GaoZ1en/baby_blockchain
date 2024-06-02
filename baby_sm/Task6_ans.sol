//SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.5.0 <0.9.0;

contract Task6_ans{

    address public immutable admin;

    receive() external payable {
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }

    function transferBalance(address payable _to) public {
        require(msg.sender == admin, "Warming, you are not the administrator.");
        uint256 balance = address(this).balance;
        _to.transfer(balance);
    }

}

https://sepolia.etherscan.io/address/0xc20c72F8E69Cd960aA07F9b142Af3885bC9b9482
