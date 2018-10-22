
// 基础信息配置

let host = window.location.host;
let devURL = "http://localhost:8000/" // 开发环境URL
let proURL = "http://localhost:8000/" // 生产环境URL

export let serverBaseURL = "";
process.env.NODE_ENV === 'development' ? serverBaseURL = devURL : serverBaseURL = proURL;


