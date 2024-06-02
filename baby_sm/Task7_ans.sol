//SPDX-License-Identifier: GPL-3.0
 
pragma solidity >=0.5.0 <0.9.0;

contract Task7_ans{
    address[] public players;

    function start() public {
        players.push(msg.sender);
    }
}

// https://sepolia.etherscan.io/address/0x07FD0e88249335f14a14bf24c1621c83d99cccc9
