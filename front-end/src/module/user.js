//sessionstorage function packae
import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';

const api='http://127.0.0.1:9090/acct/agencies/';

var userData = {
    item_num: 7,
    data:[
        {uuuid:0,uname:'user0',upassword:'passwd',unickname:'系统管理员',ulevel:'0',ulevelname:'系统管理员',uremark:'系统拥有者，权限最大。',guuid:0,ugroup:"百恒国际0",statuscode:0,statusflag:'正常',},
        {uuuid:1,uname:'user1',upassword:'passwd',unickname:'系统管理员',ulevel:'0',ulevelname:'系统管理员',uremark:'系统拥有者，权限最大。',guuid:1,ugroup:"百恒国际1",statuscode:0,statusflag:'正常',},
        {uuuid:2,uname:'user2',upassword:'passwd',unickname:'系统管理员',ulevel:'0',ulevelname:'系统管理员',uremark:'系统拥有者，权限最大。',guuid:2,ugroup:"百恒国际2",statuscode:0,statusflag:'正常',},
        {uuuid:3,uname:'user3',upassword:'passwd',unickname:'系统管理员',ulevel:'0',ulevelname:'系统管理员',uremark:'系统拥有者，权限最大。',guuid:3,ugroup:"百恒国际3",statuscode:0,statusflag:'正常',},
        {uuuid:4,uname:'user4',upassword:'passwd',unickname:'系统管理员',ulevel:'0',ulevelname:'系统管理员',uremark:'系统拥有者，权限最大。',guuid:4,ugroup:"百恒国际4",statuscode:0,statusflag:'正常',},
        {uuuid:5,uname:'user5',upassword:'passwd',unickname:'系统管理员',ulevel:'0',ulevelname:'系统管理员',uremark:'系统拥有者，权限最大。',guuid:5,ugroup:"百恒国际5",statuscode:0,statusflag:'正常',},
        {uuuid:6,uname:'user6',upassword:'passwd',unickname:'系统管理员',ulevel:'0',ulevelname:'系统管理员',uremark:'系统拥有者，权限最大。',guuid:6,ugroup:"百恒国际6",statuscode:0,statusflag:'正常',},
        {uuuid:7,uname:'user7',upassword:'passwd',unickname:'系统管理员',ulevel:'0',ulevelname:'系统管理员',uremark:'系统拥有者，权限最大。',guuid:7,ugroup:"百恒国际7",statuscode:0,statusflag:'正常',},
    ],
}

var user = {
    get : function(){
        var params = new URLSearchParams();
        params.append("userID",Sstorage.get('userID'));
        params.append("tokeID",Sstorage.get('localAgencyFk'));
        params.append("local_agency_fk",Sstorage.get('tokenID'));

        params.append("req_method","GET");

        return new Promise((resolve, reject) => {
            // console.log(userData)
            resolve(userData) ;
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
        })
    },
    update : function(value){
        var params = new URLSearchParams();
        params.append("userID",Sstorage.get('userID'));
        params.append("tokeID",Sstorage.get('localAgencyFk'));
        params.append("local_agency_fk",Sstorage.get('tokenID'));

        params.append("req_method","UPDATE");

        params.append("pk", value.id);
        params.append("name", value.name);
        params.append("remark", value.remark);

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
    insert : function(value){
        var params = new URLSearchParams();
        params.append("userID",Sstorage.get('userID'));
        params.append("tokeID",Sstorage.get('localAgencyFk'));
        params.append("local_agency_fk",Sstorage.get('tokenID'));

        params.append("req_method","UPDATE");

        params.append("name", value.name);
        params.append("remark", value.remark);

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
    }
}

export default user;