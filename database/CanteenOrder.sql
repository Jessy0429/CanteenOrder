/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2021/10/18 19:07:31                          */
/*==============================================================*/


drop trigger if exists Delinventory;

drop
table if exists OrderbyDay;

drop
table if exists OrderInfo;

drop index idx_dishname on Dish;

/*==============================================================*/
/* Table: Canteen                                               */
/*==============================================================*/
create table Canteen
(
   canteenID            bigint not null,
   managerID            bigint,
   canteenname          char(20),
   primary key (canteenID)
);

/*==============================================================*/
/* Table: DeliveredInfo                                         */
/*==============================================================*/
create table DeliveredInfo
(
   deliveredID          bigint not null,
   userID               bigint not null,
   consignee            char(10) not null,
   address              char(100) not null,
   primary key (deliveredID)
);

/*==============================================================*/
/* Table: Dish                                                  */
/*==============================================================*/
create table Dish
(
   dishID               bigint not null,
   dishname             char(10) not null,
   price                real not null,
   description          char(100),
   ingredients          char(100) not null,
   storeID              bigint not null,
   inventory            int not null,
   recommd              bool,
   typeID               int not null,
   picture              char(20),
   primary key (dishID)
);

/*==============================================================*/
/* Index: idx_dishname                                          */
/*==============================================================*/
create index idx_dishname on Dish
(
   dishname
);

/*==============================================================*/
/* Table: DishType                                              */
/*==============================================================*/
create table DishType
(
   typeID               int not null,
   typename             char(20) not null,
   description          char(200),
   primary key (typeID)
);

/*==============================================================*/
/* Table: Manager                                               */
/*==============================================================*/
create table Manager
(
   managerID            bigint not null,
   cateenID             bigint,
   name                 char(10) not null,
   telephone            char(11) not null,
   account              bigint not null,
   password             char(50) not null,
   primary key (managerID)
);

/*==============================================================*/
/* Table: `Order`                                               */
/*==============================================================*/
create table `Order`
(
   orderID              bigint not null,
   userID               bigint not null,
   deliveredID          bigint not null,
   dishware            	int not null,
   canteenID            bigint not null,
   o_time               char(20) not null,
   d_time               char(20) not null,
   status               bool not null,
   primary key (orderID)
);

/*==============================================================*/
/* Table: Order_Dish                                            */
/*==============================================================*/
create table Order_Dish
(
   dishID               bigint not null,
   orderID              bigint not null,
   dishnumber           int not null,
   primary key (dishID, orderID)
);

/*==============================================================*/
/* Table: Store                                                 */
/*==============================================================*/
create table Store
(
   storeID              bigint not null,
   storename            char(20) not null,
   canteenID            bigint not null,
   description          char(200),
   primary key (storeID)
);

/*==============================================================*/
/* Table: User                                                  */
/*==============================================================*/
create table User
(
   userID               bigint not null,
   username              char(20) not null,
   telnumber            char(11) not null,
   password             char(50) not null,
   primary key (userID)
);

/*==============================================================*/
/* View: Ct_St                                          */
/*==============================================================*/
create VIEW  Ct_St
as
select
   C.canteenID,
   JSON_ARRAYAGG(S.storeID) storesID
from
   Store S join Canteen C on S.canteenID = C.canteenID
group by C.canteenID;

/*==============================================================*/
/* View: OrderInfo                                              */
/*==============================================================*/
create VIEW  OrderInfo
as
select O.orderID, User.userID, User.username, D.consignee, D.telephone, D.address, O.dishware, C.canteenname, O.o_time, O.d_time, JSON_ARRAYAGG(concat(Dish.dishname, '   X ', OD.dishnumber))as dishes, O.status
from `Order` as O join DeliveredInfo as D join User join Order_Dish as OD join Dish join Canteen as C
    on O.orderID = OD.orderID and O.userID = User.userID and O.deliveredID = D.deliveredID
    and OD.dishID = Dish.dishID and C.canteenID = O.canteenID
group by O.orderID;

/*==============================================================*/
/* View: OrderbyDay                                             */
/*==============================================================*/
create VIEW  OrderbyDay
as
select
   date(O.o_time) date,
   S.storename,
   C.canteenname,
   count(O.orderID) sum_order
from
   Store S join Canteen C join `Order` O
   on S.canteenID = C.canteenID and O.storeID = S.storeID
group by S.storeID;


alter table Canteen add constraint FK_Canteen_Manager foreign key (managerID)
      references Manager (managerID) on delete restrict on update restrict;

alter table DeliveredInfo add constraint FK_User_DeliveredInfo foreign key (userID)
      references User (userID) on delete restrict on update restrict;

alter table Dish add constraint FK_Dish_DishType foreign key (typeID)
      references DishType (typeID) on delete restrict on update restrict;

alter table Dish add constraint FK_Dish_Store foreign key (storeID)
      references Store (storeID) on delete restrict on update restrict;

alter table Manager add constraint FK_Canteen_Manager2 foreign key (canteenID)
      references Canteen (canteenID) on delete restrict on update restrict;

alter table `Order` add constraint FK_Order_DiliverInfo foreign key (deliveredID)
      references DeliveredInfo (deliveredID) on delete restrict on update restrict;

alter table `Order` add constraint FK_Order_Store foreign key (storeID)
      references Store (storeID) on delete restrict on update restrict;

alter table `Order` add constraint FK_User_Order foreign key (userID)
      references User (userID) on delete restrict on update restrict;

alter table Order_Dish add constraint FK_Order_Dish foreign key (dishID)
      references Dish (dishID) on delete restrict on update restrict;

alter table Order_Dish add constraint FK_Order_Dish2 foreign key (orderID)
      references `Order` (orderID) on delete restrict on update restrict;

alter table Store add constraint FK_Canteen_Store foreign key (canteenID)
      references Canteen (canteenID) on delete restrict on update restrict;

DELIMITER ;;
create trigger Delinventory
    after insert on order_dish
    for each row
begin
update Dish set Dish.inventory = Dish.inventory - new.dishnumber
where dishID = new.dishID;
end;;
DELIMITER ;


