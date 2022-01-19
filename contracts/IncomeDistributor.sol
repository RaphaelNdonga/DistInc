//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IncomeDistributor {
    address payable[] shareHoldersArray;
    mapping(address => uint256) private shareHoldersMap;
    mapping(address => uint256) private addressToAmountFunded;
    uint256 buyingPrice = 40;
    uint256 sellingPrice;

    struct ShareHolder {
        address payable addressName;
        uint256 percent;
    }
    ShareHolder shareHolderData;
    ShareHolder[] shareHolderArray;

    function sellItem() public payable {
        uint256 totalPercent = 0;
        for (uint256 i = 0; i < shareHolderArray.length; i++) {
            totalPercent += shareHolderArray[i].percent;
        }
        require(totalPercent == 100, "The shareHolders equity does not add up");
        sellingPrice = msg.value;
        require(sellingPrice > buyingPrice, "You cant sell at a loss");
        distributeIncome();
    }

    function distributeIncome() public payable {
        uint256 netProfit = sellingPrice - buyingPrice;
        for (uint256 i = 0; i < shareHoldersArray.length; i++) {
            address payable currentShareHolder = shareHoldersArray[i];
            uint256 percent = shareHoldersMap[currentShareHolder];
            uint256 income = (netProfit * percent) / 100;
            payable(currentShareHolder).transfer(income);
            addressToAmountFunded[currentShareHolder] += income;
        }
    }

    function createShareHolder(address payable addressName, uint256 percent)
        public
    {
        shareHolderData = ShareHolder(addressName, percent);
        shareHolderArray.push(shareHolderData);
    }

    function addShareHolder(address payable shareHolder, uint256 percent)
        public
    {
        shareHoldersArray.push(shareHolder);
        shareHoldersMap[shareHolder] = percent;
    }

    function getShareHoldersArray(uint256 index) public view returns (address) {
        return shareHoldersArray[index];
    }

    function getShareHoldersArraySize() public view returns (uint256) {
        return shareHoldersArray.length;
    }

    function getAmountFunded(address shareHolder)
        public
        view
        returns (uint256)
    {
        return addressToAmountFunded[shareHolder];
    }

    function getBuyingPrice() public view returns (uint256) {
        return buyingPrice;
    }

    function getShareHolderPercent(address shareHolder)
        public
        view
        returns (uint256)
    {
        return shareHoldersMap[shareHolder];
    }
}
