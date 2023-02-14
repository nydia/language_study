//SPDX-License-Identifier:GPL-3.0

pragma solidity ^0.4.17;

import "./A.sol";

contract B is A{

   event LogUint(uint256);

   function sun() public pure returns(uint256) {
      return parent();
   }

}