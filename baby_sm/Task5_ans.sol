//SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.5.0 <0.9.0;

contract Task5_ans{

    receive() external payable {
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }

    function transferBalance(address payable _to) public {
        uint256 balance = address(this).balance;
        _to.transfer(balance);
    }

}

// https://sepolia.etherscan.io/address/0xe5e4de2ebed4380870b7446d41d760cf8a432371
