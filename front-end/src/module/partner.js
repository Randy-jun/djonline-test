//sessionstorage function packae
import Axios from 'axios';
import Sstorage from '@/module/sstorage.js';
import { partnerList, partnerUpdate, partnerAdd, partnerDel } from '@/api/api'

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

var partner = {
    get : function(){
        return new Promise((resolve, reject) => {
            partnerList().then((response) => {
                // console.log(response);
                resolve(response.data) ;
            }).catch((error) => {
                console.log(error);
                reject(error);
            });
        });
    },
    update : function(value){
        return new Promise((resolve, reject) => {
            console.log(value)
            partnerUpdate({
                id:value.id,
                username:value.username,
                nickname:value.nickname,
                org_id:value.e_org_id,
                type: value.e_type,
                remark:value.e_remark,
                statuscode:value.statuscode,
            }).then((response) => {
                console.log(response);
                resolve(response.data) ;
            }).catch((error) => {
                console.log(error);
                reject(error);
            });
        });
    },
    insert : function(value){
        console.log(value)
        return new Promise((resolve, reject) => {
            partnerAdd({
                id:value.id,
                username:value.username,
                nickname:value.nickname,
                org_id:value.e_org_id,
                type: value.e_type,
                remark:value.e_remark,
                statuscode:value.statuscode,
            }).then((response) => {
                console.log(response);
                resolve(response.data) ;
            }).catch((error) => {
                console.log(error);
                reject(error);
            });
        });
    },
    delete : function(value){
        return new Promise((resolve, reject) => {
            partnerDel({
                org_id: value.id,
            }).then((response) => {
                console.log(response);
                resolve(response.data) ;
            }).catch((error) => {
                console.log(error);
                reject(error);
            });
        });
    }
}

export default partner;