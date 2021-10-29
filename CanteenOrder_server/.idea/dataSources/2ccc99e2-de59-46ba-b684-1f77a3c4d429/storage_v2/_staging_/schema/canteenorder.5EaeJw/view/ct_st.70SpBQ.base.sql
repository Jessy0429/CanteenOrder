create definer = root@localhost view ct_st as
select `c`.`canteenID` AS `canteenID`, group_concat(`s`.`storeID` separator ',') AS `storesID`
from (`canteenorder`.`store` `s`
         join `canteenorder`.`canteen` `c` on ((`s`.`canteenID` = `c`.`canteenID`)))
group by `c`.`canteenID`;

