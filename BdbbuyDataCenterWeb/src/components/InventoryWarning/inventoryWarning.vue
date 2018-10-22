<template>
  <div style="margin-left: 3%;margin-right: 3%;margin-top: 20px">
    <Table  :data="tableData" :columns="tableColumns" stripe></Table>
    <div style="margin: 20px;overflow: hidden">
      <div style="float: right;">
        <Page ref="pages" :total="totalCount" :current="1" @on-change="changePage"
              :page-size="pageSize" show-sizer :page-size-opts="page_size_opts"></Page>
      </div>
    </div>

  </div>
</template>

<script>
  import {serverBaseURL} from '../../globalConfig'

  export default {
    name: 'inventoryWarning',
    data() {
      return {
        page_size_opts: [20, 40, 50, 100],
        pageSize: 20,
        tableData: [],
        tableColumns: [],
        totalCount: 0,
        allProductList: []
      }

    },
    mounted: function () {
      // 页面加载
      console.log('这里是库存预警页面')
      this.setTableColumn()
      this.getData()
    },

    methods: {

      getData:function () {
        this.tableData = []
        let url = serverBaseURL + 'product/getWarnigProduct'
        this.$http.get(url).then(function (response) {
          var status = response.status;
          if (status == 200) {
            var result = response.body;
            this.allProductList = result['data']['order_list']
            this.totalCount = result['data']['totalCount']
            this.changePage(1)
            console.log(this.totalCount)
          }
        }, function (response) {
          console.log("发生错误")
          var str = response.body.message
          this.$Message.success(str)
        });
      },

      setTableColumn:function () {
        this.tableColumns = [
          {
            title: 'id',
            key: 'product_id',
            width: 100,
            align: 'center',
          },
          {
            title: '英文名',
            key: 'en',
            width: 200,
            align: 'center',
          },
          {
            title: '中文名',
            key: 'name',
            width: 200,
            align: 'center',
          }
          ]
      },

      changePage:function (index) {
        var startPosition = 0
        var endPosition = this.allProductList.length
        if (this.allProductList.length > this.pageSize) {
          startPosition = this.pageSize * (index - 1)
          endPosition = this.pageSize * index
        }
        this.tableData = this.allProductList.slice(startPosition, endPosition)
        console.log(this.tableData)
      }

    }

  }
</script>

<style scoped>


</style>
