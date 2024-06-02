//SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.5.0 <0.9.0;

    contract Task4_ans{

    receive() external payable {
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }

}

// https://sepolia.etherscan.io/address/0x37a8fa269d33f8680daeaefea1bd9bf9aa9ccddf
