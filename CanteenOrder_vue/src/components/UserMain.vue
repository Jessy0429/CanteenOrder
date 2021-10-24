<template>
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
      <el-select v-model="sel_Store" placeholder="选择商家" clearable v-if="sel_Canteen != null" @clear="sel_Store = null">
        <el-option v-for="StoreID in this.Ct_St[this.sel_Canteen].storesID" :label="Stores[StoreID].storename" :value="StoreID" :key="StoreID"></el-option>
      </el-select>
      <el-select v-model="sel_Store" placeholder="选择商家" clearable v-else @clear="sel_Store = null">
        <el-option v-for="Store in this.Stores" :label="Store.storename" :value="Store.storeID" :key="Store.storeID"></el-option>
      </el-select>
      <el-input placeholder="想吃什么菜？" prefix-icon="el-icon-search" v-model="input_dish" style="width: 223.67px">
      </el-input>
    </div>
    <div id="StoreTable">
      <el-table width="800" :data="sel_Ct_StView" highlight-current-row @current-change="handleCurrentChange">
        <el-table-column
          prop="storename"
          label="商家名"
          width="180">
        </el-table-column>
        <el-table-column
          prop="canteenname"
          label="食堂"
          width="180">
        </el-table-column>
        <el-table-column
          prop="description"
          label="描述"
          width="440">
        </el-table-column>
      </el-table>
    </div>
    <div id="DishTable">

    </div>


  </div>

</template>

<script>
export default {
  name: "UserMain",
  data(){
    return{
      Time: new Date(),
      Canteens: [{canteenID: 0, canteenname: '一食堂'},
                {canteenID: 1, canteenname: '二食堂'},
                {canteenID: 2, canteenname: '三食堂'},
                {canteenID: 3, canteenname: '四食堂'}],
      Stores: [{storeID: 0, storename: '东北菜', canteenID: 0},
        {storeID: 1, storename:'烤肉拌饭', canteenID: 0},
        {storeID: 2, storename: '东北菜', canteenID: 1},
        {storeID: 3, storename: '姐妹豆花', canteenID: 1},
        {storeID: 4, storename: '米线', canteenID: 2},
        {storeID: 5, storename: '烤盘饭', canteenID: 2},
        {storeID: 6, storename: '杭州小笼包', canteenID: 3}],
      Ct_St:[{canteenID: 0, storesID: [0, 1]},{canteenID:1, storesID:[2, 3]},{canteenID:2, storesID:[4, 5]},{canteenID:3, storesID:[6]}],
      sel_Canteen: null,
      sel_Store: null,
      input_dish:'',
    }
  },
  computed:{
    sel_Ct_StView: function() {
      var View = [];
      // console.log(this.sel_Canteen);
      if(this.sel_Canteen != null){
        // console.log('1');
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
      return View;
    }
  },
  mounted() {
    // this.fun1();
  },
  methods: {
    fun1(){
      console.log(this.sel_Ct_StView);
    },
    handleCurrentChange(val){
      this.sel_Store = val.storeID;
      console.log(this.sel_Store);
    }
  }
}
</script>

<style scoped>

</style>
