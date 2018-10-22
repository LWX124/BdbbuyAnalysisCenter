
<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <Menu mode="horizontal" :active-name="menuActiveName"  @on-select="gotoPage">
      <MenuItem name="saleData">
        <Icon type="ios-stats" />
        销售统计
      </MenuItem>
      <Submenu name="2">
        <template slot="title">
          <Icon type="ios-warning"></Icon>
          库存预警
        </template>
        <MenuItem name="inventoryWarning_count" id="inventoryWarning_1">按个数筛选</MenuItem>
        <MenuItem name="inventoryWarning_ordercount" id="inventoryWarning_2" disabled>按销量筛选</MenuItem>
        <MenuItem name="inventoryWarning_date" id="inventoryWarning_3" disabled>筛选过期商品</MenuItem>
      </Submenu>

    </Menu>
    <router-view/>
  </div>
</template>

<script>

  export default {
    name: 'App',
    data() {
      return {
        menuActiveName: 'saleData',
      }

    },

    mounted: function () {
      // 页面加载
      this.menuActiveName = this.$route.path.replace('/', '')
    },

    methods: {
      gotoPage:function (name) {
        console.log(name)
        var pageName = name
        var routerParam = {path: pageName}
        if (name.indexOf('inventoryWarning_') != -1) {
          var pageNameList = name.split('_')
          pageName = pageNameList[0]
          routerParam = {path: pageName, query:{type: pageNameList[1]}}
        }

        this.$router.push(routerParam)
      }
    }
  }
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #f5f7f9;
  margin-top: 10px;
}


</style>
