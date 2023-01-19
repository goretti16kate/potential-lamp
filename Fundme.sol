// SPDX-License-Identifier: MIT

pragma solidity 0.8.17;
import "https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe{

    mapping (address=>uint) public addressToAmountFunded;
    address[] public funders;
    address public owner;

    constructor() {
      owner = msg.sender;
    }

    modifier onlyOwner() {
      require(msg.sender == owner, "Nyet, you are not the owner of the fund Me!!!!!");
      _;
    }

    function fund() public payable{
        // set the threshold
        uint256 minimumUSD = 50 * 10 ** 18;
        require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ether");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
        // what is the eth > usd convertion rate
    }

    function withdraw() payable public onlyOwner{
      // Ensure only the owner can withdraw the money
      payable(msg.sender).transfer(address(this).balance);
      // Resetting the amounts using for loop
      for (uint256 funderIndex = 0; funderIndex < funders.length; funderIndex++) {
        address funder = funders[funderIndex];
        addressToAmountFunded[funder] = 0;
      }
      funders = new address[](0);
    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e);
        return priceFeed.version();
    }

    function getPrice() public view returns(uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0xD4a33860578De61DBAbDc8BFdb98FD742fA7028e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
      return uint256(answer); //  156343838395
    }

    function getConversionRate(uint256 ethAmount) public view returns(uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUSD = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUSD;
    }

}
