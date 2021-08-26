<template >
  <div class="block" style="margin-top: 20px">
    <el-timeline>
      <el-timeline-item v-for="(activity, index) in activities" :key="index">
        <el-card style="width: 90%">
          <p>{{ activity.timestamp }}</p>
          <h2>{{ activity.title }}</h2>
          <h3>{{ activity.content.data }}</h3>
          <el-divider />

          <h4
            v-for="(comment, kindex) in activity.content.comments"
            :key="kindex"
          >
            <p style="color:#909399 font-weight: bold;">{{ comment.time }}</p>
            <p style="color: #409eff">{{ comment.data }}</p>
          </h4>
          <el-input
            type="textarea"
            :rows="3"
            placeholder="Comment"
            v-model="activity.content.comment"
            @keyup.enter.native="
              activity.content.comment = submitcomment(
                index,
                activity.content.comment
              )
            "
          >
          </el-input>
        </el-card>
      </el-timeline-item>
    </el-timeline>
    <!-- form input -->
    <el-divider />
    <div style="margin-left: 20px" width="50%">
      <el-select
        v-model="title"
        multiple
        filterable
        allow-create
        default-first-option
        placeholder="Select a failure pattern"
      >
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <div style="margin: 20px 0"></div>
      <el-input
        type="textarea"
        :rows="10"
        placeholder="Content"
        v-model="content"
      >
      </el-input>

      <el-row :gutter="1" style="margin-top: 20px">
        <el-button
          type="primary"
          icon="el-icon-plus"
          circle
          size="mini"
          @click="addItem"
        ></el-button>
        <el-button
          type="danger"
          icon="el-icon-minus"
          circle
          size="mini"
          @click="delItem"
        ></el-button>
        <el-button
          type="warning"
          icon="el-icon-folder-add"
          circle
          size="mini"
          @click="mkdir"
        ></el-button>
      </el-row>
    </div>
  </div>
</template>


<script>
import { mapState } from "vuex";
export default {
  props: {
    getdata: {},
  },
  data() {
    return {
      title: "",
      content: "",
      comment: "",
      dialogFormVisible: false,
      loading: true,
      reverse: true,
      state: false,
      flag: false,
      form: {},
      options: [
        {
          value: "A surface update",
          label: "A surface update",
        },
        {
          value: "Cover Hinge update",
          label: "Cover Hinge update",
        },
        {
          value: "Cushion Change",
          label: "Cushion Change",
        },
      ],
      activities: [],
    };
  },

  //  mounted() {

  // },
  created() {
    this.stringchange();
    // this.activities = JSON.parse(Value.Log);
  },
  watch: {
    getdata(Value) {
      console.log("Value.Log");
      console.log(Value.Log);
      this.stringchange();
    },
  },
  computed: {
    ...mapState({ User: (state) => state.User }),
  },
  methods: {
    submitcomment(index, comment) {
      console.log("this.User");
      console.log(this.User);
      if (this.User.Name != "") {
        comment = this.User.Name + ":\n" + comment;

        var myDate = new Date();
        // console.log(this.activities[index].content.comment)
        this.activities[index].content.comments.push({
          time: myDate.toLocaleString(),
          data: comment,
        });
        this.run(this.getdata);
      } else {
        this.$router.push({
          path: "/UserLogin",
        });
        this.$message({
          showClose: true,
          message: "Please reLogin",
          type: "error",
        });
      }
    },
    stringchange() {
      this.getdata.Log = this.getdata.Log.replace(/'/g, '"');
      this.activities = JSON.parse(this.getdata.Log);
    },
    addItem() {
      var myDate = new Date();
      // var mytime=myDate.toLocaleTimeString();     //获取当前时间
      // 获取日期与时间

      this.activities.push({
        title: this.title.join(" and "),
        content: { data: this.content, comments: [] },
        timestamp: myDate.toLocaleString(),
      });
      this.run(this.getdata);
    },
    delItem() {
      this.activities.pop({});
      this.run(this.getdata);
    },
    editlog(content) {
      this.dialogFormVisible = true;
      console.log(content);
    },
    mkdir() {},
    run(form) {
      form.Log = JSON.stringify(this.activities);
      this.$axios
        .post("/api/dabinfo", {
          params: {
            Dabinfo: JSON.stringify(form),
            Copy: false,
          },
        })
        .then(
          (response) => {
            this.$message({
              showClose: true,
              message: response.data,
              type: "success",
            });
          },
          (error) => {
            console.log(error);
          }
        );
    },
  },
};
</script>