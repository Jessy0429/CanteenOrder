<template>
  <el-container>
    <el-main>
      <div>
        <div>
      <span style="font-size: larger; font-family: 'Microsoft JhengHei'">
        <p v-if="this.Time.getHours() > 16">晚上好，</p>
        <p v-else-if="this.Time.getHours() > 10">中午好，</p>
        <p v-else-if="this.Time.getHours() > 5">早上好，</p>
        <p>今天想吃点啥？</p>
      </span>
        </div>
        <div id="SelectInput">
          <el-select v-model="sel_Canteen" placeholder="选择食堂" clearable @clear="sel_Canteen = null; sel_Store = null">
            <el-option v-for="Canteen in this.Canteens" :label="Canteen.canteenname" :value="Canteen.canteenID" :key="Canteen.canteenID"></el-option>
          </el-select>
          <el-select v-model="sel_Store" placeholder="选择商家" clearable v-if="sel_Canteen != null" @clear="sel_Store = null" @change="getDish">
            <el-option v-for="StoreID in this.Ct_St[this.sel_Canteen].storesID" :label="Stores[StoreID].storename" :value="StoreID" :key="StoreID"></el-option>
          </el-select>
          <el-select v-model="sel_Store" placeholder="选择商家" clearable v-else @clear="sel_Store = null">
            <el-option v-for="Store in this.Stores" :label="Store.storename" :value="Store.storeID" :key="Store.storeID"></el-option>
          </el-select>
          <el-input placeholder="想吃什么菜？" prefix-icon="el-icon-search" v-model="input_dish" style="width: 223.67px">
          </el-input>
        </div>
        <div id="StoreTable" v-if="this.sel_Store == null">
          <el-table :data="sel_Ct_StView" highlight-current-row @current-change="handleCurrentChange">
            <el-table-column
              prop="storename"
              label="商家名"
              width="150">
            </el-table-column>
            <el-table-column
              prop="canteenname"
              label="食堂"
              width="150">
            </el-table-column>
            <el-table-column
              prop="description"
              label="描述"
              width="200">
            </el-table-column>
          </el-table>
        </div>
        <div id="DishTable" v-else>
          <el-table :data="Dish" highlight-current-row>
            <el-table-column type="expand">
              <template slot-scope="props">
                <el-form label-position="left" inline class="demo-table-expand">
                  <el-form-item label="菜系">
                    <span>{{ props.row.typeID }}</span>
                  </el-form-item>
                  <el-form-item label="原料">
                    <span>{{ props.row.ingredients }}</span>
                  </el-form-item>
                  <el-form-item label="描述">
                    <span>{{ props.row.description }}</span>
                  </el-form-item>
                </el-form>
              </template>
            </el-table-column>
            <el-table-column
              prop="picture"
              label="图片"
              width="200">
            </el-table-column>
            <el-table-column
              prop="dishname"
              label="菜品名称"
              width="100">
            </el-table-column>
            <el-table-column
              prop="price"
              label="单价"
              width="50">
            </el-table-column>
            <el-table-column
              prop="inventory"
              label="库存数量"
              width="100">
            </el-table-column>
            <el-table-column
              label="商家"
              width="150">
              <template slot-scope="scope">
                <el-button type="text" size="small">{{scope.row.store}}</el-button>
                　　　　　　 <el-button type="text" size="small" disabled>{{scope.row.canteen}}</el-button>
              </template>
            </el-table-column>
            <el-table-column fixed="right" width="100">
              <template slot-scope="scope">
                <el-button icon="el-icon-minus" @click="minDishnum(scope.row)" circle size="mini"></el-button>
                <span>{{scope.row.dishnum}}</span>
                <el-button icon="el-icon-plus" @click="addDishnum(scope.row)" circle size="mini"></el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>
    </el-main>
    <el-footer>
      <el-dropdown trigger="click">
        <el-button type="text">
          <el-badge :value="tolDishnum" class="item" type="primary">
            <i class="el-icon-shopping-cart-2" style="color: white; font-size: 50px"></i>
          </el-badge>
        </el-button>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item v-for="(dish, index) in this.ShoppingCart" :key="index">
            {{dish.dishname}} x {{dish.dishnum}}
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <el-button type="text" style="font-size: 30px; color: white">
        <span>下单</span>
        <i class="el-icon-arrow-right"></i>
      </el-button>
    </el-footer>
  </el-container>

</template>

<script>
export default {
  name: "UserMain",
  data(){
    return{
      Time: new Date(),
      Canteens: [],
      Stores: [
        // {storeID: 0, storename: '东北菜', canteenID: 0},
        // {storeID: 1, storename:'烤肉拌饭', canteenID: 0},
        // {storeID: 2, storename: '东北菜', canteenID: 1},
        // {storeID: 3, storename: '姐妹豆花', canteenID: 1},
        // {storeID: 4, storename: '米线', canteenID: 2},
        // {storeID: 5, storename: '烤盘饭', canteenID: 2},
        // {storeID: 6, storename: '杭州小笼包', canteenID: 3}
      ],
      Ct_St:[],
      sel_Canteen: null,
      sel_Store: null,
      input_dish:'',
      Dish:[],
      tolDishnum: 0,
      ShoppingCart:[]
    }
  },
  computed:{
    sel_Ct_StView: function() {
      var View = [];
      // console.log(this.sel_Canteen);
      if(this.sel_Canteen != null){
         console.log('1');
        console.log(this.sel_Canteen);
        let name = {canteenname: this.Canteens[this.sel_Canteen].canteenname}
        for (let i = 0; i < this.Ct_St[this.sel_Canteen].storesID.length; i++){
          View.push({...this.Stores[this.Ct_St[this.sel_Canteen].storesID[i]], ...name});
        }
      }
      else {
        console.log('2');
        for(let i = 0;i < this.Stores.length; i ++){
          var store = this.Stores[i];
          let name1 = {canteenname: this.Canteens[store.canteenID].canteenname};
          View.push({...store, ...name1});
        }
      }
      console.log(View);
      return View;
    },
    // tolDishnum: function (){
    //   var tolDish = 0;
    //   var item;
    //   for(item in this.ShoppingCart){
    //     if(!item.dishnum) this.ShoppingCart.slice(this.ShoppingCart.indexOf(item));
    //     else tolDish += item.dishnum;
    //   }
    //   return tolDish;
    // }
  },
  mounted() {
    // this.fun1();
    this.getData();
  },
  methods: {
    fun1(){
      console.log(this.sel_Ct_StView);
    },
    getData(){
      const url = "http://127.0.0.1:5000/api/getCanteenInfo";
      this.axios.get(url)
        .then((res) => {
          // console.log(res.data);
          for (let i = 0; i < res.data.length; i++){
            this.Canteens.push({canteenID: res.data[i][0], canteenname: res.data[i][2]})
          }
        })
        .catch((error) => {
          console.log(error);
        })
        .then(
          () => {
            const url = "http://127.0.0.1:5000/api/getStoreInfo";
            this.axios.get(url)
              .then((res) => {
                // console.log(res.data);
                for (let i = 0; i < res.data.length; i++){
                  this.Stores.push({storeID: res.data[i][0], storename: res.data[i][1], canteenID: res.data[i][2], description: res.data[i][3]})
                }
                console.log(this.Stores)
              })
              .catch((error) => {
                console.log(error);
              })
              .then(
                () => {
                  const url = "http://127.0.0.1:5000/api/getCt_StInfo";
                  this.axios.get(url)
                    .then((res) => {
                      console.log(res.data);
                      for (let i = 0; i < res.data.length; i++) this.Ct_St.push({canteenID: res.data[i][0], storesID: res.data[i][1]});
                      console.log(this.Ct_St);
                    })
                    .catch((error) => {
                      console.log(error);
                    })
                }
              )
          }
        )
    },
    handleCurrentChange(val){
      if(val){
        this.sel_Store = val.storeID;
        this.sel_Canteen = val.canteenID;
        this.getDish();
      }
      console.log(this.sel_Store)
    },
     getDish(){
      this.Dish = []
      // console.log(this.sel_Store);
      const url = "http://127.0.0.1:5000/api/getDishInfo/" + String(this.sel_Store)
      // console.log(url)
      this.axios.get(url)
        .then((res) => {
          console.log(res.data);
          for (let i = 0; i < res.data.length; i++) {
            var data = res.data[i];
            var num = 0;
            var index = this.ShoppingCart.findIndex((dish) => dish.dishID === data[0])
            if (index >= 0) num = this.ShoppingCart[index].dishnum;
            this.Dish.push({dishID: data[0], dishname: data[1], price: data[2], description: data[3],
              ingredients: data[4], store: this.Stores[this.sel_Store].storename, canteen: this.Canteens[this.sel_Canteen].canteenname,
              inventory: data[6], recommend: data[7], typeID: data[8], picture: data[9], dishnum: num})

          }
          console.log(this.Dish);
        })
        .catch((error) => {
          console.log(error);
        })
    },
    addDishnum(row){
      row.dishnum++;
      this.tolDishnum++;
      var index = this.ShoppingCart.findIndex((dish) => dish.dishID === row.dishID);
      console.log(index);
      if(index >= 0) this.ShoppingCart[index].dishnum++;
      else this.ShoppingCart.push({dishID: row.dishID, dishname: row.dishname, dishnum: row.dishnum});
      console.log(this.ShoppingCart);
    },
    minDishnum(row){
      row.dishnum--;
      this.tolDishnum--;
      var index = this.ShoppingCart.findIndex((dish) => dish.dishID === row.dishID);
      console.log(index);
      if (!row.dishnum) this.ShoppingCart.splice(index, 1);
      console.log(this.ShoppingCart);
    }
  }
}
</script>

<style scoped>
#StoreTable{
  width: 500px;
  display: inline-block;
}
#DishTable{
   width: 800px;
   display: inline-block;
 }
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
.el-footer{
  background-color: #66CCCC;
  color: #ffffff;
  text-align: right;
  line-height: 30px;
}
</style>
