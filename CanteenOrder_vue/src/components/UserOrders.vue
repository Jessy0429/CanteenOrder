<template>
  <div>
    <el-collapse>
      <el-collapse-item  v-for="order in this.orderInfo" :key="order.orderID">
        <template slot="title">
          <el-row type="flex" align="middle" style="margin: 10px; width: 500px">
            <el-col :span="10">下单时间  {{order.o_time}}</el-col>
            <el-col :span="5">共 {{order.Dishnum}} 件商品</el-col>
          </el-row>
        </template>
        <div>
          <el-descriptions>
            <el-descriptions-item label="收货人">{{order.Consignee}}</el-descriptions-item>
            <el-descriptions-item label="电话号">{{order.Telephone}}</el-descriptions-item>
            <el-descriptions-item label="收货地址">{{order.Address}}</el-descriptions-item>
            <el-descriptions-item label="送达时间">{{order.d_time}}</el-descriptions-item>
            <el-descriptions-item label="下单食堂">{{order.canteenID}}</el-descriptions-item>
            <el-descriptions-item label="订单状态">{{Status[order.status]}}</el-descriptions-item>
          </el-descriptions>
        </div>
        <div class="dishes">
          <el-row type="flex" style="margin: 10px; text-align: center; font-size: 15px; font-weight: bold;
          display:inline-block">菜品详情</el-row>
          <el-row type="flex" style="margin: 10px; text-align: center; display:inline-block"
                  v-for="(dish, index) in order.Dishes" :key="index">{{dish}}</el-row>
          <el-row type="flex" style="margin: 10px; text-align: center; display:inline-block">餐具 X {{order.Dishware}}</el-row>
        </div>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
export default {
  name: "UserOrders",
  data(){
    return{
      userID: this.$route.query.userID,
      orderInfo:[],
      Status: ['未完成', '已完成'],
    }
  },
  mounted() {
    this.getData();
  },
  methods:{
    getData(){
      const url = "http://127.0.0.1:5000/api/getOrderInfo"
      this.axios.get(url,{params: {userID: this.userID}})
        .then((res) => {
          console.log(res.data);
          for (let i = 0; i < res.data.length; i++){
            var dishnum = 0;
            for(let j = 0; j < res.data[i][10].length; j++){
              var dish = res.data[i][10][j];
              dishnum += Number(dish.charAt(dish.length-1));
            }
            this.orderInfo.push({OrderID: res.data[0], Consignee: res.data[i][3], Telephone: res.data[i][4], Address: res.data[i][5],
              Dishware: res.data[i][6], canteenID: res.data[i][7], o_time: res.data[i][8], d_time: res.data[i][9],
              Dishes: res.data[i][10], Dishnum: dishnum + res.data[i][6], status: res.data[i][11]});
          }
          console.log(this.orderInfo)
        })
        .catch((error) => {
          console.log(error);
        })
    }
  }

}
</script>

<style scoped>
.el-collapse /deep/ .el-collapse-item__header{
  height: 70px;
  font-size: 15px;
  font-family: "Microsoft JhengHei";
  font-weight: bold;
  color: #62a8f0;
}
.dishes{
  width: 300px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  margin: 0 auto;
  display: flex;
  text-align: center;
  flex-direction:column;
  color: #3c3f41;
}
</style>
