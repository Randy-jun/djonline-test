//sesstatuscode:0,sionstflagorage function packae
import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';
import { orderList, orderDetail, orderChange, orderDel } from '@/api/api'

var orderData = {
    item_num : 7,
    data : [{id:1,user:"pearl",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pearl",isSet:false},
            {id:2,user:"pear2",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear2",isSet:false},
            {id:3,user:"pear3",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear3",isSet:false},
            {id:4,user:"pear4",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear4",isSet:false},
            {id:5,user:"pear5",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear5",isSet:false},
            {id:6,user:"pear6",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear6",isSet:false},
            {id:7,user:"pear7",linkman:"孙悟空",phone:"152-2511-5200",count:8, charge:888,address:"幸福中路", group:"中旅",name:"接机",statuscode:1,statusflag:"受理中",date:"2019-02-02",leavetime:"12:00",levaecity:"西安",arriveTime:"08:08",arrivecity:"北京",number:"T678",terminal:"T3",remark:"remark_pear7",isSet:false},],
    }
const orderDict = {
    id: "id",
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
    group:"o_tijiao",
    user:"o_zhidan",
};

var order = {
    getOne : function(value){
        return new Promise((resolve, reject) => {
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
            // orderData.result.forEach(element => {
            //     element[isSet] = false;
            // });
            // console.log(orderData)
            resolve(orderData) ;
        }).catch((error) => {
            reject(error);
        });
            // Axios.post(api, params).then((response) => {
            //     console.log(response);
            //     response.data.result.forEach(element => {
            //         this.$set(element, 'isSet', false);
            //     });
            //     resolve(response.data) ;
            // }).catch((error) => {
            //     // console.log(error);
            //     reject(error);
            // })
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
            }).catch ((error) => {
                console.log(error);
            });
        })
        // return new Promise((resolve, reject) => {
        //     Axios.post(api, params).then((response) => {
        //         if(response.data.status_flag){
        //             // console.log(response);
        //             let tempData = response.data.result;
        //             console.log(tempData);
        //             tempData.isSet = false;

        //             resolve(tempData) ;
        //         }
        //     }).catch((error) => {
        //         // console.log(error);
        //         reject(error);
        //     })
        // })
    },
    insert : function(value){
        return new Promise((resolve, reject) => {
            let tempData = value;
            tempData.isSet = false;
            resolve(tempData);
        })
        // return new Promise((resolve, reject) => {
        //     Axios.post(api, params).then((response) => {
        //         if(response.data.status_flag){
        //             // console.log(response);
        //             let tempData = response.data.result;
        //             console.log(tempData);
        //             tempData.isSet = false;

        //             resolve(tempData) ;
        //         }
        //     }).catch((error) => {
        //         // console.log(error);
        //         reject(error);
        //     })
        // })
    },
    delete : function(value){
        var params = new URLSearchParams();
        params.append("userID",Sstorage.get('userID'));
        params.append("tokeID",Sstorage.get('localAgencyFk'));
        params.append("local_agency_fk",Sstorage.get('tokenID'));

        params.append("req_method","DELETE");
        params.append("pk", value.id);

        return new Promise((resolve, reject) => {
            resolve(1);
        })
        // return new Promise((resolve, reject) => {
        //     Axios.post(api, params).then((response) => {
        //         if(response.data.status_flag){
        //             // console.log(response);

        //             resolve(tempData) ;
        //         }
        //     }).catch((error) => {
        //         // console.log(error);
        //         reject(error);
        //     })
        // })
    },
    exportOrder : function(){
        var params = new URLSearchParams();
        params.append("userID",Sstorage.get('userID'));
        params.append("tokeID",Sstorage.get('localAgencyFk'));
        params.append("local_agency_fk",Sstorage.get('tokenID'));

        params.append("req_method","GET");

        return new Promise((resolve, reject) => {
            Axios.get(api).then((response) => {
                console.log(response);
                resolve(response);
            }).catch((error) => {
                reject(error);
            });
        }).catch((error) => {
            reject(error);
        });
            // Axios.post(api, params).then((response) => {
            //     console.log(response);
            //     response.data.result.forEach(element => {
            //         this.$set(element, 'isSet', false);
            //     });
            //     resolve(response.data) ;
            // }).catch((error) => {
            //     // console.log(error);
            //     reject(error);
            // })
    },
}

export default order;