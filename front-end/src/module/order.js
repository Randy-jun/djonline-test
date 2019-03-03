//sesstatuscode:0,sionstflagorage function packae
import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';
import { orderList, orderDetail, orderChange, orderDel, orderChangeStatus, orderExport} from '@/api/api'

// var orderData = {
//     item_num : 7,
//     data : [{id:1,user:"pearl",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pearl",isSet:false},
//             {id:2,user:"pear2",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear2",isSet:false},
//             {id:3,user:"pear3",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear3",isSet:false},
//             {id:4,user:"pear4",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear4",isSet:false},
//             {id:5,user:"pear5",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear5",isSet:false},
//             {id:6,user:"pear6",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear6",isSet:false},
//             {id:7,user:"pear7",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear7",isSet:false},],
//     }

const orderDict = {
    id: "order_id",
    remark: "remark",
    statusCode:"o_status",
    typeCode:"o_type",
    linkMan:"name",
    phoneNumber:"phone_number",
    count:"number",
    charge:"fee",
    date:"date",
    leaveTime:"qifei_time",
    arriveTime:"luodi_time",
    lineNumber:"line_num",
    terminal:"hangzhanlou",
    leaveCity:"o_from",
    arriveCity:"o_to",
    address:"address",
    group:"o_from_org",
    user:"o_zhidan",
    userSubmit:"o_tijiao",
};

var order = {
    getOne : function(value){
        return new Promise((resolve, reject) => {
            console.log(value)
            orderDetail({
                id:value
            }).then((response) => {
                // console.log(response);
                let data = response.data.data;
                var orderData = {};
                for (var key in orderDict) {
                    // console.log(key + ":" + orderDict[key]);
                    orderData[key] = data[orderDict[key]];
                }
                resolve(orderData)
                if (response.data.is_success) {
                    resolve(response.data.data);
                } else {
                    reject(response.error_msg);
                }
            }).catch((error) => {
                console.log(error);
                reject(error);
            });
        });
    },
    get : function(){
        return new Promise((resolve, reject) => {
            orderList().then((response) => {
                console.log(response);
                if (response.data.is_success) {
                    // console.log(response.data)
                    let orderData = {
                        item_num : 0,
                        data : [],
                    }
                    // console.log(response.data)
                    orderData.item_num = response.data.item_num;
                    
                    response.data.data.forEach((element)=> {
                        // console.log(element, index)
                        let tempOrder = {}
                        for (var key in orderDict) {
                            // console.log(key + ":" + orderDict[key]);
                            tempOrder[key] = element[orderDict[key]];
                        }
                        orderData.data.push(tempOrder);
                    });
                    // console.log(orderData,"ddsads");
                    resolve(orderData);
                } else {
                    reject(response.error_msg);
                }
            }).catch((error) => {
                reject(error);
            });
        });
    },
    change : function(value){
        return new Promise((resolve, reject) => {
            var params = {};
            if (0 === value.typeCode) {
                value.arriveCity = "西安";
            } else if (1 === value.typeCode) {
                value.leaveCity = "西安";
            }
            for (var key in orderDict) {
                // console.log(key + ":" + orderDict[key]);
                params[orderDict[key]] = value[key];
            }
            orderChange(params).then((response) => {
                console.log(response);
                if (response.data.is_success) {
                    let data = response.data.data;
                    var orderData = {};
                    for (var key in orderDict) {
                        // console.log(key + ":" + orderDict[key]);
                        orderData[key] = data[orderDict[key]];
                    }
                    resolve(orderData)
                } else {
                    reject(response.error_msg);
                }

            }).catch ((error) => {
                console.log(error);
            });
        });
    },
    changeStatus : function(statusCode, value){
        return new Promise((resolve, reject) => {
            orderChangeStatus({
                order_status: statusCode,
                order_ids: value,
            }).then((response) => {
                // console.log(response);
                if (response.data.is_success) {
                    resolve(response.data.order_ids)
                } else {
                    reject(response.error_msg);
                }

            }).catch ((error) => {
                console.log(error);
            });
        });
    },
    delete : function(value){
        return new Promise((resolve, reject) => {
            orderDel({
                order_id: value,
            }).then((response) => {
                console.log(response);
                if (response.data.is_success) {
                    console.log(response);
                    resolve(response.data) ;
                } else {
                    reject(response.error_msg);
                }
            }).catch((error) => {
                console.log(error);
                reject(error);
            });
        });
    },
    export : function(value){
        return new Promise((resolve, reject) => {
            orderExport({
                order_ids: value,
            }).then((response) => {
                console.log(response);
                if (response.data.is_success) {
                    console.log(response);
                    resolve(response.data) ;
                } else {
                    reject(response.error_msg);
                }
            }).catch((error) => {
                console.log(error);
                reject(error);
            });
        });
    },
}

export default order;